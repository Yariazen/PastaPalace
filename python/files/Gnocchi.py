import json
import src.Utils
from pathlib import Path
import os

def generate_gnocchi(path):
    path = Path.joinpath(path, "Gnocchi")
    os.mkdir(path)
    mk_gnocchi(path)

def mk_gnocchi(path):
    rawgnocchi(path)
    uncookedgnocchi(path)
    cookedgnocchi(path)
    gnocchi(path)
    platedgnocchi(path)
    platedgnocchiwithsauce(path, "Red")
    platedgnocchiwithsauce(path, "Meat")
    platedgnocchiwithsauce(path, "Alfredo")

def rawgnocchi(path):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "RawGnocchi",
        "GDOName": "RawGnocchi",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Dark Grey", False),
        "Sets": [Utils.ItemGroup_Sets(["ingredientlib:EggDough", "PotatoChopped"], 2, 2)],
        "ItemStorageFlags": "StackableFood"
    }
    with open(Path.joinpath(path, "RawGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def uncookedgnocchi(path):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "UncookedGnocchi",
        "GDOName": "Uncooked Gnocchi",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Dark Red", False),
        "Sets": [
            Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
            Utils.ItemGroup_Sets(["Water", "PastaPalace:RawGnocchi"], 2, 2),
        ],
        "Processes": [
            {
                "Process": "Cook",
                "Result": "PastaPalace:CookedGnocchi",
                "Duration": 10
            }
        ],
        "DisposesTo": "Pot"
    }
    with open(Path.joinpath(path, "UncookedGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def cookedgnocchi(path):
    raw_json = {
        "Type": "Item",
        "Modificaiton": "NewGDO",
        "UniqueNameID": "CookedGnocchi",
        "GDOName": "CookedGnocchi",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Dark Yellow", False),
        "DisposesTo": "Pot",
        "SplitCount": 3,
        "SplitDepletedItems": ["Pot"],
        "SplitSubItem": "PastaPalace:Gnocchi"
    }
    with open(Path.joinpath(path, "CookedGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def gnocchi(path):
    raw_json = {
        "Type": "Item",
        "Modificaiton": "NewGDO",
        "UniqueNameID": "Gnocchi",
        "GDOName": "Gnocchi",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Light Yellow", False),
        "ItemStorageFlags": "StackableFood"
    }
    with open(Path.joinpath(path, "Gnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def platedgnocchi(path):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "PlatedGnocchi",
        "GDOName": "PlatedGnocchi",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Very Dark Green", False),
        "Sets": [Utils.ItemGroup_Sets(["Plate", "PastaPalace:Gnocchi"], 2, 2, False)],
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, "PlatedGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def platedgnocchiwithsauce(path, sauce):
    raw_json = {
        "Type": "CustomItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"PlatedGnocchi{sauce}Sauce",
        "GDOName": f"Plated Gnocchi with {sauce} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Shiny Gold", False),
        "Sets": [Utils.ItemGroup_Sets(["PastaPalace:PlatedGnocchi", "PastaPalace:{sauce}Sauce"], 2, 2, False)],
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, f"PlatedGnocchi{sauce}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)