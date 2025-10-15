import numpy as np
import matplotlib.pyplot as plt

# Définir l'intervalle de -10 à 10 avec 100 points
x = np.linspace(-10, 10, 100)
y = x ** 2

# Tracer la courbe
plt.plot(x, y, label="f(x) = x²")

# Ajouter un titre et des labels
plt.title("Représentation de la fonction f(x) = x²")
plt.xlabel("x")
plt.ylabel("f(x)")

# Ajouter une grille et une légende
plt.grid(True)
plt.legend()

# Afficher la figure
plt.show()
