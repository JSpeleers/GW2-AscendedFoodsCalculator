def calc_price_exquisite_extract_of_nourishment(fine_price, masterwork_price, rare_price, exotic_price):
    """ https://wiki.guildwars2.com/wiki/Exquisite_Extract_of_Nourishment """
    return 5 * fine_price + 5 * masterwork_price + 5 * rare_price + 10 * exotic_price


_COMPOST_STARTER_PRICE = 1496 / 10  # 10 Piles of Compost Starter for 14s 96c


def calc_price_enriched_compost(exquisite_extract_price):
    """ https://wiki.guildwars2.com/wiki/Pile_of_Enriched_Compost """
    return 5 * _COMPOST_STARTER_PRICE + exquisite_extract_price
