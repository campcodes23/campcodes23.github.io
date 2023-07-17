import pandas as pd

df = pd.read_csv('spotify.csv')
df.head(300).to_csv('spotify.csv')


# eof