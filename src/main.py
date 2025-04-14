from agents.product_lookup import lookup_product
from agents.data_extraction import extract_product_details
from agents.risk_analysis import analyze_risks
from agents.alternative_search import search_alternatives
from agents.report_generation import generate_report

def main():
    product = "Glyphosate"

    print(f"🔎 Recherche du produit : {product}")
    result = lookup_product(product)
    
    if result:
        details = extract_product_details(result)

        if details and details.get("name"):
            print(f"✅ Produit trouvé : {details['name']}")

            risks = analyze_risks(details)
            alternatives = search_alternatives(details.get("name"))
            generate_report(details, risks, alternatives)

            print("✅ Rapport généré avec succès !")
        else:
            print("❌ Détails du produit incomplets.")
    else:
        print("❌ Produit non trouvé.")

if __name__ == "__main__":
    main()
