
import unittest
import numpy as np
from src.optimization import QuantumOptimization

class TestQuantumOptimization(unittest.TestCase):
    def setUp(self):
        """Initialize the Quantum Optimization model with default parameters."""
        self.num_qubits = 2
        self.optimizer = QuantumOptimization(num_qubits=self.num_qubits)

    def test_optimize(self):
        """Test the basic optimization process using a simple objective function."""
        def objective_function(params):
            return np.sum(params ** 2)

        initial_params = np.array([0.5, -0.5])
        result = self.optimizer.optimize(objective_function, initial_params)
        self.assertTrue(result.success)

    def test_quantum_variational_circuit(self):
        """Test if the variational quantum circuit is built and transpiled correctly."""
        params = np.random.rand(2)
        circuit = self.optimizer.quantum_variational_circuit(params)
        self.assertIsNotNone(circuit)

    def test_evaluate_quantum_circuit(self):
        """Test if the quantum circuit returns measurement results after evaluation."""
        params = np.random.rand(2)
        circuit = self.optimizer.quantum_variational_circuit(params)
        results = self.optimizer.evaluate_quantum_circuit(circuit)
        self.assertIsInstance(results, dict)

    def test_optimize_variational_circuit(self):
        """Test the optimization of a variational quantum circuit over iterations."""
        def objective_function(params):
            return np.sum(params ** 2)

        initial_params = np.random.rand(2)
        best_params = self.optimizer.optimize_variational_circuit(objective_function, initial_params, iterations=10)
        self.assertIsNotNone(best_params)

    def test_optimize_with_penalty(self):
        """Test the optimization process with a penalty applied to parameters."""
        def objective_function(params):
            return np.sum(params ** 2)

        initial_params = np.random.rand(2)
        result = self.optimizer.optimize_with_penalty(objective_function, initial_params, penalty_factor=0.05)
        self.assertTrue(result.success)

if __name__ == '__main__':
    unittest.main()
