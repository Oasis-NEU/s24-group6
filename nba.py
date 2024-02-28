from nba_api.stats.endpoints import leaguedashteamstats
import requests
import json
import pandas as pd

response = leaguedashteamstats.LeagueDashTeamStats(
    team_id_nullable='0',
    league_id_nullable='00',
    season= '2023-24',
    season_type_all_star='Regular Season',
    headers={'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Host': 'stats.nba.com',
'Origin': 'https://www.nba.com',
'Referer': 'https://www.nba.com/',
'sec-ch-ua': '"Google Chrome";v="87", "\"Not;A\\Brand";v="99", "Chromium";v="87"',
'sec-ch-ua-mobile': '?1',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
'x-nba-stats-origin': 'stats',
'x-nba-stats-token': 'true'})


df = response.get_data_frames()[0]

print(df.to_string())