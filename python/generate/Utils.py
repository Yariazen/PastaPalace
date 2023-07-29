def Prefab(ScaleX, ScaleY, ScaleZ, MaterialName, Collider):
    return {
        "ScaleX": ScaleX,
        "ScaleY": ScaleY,
        "ScaleZ": ScaleZ,
        "MaterialName": MaterialName,
        "Collider": Collider
    }

def ItemGroup_Sets(Items, Min, Max, IsMandatory=False):
    return {
        "Items": Items,
        "Min": Min,
        "Max": Max,
        "IsMandatory": IsMandatory
    }

def Item_Processes(Process, Result, Duration):
    return {
        "Process": Process,
        "Result": Result,
        "Duration": Duration
    }

def ItemGroupView_Component(Item, GameObject, Objects, DrawAll=False):
    return {
        "Item": Item,
        "GameObject": GameObject,
        "Objects": Objects,
        "DrawAll": DrawAll
    }

def Dish_MenuItem(Item, Phase, Weight, DynamicMenuType):
    return {
        "Item": Item,
        "Phase": Phase,
        "Weight": Weight,
        "DynamicMenuType": DynamicMenuType
    }