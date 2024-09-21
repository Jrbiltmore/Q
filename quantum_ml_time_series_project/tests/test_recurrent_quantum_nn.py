
import unittest
import numpy as np
from src.recurrent_quantum_nn import RecurrentQuantumNN

class TestRecurrentQuantumNN(unittest.TestCase):
    def setUp(self):
        """Initialize the Recurrent Quantum Neural Network with default parameters.""" 
        self.num_qubits = 2
        self.time_steps = 3
        self.rqnn = RecurrentQuantumNN(num_qubits=self.num_qubits, time_steps=self.time_steps)

    def test_build_model(self):
        """Test if the model builds successfully with valid input data.""" 
        data = np.random.rand(100, self.time_steps)
        model = self.rqnn.build_model(data)
        self.assertIsNotNone(model)

    def test_predict(self):
        """Test if the model predicts output for given time series data."""
        data = np.random.rand(100, self.time_steps)
        model = self.rqnn.build_model(data)
        predictions = self.rqnn.predict(model, data)
        self.assertEqual(len(predictions), len(data) - self.time_steps)

    def test_evaluate(self):
        """Test if the model evaluates and returns a valid score (e.g., MSE)."""
        data = np.random.rand(100, self.time_steps)
        model = self.rqnn.build_model(data)
        mse = self.rqnn.evaluate(model, data)
        self.assertGreaterEqual(mse, 0)

    def test_hyperparameter_optimization(self):
        """Test the hyperparameter optimization for the recurrent quantum model."""
        data = np.random.rand(100, self.time_steps)
        param_grid = [{'learning_rate': 0.01}, {'learning_rate': 0.05}]
        best_params, best_score = self.rqnn.optimize_hyperparameters(data, param_grid)
        self.assertIsNotNone(best_params)
        self.assertIsInstance(best_score, float)

    def test_save_and_load_model(self):
        """Test saving and loading the trained quantum recurrent model."""
        data = np.random.rand(100, self.time_steps)
        model = self.rqnn.build_model(data)
        path = 'test_rqnn_model.h5'
        self.rqnn.save_model(model, path)
        loaded_model = self.rqnn.load_model(path)
        self.assertIsNotNone(loaded_model)

if __name__ == '__main__':
    unittest.main()
