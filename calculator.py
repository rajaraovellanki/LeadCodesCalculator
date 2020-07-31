import logger
import leadrule
import pricingrules
import constants

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
        if LeadCode == constants.B:
            self.__b += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')			
        elif LeadCode == constants.R:
            self.__r += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')
        elif LeadCode == constants.ST:
            self.__st += 1
            self.logging.info(self.moduleName+'Lead code \''+LeadCode+'\' has been added')
        else:
            self.logging.warning(self.moduleName+'Lead code \''+LeadCode+'\' has not been accepted. Please provide one of the following lead codes: \'b\', \'r\', \'st\'')
            raise Exception("Lead code \''+LeadCode+'\' has not been accepted. Please provide one of the following lead codes: \'b\', \'r\', \'st\'")
        
        
    #function to calculate the total pricing using the assigned pricing rules
    def total(self):
        if self.__b >= self.__pricing_rules.getBRule().getQuantity():
            if self.__pricing_rules.getBRule().getIncrementType() == constants.INCREMENT_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(self.__pricing_rules.getBRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getBRule().getIncrement()))
                self.__totalPrice += self.__b*constants.B_PRICE + self.__pricing_rules.getBRule().getIncrement()
            elif self.__pricing_rules.getBRule().getIncrementType() == constants.INCREMENT_TYPE_VARIABLE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(self.__pricing_rules.getBRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getBRule().getIncrement())+"% on the base pay")
                self.__totalPrice += self.__b*constants.B_PRICE + self.__pricing_rules.getBRule().getIncrement()*self.__b*constants.B_PRICE/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of buyers ')
            self.__totalPrice += self.__b*constants.B_PRICE
            
        if self.__r >= self.__pricing_rules.getRRule().getQuantity():
            if self.__pricing_rules.getRRule().getIncrementType() == constants.INCREMENT_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(self.__pricing_rules.getRRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getRRule().getIncrement()))
                self.__totalPrice += self.__r*constants.R_PRICE + self.__pricing_rules.getRRule().getIncrement()
            elif self.__pricing_rules.getRRule().getIncrementType() == constants.INCREMENT_TYPE_VARIABLE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(self.__pricing_rules.getRRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getRRule().getIncrement())+"% on the base pay")
                self.__totalPrice += self.__r*constants.R_PRICE + self.__pricing_rules.getRRule().getIncrement()*self.__r*constants.R_PRICE/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of rents ')
            self.__totalPrice += self.__r*constants.R_PRICE            
            
        if self.__st >= self.__pricing_rules.getSTRule().getQuantity():
            if self.__pricing_rules.getSTRule().getIncrementType() == constants.INCREMENT_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(self.__pricing_rules.getSTRule().getQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getSTRule().getIncrement()))
                self.__totalPrice += self.__st*constants.ST_PRICE + self.__pricing_rules.getSTRule().getIncrement()
            elif self.__pricing_rules.getSTRule().getIncrementType() == constants.INCREMENT_TYPE_VARIABLE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(self.__pricing_rules.getSTRule().getQuantity())+', add a variable pay of '+str(self.__pricing_rules.getSTRule().getIncrement())+"% on the base pay")
                self.__totalPrice += self.__st*constants.ST_PRICE + self.__pricing_rules.getSTRule().getIncrement()*self.__st*constants.ST_PRICE/100
        else:
            self.logging.debug(self.moduleName+'No rule is applicable for the present amount of short term lease')
            self.__totalPrice += self.__st*constants.ST_PRICE            

        self.logging.debug(self.moduleName+'Total price is $'+str(self.__totalPrice))            
        return self.__totalPrice