import sys
import subprocess

def run_tests():
    # Runs pytest and returns True if all pass
    result = subprocess.run(["pytest", "tests/test_calculator.py"], capture_output=True)
    return result.returncode == 0

if __name__ == "__main__":
    if run_tests():
        print("Verification Successful: Green")
        sys.exit(0)
    else:
        print("Verification Failed: Red")
        sys.exit(1)
