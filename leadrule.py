import logger
import constants
#class for setting rules for leads
class LeadRule:
    __quantity = constants.DEFAULT_QUANTITY
    __incrementType = constants.DEFAULT_INCREMENT_TYPE
    __increment = constants.DEFAULT_INCREMENT

    moduleName='[LeadRule] '
    logging = logger.getLogger()

    def __init__(self, quantity, increment, incrementType):
        if isinstance(quantity, int) and isinstance(increment, int) and (incrementType == constants.INCREMENT_TYPE_FIXED or incrementType == constants.INCREMENT_TYPE_VARIABLE):
            self.__quantity = quantity
            self.__increment = increment
            self.__incrementType = incrementType
        else:
            self.logging.warning(self.moduleName+'Incorrect argument types. Please check if quantity is  \'int\', increment is \'int\' and increment type is \'fixed\', or \'variable\'')
            raise Exception("Incorrect argument types. Please check if quantity is  \'int\', increment is \'int\' and increment type is \'fixed\', or \'variable\'")
    
    def setQuantity(self, quantity):
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            self.logging.warning(self.moduleName+'Quantity should be of type: \'int\'')
            raise Exception("Quantity should be of type: \'int\'")
        
    def setIncrementType(self, incrementType):
        if incrementType == constants.INCREMENT_TYPE_FIXED or incrementType == constants.INCREMENT_TYPE_VARIABLE :
            self.__incrementType = incrementType
        else:
            self.logging.warning(self.moduleName+'Increment type should be either \'fixed\', or \'variable\'')
            raise Exception("Increment type should be either \'fixed\', or \'variable\'")

    def setIncrement(self, increment):
        if isinstance(increment, int):
            self.__increment = increment
        else:
            self.logging.warning(self.moduleName+'Increment should be of type: \'int\'')
            raise Exception("Increment should be of type: \'int\'")
                
    def getQuantity(self):
        return self.__quantity
        
    def getIncrementType(self):
        return self.__incrementType

    def getIncrement(self):
        return self.__increment