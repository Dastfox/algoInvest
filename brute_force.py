import csv
import itertools
import os
import time
from itertools import combinations
from utils import clear_console


def brute_force(actions, budget=500):
    n = len(actions)
    max_profit = -1
    best_portfolio = None
    portfolio_count = 0  # Initialiser le compteur

    # Parcourir tous les portfolios possibles
    for i in range(2**n):
        clear_console()
        portfolio = []
        total_cost = 0
        total_profit = 0

        # Convertir le nombre entier en binaire pour représenter le portfolio
        binary = bin(i)[2:].zfill(n)
 
        # Parcourir chaque action et ajouter à la liste du portfolio si l'action est sélectionnée
        for j in range(n):
            if binary[j] == "1":
                portfolio.append(actions[j]["name"])
                total_cost += actions[j]["price"]
                total_profit += actions[j]["benefit"]

        # Si le coût total est inférieur ou égal au budget et que le profit est le maximum jusqu'à présent, mettre à jour le résultat
        if total_cost <= budget and total_profit > max_profit:
            max_profit = total_profit
            best_portfolio = portfolio

        # Incrementer le compteur et afficher l'index du portfolio en cours de calcul
        portfolio_count += 1
        print(
            f"Calcul du portfolio {portfolio_count}, meilleur profit trouvé: {round(max_profit,2)} pour le portfolio: {best_portfolio}"
        )

    # Retourner le résultat
    return (max_profit, best_portfolio)
