
from datetime import datetime, timedelta

class QuantumSynchronization:
    def __init__(self):
        self.synchronized_times = {}

    def synchronize_time(self, node_id: str, sync_time: datetime = None):
        """Synchronize a node's quantum system to a given time or the current UTC time"""
        sync_time = sync_time if sync_time else datetime.utcnow()
        self.synchronized_times[node_id] = sync_time
        return sync_time

    def adjust_time(self, node_id: str, time_offset: timedelta):
        """Adjust a node's synchronized time by a given time offset"""
        if node_id in self.synchronized_times:
            self.synchronized_times[node_id] += time_offset
        else:
            raise ValueError(f"Node {node_id} is not synchronized yet.")
        return self.synchronized_times[node_id]

    def get_synchronized_time(self, node_id: str):
        """Retrieve the synchronized time for a specific node"""
        return self.synchronized_times.get(node_id, None)

    def check_synchronization(self, node_id: str, tolerance: timedelta):
        """Check if a node's time is within a given tolerance of UTC"""
        if node_id not in self.synchronized_times:
            return False
        current_time = datetime.utcnow()
        time_diff = abs(current_time - self.synchronized_times[node_id])
        return time_diff <= tolerance

    def clear_synchronizations(self):
        """Clear all synchronized times"""
        self.synchronized_times.clear()
