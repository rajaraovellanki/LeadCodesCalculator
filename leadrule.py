import logger
import constants
# class for setting rules for leads


class LeadRule:
    __quantity = constants.DEFAULT_QUANTITY
    __bonus_type = constants.DEFAULT_BONUS_TYPE
    __bonus = constants.DEFAULT_BONUS

    moduleName = '[LeadRule] '
    logging = logger.getLogger()

    def __init__(self, quantity, bonus, bonus_type):
        if isinstance(quantity, int) and (isinstance(bonus, int) or isinstance(bonus, float)) and (bonus_type == constants.BONUS_TYPE_FIXED or bonus_type == constants.BONUS_TYPE_PERCENTAGE):
            self.__quantity = quantity
            self.__bonus = bonus
            self.__bonus_type = bonus_type
        else:
            self.logging.warning(
                self.moduleName+'Incorrect argument types. Please check if quantity is  \'int\', bonus is \'int\' and bonus type is \'fixed\', or \'variable\'')
            raise Exception(
                "Incorrect argument types. Please check if quantity is  \'int\', bonus is \'int\' and bonus type is \'fixed\', or \'variable\'")

    def setMinQuantity(self, quantity):
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            self.logging.warning(
                self.moduleName+'Quantity should be of type: \'int\'')
            raise Exception("Quantity should be of type: \'int\'")

    def setBonusType(self, bonus_type):
        if bonus_type == constants.BONUS_TYPE_FIXED or bonus_type == constants.BONUS_TYPE_PERCENTAGE:
            self.__bonus_type = bonus_type
        else:
            self.logging.warning(
                self.moduleName+'Bonus type should be either \'fixed\', or \'variable\'')
            raise Exception(
                "Bonus type should be either \'fixed\', or \'variable\'")

    def setBonus(self, bonus):
        if isinstance(bonus, int):
            self.__bonus = bonus
        else:
            self.logging.warning(
                self.moduleName+'Bonus should be of type: \'int\'')
            raise Exception("Bonus should be of type: \'int\'")

    def getMinQuantity(self):
        return self.__quantity

    def getBonusType(self):
        return self.__bonus_type

    def getBonus(self):
        return self.__bonus
