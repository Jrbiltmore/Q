
import unittest
from datetime import datetime
from qiskit import QuantumCircuit
from quantum_state_anchoring.src.state_anchoring import QuantumStateAnchor

class TestQuantumStateAnchor(unittest.TestCase):
    def setUp(self):
        """Set up a simple quantum circuit for testing"""
        self.qc = QuantumCircuit(1)
        self.qc.h(0)  # Apply Hadamard gate
        self.anchor = QuantumStateAnchor(self.qc)

    def test_initialize_state(self):
        """Test that the quantum state is initialized properly"""
        self.anchor.initialize_state()
        self.assertIsNotNone(self.anchor.statevector, "Statevector should not be None after initialization")

    def test_anchor_state(self):
        """Test that a quantum state is anchored at the current time"""
        anchored_state = self.anchor.anchor_state()
        self.assertIn('statevector', anchored_state)
        self.assertIn('anchor_time', anchored_state)
        self.assertTrue(isinstance(anchored_state['anchor_time'], str), "Anchor time should be a string")

    def test_compare_states(self):
        """Test that two identical quantum states are recognized as similar"""
        self.anchor.anchor_state()
        new_qc = QuantumCircuit(1)
        new_qc.h(0)
        self.anchor.initialize_state()  # Reinitialize with the same circuit
        self.assertTrue(self.anchor.compare_states(self.anchor.statevector), "States should be identical")

    def test_time_travel(self):
        """Test the time travel functionality"""
        initial_time = self.anchor.anchor_time
        future_time = self.anchor.time_travel(1000)
        self.assertGreater(future_time, initial_time, "Future time should be greater than the initial time")

    def test_save_and_load_state(self):
        """Test saving and loading a quantum state to and from a file"""
        self.anchor.anchor_state()
        self.anchor.save_state('test_state.txt')
        loaded_anchor = QuantumStateAnchor(self.qc)
        loaded_anchor.load_state('test_state.txt')
        self.assertEqual(self.anchor.anchor_time, loaded_anchor.anchor_time, "Loaded anchor time should match saved time")
        self.assertTrue(self.anchor.compare_states(loaded_anchor.statevector), "Loaded state should match saved state")

if __name__ == '__main__':
    unittest.main()
