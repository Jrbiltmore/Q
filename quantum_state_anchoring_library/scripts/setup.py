
from setuptools import setup, find_packages

setup(
    name='quantum_state_anchoring',
    version='1.0.0',
    description='A library for anchoring, verifying, and managing quantum states over time',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'qiskit',
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'run_tests=scripts.run_tests:main',
        ],
    },
)
