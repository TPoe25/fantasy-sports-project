import requests

def get_nfl_data():
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        data = r.json()
        return [t["team"]["displayName"] for t in data["sports"][0]["leagues"][0]["teams"]]
    return {"error": "NFL API unavailable"}
