import numpy as np
import matplotlib.pyplot as plt

# Semaine 2

# Question 1
# Tracer dans une même figure les 3 premiers polynôme de Legendre-Fournier dans un même graphique
# Pour x entre -1 et 1

# Nombre de pas (arbitraire)
N = 100

# Intervalle
x = np.linspace(-1, 1, N+1) # Une autre technique que celle utiliser à la semaine 1, et que je préfère, mais,
# Prof ne donne pas la fonction linspace
# Donc finalement, je pense qu'il est préférable de définir x dans une boucle, selon x[i] = xmin + p*i

# P_0
P_0 = np.ones(N+1)

# P_1
P_1 = np.zeros(N+1)
for i in range(0, N+1):
    P_1[i] = x[i]

# P_2
P_2 = np.zeros(N+1)
for i in range(0, N+1):
    P_2[i] = 1/2 * (3*x[i]**2 - 1)


plt.figure()
plt.plot(x, P_0)
plt.plot(x, P_1)
plt.plot(x, P_2)

# Correct!


# Semaine 1

# Question 1
# Sachant la solution y(x), tracer y(x)
# y(x) = 3e^-2x + 2xe^-2

# 1.paramètre (Tous arbitraire)
x_min = 0
x_max = 5 # on pose le range de notre graphique (arbitraire)
N = 100 # nb de pas (arbitraire)

# 2. Crée tableau
x = np.zeros(N+1) # tableau à 1 ligne de N+1 valeurs (car on itère N+1 fois plus tard)
y = np.zeros(N+1)
# on pose les variable comme des tableau, car pour le graphique, il faut que
# x et y forme une suite de point (ou plutoit plusieurs couples de points), et que ce soit donc des itérables
# On aurait donc pu aussi utiliser une simple liste

# 3. calcul du pas (saut entre les points)
# va servir pour savoir combien il faut ajouter à entre chaque x
p = (x_max - x_min)/N

# 4. Équation (on optient une liste de point utilisable dans le graphique)
for i in range(0, N+1): # Rappel: i va prendre les valeur de 0 à N
    x[i] = x_min + i * p # valeur de x pour cet itération (et en même temps on remplis le tableau de x)
    y[i] = 3 * np.exp(-2*x[i]) + 2 * x[i] * np.exp(-2*x[i])

# Tracer
plt.plot(x,y)

# Correct!

