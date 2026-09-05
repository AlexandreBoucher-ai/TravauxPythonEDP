import numpy as np
import matplotlib.pyplot as plt

# Question 1
# Sachant la solution y(x), tracer y(x)
# y(x) = 3e^-2x + 2xe^-2

# paramètre (Tous arbitraire)
x_min = 0
x_max = 5 # on pose le range de notre graphique (arbitraire)
N = 100 # nb de pas (arbitraire)

# Crée tableau
x = np.zeros(N+1) # tableau à 1 ligne de N+1 valeurs (car on itère N+1 fois plus tard)
y = np.zeros(N+1)
# on pose les variable comme des tableau, car pour le graphique, il faut que
# x et y forme une suite de point (ou plutoit plusieurs couples de points), et que ce soit donc des itérables
# On aurait donc pu aussi utiliser une simple liste

# calcul du pas (saut entre les points)
# correspond à la dérivé, mais sans que ça soit infinitécimal (car on est en numérique ici)
p = (x_max - x_min)/N

# Équation
for i in range(0, N+1): # Rappel: i va prendre les valeur de 0 à N
    x[i] = x_min + i * p # valeur de x pour cet itération (et en même temps on remplis le tableau de x)
    y[i] = 3 * np.exp(-2*x[i]) + 2 * x[i] * np.exp(-2*x[i])

# Tracer
plt.plot(x,y)

# Correct!

