def extract_product_details(data):
    if not data:
        return None
    
    return {
        "name": data.get("title", ""),  # Utiliser 'title' si 'name' est absent
        "description": data.get("snippet", ""),
        "link": data.get("link", "")
    }
