import logging
import math
import sys

TP_TAX = 0.85


def init_logging():
    """Initialise logging"""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def format_coins(amount):
    """
    Format amount of coins
    :param amount: amount of copper
    :return: Amount of coins in a readable format <x>g <y>s <z>c
    """
    logging.debug(f'Formatting coins for {amount}')
    is_amount_negative = amount < 0
    amount = abs(amount)
    gold = math.floor(amount // 10000)
    silver = math.floor(amount // 100 % 100)
    copper = math.floor(amount % 100)
    return '{}{}{}{}'.format('-' if is_amount_negative else '',
                             str(gold) + 'g ' if gold > 0 else '',
                             str(silver) + 's ' if silver > 0 else '',
                             str(copper) + 'c' if copper > 0 else '')
