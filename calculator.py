from __future__ import division
import logger
import leadrule
import pricingrules
import constants


class Calculator:
    __total_buys = 0
    __total_rents = 0
    __total_short_terms = 0
    __total_price = 0

    moduleName = '[Calculator] '
    logging = logger.getLogger()

    # Constructor to assign pricing rules
    def __init__(self, pricing_rules):
        self.__pricing_rules = pricing_rules
        self.logging.debug(
            self.moduleName+'The provided pricing rules have been assigned successfully')

    # function to add a leadcode
    def add(self, LeadCode):
        if LeadCode == constants.IS_BUY:
            self.__total_buys += 1
            self.logging.info(self.moduleName+'Lead code \'' +
                              LeadCode+'\' has been added')
        elif LeadCode == constants.IS_RENT:
            self.__total_rents += 1
            self.logging.info(self.moduleName+'Lead code \'' +
                              LeadCode+'\' has been added')
        elif LeadCode == constants.IS_SHORT_TERM:
            self.__total_short_terms += 1
            self.logging.info(self.moduleName+'Lead code \'' +
                              LeadCode+'\' has been added')
        else:
            self.logging.warning(self.moduleName+'Lead code \''+LeadCode +
                                 '\' has not been accepted. Please provide one of the following lead codes: \'b\', \'r\', \'st\'')
            raise Exception(
                "Lead code \''+LeadCode+'\' has not been accepted. Please provide one of the following lead codes: \'b\', \'r\', \'st\'")

    # function to calculate the total pricing using the assigned pricing rules
    def total(self):
        if self.__total_buys >= self.__pricing_rules.getBuyBonusRule().getMinQuantity():
            if self.__pricing_rules.getBuyBonusRule().getBonusType() == constants.BONUS_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(
                    self.__pricing_rules.getBuyBonusRule().getMinQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getBuyBonusRule().getBonus()))
                self.__total_price += self.__total_buys*constants.B_PRICE + \
                    self.__pricing_rules.getBuyBonusRule().getBonus()
            elif self.__pricing_rules.getBuyBonusRule().getBonusType() == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of buyers above '+str(self.__pricing_rules.getBuyBonusRule(
                ).getMinQuantity())+', add a variable pay of '+str(self.__pricing_rules.getBuyBonusRule().getBonus())+"% on the base pay")
                self.__total_price += self.__total_buys*constants.B_PRICE + \
                    self.__pricing_rules.getBuyBonusRule().getBonus()*self.__total_buys * \
                    constants.B_PRICE/100
        else:
            self.logging.debug(
                self.moduleName+'No rule is applicable for the present amount of buyers ')
            self.__total_price += self.__total_buys*constants.B_PRICE

        if self.__total_rents >= self.__pricing_rules.getRentBonusRule().getMinQuantity():
            if self.__pricing_rules.getRentBonusRule().getBonusType() == constants.BONUS_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(
                    self.__pricing_rules.getRentBonusRule().getMinQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getRentBonusRule().getBonus()))
                self.__total_price += self.__total_rents*constants.R_PRICE + \
                    self.__pricing_rules.getRentBonusRule().getBonus()
            elif self.__pricing_rules.getRentBonusRule().getBonusType() == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of rents above '+str(self.__pricing_rules.getRentBonusRule(
                ).getMinQuantity())+', add a variable pay of '+str(self.__pricing_rules.getRentBonusRule().getBonus())+"% on the base pay")
                self.__total_price += self.__total_rents*constants.R_PRICE + \
                    self.__pricing_rules.getRentBonusRule().getBonus()*self.__total_rents * \
                    constants.R_PRICE/100
        else:
            self.logging.debug(
                self.moduleName+'No rule is applicable for the present amount of rents ')
            self.__total_price += self.__total_rents*constants.R_PRICE

        if self.__total_short_terms >= self.__pricing_rules.getSTBonusRule().getMinQuantity():
            if self.__pricing_rules.getSTBonusRule().getBonusType() == constants.BONUS_TYPE_FIXED:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(
                    self.__pricing_rules.getSTBonusRule().getMinQuantity())+', add a fixed amount of $'+str(self.__pricing_rules.getSTBonusRule().getBonus()))
                self.__total_price += self.__total_short_terms*constants.ST_PRICE + \
                    self.__pricing_rules.getSTBonusRule().getBonus()
            elif self.__pricing_rules.getSTBonusRule().getBonusType() == constants.BONUS_TYPE_PERCENTAGE:
                self.logging.debug(self.moduleName+'Applying the rule: For the number of short term leases above '+str(self.__pricing_rules.getSTBonusRule(
                ).getMinQuantity())+', add a variable pay of '+str(self.__pricing_rules.getSTBonusRule().getBonus())+"% on the base pay")
                self.__total_price += self.__total_short_terms*constants.ST_PRICE + \
                    self.__pricing_rules.getSTBonusRule().getBonus()*self.__total_short_terms * \
                    constants.ST_PRICE/100
        else:
            self.logging.debug(
                self.moduleName+'No rule is applicable for the present amount of short term lease')
            self.__total_price += self.__total_short_terms*constants.ST_PRICE

        self.logging.debug(
            self.moduleName+'Total price is $'+str(self.__total_price))
        return self.__total_price
