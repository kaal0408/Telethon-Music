


import glob
from pathlib import Path
from Murat.utils import load_plugins
import logging
from Murat import Murat

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Murat/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Visit @kaalxsupport")

if __name__ == "__main__":
    Murat.run_until_disconnected()
