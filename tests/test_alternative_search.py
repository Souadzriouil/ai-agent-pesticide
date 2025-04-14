from src.agents.alternative_search import search_alternatives

def test_search_alternatives():
    product_name = "Glyphosate"
    results = search_alternatives(product_name)
    
    assert results is not None
    assert len(results) > 0
    
    print("✔️ Test OK : Alternatives trouvées")
    for result in results:
        print(f"- {result['title']}\n{result['snippet']}\n{result['link']}\n")

if __name__ == "__main__":
    test_search_alternatives()
