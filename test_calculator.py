"""This module is for testing the calculator functionality"""
import unittest

import leadrule
import pricingrules
import calculator
import constants


class TestTotalPricing(unittest.TestCase):
    """This class is for testing the total price"""
    def test_total(self):
        """Function to test the total price"""
        buy_bonus_rule = leadrule.LeadRule(5, 10, constants.BONUS_TYPE_FIXED)
        rent_bonus_rule = leadrule.LeadRule(8, 10,
                                            constants.BONUS_TYPE_PERCENTAGE)

        #Add the rules
        pricing_rules = pricingrules.PricingRules()
        pricing_rules.set_buy_bonus_rule(buy_bonus_rule)
        pricing_rules.set_rent_bonus_rule(rent_bonus_rule)

        #Add the Lead codes
        calc = calculator.Calculator(pricing_rules)

        for _ in range(10):
            calc.add(constants.IS_BUY)
        for _ in range(9):
            calc.add(constants.IS_RENT)
        for _ in range(5):
            calc.add(constants.IS_SHORT_TERM)

        self.assertEqual(calc.total(), 172.0)

    def test_add(self):
        """Function to test the add method with wrong values"""
        buy_bonus_rule = leadrule.LeadRule(5, 10, constants.BONUS_TYPE_FIXED)

        pricing_rules = pricingrules.PricingRules()
        pricing_rules.set_buy_bonus_rule(buy_bonus_rule)

        calc = calculator.Calculator(pricing_rules)

        self.assertRaises(ValueError, calc.add, 'aa')
        self.assertRaises(ValueError, calc.add, 'sts')
