
import numpy as np
import pandas as pd
from qiskit import QuantumCircuit

class QuantumDataLoader:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits

    def load_csv(self, file_path):
        """Loads time series data from a CSV file."""
        return pd.read_csv(file_path)

    def load_from_quantum_circuit(self, quantum_circuit: QuantumCircuit):
        """Convert quantum circuit measurements into classical data."""
        job = execute(quantum_circuit, backend=Aer.get_backend('qasm_simulator'), shots=1024)
        result = job.result()
        counts = result.get_counts()
        data = [int(state, 2) for state, _ in counts.items()]
        return np.array(data)

    def preprocess(self, data, scale=True):
        """Preprocess the data by scaling and reshaping for quantum models."""
        if scale:
            from sklearn.preprocessing import MinMaxScaler
            scaler = MinMaxScaler()
            data = scaler.fit_transform(data)
        return data.reshape(-1, self.num_qubits)

    def split_train_test(self, data, test_size=0.2):
        """Split the data into training and testing sets."""
        num_train = int((1 - test_size) * len(data))
        return data[:num_train], data[num_train:]

    def batch_generator(self, data, batch_size):
        """Generates batches of data for quantum models."""
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]

    def load_quantum_state(self, quantum_state, shots=1024):
        """Load a quantum state and return measurement results as classical data."""
        backend = Aer.get_backend('qasm_simulator')
        job = execute(quantum_state, backend, shots=shots)
        result = job.result()
        counts = result.get_counts()
        classical_data = [int(state, 2) for state in counts.keys()]
        return np.array(classical_data)

    def augment_data(self, data, augmentation_factor=2):
        """Applies data augmentation techniques to time series data."""
        augmented_data = []
        for i in range(augmentation_factor):
            noise = np.random.normal(0, 0.1, data.shape)
            augmented_data.append(data + noise)
        return np.vstack(augmented_data)

    def save_processed_data(self, data, file_path):
        """Saves preprocessed data to a CSV file."""
        pd.DataFrame(data).to_csv(file_path, index=False)

    def load_from_qiskit_backend(self, backend_name, shots=1024):
        """Loads quantum data from a Qiskit backend."""
        backend = Aer.get_backend(backend_name)
        quantum_circuit = QuantumCircuit(self.num_qubits)
        job = execute(quantum_circuit, backend, shots=shots)
        result = job.result()
        counts = result.get_counts()
        return np.array([int(state, 2) for state in counts.keys()])

    def time_series_from_quantum_data(self, quantum_data, look_back=3):
        """Generates time series data from quantum measurements."""
        time_series_data = []
        for i in range(len(quantum_data) - look_back):
            time_series_data.append(quantum_data[i:i + look_back])
        return np.array(time_series_data)
