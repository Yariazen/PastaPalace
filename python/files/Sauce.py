import json
import Utils
from pathlib import Path
import os

def generate_sauces(path):
    path = Path.joinpath(path, "Sauce")
    os.mkdir(path)

    UncookedRedSauce_Sets = [
        Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
        Utils.ItemGroup_Sets(["TomatoSauce", "TomatoSauce"], 2, 2)
    ]
    mk_sauce(path, "Red", UncookedRedSauce_Sets)

    UncookedMeatSauce_Sets = [
        Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
        Utils.ItemGroup_Sets(["TomatoSauce", "MeatChopped"], 2, 2)
    ]
    mk_sauce(path, "Meat", UncookedMeatSauce_Sets)

    UncookedAlfredoSauce_Sets = [
        Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
        Utils.ItemGroup_Sets(["CheeseGrated", "ingredientlib:milk ingredient", "WineBottle"], 2, 2)
    ]
    mk_sauce(path, "Alfredo", UncookedAlfredoSauce_Sets)

def mk_sauce(path, name, Sets):
    uncookedsauce(path, name, Sets)
    cookedsauce(path, name)
    sauce(path, name)

def uncookedsauce(path, name, Sets):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Uncooked{name}Sauce",
        "GDOName": f"Uncooked {name} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Red", False),
        "Sets": Sets,
        "Processes": [
            {
                "Process": "Cook",
                "Result": f"PastaPalace:Cooked{name}Sauce",
                "Duration": 10
            }
        ]
    }
    with open(Path.joinpath(path, f"Uncooked{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def cookedsauce(path, name):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": f"Cooked{name}Sauce",
        "GDOName": f"Cooked {name} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Blue", False),
        "AllowSplitMerging": True,
        "DisposesTo": "Pot",
        "PreventExplicitSplit": True,
        "SplitCount": 10,
        "SplitDepletedItems": ["Pot"],
        "SplitSubItem": f"PastaPalace:{name}Sauce"
    }
    with open(Path.joinpath(path, f"Cooked{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def sauce(path, name):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": f"{name}Sauce",
        "GDOName": f"{name} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Green", False)
    }
    with open(Path.joinpath(path, f"{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)