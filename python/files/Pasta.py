import json
import src.Utils
from pathlib import Path
import os

def generate_pastas(path):
    path = Path.joinpath(path, "Pasta")
    os.mkdir(path)

    PlatedPasta_Sets = [
        Utils.ItemGroup_Sets(["Plate", "ingredientlib:Cooked Pasta"], 2, 2, False),
    ]
    mk_platedpasta(path, PlatedPasta_Sets)
    mk_platedpastawithsauce(path, "Red")
    mk_platedpastawithsauce(path, "Meat")
    mk_platedpastawithsauce(path, "Alfredo")

def mk_platedpasta(path, Sets):
    raw_json = {
        "Type": "ItemGroup",
        "Modificaton": "NewGDO",
        "UniqueNameID": "PlatedPasta",
        "GDOName": "Plated Pasta",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Black", False),
        "Sets": Sets,
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, f"PlatedPasta.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def mk_platedpastawithsauce(path, name):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"PlatedPasta{name}Sauce",
        "GDOName": f"Plated Pasta with {name} Sauce",
        "Prefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Black", False),
        "Sets": [
            {
                "Items": [
                    "PastaPalace:PlatedPasta",
                    f"PastaPalace:{name}Sauce"
                ],
                "Min": 2,
                "Max": 2
            }
        ],
        "DirtiesTo": "Plate",
        "DisposesTo": "Plate"
    }
    with open(Path.joinpath(path, f"PlatedPasta{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def mk_platedsauce(path, name, dict):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Plated{name}Sauce",
        "GDOName": f"Plated {name} Sauce",
        "Prefab": "PlatedPasta",
        "Sets": [Utils.ItemGroup_Sets(["Plate", f"PastaPalace:{name}Sauce"], 2, 2)],
        "DisposesTo": "Plate",
        "Materials": dict["Plated"]["Materials"],
        "View": {
            "Type": "ItemGroupView",
            "ComponentGroups": [
                {
                    "Item": "Plate",
                    "GameObject": "plate"
                },
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
        }
    }
    with open(Path.joinpath(path, f"Plated{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)