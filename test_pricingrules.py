"""This module is for testing the pricing rule functionality"""
import unittest

from pricingrules import PricingRules


class TestPriceRules(unittest.TestCase):
    """Class to test the lead rule functionality"""
    def test_rules(self):
        """Function for testing the set methods with wrong values"""
        self.assertRaises(TypeError, PricingRules.set_buy_bonus_rule, "test")
        self.assertRaises(TypeError, PricingRules.set_rent_bonus_rule, "test")
        self.assertRaises(TypeError, PricingRules.set_st_bonus_rule, "test")
