import csv
import logging

import config
import recipes
from api import Commerce
from material import CraftingMaterial, Seed

RARITIES = ['fine', 'masterwork', 'rare', 'exotic']


def main():
    # Collect materials
    logging.info("Collecting all material prices")
    materials = collect_material_prices()
    for i, material in enumerate(materials):
        logging.debug(material)

    # Calculate best price
    logging.info("Calculating best price")
    material_all_prices = [[material.get_fine_prices(), material.get_masterwork_prices(), material.get_rare_prices(),
                            material.get_exotic_prices()] for material in materials]
    cheapest_nourishments = find_cheapest_nourishments(material_all_prices)

    # Print cheapest materials
    for i in range(len(RARITIES)):
        log_cheapest_materials(i, materials, cheapest_nourishments)

    # Calculate crafting prices
    exquisite_extract_price = recipes.calc_price_exquisite_extract_of_nourishment(cheapest_nourishments[0][3],
                                                                                  cheapest_nourishments[1][3],
                                                                                  cheapest_nourishments[2][3],
                                                                                  cheapest_nourishments[3][3])
    logging.info(f'An Exquisite Extract of Nourishment would thus cost {config.format_coins(exquisite_extract_price)}')
    enriched_compost_price = recipes.calc_price_enriched_compost(exquisite_extract_price)
    logging.info(f'A Pile of Enriched Compost would thus cost {config.format_coins(enriched_compost_price)}')

    # Find most profitable seed
    seeds = collect_seed_prices()
    most_profitable_seed = None
    most_profit_seed = 0
    logging.info('---')
    for seed in seeds:
        profit = seed.harvest_price * config.TP_TAX - seed.seed_price - enriched_compost_price
        logging.info(f'The profit of crafting a {seed.pouch_name} and growing it to a {seed.seed_name} is'
                     f' {config.format_coins(profit)}')
        if most_profit_seed < profit:
            most_profit_seed = profit
            most_profitable_seed = seed
    if most_profitable_seed:
        logging.info(
            f'The most profitable Pouch is thus {most_profitable_seed.pouch_name}'
            f' ({config.format_coins(most_profit_seed)})')
    else:
        logging.info(f'By Ogden\'s hammer, what savings. Sadly, there is no money to be made here.')


def collect_material_prices():
    """
    Read the materials.csv list; for each material collect the current price and return a list of CraftingMaterial
    objects
    :return: list of CraftingMaterials
    """
    # with timebudget("Collecting material prices"):
    commerce = Commerce()
    materials = []
    with open('resources/materials.csv', 'r') as material_list:
        next(material_list)  # Skip first line
        for row in csv.reader(material_list, delimiter=";"):
            commerce.ids.append(row[0])
            materials.append(CraftingMaterial(row[0], row[1], row[2], row[3], row[4], row[5]))
    prices = commerce.get_prices()
    for i, material in enumerate(materials):
        material.order_price = prices[i]['buys']['unit_price']
        material.instant_price = prices[i]['sells']['unit_price']
    return materials


def find_cheapest_nourishments(material_all_prices):
    """
    For each rarity, return the cheapest consumable to salvage in order to gain nourishments :param
    material_all_prices: 2D list where each inner list represents the price of a consumable to be salvaged in order to
    get a single nourishment
    :return: 2D list where each inner list represents the cheapest material to salvage to get a single nourishment
    """
    cheapest = [[None, 999999, None, 999999] for _ in range(4)]
    for i, material_price in enumerate(material_all_prices):
        for j, prices in enumerate(material_price):
            if all(prices):
                if cheapest[j][1] > prices[0]:
                    cheapest[j][1] = prices[0]
                    cheapest[j][0] = i
                if cheapest[j][3] > prices[1]:
                    cheapest[j][3] = prices[1]
                    cheapest[j][2] = i
    return cheapest


def collect_seed_prices():
    """
    Read the seeds.csv list; for each material collect the current price and return a list of Seed objects
    :return: list of Seeds
    """
    seeds = []
    commerce = Commerce()
    with open('resources/seeds.csv', 'r') as seed_list:
        next(seed_list)  # Skip first line
        for row in csv.reader(seed_list, delimiter=";"):
            commerce.ids.append(row[2])
            commerce.ids.append(row[4])
            seeds.append(Seed(row[0], row[1], row[2], row[3], row[4], row[5]))
    seed_prices = commerce.get_prices()
    for i, seed in enumerate(seeds):
        seed.seed_price = seed_prices[i * 2]['sells']['unit_price']
        seed.harvest_price = seed_prices[i * 2 + 1]['sells']['unit_price']
    return seeds


def log_cheapest_materials(index, materials, cheapest_nourishments):
    logging.info(
        f'Cheapest {RARITIES[index]}:\t{materials[cheapest_nourishments[index][2]].name}'
        f' for {config.format_coins(cheapest_nourishments[index][3])} each')


if __name__ == '__main__':
    config.init_logging()
    main()
