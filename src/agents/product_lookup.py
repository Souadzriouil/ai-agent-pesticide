import sys
import os

# Ajoute le chemin vers le dossier `src`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from utils.google_search import lookup_google
from agents.alternative_search import search_alternatives

def lookup_alternatives(product_name):
    alternatives = search_alternatives(product_name)
    if alternatives:
        print(f"✅ {len(alternatives)} alternatives trouvées !")
        return alternatives
    else:
        print("❌ Aucune alternative trouvée.")
        return None

def lookup_product(product_name):
    print(f"🔎 Recherche du produit : {product_name}")
    result = lookup_google(product_name)
    
    if result:
        print(f"✅ Produit trouvé : {result['title']}")
        return result
    else:
        print("❌ Produit non trouvé !")
        return None
