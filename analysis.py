import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

print("DATA PREVIEW")
print(df.head())

print("\nSTATS")
print(df.describe())

plt.scatter(df["sleep_hours"], df["productivity_score"])
plt.title("Sommeil vs Productivité")
plt.xlabel("Heures de sommeil")
plt.ylabel("Productivité")
plt.show()

plt.scatter(df["exercise_minutes"], df["sleep_hours"])
plt.title("Sport vs Sommeil")
plt.xlabel("Minutes de sport")
plt.ylabel("Heures de sommeil")
plt.show()

plt.scatter(df["coffee_intake"], df["productivity_score"])
plt.title("Café vs Productivité")
plt.xlabel("Café")
plt.ylabel("Productivité")
plt.show()
correlation = df.corr(numeric_only=True)

print("\nMatrice de corrélation")
print(correlation)