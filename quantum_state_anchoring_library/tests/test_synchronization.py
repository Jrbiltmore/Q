
import unittest
from datetime import datetime, timedelta
from quantum_state_anchoring.src.synchronization import QuantumSynchronization

class TestQuantumSynchronization(unittest.TestCase):
    def setUp(self):
        """Set up a synchronization instance"""
        self.synchronization = QuantumSynchronization()

    def test_synchronize_time(self):
        """Test that time is synchronized properly"""
        node_id = 'node_1'
        sync_time = self.synchronization.synchronize_time(node_id)
        self.assertIsInstance(sync_time, datetime, "Synchronization time should be a datetime object")
        self.assertEqual(self.synchronization.get_synchronized_time(node_id), sync_time, "Stored time should match synchronized time")

    def test_adjust_time(self):
        """Test that synchronized time can be adjusted by an offset"""
        node_id = 'node_2'
        initial_time = self.synchronization.synchronize_time(node_id)
        offset = timedelta(seconds=100)
        adjusted_time = self.synchronization.adjust_time(node_id, offset)
        self.assertGreater(adjusted_time, initial_time, "Adjusted time should be greater than initial time")

    def test_check_synchronization(self):
        """Test that synchronization status is checked within a tolerance"""
        node_id = 'node_3'
        self.synchronization.synchronize_time(node_id)
        tolerance = timedelta(seconds=5)
        within_tolerance = self.synchronization.check_synchronization(node_id, tolerance)
        self.assertTrue(within_tolerance, "Node should be within the synchronization tolerance")

    def test_clear_synchronizations(self):
        """Test that all synchronizations can be cleared"""
        self.synchronization.synchronize_time('node_4')
        self.synchronization.clear_synchronizations()
        self.assertIsNone(self.synchronization.get_synchronized_time('node_4'), "Synchronization should be cleared")

if __name__ == '__main__':
    unittest.main()
