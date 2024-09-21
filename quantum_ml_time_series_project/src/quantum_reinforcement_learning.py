
import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.circuit import Parameter
from sklearn.preprocessing import StandardScaler
from collections import deque

class QuantumReinforcementLearningAgent:
    def __init__(self, num_qubits, action_space, gamma=0.99, alpha=0.01, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.num_qubits = num_qubits
        self.action_space = action_space
        self.gamma = gamma  # Discount factor
        self.alpha = alpha  # Learning rate
        self.epsilon = epsilon  # Exploration rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = np.zeros((2**num_qubits, action_space))  # Q-table for quantum states and actions
        self.memory = deque(maxlen=1000)  # Replay memory

        self.qc = QuantumCircuit(num_qubits)
        self.simulator = Aer.get_backend('qasm_simulator')

    def _quantum_encoding(self, state):
        """Encodes classical state into a quantum state."""
        self.qc.reset(range(self.num_qubits))
        for i, bit in enumerate(state):
            if bit == 1:
                self.qc.x(i)  # Apply X-gate if state bit is 1
        return transpile(self.qc, self.simulator)

    def _quantum_state_to_classical(self):
        """Measure quantum state and return classical state."""
        self.qc.measure_all()
        job = execute(self.qc, self.simulator, shots=1)
        result = job.result().get_counts()
        measured_state = list(result.keys())[0]  # Get measurement result as string
        return int(measured_state, 2)  # Convert binary string to integer

    def act(self, state):
        """Choose an action based on epsilon-greedy policy."""
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_space)  # Exploration
        quantum_state = self._quantum_encoding(state)
        classical_state = self._quantum_state_to_classical()
        return np.argmax(self.q_table[classical_state])  # Exploitation

    def learn(self, state, action, reward, next_state, done):
        """Update Q-table based on the agent's experience."""
        quantum_state = self._quantum_encoding(state)
        classical_state = self._quantum_state_to_classical()
        quantum_next_state = self._quantum_encoding(next_state)
        classical_next_state = self._quantum_state_to_classical()

        target = reward
        if not done:
            target += self.gamma * np.max(self.q_table[classical_next_state])  # Q-learning update rule

        self.q_table[classical_state, action] += self.alpha * (target - self.q_table[classical_state, action])

        if done:
            self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def remember(self, state, action, reward, next_state, done):
        """Store experience in replay memory."""
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        """Sample a batch from memory and learn from it."""
        if len(self.memory) < batch_size:
            return
        batch = np.random.choice(len(self.memory), batch_size, replace=False)
        for i in batch:
            state, action, reward, next_state, done = self.memory[i]
            self.learn(state, action, reward, next_state, done)

    def save_model(self, path):
        """Save the Q-table to a file."""
        np.save(path, self.q_table)

    def load_model(self, path):
        """Load the Q-table from a file."""
        self.q_table = np.load(path)
