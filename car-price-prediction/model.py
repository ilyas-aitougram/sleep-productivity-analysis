import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Charger les données
import os

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "data.csv")

df = pd.read_csv(csv_path)

print("=== APERCU DES DONNEES ===")
print(df.head())

# Variables d'entrée
X = df[["age", "km", "power", "brand_score"]]

# Variable à prédire
y = df["price"]

# Séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Création du modèle
model = LinearRegression()

# Entraînement
model.fit(X_train, y_train)

# Prédictions
predictions = model.predict(X_test)

print("\n=== RESULTATS ===")
print("Erreur moyenne :", mean_absolute_error(y_test, predictions))
print("Score R2 :", r2_score(y_test, predictions))

# Exemple de prédiction
new_car = pd.DataFrame({
    "age": [3],
    "km": [50000],
    "power": [120],
    "brand_score": [7]
})

price = model.predict(new_car)

print("\nPrix estimé :")
print(round(price[0], 2), "€")
import matplotlib.pyplot as plt

plt.scatter(y_test, predictions)
plt.xlabel("Prix réel")
plt.ylabel("Prix prédit")
plt.title("Comparaison prix réels / prix prédits")
plt.show()