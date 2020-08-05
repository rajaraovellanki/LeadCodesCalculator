import leadrule
import logger
import constants

#class for setting overall pricing rules


class PricingRules:
    __buy_bonus_rule = leadrule.LeadRule(
        constants.DEFAULT_QUANTITY, constants.DEFAULT_BONUS, constants.DEFAULT_BONUS_TYPE)
    __rent_bonus_rule = leadrule.LeadRule(
        constants.DEFAULT_QUANTITY, constants.DEFAULT_BONUS, constants.DEFAULT_BONUS_TYPE)
    __st_bonus_rule = leadrule.LeadRule(
        constants.DEFAULT_QUANTITY, constants.DEFAULT_BONUS, constants.DEFAULT_BONUS_TYPE)

    moduleName = '[PricingRules] '
    logging = logger.getLogger()

    def setBuyBonusRule(self, buy_bonus_rule):
        self.logging.debug(self.moduleName+'Setting the pricing rule for Buys')
        self.__buy_bonus_rule = buy_bonus_rule

    def setRentBonusRule(self, rent_bonus_rule):
        self.logging.debug(
            self.moduleName+'Setting the pricing rule for Rents')
        self.__rent_bonus_rule = rent_bonus_rule

    def setSTBonusRule(self, st_bonus_rule):
        self.logging.debug(
            self.moduleName+'Setting the pricing rule for Short term leases')
        self.__st_bonus_rule = st_bonus_rule

    def getBuyBonusRule(self):
        return self.__buy_bonus_rule

    def getRentBonusRule(self):
        return self.__rent_bonus_rule

    def getSTBonusRule(self):
        return self.__st_bonus_rule
