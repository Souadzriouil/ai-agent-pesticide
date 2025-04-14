import sys
import os

# Ajoute le chemin vers le dossier `src` pour reconnaître `config`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from config.settings import SERP_API_KEY
from serpapi import GoogleSearch

def lookup_google(product_name):
    try:
        search = GoogleSearch({
            "q": product_name,
            "location": "France",
            "hl": "fr",
            "gl": "fr",
            "api_key": SERP_API_KEY
        })
        results = search.get_dict()

        if 'organic_results' in results:
            first_result = results['organic_results'][0]
            return {
                'title': first_result.get('title'),
                'link': first_result.get('link'),
                'snippet': first_result.get('snippet')
            }
        else:
            return None
    except Exception as e:
        print(f"Erreur recherche Google: {e}")
        return None
