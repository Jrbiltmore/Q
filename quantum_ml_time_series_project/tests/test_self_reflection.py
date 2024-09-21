
import unittest
import numpy as np
from src.self_reflection import QuantumSelfReflection

class TestQuantumSelfReflection(unittest.TestCase):
    def setUp(self):
        """Initialize the Quantum Self Reflection model with default parameters."""
        self.num_qubits = 2
        self.reflection_model = QuantumSelfReflection(num_qubits=self.num_qubits)

    def test_reflect(self):
        """Test if the model successfully reflects on a given state and action."""
        state = np.array([0, 1])
        action = 1
        reward = self.reflection_model.reflect(state, action)
        self.assertIsInstance(reward, float)

    def test_memory_storage(self):
        """Test if the model correctly stores state-action pairs in memory."""
        state = np.array([0, 1])
        action = 1
        self.reflection_model.reflect(state, action)
        self.assertEqual(len(self.reflection_model.memory), 1)

    def test_memory_limit(self):
        """Test if the memory respects the size limit by removing old entries."""
        for _ in range(self.reflection_model.memory_size + 2):
            self.reflection_model.reflect(np.random.randint(2, size=self.num_qubits), 1)
        self.assertEqual(len(self.reflection_model.memory), self.reflection_model.memory_size)

    def test_save_and_load_memory(self):
        """Test saving and loading reflection memory from a file."""
        state = np.array([0, 1])
        action = 1
        self.reflection_model.reflect(state, action)
        path = 'test_reflection_memory.npy'
        self.reflection_model.save_memory(path)
        loaded_model = QuantumSelfReflection(num_qubits=self.num_qubits)
        loaded_model.load_memory(path)
        self.assertEqual(len(loaded_model.memory), 1)

if __name__ == '__main__':
    unittest.main()
