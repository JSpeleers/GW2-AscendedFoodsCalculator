# GW2-AscendedFoodsCalculator

Another GuildWars2 calculator to see if you can earn a little more money, doing the bare minimum. 

This little Python script will use the GW2 API to collect prices of several items in order to determine if crafting and
planting Pouches in your [Garden Plot](https://wiki.guildwars2.com/wiki/Garden_plot) could be a lucrative business.
And if so, what Pouch is most profitable.

## Setup

Run and install using Python 3.6 and above.

1. Clone the repo
2. Setup the Python virtual environment `$ python -m venv venv`
3. Activate the virtual environment
    - Windows: `$ venv\Scripts\activate.bat` 
    - Unix & MacOS: `$ venv btd6bot/bin/activate`
4. Install requirements: `$ pip install -r requirements.txt`

## Run

Start script by running `$ python calculator.py`

### Example output

```
2020-11-09 21:36:28,686 - INFO - Collecting all material prices
2020-11-09 21:36:37,846 - INFO - Calculating best price
2020-11-09 21:36:37,848 - INFO - Cheapest fine:         Bowl of Candy Corn Custard for 7c each
2020-11-09 21:36:37,848 - INFO - Cheapest masterwork:   Roasted Rutabaga for 11c each
2020-11-09 21:36:37,848 - INFO - Cheapest rare:         Roasted Rutabaga for 33c each
2020-11-09 21:36:37,848 - INFO - Cheapest exotic:       Pitcher of Desert-Spiced Coffee for 95c each
2020-11-09 21:36:37,848 - INFO - An Exquisite Extract of Nourishment would thus cost 12s 12c
2020-11-09 21:36:37,848 - INFO - A Pile of Enriched Compost would thus cost 19s 60c
2020-11-09 21:36:38,529 - INFO - ---
2020-11-09 21:36:38,529 - INFO - The profit of crafting a Varietal Cilantro Seed Pouch and growing it to a Varietal Cilantro Seed is 3s 4c
2020-11-09 21:36:38,529 - INFO - The profit of crafting a Varietal Clove Seed Pouch and growing it to a Varietal Clove Seed is 1s 92c
2020-11-09 21:36:38,529 - INFO - The profit of crafting a Varietal Mint Seed Pouch and growing it to a Varietal Mint Seed is -5s 77c
2020-11-09 21:36:38,529 - INFO - The profit of crafting a Varietal Peppercorn Seed Pouch and growing it to a Varietal Peppercorn Seed is 2s 53c
2020-11-09 21:36:38,529 - INFO - The profit of crafting a Varietal Sesame Seed Pouch and growing it to a Varietal Sesame Seed is 5s 97c
2020-11-09 21:36:38,529 - INFO - The most profitable Pouch is thus Varietal Sesame Seed Pouch (5s 97c)
```

## Maintainability

Please update CSV files in [resources](./resources) when extra consumables or pouches are in scope. 
