
import unittest
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from quantum_state_anchoring.src.state_verification import QuantumStateVerifier

class TestQuantumStateVerifier(unittest.TestCase):
    def setUp(self):
        """Set up reference quantum states for testing"""
        self.qc = QuantumCircuit(1)
        self.qc.h(0)
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        result = job.result()
        self.reference_state = Statevector(result.get_statevector(self.qc))
        self.verifier = QuantumStateVerifier(self.reference_state)

    def test_verify_state(self):
        """Test that the state verification works for identical states"""
        identical_state = self.reference_state
        self.assertTrue(self.verifier.verify_state(identical_state), "States should match with high fidelity")

    def test_fidelity_calculation(self):
        """Test the fidelity calculation between two states"""
        self.qc.x(0)
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        result = job.result()
        different_state = Statevector(result.get_statevector(self.qc))
        fidelity = self.verifier.calculate_fidelity(different_state)
        self.assertLess(fidelity, 1.0, "Fidelity should be less than 1 for different states")

    def test_detect_state_change(self):
        """Test detection of a significant state change"""
        self.qc.x(0)
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        result = job.result()
        different_state = Statevector(result.get_statevector(self.qc))
        change_detected, fidelity = self.verifier.detect_state_change(different_state)
        self.assertTrue(change_detected, "State change should be detected")
        self.assertLess(fidelity, 1.0, "Fidelity should indicate a state change")

    def test_estimate_error(self):
        """Test error estimation between two states"""
        self.qc.x(0)
        backend = Aer.get_backend('statevector_simulator')
        job = execute(self.qc, backend)
        result = job.result()
        different_state = Statevector(result.get_statevector(self.qc))
        error = self.verifier.estimate_error(different_state)
        self.assertGreater(error, 0, "Error should be greater than 0 for different states")

if __name__ == '__main__':
    unittest.main()
