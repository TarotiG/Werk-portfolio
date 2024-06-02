import requests
import json


api_token = "sMX03TE0zXt9tpkax_FjcVA1VI-pLh-JMW7GSNk6AO8"
req = requests.get(f"https://trefle.io/api/v1/plants/search?token={api_token}&q=coconut")

if req.status_code == 200:
    coconut_data = req.json()

    with open("./test.txt", "w") as test:
        test.write(json.dumps(
            coconut_data,
            indent=4
            )
        )

# id
# common_name
# image_url