
import unittest
import numpy as np
from src.quantum_feature_extraction import QuantumFeatureExtraction

class TestQuantumFeatureExtraction(unittest.TestCase):
    def setUp(self):
        """Initialize the Quantum Feature Extraction model with default parameters."""
        self.num_qubits = 3
        self.feature_extractor = QuantumFeatureExtraction(num_qubits=self.num_qubits)

    def test_extract_principal_components(self):
        """Test if principal components are extracted correctly using PCA."""
        data = np.random.rand(100, self.num_qubits)
        components = self.feature_extractor.extract_principal_components(data, n_components=2)
        self.assertEqual(components.shape, (100, 2))

    def test_quantum_mutual_information(self):
        """Test calculation of mutual information between features and target."""
        X = np.random.rand(100, self.num_qubits)
        y = np.random.randint(0, 2, size=100)
        mi = self.feature_extractor.quantum_mutual_information(X, y)
        self.assertEqual(len(mi), self.num_qubits)

    def test_apply_quantum_entanglement(self):
        """Test transformation of features using quantum entanglement operations."""
        data = np.random.rand(100, self.num_qubits)
        entangled_data = self.feature_extractor.apply_quantum_entanglement(data)
        self.assertEqual(entangled_data.shape, (100, self.num_qubits))

    def test_extract_temporal_quantum_features(self):
        """Test extraction of temporal quantum-specific features from time series data."""
        time_series_data = np.random.rand(100)
        temporal_features = self.feature_extractor.extract_temporal_quantum_features(time_series_data, look_back=3)
        self.assertEqual(temporal_features.shape[0], 100 - 3)

    def test_save_and_load_features(self):
        """Test saving and loading extracted features from a file."""
        data = np.random.rand(100, self.num_qubits)
        path = 'test_features.npy'
        self.feature_extractor.save_features(data, path)
        loaded_features = self.feature_extractor.load_features(path)
        self.assertTrue(np.array_equal(data, loaded_features))

if __name__ == '__main__':
    unittest.main()
