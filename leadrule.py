import logger
#class for setting rules for leads
class LeadRule:
    __quantity = 0
    __incrementType = "fixed"
    __increment = 0

    moduleName='[LeadRule] '
    logging = logger.getLogger()	
    logging = logger.getLogger()
    
    def setQuantity(self, quantity):
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            self.logging.warning(self.moduleName+'Quantity should be of type: \'int\'')
        
    def setIncrementType(self, incrementType):
        if incrementType == "fixed" or incrementType == "variable" :
            self.__incrementType = incrementType
        else:
            self.logging.warning(self.moduleName+'Increment type should be either \'fixed\', or \'variable\'')

    def setIncrement(self, increment):
        if isinstance(increment, int):
            self.__increment = increment
        else:
            self.logging.warning(self.moduleName+'Increment should be of type: \'int\'')
                
    def getQuantity(self):
        return self.__quantity
        
    def getIncrementType(self):
        return self.__incrementType

    def getIncrement(self):
        return self.__increment