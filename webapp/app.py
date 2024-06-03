from flask import Flask, render_template
import requests
# from scripts.plants import get_coconuts

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

app = Flask(__name__)
coconuts = get_coconuts()

@app.route("/")
def homepage():
    return render_template(
        "home.html",
        COCONUTS=coconuts
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )