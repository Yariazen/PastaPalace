import json
import src.Utils
from pathlib import Path
import os

def generate_dish(path):
    path = Path.joinpath(path, "Dish")
    os.mkdir(path)

def dish(path, lobby, nameset, name, miningredients, recipe, info):
    raw_json = {
        "Type": "Dish",
        "Modification": "NewGDO",
        "UniqueNameID": f"",
        "DisplayPrefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Shiny Red", False),
        "IconPrefab": Utils.Prefab(0.5, 0.5, 0.5, "Plastic - Shiny Red", False),
        "CustomerMultiplier": "SmallDecrease",
        "ExpReward": "Medium",
        "UnlockGroup": "Dish",
        "IsAvailableAsLobbyOption": lobby,
        "StartingNameSet": nameset,
        "ResultingMenuItems": [Utils.Dish_MenuItem(f"PastaPalace:{name}", "Main", 1, "Static")],
        "MinimumIngredients": miningredients,
        "RequiredProcesses": ["Cook"],
        "Recipe": recipe,
        "Info": info
    }