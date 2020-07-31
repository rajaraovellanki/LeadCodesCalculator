import leadrule
import logger
#class for setting overall pricing rules
class PricingRules:
    __bRule = leadrule.LeadRule()
    __rRule = leadrule.LeadRule()
    __stRule = leadrule.LeadRule()

    moduleName='[PricingRules] '
    logging = logger.getLogger()
    logging = logger.getLogger()
    
    def setBRule(self, bRule):
        self.logging.debug(self.moduleName+'Setting the pricing rule for Buys')
        self.__bRule = bRule
        
    def setRRule(self, rRule):
        self.logging.debug(self.moduleName+'Setting the pricing rule for Rents')
        self.__rRule = rRule

    def setSTRule(self, stRule):
        self.logging.debug(self.moduleName+'Setting the pricing rule for Short term leases')
        self.__stRule = stRule
                
    def getBRule(self):
        return self.__bRule
        
    def getRRule(self):
        return self.__rRule

    def getSTRule(self):
        return self.__stRule  