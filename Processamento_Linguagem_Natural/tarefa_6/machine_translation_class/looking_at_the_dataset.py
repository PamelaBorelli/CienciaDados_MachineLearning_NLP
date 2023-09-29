import pandas as pd

news_csv = "machine_translation_class\data\simplest_eng_fra.csv"

df = pd.read_csv(news_csv)

print(df)

print(" ")

print(df.columns)

print(" ")
print(df['split'].value_counts())

