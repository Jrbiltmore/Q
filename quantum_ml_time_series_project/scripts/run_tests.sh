#!/bin/bash

# Script to run all test cases for the Quantum ML Time Series Project

# Define the directory for test cases
TEST_DIR="../tests"

# Define the test report directory
REPORT_DIR="../reports/tests"
mkdir -p $REPORT_DIR

# Run unit tests with pytest and generate a test report
echo "Running unit tests..."
pytest $TEST_DIR --junitxml=$REPORT_DIR/unit_test_report.xml

# Check if the unit tests passed
if [ $? -eq 0 ]; then
    echo "Unit tests passed!"
else
    echo "Some unit tests failed. Check the report for details: $REPORT_DIR/unit_test_report.xml"
    exit 1
fi

# Optional: Add coverage testing
echo "Generating test coverage report..."
pytest --cov=$TEST_DIR --cov-report=html:$REPORT_DIR/coverage_html --cov-report=xml:$REPORT_DIR/coverage.xml

# Display completion message
echo "Test execution completed. Check the reports in the $REPORT_DIR folder."
