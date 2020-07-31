import logger
import leadrule
import pricingrules
import calculator
import constants


#Test the program with some rules
if constants.TEST_WRONG_INPUT == "false":
    # Passing correct data
    bRule = leadrule.LeadRule(5, 10, constants.INCREMENT_TYPE_FIXED)
    rRule = leadrule.LeadRule(8, 10, constants.INCREMENT_TYPE_VARIABLE)
else:
    #Set wrong data types to check how the program behaves
    rRule = leadrule.LeadRule(8.65, 'as', 'variab')

#Add the rules
pricing_rules = pricingrules.PricingRules()
pricing_rules.setBRule(bRule)
pricing_rules.setRRule(rRule)

#Add the Lead codes
calc = calculator.Calculator(pricing_rules)

if constants.TEST_WRONG_INPUT == "false":
    for x in range(10):
        calc.add(constants.B)

    for x in range(9):
        calc.add(constants.R)

    for x in range(5):
        calc.add(constants.ST)
else:
    calc.add('bb')
    calc.add('sst')
    calc.add('brs')

print(calc.total())