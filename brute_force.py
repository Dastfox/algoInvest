from utils import clear_console


def brute_force(actions, budget=500):
    actions = [action for action in actions if action.price > 0 or action.benefit > 0]
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
                portfolio.append(actions[j].name)
                total_cost += actions[j].price
                total_profit += actions[j].benefit

        # Si le coût total est inférieur ou égal au budget et que
        # le profit est le maximum jusqu'à présent, mettre à jour le résultat
        if total_cost <= budget and total_profit > max_profit:
            max_profit = total_profit
            best_portfolio = portfolio

        # Incrementer le compteur et afficher l'index du portfolio en cours de calcul
        portfolio_count += 1
        print(
            f"Calcul du portfolio {portfolio_count},",
            f"meilleur profit trouvé: {round(max_profit,2)} pour le portfolio: {best_portfolio}",
        )

    # Retourner le résultat
    return (max_profit, best_portfolio)


from queue import PriorityQueue
from utils import clear_console


def brute_force_PQ(actions, budget=500):
    # Sort the actions by their benefits in decreasing order
    actions = sorted(actions, key=lambda x: x.benefit, reverse=True)

    # Clean the actions list by removing actions with a price of > 0 and a benefit > 0
    actions = [action for action in actions if action.price > 0 or action.benefit > 0]
    # Create a priority queue to store the subsets to be processed
    q = PriorityQueue()

    # Add the root node (empty subset) to the priority queue
    q.put((0, [], 0, 0))

    max_profit = -1
    best_subset = None
    processed_count = 0  # Initialiser le compteur

    # Process the subsets in the priority queue
    while not q.empty():
        # Get the subset with the highest benefit-to-cost ratio
        _, subset, total_cost, total_profit = q.get()

        # If the subset has a higher profit than the best subset found so far,
        # update the best subset and the maximum profit
        if total_profit > max_profit:
            max_profit = total_profit
            best_subset = subset

        # Add each action to the subset, calculate the cost and profit of the new subset,
        # and add it to the priority queue if its cost is less than or equal to the budget
        for i, action in enumerate(actions):
            actions_in_best_subset = [actions[i] for i in best_subset]
            clear_console()
            print(
                f"Processing subset {processed_count +1}...\nBest profit found: {round(max_profit,2)} for subset: {actions_in_best_subset}\nAction: #{i}"
            )
            new_subset = subset + [i]
            new_cost = total_cost + action.price
            new_profit = total_profit + action.benefit

            if new_cost <= budget and new_subset != subset:
                q.put(
                    (new_profit / (new_cost + 1e-9), new_subset, new_cost, new_profit)
                )

        # Increment the processed count and print the progress
        processed_count += 1
        if processed_count % 10000 == 0:
            print(f"Processed {processed_count} subsets so far...")

    # Construct the list of actions in the best subset
    actions_in_best_subset = [actions[i] for i in best_subset]

    # Return the maximum profit and the list of actions in the best subset
    return max_profit, actions_in_best_subset
