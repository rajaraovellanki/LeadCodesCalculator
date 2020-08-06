"""This module is used for setting and providing the pricing rules"""
import leadrule
import logger
import constants


class PricingRules:
    """Class for setting overall pricing rules"""
    __buy_bonus_rule = leadrule.LeadRule(constants.DEFAULT_QUANTITY,
                                         constants.DEFAULT_BONUS,
                                         constants.DEFAULT_BONUS_TYPE)
    __rent_bonus_rule = leadrule.LeadRule(constants.DEFAULT_QUANTITY,
                                          constants.DEFAULT_BONUS,
                                          constants.DEFAULT_BONUS_TYPE)
    __st_bonus_rule = leadrule.LeadRule(constants.DEFAULT_QUANTITY,
                                        constants.DEFAULT_BONUS,
                                        constants.DEFAULT_BONUS_TYPE)

    moduleName = '[PricingRules] '
    logging = logger.get_logger()

    def set_buy_bonus_rule(self, buy_bonus_rule):
        """Function for setting the buy bonus rule"""
        if isinstance(buy_bonus_rule, leadrule.LeadRule):
            self.logging.debug(self.moduleName +
                               'Setting the pricing rule for Buys')
            self.__buy_bonus_rule = buy_bonus_rule
        else:
            raise TypeError(
                "The type of the argument buy_bonus_rule is not LeadRule")

    def set_rent_bonus_rule(self, rent_bonus_rule):
        """Function for setting the rent bonus rule"""
        if isinstance(rent_bonus_rule, leadrule.LeadRule):
            self.logging.debug(self.moduleName +
                               'Setting the pricing rule for Rents')
            self.__rent_bonus_rule = rent_bonus_rule
        else:
            raise TypeError(
                "The type of the argument rent_bonus_rule is not LeadRule")

    def set_st_bonus_rule(self, st_bonus_rule):
        """Function for setting the short term bonus rule"""
        if isinstance(st_bonus_rule, leadrule.LeadRule):
            self.logging.debug(
                self.moduleName +
                'Setting the pricing rule for Short term leases')
            self.__st_bonus_rule = st_bonus_rule
        else:
            raise TypeError(
                "The type of the argument st_bonus_rule is not LeadRule")

    def get_buy_bonus_rule(self):
        """Function for providing the buy bonus rule"""
        return self.__buy_bonus_rule

    def get_rent_bonus_rule(self):
        """Function for providing the rent bonus rule"""
        return self.__rent_bonus_rule

    def get_st_bonus_rule(self):
        """Function for providing the short term bonus rule"""
        return self.__st_bonus_rule
