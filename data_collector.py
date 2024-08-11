import requests
import pandas as pd

def fetch_soccer_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    headers = {
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "YOUR_API_KEY"
    }
    params = {"league": "39", "season": "2023"}  # Premier League, 2023 season
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    fixtures = data['response']
    
    matches = []
    for fixture in fixtures:
        match = {
            'date': fixture['fixture']['date'],
            'home_team': fixture['teams']['home']['name'],
            'away_team': fixture['teams']['away']['name'],
            'home_goals': fixture['goals']['home'],
            'away_goals': fixture['goals']['away']
        }
        matches.append(match)
    
    df = pd.DataFrame(matches)
    df.to_csv('soccer_matches.csv', index=False)
    print("Data saved to soccer_matches.csv")

if __name__ == "__main__":
    fetch_soccer_data()
