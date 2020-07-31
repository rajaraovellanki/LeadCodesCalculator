import logger
import leadrule
import pricingrules
import calculator

#Test the program with some rules
bRule = leadrule.LeadRule()
bRule.setQuantity(5)
bRule.setIncrement(10)
bRule.setIncrementType("fixed")

rRule = leadrule.LeadRule()
rRule.setQuantity(8)
rRule.setIncrement(10)
rRule.setIncrementType("variable")

#Set wrong data types to check how the program behaves
rRule.setQuantity(8.65)
rRule.setIncrement('as')
rRule.setIncrementType("variab")

#Add the rules
pricing_rules = pricingrules.PricingRules()
pricing_rules.setBRule(bRule)
pricing_rules.setRRule(rRule)

#Add the Lead codes
calculator = calculator.Calculator(pricing_rules)
calculator.add('b')
calculator.add('b')
calculator.add('b')
calculator.add('b')
calculator.add('b')
calculator.add('b')

calculator.add('r')
calculator.add('r')

calculator.add('st')
calculator.add('s')

print(calculator.total())