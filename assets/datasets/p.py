import pandas as pd

df = pd.read_csv('https://campcodes23.github.io/assets/datasets/spotify.csv')
df.head(300).to_csv('spotify_small.csv')

# eof

