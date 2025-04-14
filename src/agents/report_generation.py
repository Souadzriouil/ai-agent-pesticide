def generate_report(details, risks, alternatives):
    report = f"""
    🔎 **Produit :** {details['name']}
    📖 **Description :** {details['description']}
    🌍 **Lien :** {details['link']}
    
    🚨 **Analyse des Risques :**
    {risks}
    
    🌿 **Alternatives Biologiques :**
    """
    
    if alternatives:
        for alt in alternatives:
            report += f"\n- [{alt['title']}]({alt['link']}) : {alt['snippet']}"
    else:
        report += "\n❌ Aucune alternative trouvée."
    
    with open("rapport.txt", "w", encoding="utf-8") as file:
        file.write(report)
    
    print("✅ Rapport généré avec succès !")
