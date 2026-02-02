# test_hubfoundry.py
"""
Tests for HubFoundry module.
"""

import unittest
from hubfoundry import HubFoundry

class TestHubFoundry(unittest.TestCase):
    """Test cases for HubFoundry class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HubFoundry()
        self.assertIsInstance(instance, HubFoundry)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HubFoundry()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
