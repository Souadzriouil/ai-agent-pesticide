from src.agents.risk_analysis import analyze_risks

def test_analyze_risks():
    details = {
        "name": "Glyphosate",
        "description": "Herbicide controversé utilisé en agriculture."
    }
    result = analyze_risks(details)
    assert result is not None
    print("✔️ Test OK : Risque analysé")
    print(result)

if __name__ == "__main__":
    test_analyze_risks()
