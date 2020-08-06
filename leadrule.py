"""Thid module is for setting and providing the bonus rules"""
import logger
import constants


class LeadRule:
    """class for setting rules for leads"""
    __min_quantity = constants.DEFAULT_QUANTITY
    __bonus_type = constants.DEFAULT_BONUS_TYPE
    __bonus = constants.DEFAULT_BONUS

    moduleName = '[LeadRule] '
    logging = logger.get_logger()

    def __init__(self, min_quantity, bonus, bonus_type):
        """Constructor which accepts the quantity, bonus and bonus type"""
        if isinstance(min_quantity, int) and isinstance(
                bonus,
                (float, int)) and bonus_type in (constants.BONUS_TYPE_FIXED,
                                                 constants.BONUS_TYPE_PERCENTAGE):
            if min_quantity < 0 or bonus < 0:
                raise ValueError("Quantity should be greater than 0")
            self.__min_quantity = min_quantity
            self.__bonus = bonus
            self.__bonus_type = bonus_type
        else:
            self.logging.warning(
                self.moduleName +
                'Incorrect argument types. Please check if quantity is  \'int\',\
                     bonus is \'int\' and bonus type is \'fixed\', or \'variable\''
            )
            raise TypeError(
                "Incorrect argument types. Please check if quantity is  \'int\',\
                     bonus is \'int\' and bonus type is \'fixed\', or \'variable\'"
            )

    def set_min_quantity(self, min_quantity):
        """Function to set the quantity"""
        if isinstance(min_quantity, int):
            self.__min_quantity = min_quantity
        else:
            self.logging.warning(self.moduleName +
                                 'Quantity should be of type: \'int\'')
            raise TypeError("Quantity should be of type: \'int\'")

    def set_bonus_type(self, bonus_type):
        """Function to set the bonus type"""
        if bonus_type in (constants.BONUS_TYPE_FIXED,
                          constants.BONUS_TYPE_PERCENTAGE):
            self.__bonus_type = bonus_type
        else:
            self.logging.warning(
                self.moduleName +
                'Bonus type should be either \'fixed\', or \'variable\'')
            raise ValueError(
                "Bonus type should be either \'fixed\', or \'variable\'")

    def set_bonus(self, bonus):
        """Function to set the bonus"""
        if isinstance(bonus, int):
            self.__bonus = bonus
        else:
            self.logging.warning(self.moduleName +
                                 'Bonus should be of type: \'int\'')
            raise TypeError("Bonus should be of type: \'int\'")

    def get_min_quantity(self):
        """Function to provide the quantity"""
        return self.__min_quantity

    def get_bonus_type(self):
        """Function to provide the bonus type"""
        return self.__bonus_type

    def get_bonus(self):
        """Function to provide the bonus"""
        return self.__bonus
