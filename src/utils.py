
import numpy as np
from qiskit import QuantumCircuit

def generate_random_quantum_circuit(num_qubits: int, depth: int):
    """Generate a random quantum circuit with a given number of qubits and depth"""
    circuit = QuantumCircuit(num_qubits)
    for _ in range(depth):
        for qubit in range(num_qubits):
            random_gate = np.random.choice(['x', 'h', 'z'])
            if random_gate == 'x':
                circuit.x(qubit)
            elif random_gate == 'h':
                circuit.h(qubit)
            elif random_gate == 'z':
                circuit.z(qubit)
    return circuit

def calculate_state_fidelity(state1, state2):
    """Calculate the fidelity between two quantum states"""
    return np.abs(np.dot(np.conjugate(state1), state2)) ** 2

def save_quantum_circuit(circuit: QuantumCircuit, file_path: str):
    """Save a quantum circuit to a file in QASM format"""
    with open(file_path, 'w') as f:
        f.write(circuit.qasm())

def load_quantum_circuit(file_path: str):
    """Load a quantum circuit from a QASM file"""
    with open(file_path, 'r') as f:
        qasm_code = f.read()
    circuit = QuantumCircuit.from_qasm_str(qasm_code)
    return circuit

def print_circuit_details(circuit: QuantumCircuit):
    """Print details of the quantum circuit including depth and number of gates"""
    print(f"Quantum Circuit Depth: {circuit.depth()}")
    print(f"Quantum Circuit Width: {circuit.width()}")
    print(f"Quantum Circuit Operations: {circuit.count_ops()}")
