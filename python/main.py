import os
import shutil
from pathlib import Path
import json

from generate import Sauce
from generate import Pasta
from generate import Gnocchi
from generate import Carbonara

def main():
    root = Path(os.getcwd())
    release = root / "PastaPalace"

    if(release.exists()):
        shutil.rmtree(release)

    mod = release / "content" / "Customs"
    mod.mkdir(parents=True, exist_ok=True)

    dummypath = root / "python" / "files" / "Dummy.dll"
    shutil.copy(dummypath, release / "content")

    manifest = {
        "Author": "Yariazen",
        "ModName": "PastaPalace"
    }
    with open(release / "content" / "manifest.json", "w") as file:
        json.dump(manifest, file, indent=4)
    
    asset = root / "My project" / "Assets" / "AssetBundles" / "pastapalace.assets"
    if(asset.exists()):
        shutil.copy(asset, release / "content")

    Sauce.generate_sauces(mod)
    Pasta.generate_pastas(mod)
    #Gnocchi.generate_gnocchi(mod)
    #Carbonara.generate_Carbonara(mod)

    modfolder = Path("/mnt/d/Program Files (x86)/Steam/steamapps/common/PlateUp/PlateUp/Mods") / "PastaPalace"
    if(modfolder.exists()):
        shutil.rmtree(modfolder)
    shutil.copytree(release, modfolder)

if __name__ == "__main__":
    main()