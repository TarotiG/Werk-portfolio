"""
Acties nog te doen:
- Script aanpassen, zodat het de database kan vullen met data
- Meer items binnen halen via de API
"""
import requests


def get_coconuts() -> list:
    api_token = "sMX03TE0zXt9tpkax_FjcVA1VI-pLh-JMW7GSNk6AO8"
    req = requests.get(f"https://trefle.io/api/v1/plants/search?token={api_token}&q=coconut")
        
    coconuts = []
        
    if req.status_code == 200:
        coconut_data = req.json()
        
        for type_coconut in coconut_data["data"]:
            coconut = {
                "id": type_coconut["id"],
                "naam": type_coconut["common_name"],
                "afbeelding_url": type_coconut["image_url"]
            }
        
            if coconut["naam"] is None:
                coconut["naam"] = coconut_data["data"][0]["synonyms"][0]
        
            for i in range(len(coconut_data["data"])):
        
                if coconut in coconuts:
                    continue
                else:
                    coconuts.append(coconut)
    
    return coconuts