import json
from pathlib import Path
import os
from . import Utils

RedSauce_Dict = {
    "Uncooked": {
        "Sets": [
            Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
            Utils.ItemGroup_Sets(["TomatoSauce", "TomatoSauce"], 2, 2)
        ],
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Component1": {
                    "sauce.001": "Tomato Flesh",
                    "herbs.001": "Plastic - Green",
                    "tomatochunks.001": "AppleRed"
                },
                "Component2": {
                    "sauce.002": "Tomato Flesh",
                    "herbs.002": "Plastic - Green",
                    "tomatochunks.002": "AppleRed"
                }
            }
        },
        "ComponentGroups": [
            {
                "Item": "TomatoSauce",
                "Objects": [
                    "Component1",
                    "Component2"
                ]
            }
        ]
    },
    "Cooked": {
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Sauce": {
                    "sauce": "Plastic - Red",
                    "herbs": "Plastic - Green",
                    "tomatochunks": "AppleRed"
                }
            }
        }
    },
    "Plated": {
        "Materials": {
            "Tree": {
                "plate": ["Plate", "Plate - Ring"],
                "Red": {
                    "redherbs": "Plastic - Green",
                    "redsauce": "Plastic - Red",
                    "redtomatochunks": "AppleRed"
                }
            }
        }
    }
}

MeatSauce_Dict = {
    "Uncooked": {
        "Sets": [
            Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
            Utils.ItemGroup_Sets(["TomatoSauce", "MeatChopped"], 2, 2)
        ],
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Component1": {
                    "meatchopped": ["Raw Fat", "Raw"]
                },
                "Component2": {
                    "sauce": "Tomato Flesh",
                    "tomatochunks": "AppleRed"
                }
            }
        },
        "ComponentGroups": [
            {
                "Item": "MeatChopped",
                "GameObject": "Component1"
            },
            {
                "Item": "TomatoSauce",
                "GameObject": "Component2"
            }
        ]
    },
    "Cooked": {
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Sauce": {
                    "sauce": "brownDark",
                    "herbs": "Meat Piece Cooked",
                    "tomatochunks": "AppleRed"
                }
            }
        }
    },
    "Plated": {
        "Materials": {
            "Tree": {
                "plate": ["Plate", "Plate - Ring"],
                "Meat": {
                    "meatchunk": "Meat Piece Cooked",
                    "meatsauce": "brownDark",
                    "meattomatochunks": "AppleRed"
                }
            }
        }
    }
}

AlfredoSauce_Dict = {
    "Uncooked": {
        "Sets": [
            Utils.ItemGroup_Sets(["Pot"], 1, 1, True),
            Utils.ItemGroup_Sets(["CheeseGrated", "Milk"], 2, 2)
        ],
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Component1": {
                    "cheese1": "Cheese - Default",
                    "cheese2": "Cheese - Default",
                    "cheese3": "Cheese - Default"
                },
                "Component2": {
                    "sauce": "Plastic - White",
                    "herbs": "Plastic - Green"
                }
            }
        },
        "ComponentGroups": [
            {
                "Item": "CheeseGrated",
                "GameObject": "Component1"
            },
            {
                "Item": "Milk",
                "GameObject": "Component2"
            }
        ]
    },
    "Cooked": {
        "Materials": {
            "Tree": {
                "Pot": {
                    "base": "Metal",
                    "handle": "Metal Dark"
                },
                "Sauce": {
                    "sauce": "Plastic - Light Yellow",
                    "herbs": "Plastic - Green"
                }
            }
        }
    },
    "Plated": {
        "Materials": {
            "Tree": {
                "plate": ["Plate", "Plate - Ring"],
                "Alfredo": {
                    "alfredoherbs": "Plastic - Green",
                    "alfredosauce": "Plastic - Light Yellow"
                }
            }
        }
    }
}

def generate_sauces(path):
    path = Path.joinpath(path, "Sauce")
    os.mkdir(path)

    mk_sauce(path, "Red", RedSauce_Dict)
    mk_sauce(path, "Meat", MeatSauce_Dict)
    mk_sauce(path, "Alfredo", AlfredoSauce_Dict)

def mk_sauce(path, name, dict):
    uncookedsauce(path, name, dict)
    cookedsauce(path, name, dict)
    sauce(path, name)

def uncookedsauce(path, name, dict):
    raw_json = {
        "Type": "ItemGroup",
        "Modification": "NewGDO",
        "UniqueNameID": f"Uncooked{name}Sauce",
        "GDOName": f"Uncooked {name} Sauce",
        "Prefab": f"Uncooked{name}Sauce",
        "Sets": dict["Uncooked"]["Sets"],
        "Materials": dict["Uncooked"]["Materials"],
        "View": {
            "Type": "ItemGroupView",
            "ComponentGroups": dict["Uncooked"]["ComponentGroups"]
        },
        "Processes" : [Utils.Item_Processes("Cook", f"PastaPalace:Cooked{name}Sauce", 10)],
        "DisposesTo" : "Pot"
    }
    with open(Path.joinpath(path, f"Uncooked{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def cookedsauce(path, name, dict):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": f"Cooked{name}Sauce",
        "GDOName": f"Cooked {name} Sauce",
        "Prefab": f"Cooked{name}Sauce",
        "AllowSplitMerging": True,
        "DisposesTo": "Pot",
        "PreventExplicitSplit": True,
        "SplitCount": 10,
        "SplitDepletedItems": ["Pot"],
        "SplitSubItem": f"PastaPalace:{name}Sauce",
        "Materials": dict["Cooked"]["Materials"],
        "View": {
            "Type": "PositionSplittableView",
            "FullPosition": {
                "x": 0,
                "y": 0.05,
                "z": 0
            },
            "EmptyPosition": {
                "x": 0,
                "y": -0.2,
                "z": 0
            },
            "Objects": ["Sauce"]
        }
    }
    with open(Path.joinpath(path, f"Cooked{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)

def sauce(path, name):
    raw_json = {
        "Type": "Item",
        "Modification": "NewGDO",
        "UniqueNameID": f"{name}Sauce",
        "GDOName": f"{name} Sauce",
        "Prefab": "placeholder"
    }
    with open(Path.joinpath(path, f"{name}Sauce.json"), "w") as file:
        json.dump(raw_json, file, indent=4)