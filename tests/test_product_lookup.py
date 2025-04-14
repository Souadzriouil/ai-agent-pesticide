import sys
import os

# Ajoute le chemin vers le dossier `src`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.agents.product_lookup import lookup_product

def test_lookup_product():
    product_name = "Glyphosate"
    result = lookup_product(product_name)
    assert result is not None
    print("✔️ Test OK : Produit trouvé")
    print(result)

if __name__ == "__main__":
    test_lookup_product()
