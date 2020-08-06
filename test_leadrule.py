"""This module is for testing the lead rule functionality"""
import unittest

from leadrule import LeadRule

class TestLeadRule(unittest.TestCase):
    """Class to test the lead rule functionality"""
    def test_constructor(self):
        """Function to test the constructor with wrong values"""
        self.assertRaises(ValueError, LeadRule, -1, 1, "fixed")
        self.assertRaises(ValueError, LeadRule, 1, -1, "fixed")
        self.assertRaises(TypeError, LeadRule, 1.1, 1, "fixed")
        self.assertRaises(TypeError, LeadRule, 1, "aa", "fixed")
        self.assertRaises(TypeError, LeadRule, 1, 1, "fix")
