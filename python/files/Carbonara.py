import json
import src.Utils
from pathlib import Path
import os

def generate_carbonara(path):
    path = Path.joinpath(path, "Carbonara")
    os.mkdir(path)
    mk_carbonara(path)

def mk_carbonara(path):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "PlatedCarbonara",
        "GDOName": "Plated Carbonara",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Dark Green", False),
        "Sets": [
            Utils.ItemGroup_Sets(["PastaPalace:PlatedPasta", "ingredientlib:bacon"], 2, 2, True),
            Utils.ItemGroup_Sets(["CheeseChopped", "EggCracked"], 2, 2, False)
        ]
    }
    with open(Path.joinpath(path, "Carbonara.json"), "w") as file:
        json.dump(raw_json, file, indent=4)