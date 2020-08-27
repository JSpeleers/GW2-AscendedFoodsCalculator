import logging
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
    :return: Amount of coins in a readible format <x>g <y>s <z>c
    """
    gold = round(amount // 10000)
    silver = round(amount // 100 % 100)
    copper = round(amount % 100)
    return '{}{}{}'.format(str(gold) + 'g ' if gold > 0 else '',
                           str(silver) + 's ' if silver > 0 else '',
                           str(copper) + 'c' if copper > 0 else '')
