import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.data_extraction import extract_product_details

def test_extract_product_details():
    sample_data = {
        "title": "Glyphosate",
        "snippet": "Herbicide controversé utilisé en agriculture.",
        "link": "https://fr.wikipedia.org/wiki/Glyphosate"
    }
    result = extract_product_details(sample_data)
    assert result is not None
    assert result['name'] == "Glyphosate"
    print("✔️ Test OK : Détails extraits")

if __name__ == "__main__":
    test_extract_product_details()
