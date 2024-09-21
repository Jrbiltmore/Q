
import unittest
import numpy as np
from src.quantum_reinforcement_learning import QuantumReinforcementLearningAgent

class TestQuantumReinforcementLearning(unittest.TestCase):
    def setUp(self):
        """Initialize the Quantum Reinforcement Learning agent with default parameters."""
        self.num_qubits = 3
        self.action_space = 4
        self.agent = QuantumReinforcementLearningAgent(num_qubits=self.num_qubits, action_space=self.action_space)

    def test_initial_q_table(self):
        """Test if the Q-table is initialized correctly with zero values."""
        q_table_shape = (2 ** self.num_qubits, self.action_space)
        self.assertEqual(self.agent.q_table.shape, q_table_shape)
        self.assertTrue(np.all(self.agent.q_table == 0))

    def test_act_exploration(self):
        """Test the exploration behavior of the agent when epsilon is high."""
        self.agent.epsilon = 1.0  # Force exploration
        state = np.array([0, 1, 1])
        action = self.agent.act(state)
        self.assertIn(action, range(self.action_space))

    def test_act_exploitation(self):
        """Test the exploitation behavior of the agent when epsilon is low."""
        self.agent.epsilon = 0.0  # Force exploitation
        state = np.array([0, 1, 1])
        self.agent.q_table[3, 2] = 10  # Mock high Q-value for action 2
        action = self.agent.act(state)
        self.assertEqual(action, 2)

    def test_learn(self):
        """Test the learning process and Q-table update."""
        state = np.array([0, 1, 0])
        next_state = np.array([1, 0, 1])
        action = 2
        reward = 5
        done = False

        initial_q_value = self.agent.q_table[1, action]
        self.agent.learn(state, action, reward, next_state, done)
        updated_q_value = self.agent.q_table[1, action]

        self.assertNotEqual(initial_q_value, updated_q_value)

    def test_memory(self):
        """Test if the memory correctly stores experience."""
        state = np.array([0, 1, 0])
        next_state = np.array([1, 0, 1])
        action = 2
        reward = 5
        done = False

        self.agent.remember(state, action, reward, next_state, done)
        self.assertEqual(len(self.agent.memory), 1)

    def test_save_and_load_model(self):
        """Test saving and loading the Q-table."""
        path = "test_q_table.npy"
        self.agent.q_table[3, 2] = 10
        self.agent.save_model(path)
        loaded_agent = QuantumReinforcementLearningAgent(num_qubits=self.num_qubits, action_space=self.action_space)
        loaded_agent.load_model(path)

        self.assertEqual(self.agent.q_table[3, 2], loaded_agent.q_table[3, 2])

if __name__ == '__main__':
    unittest.main()
