
import unittest
import numpy as np
from src.time_loop_learning import TimeLoopLearning

class TestTimeLoopLearning(unittest.TestCase):
    def setUp(self):
        """Initialize the Time Loop Learning model with default parameters."""
        self.num_qubits = 3
        self.time_loop_model = TimeLoopLearning(num_qubits=self.num_qubits)

    def test_loop_time(self):
        """Test the time-loop process by comparing states and rewards."""
        state = np.array([0, 1, 1])
        future_state = np.array([1, 0, 1])
        reward = self.time_loop_model.loop_time(state, future_state)
        self.assertIsInstance(reward, float)

    def test_memory_storage(self):
        """Test if the model correctly stores past and future states in memory."""
        state = np.array([0, 1, 1])
        future_state = np.array([1, 0, 1])
        self.time_loop_model.loop_time(state, future_state)
        self.assertEqual(len(self.time_loop_model.memory), 1)

    def test_memory_limit(self):
        """Test if the time-loop memory respects its size limit."""
        for _ in range(self.time_loop_model.max_time_loops + 2):
            self.time_loop_model.loop_time(np.random.randint(2, size=self.num_qubits), np.random.randint(2, size=self.num_qubits))
        self.assertEqual(len(self.time_loop_model.memory), self.time_loop_model.max_time_loops)

    def test_save_and_load_memory(self):
        """Test saving and loading the time-loop memory to and from a file."""
        state = np.array([0, 1, 1])
        future_state = np.array([1, 0, 1])
        self.time_loop_model.loop_time(state, future_state)
        path = 'test_time_loop_memory.npy'
        self.time_loop_model.save_memory(path)
        loaded_model = TimeLoopLearning(num_qubits=self.num_qubits)
        loaded_model.load_memory(path)
        self.assertEqual(len(loaded_model.memory), 1)

if __name__ == '__main__':
    unittest.main()
