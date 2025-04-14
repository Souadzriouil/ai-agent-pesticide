import sys
import os

# Ajouter le répertoire racine au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.product_lookup import lookup_product
from src.agents.data_extraction import extract_product_details
from src.agents.risk_analysis import analyze_risks
from src.agents.alternative_search import search_alternatives
from src.agents.report_generation import generate_report
import streamlit as st


def main():
    st.set_page_config(page_title="AI Agent for Pesticide Analysis", layout="wide")
    
    st.title("🌿 AI Agent for Pesticide Analysis")
    st.markdown("## Analyse des risques liés aux pesticides et recherche d'alternatives biologiques")

    # ✅ Saisie du produit
    product = st.text_input("🔍 Saisir le nom du produit (ex : Glyphosate)")

    if st.button("Analyser le Produit"):
        if product:
            st.write(f"🔎 **Recherche du produit :** {product}")

            # ✅ Lookup du produit
            result = lookup_product(product)
            if result:
                details = extract_product_details(result)

                if details and details.get("name"):
                    st.success(f"✅ Produit trouvé : {details['name']}")

                    # ✅ Affichage des détails du produit
                    st.markdown("### 🧪 **Détails du produit**")
                    st.write(f"- **Nom :** {details['name']}")
                    st.write(f"- **Description :** {details['description']}")
                    st.write(f"- [Lien vers le produit]({details['link']})")

                    # ✅ Analyse des risques
                    st.markdown("### 🚨 **Analyse des risques**")
                    with st.spinner("Analyse en cours..."):
                        risks = analyze_risks(details)
                        if risks:
                            st.success("✅ Analyse des risques complétée !")
                            st.write(risks)
                        else:
                            st.error("❌ Aucune analyse disponible.")

                    # ✅ Recherche d'alternatives biologiques
                    st.markdown("### 🌿 **Alternatives biologiques**")
                    with st.spinner("Recherche des alternatives..."):
                        alternatives = search_alternatives(details['name'])
                        if alternatives:
                            for alt in alternatives:
                                st.markdown(f"- **[{alt['title']}]({alt['link']})** : {alt['snippet']}")
                        else:
                            st.error("❌ Aucune alternative trouvée.")

                    # ✅ Génération du rapport
                    if st.button("📝 Générer le Rapport"):
                        generate_report(details, risks, alternatives)
                        st.success("✅ Rapport généré avec succès !")

                        # ✅ Lien pour télécharger le rapport
                        with open("rapport.txt", "rb") as file:
                            st.download_button(
                                label="📥 Télécharger le rapport",
                                data=file,
                                file_name="rapport.txt",
                                mime="text/plain"
                            )

                else:
                    st.error("❌ Détails du produit incomplets.")
            else:
                st.error("❌ Produit non trouvé.")

if __name__ == "__main__":
    main()
