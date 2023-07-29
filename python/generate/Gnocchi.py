import json
from pathlib import Path
import os
from . import Utils

RedSauce_Dict = {
    "Materials": {
        "Tree": {
            "plate": ["Plate", "Plate - Ring"],
            "gnocchi": "Raw Pastry",
            "Red": {
                "redherbs": "Plastic - Green",
                "redsauce": "Plastic - Red",
                "redtomatochunks": "AppleRed"
            }
        }
    }
}

MeatSauce_Dict = {
    "Materials": {
        "Tree": {
            "plate": ["Plate", "Plate - Ring"],
            "gnocchi": "Raw Pastry",
            "Meat": {
                "meatchunk": "Meat Piece Cooked",
                "meatsauce": "brownDark",
                "meattomatochunks": "AppleRed"
            }
        }
    }
}

AlfredoSauce_Dict = {
    "Materials": {
        "Tree": {
            "plate": ["Plate", "Plate - Ring"],
            "gnocchi": "Raw Pastry",
            "Alfredo": {
                "alfredoherbs": "Plastic - Green",
                "alfredosauce": "Plastic - Light Yellow"
            }
        }
    }
}

ComponentGroups = [
    {
        "Item": "PastaPalace:Gnocchi",
        "GameObject": "gnocchi"
    },
    {
        "Item": "PastaPalace:RedSauce",
        "GameObject": "Red"
    },
    {
        "Item": "PastaPalace:MeatSauce",
        "GameObject": "Meat"
    },
    {
        "Item": "PastaPalace:AlfredoSauce",
        "GameObject": "Alfredo"
    }
]

def generate_gnocchi(path):
    path = Path.joinpath(path, "Gnocchi")
    os.mkdir(path)

    rawgnocchi(path)
    uncookedgnocchi(path)
    cookedgnocchi(path)
    gnocchi(path)
    mk_platedgnocchi(path)

def mk_platedgnocchi(path):
    platedgnocchiwithsauce(path, "Red", RedSauce_Dict)
    platedgnocchiwithsauce(path, "Meat", MeatSauce_Dict)
    platedgnocchiwithsauce(path, "Alfredo", AlfredoSauce_Dict)

def rawgnocchi(path):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "RawGnocchi",
        "GDOName": "Raw Gnocchi",
        "Prefab": "Gnocchi",
        "Sets": [Utils.ItemGroup_Sets(["ingredientlib:egg dough", "PotatoChopped"], 2, 2)],
        "ItemStorageFlags": "StackableFood",
        "Materials": {
            "Tree" : {
                "gnocchi1": "Egg Dough",
                "gnocchi2": "Egg Dough",
                "gnocchi3": "Egg Dough"
            }
        }
    }
    with open(Path.joinpath(path, "RawGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def uncookedgnocchi(path):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": "UncookedGnocchi",
        "GDOName": "Uncooked Gnocchi",
        "Prefab": "UncookedGnocchi",
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
        "DisposesTo": "Pot",
        "Materials": {
            "Tree" : {
                "Gnocchi": {
                    "gnocchi1": "Egg Dough",
                    "gnocchi2": "Egg Dough",
                    "gnocchi3": "Egg Dough"
                },
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Water": {
                    "water": "Water"
                }
            }
        },
        "View": {
            "Type": "ItemGroupView",
            "ComponentGroups": [
                {
                    "Item": "PastaPalace:RawGnocchi",
                    "GameObject": "Gnocchi"
                },
                {
                    "Item": "Water",
                    "GameObject": "Water"
                }
            ]
        }
    }
    with open(Path.joinpath(path, "UncookedGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def cookedgnocchi(path):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": "CookedGnocchi",
        "GDOName": "Cooked Gnocchi",
        "Prefab": "CookedGnocchi",
        "DisposesTo": "Pot",
        "SplitCount": 3,
        "SplitDepletedItems": ["Pot"],
        "SplitSubItem": "PastaPalace:Gnocchi",
        "Materials": {
            "Tree" : {
                "Gnocchi": {
                    "gnocchi1": "Egg Dough",
                    "gnocchi2": "Egg Dough",
                    "gnocchi3": "Egg Dough"
                },
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                }
            }
        },
        "View": {
            "Type": "ObjectsSplittableView",
            "Objects": [
                "Gnocchi/gnocchi1",
                "Gnocchi/gnocchi2",
                "Gnocchi/gnocchi3"
            ]
        }
    }
    with open(Path.joinpath(path, "CookedGnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def gnocchi(path):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": "Gnocchi",
        "GDOName": "Gnocchi",
        "Prefab": "Gnocchi",
        "ItemStorageFlags": "StackableFood",
        "Materials": {
            "Tree" : {
                "gnocchi1": "Raw Pastry"
            }
        }
    }
    with open(Path.joinpath(path, "Gnocchi.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def platedgnocchiwithsauce(path, name, dict):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"PlatedGnocchi{name}Sauce",
        "GDOName": f"Plated Gnocchi with {name} Sauce",
        "Prefab": "PlatedGnocchi",
        "Sets": [
            Utils.ItemGroup_Sets(["Plate"], 1, 1, True),
            Utils.ItemGroup_Sets([
                "PastaPalace:Gnocchi",
                f"PastaPalace:{name}Sauce"], 2, 2)
        ],
        "DirtiesTo": "PlateDirty",
        "DisposesTo": "Plate",
        "Materials": dict["Materials"],
        "View": {
            "Type": "ItemGroupView",
            "ComponentGroups": ComponentGroups
        }
    }
    with open(Path.joinpath(path, f"PlatedGnocchi{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)