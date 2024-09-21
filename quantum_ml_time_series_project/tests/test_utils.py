
import unittest
import numpy as np
import os
from src.utils import QuantumUtils

class TestQuantumUtils(unittest.TestCase):
    def test_normalize_data(self):
        """Test normalization of data between 0 and 1."""
        data = np.array([10, 20, 30])
        normalized_data = QuantumUtils.normalize_data(data)
        self.assertTrue(np.all(normalized_data >= 0) and np.all(normalized_data <= 1))

    def test_setup_logging(self):
        """Test setting up logging by creating a log file."""
        log_file = 'test_log.log'
        QuantumUtils.setup_logging(log_file)
        self.assertTrue(os.path.exists(log_file))

    def test_create_directory(self):
        """Test creating a directory if it doesn't exist."""
        dir_path = 'test_dir'
        QuantumUtils.create_directory(dir_path)
        self.assertTrue(os.path.exists(dir_path))
        os.rmdir(dir_path)

    def test_save_and_load_numpy_array(self):
        """Test saving and loading a NumPy array to and from a file."""
        data = np.random.rand(100)
        path = 'test_array.npy'
        QuantumUtils.save_numpy_array(data, path)
        loaded_data = QuantumUtils.load_numpy_array(path)
        self.assertTrue(np.array_equal(data, loaded_data))
        os.remove(path)

    def test_calculate_moving_average(self):
        """Test calculating the moving average of a dataset."""
        data = np.array([1, 2, 3, 4, 5])
        moving_average = QuantumUtils.calculate_moving_average(data, window_size=3)
        self.assertEqual(len(moving_average), 3)

    def test_split_time_series(self):
        """Test splitting a time series into training and testing datasets."""
        data = np.random.rand(100)
        train_data, test_data = QuantumUtils.split_time_series(data)
        self.assertEqual(len(train_data), 80)
        self.assertEqual(len(test_data), 20)

if __name__ == '__main__':
    unittest.main()
