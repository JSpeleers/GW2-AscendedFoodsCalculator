class CraftingMaterial:

    def __init__(self, item_id, name, numb_fine, numb_masterwork, numb_rare, numb_exotic):
        self.id = item_id
        self.name = name
        self.numb_fine = numb_fine
        self.numb_masterwork = numb_masterwork
        self.numb_rare = numb_rare
        self.numb_exotic = numb_exotic
        self.order_price = None
        self.instant_price = None

    def __repr__(self):
        return f'{self.id};{self.name};{self.numb_fine};{self.numb_masterwork};{self.numb_rare};{self.numb_exotic};' \
               f'{self.order_price};{self.instant_price}'

    def get_fine_prices(self):
        return self._get_prices(self.numb_fine)

    def get_masterwork_prices(self):
        return self._get_prices(self.numb_masterwork)

    def get_rare_prices(self):
        return self._get_prices(self.numb_rare)

    def get_exotic_prices(self):
        return self._get_prices(self.numb_exotic)

    def _get_prices(self, numb):
        numb = float(numb)
        if not numb:
            return None, None
        return self.order_price / numb, self.instant_price / numb


class Seed:

    def __init__(self):
        pass
