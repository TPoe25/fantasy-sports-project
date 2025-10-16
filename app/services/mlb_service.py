import requests

def get_mlb_team_stats():
    url = "https://statsapi.mlb.com/api/v1/teams"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        data = r.json()
        return [{"name": t["name"], "league": t["league"]["name"]} for t in data["teams"]]
    return {"error": "MLB API unavailable"}
