import logger
import leadrule
import pricingrules

class Calculator:    
    __b=0 
    __r=0 
    __st=0
    __totalPrice = 0
	
    moduleName='[Calculator] '
    logging = logger.getLogger()
        
    #Constructor to assign pricing rules
    def __init__(self, pricing_rules):        
        self.__pricing_rules = pricing_rules
        self.logging.debug(self.moduleName+'The provided pricing rules have been assigned successfully')
                
    #function to add a leadcode
    def add(self, LeadCode):
        if LeadCode == 'b':
            self.__b += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')			
        elif LeadCode == 'r':
            self.__r += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')
        elif LeadCode == 'st':
            self.__st += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')
        else:
            self.logging.warning(self.moduleName+'Lead code \''+LeadCode+'\' has not been accepted. Please provide one of the following lead codes: \'b\', \'r\', \'st\'')
        
        
    #function to calculate the total pricing using the assigned pricing rules
    def total(self):
        if self.__b >= self.__pricing_rules.getBRule().getQuantity():
            if self.__pricing_rules.getBRule().getIncrementType() == "fixed":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(self.__pricing_rules.getBRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getBRule().getIncrement()))
                self.__totalPrice += self.__b*10 + self.__pricing_rules.getBRule().getIncrement()
            elif self.__pricing_rules.getBRule().getIncrementType() == "variable":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(self.__pricing_rules.getBRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getBRule().getIncrement()+"% on the base pay"))
                self.__totalPrice += self.__b*10 + self.__pricing_rules.getBRule().getIncrement()*self.__b*10/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of buyers ')
            self.__totalPrice += self.__b*10
            
        if self.__r >= self.__pricing_rules.getRRule().getQuantity():
            if self.__pricing_rules.getRRule().getIncrementType() == "fixed":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(self.__pricing_rules.getRRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getRRule().getIncrement()))
                self.__totalPrice += self.__r*5 + self.__pricing_rules.getRRule().getIncrement()
            elif self.__pricing_rules.getRRule().getIncrementType() == "variable":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(self.__pricing_rules.getRRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getRRule().getIncrement()+"% on the base pay"))
                self.__totalPrice += self.__r*5 + self.__pricing_rules.getRRule().getIncrement()*self.__r*5/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of rents ')
            self.__totalPrice += self.__r*5            
            
        if self.__st >= self.__pricing_rules.getSTRule().getQuantity():
            if self.__pricing_rules.getSTRule().getIncrementType() == "fixed":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(self.__pricing_rules.getSTRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getSTRule().getIncrement()))
                self.__totalPrice += self.__st*2.5 + self.__pricing_rules.getSTRule().getIncrement()
            elif self.__pricing_rules.getSTRule().getIncrementType() == "variable":
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(self.__pricing_rules.getSTRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getSTRule().getIncrement()+"% on the base pay"))
                self.__totalPrice += self.__st*2.5 + self.__pricing_rules.getSTRule().getIncrement()*self.__st*2.5/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of short term lease')
            self.__totalPrice += self.__st*2.5            

        self.logging.debug(self.moduleName+'Total price is $'+str(self.__totalPrice))            
        return self.__totalPrice