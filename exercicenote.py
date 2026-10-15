import numpy as np
import matplotlib.pyplot as plt




# Module 3:
# Question 1: Variation en x: (valeur de t constante)

# 1. Valeurs imposés:
L = 1.0 # (= x_max)
c = 1.0
t = 0.25
Nx = 1001 # Nombre de point (arbitraire) 
N = 20 # Indice n pour la somme partielle de la série (arbitraires)

# 2. Calcul du Pas en x (domaine spatiale) = longueur entre chaque points
P = L/(Nx - 1)

# 3. Innitialisation (itérable avec Nx case libre)
x = np.zeros(Nx)
u = np.zeros(Nx)

# 4. Valeurs pour x:
for i in range(Nx):
    x[i] = P*i
# remarque: x_min va être = 0 car le premier i = 0

# 5. Valeus pour u, où on approxime u par une série (sommation) des n premiers termes (n=20)
# on utilise l'équation du cahier: Sommation((Acos(kt)+Bsin(kt))sin(kx))
# k = n * Pi * c / L = n * Pi (car c et L =1)
for n in range(N+1):
    # 5.1 Calcul coefficient
    if n % 2 == 0:
        continue
        # a_n pair = 0
    else:
        # Le corrigé ne donne pas f(x) et il ici il faut assumer que l'intégrale a été résolu à la main préalablement
        a_n = (4/(n*np.pi)*np.cos(n*np.pi*t)
            - 8*L/(n**2*np.pi**2))
        # 5.2 Calcul de la sommation (approximation de u)
        # Remarque: On additionne le résultat précédent, donc pour chaque n (a_n), on additionne toutes les valeurs u(x_i,t) 
        # Boucle dans une boucle, donc le a_n calculé dans la boucle courante est utilisé dans une autre boucle
        for i in range(Nx):
            u[i] += (a_n * np.sin(n*np.pi*t))*np.sin(n*np.pi*x[i])

# 6. Tracer
plt.plot(x, u)
# OK (pas exactement pareil, petite erreur à quelque part)

# Question 2: Variation en t: (valeur de x constant)
# 1. Valeur imposé:
L = 1.0
c = 1.0
x = 0.5
t_fin = 2.0 # car t n'est pas sur l'intervalle de L
Nt = 1001 # (Nb de points de t)
N = 20

# 2. Pas entre chaque t
P = t_fin/(Nt - 1)

# 3. Défini nos espaces:
t = np.zeros(Nt)
u = np.zeros(Nt)

# 4. Défini le domaine de t: (t0 = 0)
for i in range(Nt):
    t[i] = P*i

# 5. Valeur pour u par une sommation de n = 20
for n in range(N+1):
    if n%2 == 0:
        A = 0
        B = 0
    else: # ici j'ai aucune idée d'où sorte les équations des coefficients 
        A = 4/(n*np.pi)
        B = -8*L/(n**2*np.pi**2*c)

        #Calcul de u fixer à x pour chaque instant t:
        for i in range(Nt):
            u[i] += (
            A*np.cos(n*np.pi*c*t[i]/L)
            + B*np.sin(n*np.pi*c*t[i]/L)
        )*np.sin(n*np.pi*x/L)
plt.figure()
plt.plot(t,u)
#Correct

# Module 2

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

