# pylint: disable=missing-module-docstring


def exchange_money(budget, exchange_rate):
    """
    This function return the value of the exchanged currency

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    This function return the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    This function return the amount of money given a number of bills and their
    denomination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    This function return the number of new currency bills that you can receive
    within the given budget.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function return the maximum value of the new currency after calculating
    the exchange rate plus the spread

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    total_value = exchange_money(budget, (exchange_rate * (1 + spread / 100)))
    total_exchange = get_value_of_bills(
        denomination, get_number_of_bills(total_value, denomination)
    )

    return total_exchange


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function should return the value that is not exchangeable due to the
    denomination of the bills

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    total_value = exchange_money(budget, (exchange_rate * (1 + spread / 100)))
    total_exchange = exchangeable_value(budget, exchange_rate, spread, denomination)

    return int(total_value - total_exchange)
