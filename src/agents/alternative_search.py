from serpapi import GoogleSearch
from config.settings import SERP_API_KEY

def search_alternatives(product_name):
    try:
        print(f"🔎 Recherche d'alternatives biologiques pour : {product_name}")

        search = GoogleSearch({
            "q": f"alternative biologique à {product_name}",
            "location": "France",
            "hl": "fr",
            "gl": "fr",
            "api_key": SERP_API_KEY
        })

        results = search.get_dict()

        if 'organic_results' in results:
            alternatives = []
            for result in results['organic_results'][:5]:
                alternative = {
                    'title': result.get('title'),
                    'link': result.get('link'),
                    'snippet': result.get('snippet')
                }
                alternatives.append(alternative)

            return alternatives
        else:
            print("❌ Aucune alternative trouvée.")
            return None

    except Exception as e:
        print(f"Erreur lors de la recherche d'alternatives : {e}")
        return None
