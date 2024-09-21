
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

class QuantumMemory:
    def __init__(self, memory_size: int = 1):
        self.memory_size = memory_size
        self.memory_storage = {}

    def store_state(self, key: str, quantum_circuit: QuantumCircuit):
        """Store a quantum state in memory after executing the quantum circuit"""
        backend = Aer.get_backend('statevector_simulator')
        job = execute(quantum_circuit, backend)
        result = job.result()
        statevector = Statevector(result.get_statevector(quantum_circuit))
        self.memory_storage[key] = statevector

    def retrieve_state(self, key: str):
        """Retrieve a stored quantum state from memory"""
        return self.memory_storage.get(key, None)

    def delete_state(self, key: str):
        """Delete a stored quantum state from memory"""
        if key in self.memory_storage:
            del self.memory_storage[key]

    def clear_memory(self):
        """Clear all stored quantum states from memory"""
        self.memory_storage.clear()

    def list_stored_states(self):
        """List all keys of stored quantum states"""
        return list(self.memory_storage.keys())

    def get_memory_usage(self):
        """Get the current memory usage in terms of stored states"""
        return len(self.memory_storage)
