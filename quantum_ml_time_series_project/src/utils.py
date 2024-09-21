
import numpy as np
import logging
import os

class QuantumUtils:
    @staticmethod
    def normalize_data(data):
        """Normalize the data to a range between 0 and 1."""
        min_val = np.min(data)
        max_val = np.max(data)
        return (data - min_val) / (max_val - min_val)

    @staticmethod
    def setup_logging(log_file='quantum_ml.log'):
        """Setup logging configuration for the project."""
        logging.basicConfig(
            filename=log_file,
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    @staticmethod
    def create_directory(directory):
        """Create a directory if it doesn't exist."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def save_numpy_array(array, file_path):
        """Save a NumPy array to a binary file."""
        np.save(file_path, array)

    @staticmethod
    def load_numpy_array(file_path):
        """Load a NumPy array from a binary file."""
        return np.load(file_path)

    @staticmethod
    def calculate_moving_average(data, window_size=3):
        """Calculate the moving average of a given dataset."""
        return np.convolve(data, np.ones(window_size), 'valid') / window_size

    @staticmethod
    def split_time_series(data, split_ratio=0.8):
        """Split the time series data into training and testing datasets."""
        split_index = int(len(data) * split_ratio)
        return data[:split_index], data[split_index:]

    @staticmethod
    def get_logger(name):
        """Get a logger instance."""
        return logging.getLogger(name)
