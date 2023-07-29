import json
from pathlib import Path
import os
from . import Utils

def generate_Carbonara(path):
    path = Path.joinpath(path, "Carbonara")
    os.mkdir(path)

    mk_Carbonara(path)

def mk_Carbonara(path):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "PlatedCarbonara",
        "GDOName": "Plated Carbonara",
        "Prefab": "PlatedCarbonara",
        "Sets": [
            Utils.ItemGroup_Sets(["Plate", "ingredientlib:pasta noodles", "ingredientlib:bacon"], 3, 3, True),
            Utils.ItemGroup_Sets(["CheeseGrated", "EggCracked"], 2, 2, False)
        ],
        "Materials": {
            "Tree": {
                "plate": ["Plate", "Plate - Ring"],
                "noodles": "Raw Pastry",
                "bacon": "Bacon",
                "cheese": "Cheese - Default",
                "Egg": {
                    "eggwhite": "Egg - White",
                    "eggyoke": "Egg - Yolk"
                }
            }
        },
        "View": {
            "Type": "ItemGroupView",
            "ComponentGroups": [
                {
                    "Item": "ingredientlib:pasta noodles",
                    "GameObject": "noodles"
                },
                {
                    "Item": "ingredientlib:bacon",
                    "GameObject": "bacon"
                },
                {
                    "Item": "CheeseGrated",
                    "GameObject": "cheese"
                },
                {
                    "Item": "EggCracked",
                    "GameObject": "Egg"
                },
                {
                    "Item": "Plate",
                    "GameObject": "plate"
                }
            ]
        }
    }
    with open(Path.joinpath(path, "Carbonara.json"), "w") as file:
        json.dump(raw_json, file, indent=4)