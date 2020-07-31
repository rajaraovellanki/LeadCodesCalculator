# LeadCodesCalculator

User can add the rules in the file main_calc.py. This file will call the main module Calculator where the actual calculations happen.


To run the program, use the below command:
py main_calc.py


The logs will be generated in the logs directory with the name app.log. 
By default, the logs are in DEBUG mode. You can change the mode to INFO or WARNING by changing the level in logger.py file.
Eg:
level=logging.INFO


### Code Structure:

 - pricingrules.py has the class PricingRules which is used to set and get the required rules for all the lead codes
 - leadrule.py has the class LeadRule which is used to set the rules for a particular lead code. 
 - User needs to set the quantity(by which the rule should be applied), the type of the increment(fixed or variable) and the increment value in the leadrule.py for each leat rule that is defined in the pricingrules.py

> Eg 1:
> For  the rule  - providing more than 5 buy leads gives us a £10 bonus,
> quantity = 5, 
> incrementType = "fixed", 
> increment = 10

> Eg 2:
> For the rule  - providing more than 8 rent leads we get a 10% bonus on total base price,
> quantity = 8,
> incrementType = "variable",
> increment = 10

 - calculator.py is the main module which calculates the total pricing based on the provided pricing rules
