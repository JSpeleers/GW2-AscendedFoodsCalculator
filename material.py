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
