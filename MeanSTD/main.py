# main.py
from mean_var_std import calculate
import unittest
import test_module

# Quick manual test
if __name__ == "__main__":
    # Example check
    print("Manual check for [0,1,2,3,4,5,6,7,8]:")
    print(calculate([0,1,2,3,4,5,6,7,8]))
    print("\nRunning unit tests...\n")

    # Run the unit tests
    unittest.main(module=test_module, exit=False)
