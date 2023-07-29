import json
from pathlib import Path
import os
from . import Utils

RedSauce_Dict = {
    "Materials": {
        "Tree": {
            "plate": ["Plate", "Plate - Ring"],
            "noodles": "Raw Pastry",
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
            "noodles": "Raw Pastry",
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
            "noodles": "Raw Pastry",
            "Alfredo": {
                "alfredoherbs": "Plastic - Green",
                "alfredosauce": "Plastic - Light Yellow"
            }
        }
    }
}

ComponentGroups = [
    {
        "Item": "ingredientlib:pasta noodles",
        "GameObject": "noodles"
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

def generate_pastas(path):
    path = Path.joinpath(path, "Pasta")
    os.mkdir(path)

    mk_platedpastawithsauce(path, "Red", RedSauce_Dict)
    mk_platedpastawithsauce(path, "Meat", MeatSauce_Dict)
    mk_platedpastawithsauce(path, "Alfredo", AlfredoSauce_Dict)

def mk_platedpastawithsauce(path, name, dict):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"PlatedPasta{name}Sauce",
        "GDOName": f"Plated Pasta with {name} Sauce",
        "Prefab": "PlatedPasta",
        "Sets": [
            Utils.ItemGroup_Sets(["Plate"], 1, 1, True),
            Utils.ItemGroup_Sets([
                "ingredientlib:pasta noodles",
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
    with open(Path.joinpath(path, f"PlatedPasta{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)