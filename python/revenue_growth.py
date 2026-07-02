import pandas as pd

# BlackRock Revenue (USD Billions)
data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Revenue": [16.2, 19.4, 17.9, 17.9, 20.4]
}

df = pd.DataFrame(data)

df["Growth %"] = df["Revenue"].pct_change() * 100

print(df)