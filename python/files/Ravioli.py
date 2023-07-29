import json
import src.Utils
from pathlib import Path
import os

def generate_raviolis(path):
    path = Path.joinpath(path, "Ravioli")
    os.mkdir(path)

    RawCheeseRavioli_Sets = [
        Utils.ItemGroup_Sets(["ingredientlib:EggDough", "CheeseChopped"], 2, 2, False)
    ]
    mk_ravioli(path, "Cheese", RawCheeseRavioli_Sets)

    RawMeatRavioli_Sets = [
        Utils.ItemGroup_Sets(["ingredientlib:EggDough", "MeatChopped"], 2, 2, False)
    ]
    mk_ravioli(path, "Meat", RawMeatRavioli_Sets)

    RawMushroomRavioli_Sets = [
        Utils.ItemGroup_Sets(["ingredientlib:EggDough", "MushroomChopped"], 2, 2, False)
    ]
    mk_ravioli(path, "Mushroom", RawMushroomRavioli_Sets)

def mk_ravioli(path, name, Sets):
    rawravioli(path, name, Sets)
    uncookedravioli(path, name)
    cookedravioli(path, name)
    ravioli(path, name)
    platedravioli(path, name)
    sauceravioli(path, name, "Red")
    sauceravioli(path, name, "Meat")
    sauceravioli(path, name, "Alfredo")

def rawravioli(path, name, Sets):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Raw{name}Ravioli",
        "GDOName": f"Raw {name} Ravioli",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Orange", False),
        "Sets": Sets,
        "ItemStorageFlags": "StackableFood"
    }
    with open(Path.joinpath(path, f"Raw{name}Ravioli.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def uncookedravioli(path, name):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Uncooked{name}Ravioli",
        "GDOName": f"Uncooked {name} Ravioli",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Purple", False),
        "Sets": [
            Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
            Utils.ItemGroup_Sets(["Water", f"PastaPalace:Raw{name}Ravioli"], 2, 2, False),
        ],
        "Processes": [
            {
                "Process": "Cook",
                "Result": f"PastaPalace:Cooked{name}Ravioli",
                "Duration": 10
            }
        ],
        "DisposesTo": "Pot"
    }
    with open(Path.joinpath(path, f"Uncooked{name}Ravioli.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def cookedravioli(path, name):
    raw_json = {
        "Type": "Item",
        "Modificaiton": "NewGDO",
        "UniqueNameID": f"Cooked{name}Ravioli",
        "GDOName": f"Cooked {name} Ravioli",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Grey", False),
        "DisposesTo": "Pot",
        "SplitCount": 3,
        "SplitDepletedItems": ["Pot"],
        "SplitSubItem": f"PastaPalace:{name}Ravioli"
    }
    with open(Path.joinpath(path, f"Cooked{name}Ravioli.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def ravioli(path, name):
    raw_json = {
        "Type": "Item",
        "Modificaiton": "NewGDO",
        "UniqueNameID": f"{name}Ravioli",
        "GDOName": f"{name} Ravioli",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - White", False),
        "ItemStorageFlags": "StackableFood"
    }
    with open(Path.joinpath(path, f"{name}Ravioli.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def platedravioli(path, name):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Plated{name}Ravioli",
        "GDOName": f"Plated {name} Ravioli",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Black Dark", False),
        "Sets": [Utils.ItemGroup_Sets(["Plate", f"{name}Ravioli"], 2, 2, False)],
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, f"Plated{name}Ravioli.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def sauceravioli(path, name, sauce):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Plated{name}Ravioli{sauce}Sauce",
        "GDOName": f"Plated {name} Ravioli with {sauce} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Dark Blue", False),
        "Sets": [Utils.ItemGroup_Sets([f"PastaPalace:Plated{name}Ravioli", f"PastaPalace:{sauce}Sauce"], 2, 2, False)],
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, f"Plated{name}Ravioli{sauce}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)