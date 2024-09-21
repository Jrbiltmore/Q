
from qiskit.quantum_info import Statevector
import numpy as np

class QuantumStateVerifier:
    def __init__(self, reference_state: Statevector, verification_threshold: float = 1e-5):
        self.reference_state = reference_state
        self.verification_threshold = verification_threshold

    def verify_state(self, state_to_verify: Statevector):
        """Verify that the provided state matches the reference state"""
        fidelity = self.reference_state.fidelity(state_to_verify)
        return fidelity > (1 - self.verification_threshold)

    def calculate_fidelity(self, state_to_verify: Statevector):
        """Calculate the fidelity between the reference state and the state to verify"""
        return self.reference_state.fidelity(state_to_verify)

    def detect_state_change(self, state_to_verify: Statevector):
        """Detect if a significant state change has occurred"""
        fidelity = self.calculate_fidelity(state_to_verify)
        if fidelity < (1 - self.verification_threshold):
            return True, fidelity
        return False, fidelity

    def estimate_error(self, state_to_verify: Statevector):
        """Estimate the error between the reference state and the state to verify"""
        difference_vector = np.abs(self.reference_state.data - state_to_verify.data)
        return np.linalg.norm(difference_vector)
