
import unittest
from qiskit import QuantumCircuit, Aer, execute
from quantum_state_anchoring.src.quantum_memory import QuantumMemory

class TestQuantumMemory(unittest.TestCase):
    def setUp(self):
        """Set up a quantum memory and a test quantum circuit"""
        self.memory = QuantumMemory()
        self.qc = QuantumCircuit(1)
        self.qc.h(0)  # Apply Hadamard gate
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        self.result = job.result()

    def test_store_and_retrieve_state(self):
        """Test that a quantum state can be stored and retrieved correctly"""
        self.memory.store_state('test_state', self.qc)
        stored_state = self.memory.retrieve_state('test_state')
        self.assertIsNotNone(stored_state, "Stored state should not be None")
        self.assertEqual(self.result.get_statevector(self.qc), stored_state.data, "Stored state should match the original statevector")

    def test_delete_state(self):
        """Test that a quantum state can be deleted from memory"""
        self.memory.store_state('test_state', self.qc)
        self.memory.delete_state('test_state')
        deleted_state = self.memory.retrieve_state('test_state')
        self.assertIsNone(deleted_state, "State should be None after deletion")

    def test_clear_memory(self):
        """Test that the quantum memory can be cleared of all stored states"""
        self.memory.store_state('state1', self.qc)
        self.memory.store_state('state2', self.qc)
        self.memory.clear_memory()
        self.assertEqual(self.memory.get_memory_usage(), 0, "Memory usage should be zero after clearing")

    def test_list_stored_states(self):
        """Test that the correct list of stored states is returned"""
        self.memory.store_state('state1', self.qc)
        self.memory.store_state('state2', self.qc)
        stored_states = self.memory.list_stored_states()
        self.assertListEqual(stored_states, ['state1', 'state2'], "Stored states should match the list of keys")

if __name__ == '__main__':
    unittest.main()
