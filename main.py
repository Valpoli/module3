import sys
import os

# Ajoute le chemin vers modules/moduleA et modules/moduleB
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "modules/moduleA")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "modules/moduleB")))

from moduleA import do_a_stuff
from moduleB import do_b_stuff

def fusion_module_divin():
    print("=== Fusion divine des modules ===")
    print("Module A dit :", do_a_stuff())
    print("Module B répond :", do_b_stuff())

if __name__ == "__main__":
    fusion_module_divin()
