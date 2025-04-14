import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Configurer l'API Gemini
genai.configure(api_key=GEMINI_API_KEY)

def analyze_risks(details):
    try:
        prompt = f"Analyse les risques du produit suivant : {details['name']}\nDescription : {details['description']}"
        
        # Utilisation du modèle gemini-1.5-flash-latest
        model = genai.GenerativeModel('gemini-1.5-flash-latest') 
        response = model.generate_content(prompt)
        
        if response and hasattr(response, 'text'):
            return response.text.strip()
        else:
            print("⚠️ Aucune réponse du modèle Gemini.")
            return None
    except Exception as e:
        print(f"Erreur lors de l'analyse des risques : {e}")
        return None
