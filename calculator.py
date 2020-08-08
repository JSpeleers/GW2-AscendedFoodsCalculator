import csv
import logging

from timebudget import timebudget

import config
from api import Commerce
from material import CraftingMaterial


def main():
    logging.info("Collecting all material prices")
    materials = collect_material_prices()
    for material in materials:
        logging.debug(material)


def collect_material_prices():
    with timebudget("Collecting material prices"):
        commerce = Commerce()
        materials = []
        with open('materials.csv', 'r') as material_list:
            for row in csv.reader(material_list, delimiter=";"):
                commerce.ids.append(row[0])
                materials.append(CraftingMaterial(row[0], row[1], row[2], row[3], row[4], row[5]))
        prices = commerce.get_prices()
        for i, material in enumerate(materials):
            material.order_price = prices[i]['buys']['unit_price']
            material.instant_price = prices[i]['sells']['unit_price']
    return materials


if __name__ == '__main__':
    config.init_logging()
    main()
