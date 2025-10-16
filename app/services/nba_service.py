import requests

def get_latest_nba_stats():
    url = "https://www.balldontlie.io/api/v1/players?per_page=5"
    r = requests.get(url, timeout=10)
    return r.json() if r.status_code == 200 else {"error": "NBA API unavailable"}
