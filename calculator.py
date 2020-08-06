"""This is the main module which calculates the total pricing\
based on the provided pricing rules"""
from __future__ import division
import logger
import constants

class Calculator:
    """Calculator class constructor takes the object of PricingRules\
    as an argument. This is the class which calculates the total price"""
    __total_buys = 0
    __total_rents = 0
    __total_short_terms = 0
    __total_price = 0

    moduleName = '[Calculator] '
    logging = logger.get_logger()

    def __init__(self, pricing_rules):
        """Constructor to assign pricing rules"""
        self.__pricing_rules = pricing_rules
        self.logging.debug(
            self.moduleName +
            'The provided pricing rules have been assigned successfully')

    def add(self, lead_code):
        """Function to add a leadcode"""
        if lead_code == constants.IS_BUY:
            self.__total_buys += 1
            self.logging.info(self.moduleName + 'Lead code \'' + lead_code +
                              '\' has been added')
        elif lead_code == constants.IS_RENT:
            self.__total_rents += 1
            self.logging.info(self.moduleName + 'Lead code \'' + lead_code +
                              '\' has been added')
        elif lead_code == constants.IS_SHORT_TERM:
            self.__total_short_terms += 1
            self.logging.info(self.moduleName + 'Lead code \'' + lead_code +
                              '\' has been added')
        else:
            self.logging.warning(self.moduleName + 'Lead code \'' + lead_code +
                                 '\' has not been accepted. Please provide \
                                     one of the following lead codes: \'b\', \'r\', \'st\''
                                 )
            raise Exception(
                "Lead code \''+LeadCode+'\' has not been accepted. Please \
                    provide one of the following lead codes: \'b\', \'r\', \'st\'"
            )

    def total(self):
        """Function to calculate the total pricing using the assigned pricing rules"""
        if self.__total_buys >= self.__pricing_rules.get_buy_bonus_rule(
        ).get_min_quantity():
            if self.__pricing_rules.get_buy_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_FIXED:
                self.logging.debug(
                    self.moduleName + 'Applying the rule: \
                    For the number of buyers above ' +
                    str(self.__pricing_rules.get_buy_bonus_rule().get_min_quantity(
                    )) + ', add a fixed amount of $' +
                    str(self.__pricing_rules.get_buy_bonus_rule().get_bonus()))
                self.__total_price += self.__total_buys*constants.B_PRICE + \
                    self.__pricing_rules.get_buy_bonus_rule().get_bonus()
            elif self.__pricing_rules.get_buy_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(
                    self.moduleName +
                    'Applying the rule: For the number of buyers above ' +
                    str(self.__pricing_rules.get_buy_bonus_rule().get_min_quantity(
                    )) + ', add a variable pay of ' +
                    str(self.__pricing_rules.get_buy_bonus_rule().get_bonus()) +
                    "% on the base pay")
                self.__total_price += self.__total_buys*constants.B_PRICE + \
                    self.__pricing_rules.get_buy_bonus_rule().get_bonus()*self.__total_buys * \
                    constants.B_PRICE/100
        else:
            self.logging.debug(
                self.moduleName +
                'No rule is applicable for the present amount of buyers ')
            self.__total_price += self.__total_buys * constants.B_PRICE

        if self.__total_rents >= self.__pricing_rules.get_rent_bonus_rule(
        ).get_min_quantity():
            if self.__pricing_rules.get_rent_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_FIXED:
                self.logging.debug(
                    self.moduleName +
                    'Applying the rule: For the number of rents above ' +
                    str(self.__pricing_rules.get_rent_bonus_rule().get_min_quantity(
                    )) + ', add a fixed amount of $' +
                    str(self.__pricing_rules.get_rent_bonus_rule().get_bonus()))
                self.__total_price += self.__total_rents*constants.R_PRICE + \
                    self.__pricing_rules.get_rent_bonus_rule().get_bonus()
            elif self.__pricing_rules.get_rent_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(
                    self.moduleName +
                    'Applying the rule: For the number of rents above ' +
                    str(self.__pricing_rules.get_rent_bonus_rule().get_min_quantity(
                    )) + ', add a variable pay of ' +
                    str(self.__pricing_rules.get_rent_bonus_rule().get_bonus()) +
                    "% on the base pay")
                self.__total_price += self.__total_rents*constants.R_PRICE + \
                    self.__pricing_rules.get_rent_bonus_rule().get_bonus()*self.__total_rents * \
                    constants.R_PRICE/100
        else:
            self.logging.debug(
                self.moduleName +
                'No rule is applicable for the present amount of rents ')
            self.__total_price += self.__total_rents * constants.R_PRICE

        if self.__total_short_terms >= self.__pricing_rules.get_st_bonus_rule(
        ).get_min_quantity():
            if self.__pricing_rules.get_st_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_FIXED:
                self.logging.debug(
                    self.moduleName +
                    'Applying the rule: For the number of short term leases above '
                    + str(self.__pricing_rules.get_st_bonus_rule().get_min_quantity(
                    )) + ', add a fixed amount of $' +
                    str(self.__pricing_rules.get_st_bonus_rule().get_bonus()))
                self.__total_price += self.__total_short_terms*constants.ST_PRICE + \
                    self.__pricing_rules.get_st_bonus_rule().get_bonus()
            elif self.__pricing_rules.get_st_bonus_rule().get_bonus_type(
            ) == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(
                    self.moduleName +
                    'Applying the rule: For the number of short term leases above '
                    + str(self.__pricing_rules.get_st_bonus_rule().get_min_quantity(
                    )) + ', add a variable pay of ' +
                    str(self.__pricing_rules.get_st_bonus_rule().get_bonus()) +
                    "% on the base pay")
                self.__total_price += self.__total_short_terms*constants.ST_PRICE + \
                    self.__pricing_rules.get_st_bonus_rule().get_bonus()*self.__total_short_terms * \
                    constants.ST_PRICE/100
        else:
            self.logging.debug(
                self.moduleName +
                'No rule is applicable for the present amount of short term lease'
            )
            self.__total_price += self.__total_short_terms * constants.ST_PRICE

        self.logging.debug(self.moduleName + 'Total price is $' +
                           str(self.__total_price))
        return self.__total_price
