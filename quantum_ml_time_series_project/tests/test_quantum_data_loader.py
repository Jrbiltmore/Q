
import unittest
import numpy as np
import pandas as pd
from src.quantum_data_loader import QuantumDataLoader

class TestQuantumDataLoader(unittest.TestCase):
    def setUp(self):
        """Initialize the Quantum Data Loader with default parameters."""
        self.num_qubits = 2
        self.data_loader = QuantumDataLoader(num_qubits=self.num_qubits)

    def test_load_csv(self):
        """Test loading data from a CSV file."""
        # Create dummy CSV data
        data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        path = 'test_data.csv'
        data.to_csv(path, index=False)
        loaded_data = self.data_loader.load_csv(path)
        self.assertTrue(loaded_data.equals(data))

    def test_preprocess(self):
        """Test preprocessing of data, including scaling and reshaping."""
        data = np.array([[1, 2], [3, 4], [5, 6]])
        preprocessed_data = self.data_loader.preprocess(data, scale=True)
        self.assertEqual(preprocessed_data.shape, (3, self.num_qubits))

    def test_split_train_test(self):
        """Test splitting data into training and testing sets."""
        data = np.random.rand(100, self.num_qubits)
        train_data, test_data = self.data_loader.split_train_test(data)
        self.assertEqual(len(train_data), 80)
        self.assertEqual(len(test_data), 20)

    def test_batch_generator(self):
        """Test generating batches from the data."""
        data = np.random.rand(100, self.num_qubits)
        batch_size = 10
        batches = list(self.data_loader.batch_generator(data, batch_size))
        self.assertEqual(len(batches), 10)
        self.assertEqual(batches[0].shape, (batch_size, self.num_qubits))

    def test_save_and_load_data(self):
        """Test saving and loading processed quantum data from a file."""
        data = np.random.rand(100, self.num_qubits)
        path = 'test_processed_data.npy'
        self.data_loader.save_processed_data(data, path)
        loaded_data = np.load(path)
        self.assertTrue(np.array_equal(data, loaded_data))

if __name__ == '__main__':
    unittest.main()
