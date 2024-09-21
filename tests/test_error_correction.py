
import unittest
from qiskit import QuantumCircuit, Aer, execute
from quantum_state_anchoring.src.error_correction import QuantumErrorCorrection
from qiskit.quantum_info import Statevector

class TestQuantumErrorCorrection(unittest.TestCase):
    def setUp(self):
        """Set up a simple quantum circuit and error correction instance"""
        self.qc = QuantumCircuit(1)
        self.qc.h(0)  # Apply Hadamard gate
        self.error_correction = QuantumErrorCorrection()
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        self.result = job.result()
        self.statevector = Statevector(self.result.get_statevector(self.qc))

    def test_apply_error_correction(self):
        """Test that error correction is applied and the state is modified"""
        corrected_state = self.error_correction.apply_error_correction(self.qc)
        self.assertIsNotNone(corrected_state, "Corrected state should not be None")
        self.assertNotEqual(corrected_state, self.statevector, "Corrected state should differ from the original state")

    def test_correct_state(self):
        """Test that noise is properly corrected in the statevector"""
        noisy_state = self.statevector.copy()
        noisy_state.data += 1e-2  # Add small noise
        corrected_state = self.error_correction.correct_state(noisy_state)
        self.assertLess(np.linalg.norm(noisy_state.data - corrected_state.data), np.linalg.norm(noisy_state.data), "Corrected state should reduce the noise")

    def test_store_and_retrieve_corrected_state(self):
        """Test that corrected states can be stored and retrieved"""
        corrected_state = self.error_correction.apply_error_correction(self.qc)
        self.error_correction.store_corrected_state('corrected_state', corrected_state)
        retrieved_state = self.error_correction.retrieve_corrected_state('corrected_state')
        self.assertEqual(corrected_state, retrieved_state, "Retrieved state should match the corrected state")

    def test_clear_corrected_states(self):
        """Test that all corrected states can be cleared"""
        self.error_correction.store_corrected_state('corrected_state', self.statevector)
        self.error_correction.clear_corrected_states()
        self.assertIsNone(self.error_correction.retrieve_corrected_state('corrected_state'), "Corrected states should be cleared")

if __name__ == '__main__':
    unittest.main()
