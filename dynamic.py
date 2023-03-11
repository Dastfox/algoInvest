import time
from utils import clear_console


def dynamic_programming(actions, max_budget):
    """
    Calcule la solution optimale d'un problème de sac à dos.

    Args:
        actions (list): une liste d'actions, chaque action étant représentée par une liste contenant trois éléments :
                        le nom de l'action (str), son coût (float) et son profit (float).
        max_budget (float): le budget maximal disponible.

    Returns:
        Un tuple contenant trois éléments :
            - le profit maximal (float),
            - la somme totale dépensée (float),
            - la liste des actions sélectionnées pour atteindre le profit maximal (list).
    """
    clear_console()
    print("Calcul de la solution optimale avec la programmation dynamique...")
    actions = actions_to_list(actions)

    # Convertir les coûts et profits des actions en centimes pour éviter les erreurs d'arrondi avec les float
    max_budget *= 100
    for action in actions:
        action[1] = int(action[1] * 100)
        action[2] = action[2] * action[1] / 100

    # Initialiser la matrice de programmation dynamique avec des zéros
    matrix = [
        [0 for budget in range(max_budget + 1)]
        for action_index in range(len(actions) + 1)
    ]

    # Remplir la matrice avec les valeurs optimales
    for action_index in range(1, len(actions) + 1):
        for budget in range(1, max_budget + 1):
            if actions[action_index - 1][1] <= budget:
                matrix[action_index][budget] = max(
                    actions[action_index - 1][2]
                    + matrix[action_index - 1][budget - actions[action_index - 1][1]],
                    matrix[action_index - 1][budget],
                )
            else:
                matrix[action_index][budget] = matrix[action_index - 1][budget]

    # Récupérer la liste des actions sélectionnées pour atteindre le profit maximal
    max_profit = matrix[-1][-1] / 100
    remaining_budget = max_budget
    selected_actions = []
    action_len = len(actions)

    while remaining_budget >= 0 and action_len >= 0:
        current_action = actions[action_len - 1]
        if (
            matrix[action_len][remaining_budget]
            == matrix[action_len][remaining_budget - current_action[1]]
            + current_action[2]
        ):
            selected_actions.append(current_action)
            remaining_budget -= current_action[1]
        action_len -= 1

    # Reconvertir les coûts et profits des actions en float
    for action in selected_actions:
        action[1] /= 100
        action[2] = round(action[2] / 100, 3)

    # Calculer la somme totale dépensée
    total_spending = 0
    for action in selected_actions:
        total_spending += action[1]

    return max_profit, total_spending, selected_actions


def print_dynamic_results(actions, budget=500):
    start = time.time()
    result = dynamic_programming(actions, budget)
    for action in result[2]:
        print(
            action[0],
            action[1],
        )
    print("Total cost: {}€".format(round(result[1], 2)))
    print("Total benefit after 2 years: {}€".format(round(result[0], 2)))
    print("Time taken: {} seconds".format(round(time.time() - start, 5)))


def actions_to_list(actions):
    """
    Converts a list of Action objects into a nested list.

    Args:
        actions (list[Action]): List of Action objects.

    Returns:
        list[list]: Nested list representation of the Action objects.
    """
    nested_list = []

    for action in actions:
        if action.price > 0:
            nested_list.append([action.name, action.price, action.profit])

    return nested_list
