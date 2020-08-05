import logger
import leadrule
import pricingrules
import calculator
import constants

TOTAL_NUMBER_OF_BUYS = 10
TOTAL_NUMBER_OF_RENTS = 9
TOTAL_NUMBER_OF_SHORT_TERM = 5

#Test the program with some rules
if constants.TEST_WRONG_INPUT == False:
    # Passing correct data
    buy_bonus_rule = leadrule.LeadRule(5, 10, constants.BONUS_TYPE_FIXED)
    rent_bonus_rule = leadrule.LeadRule(8, 10, constants.BONUS_TYPE_PERCENTAGE)
else:
    #Set wrong data types to check how the program behaves
    rent_bonus_rule = leadrule.LeadRule(8.65, 'as', 'variab')

#Add the rules
pricing_rules = pricingrules.PricingRules()
pricing_rules.setBuyBonusRule(buy_bonus_rule)
pricing_rules.setRentBonusRule(rent_bonus_rule)

#Add the Lead codes
calc = calculator.Calculator(pricing_rules)

if constants.TEST_WRONG_INPUT == False:
    for x in range(TOTAL_NUMBER_OF_BUYS):
        calc.add(constants.IS_BUY)

    for x in range(TOTAL_NUMBER_OF_RENTS):
        calc.add(constants.IS_RENT)

    for x in range(TOTAL_NUMBER_OF_SHORT_TERM):
        calc.add(constants.IS_SHORT_TERM)
else:
    calc.add('bb')
    calc.add('sst')
    calc.add('brs')

print(calc.total())
