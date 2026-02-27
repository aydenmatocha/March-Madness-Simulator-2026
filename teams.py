import pandas as pd

url = "https://www.teamrankings.com/ncb"
tables = pd.read_html(url)

df = tables[0]
#print(df)

df["Team"] = df["Team"].str.replace(r"\s*\(.*\)", "", regex=True)

team_ratings = dict(zip(df["Team"], df["Rating"]))
#print(team_ratings)