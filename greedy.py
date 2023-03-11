import time


def greedy(data):
    # Calculate the benefit for each action
    benefits = [(action.price * (100 + action.profit) / 100) for action in data]
    for i, action in enumerate(data):
        action.benefit = benefits[i]
    # Sort the actions by descending order of benefit
    sorted_data = sorted(
        data,
        key=lambda x: x.benefit,
        reverse=True,
    )

    # Initialize the knapsack
    budget = 500
    portfolio = []
    total_benefit = 0
    actions_checked = 0
    start_time = time.time()
    # Fill the knapsack with actions
    for action in sorted_data:
        if action.price <= budget and action.benefit > 0:
            portfolio.append(action)
            total_benefit += action.benefit
            budget -= action.price
        actions_checked += 1
        if budget <= 0:
            break

    # Consider any unused budget as profit
    total_benefit += budget

    end_time = time.time()
    total_time = end_time - start_time
    # Print the portfolio and total benefit
    for action in portfolio:
        print(
            action.name,
            action.price,
            round(action.benefit, 2),
        )
    print("Total benefit after 2 years: {}€".format(round(total_benefit - 500, 2)))
    print("Total cost: {}€".format(round(500 - budget, 2)))
    print("Actions checked: {}".format(actions_checked))
    print("Time taken: {} seconds".format(round(total_time, 5)))
