def knapsack(weights, values, capacity):
    """Solves the 0-1 knapsack problem using the branch and bound strategy.

    Args:
        weights: A list of weights for each item.
        values: A list of values for each item.
        capacity: The knapsack capacity.

    Returns:
        The maximum value that can be obtained by filling the knapsack.
    """

    n = len(weights)

    # Initialize the best solution with an empty set of items and a value of 0.
    best_solution = []
    best_value = 0

    # Define a recursive function to explore the search tree.
    def explore(solution, value, weight, level):
        nonlocal best_solution, best_value

        # Check if the current solution is feasible.
        if weight > capacity:
            return

        # Update the best solution if the current solution is better.
        if value > best_value:
            best_solution = solution[:]
            best_value = value

        # If we have reached the last level of the search tree, return the current solution.
        if level == n:
            return

        # Explore the two possible branches: include the current item or not.
        explore(solution + [level], value + values[level], weight + weights[level], level + 1)
        explore(solution, value, weight, level + 1)

    # Explore the search tree starting from the root node.
    explore([], 0, 0, 0)

    return best_value, best_solution

# Get user input for weights, values, and capacity
n = int(input("Enter the number of items: "))
weights = [int(input(f"Enter weight {i + 1}: ")) for i in range(n)]
values = [int(input(f"Enter value {i + 1}: ")) for i in range(n)]
capacity = int(input("Enter knapsack capacity: "))

# Solve the knapsack problem using branch and bound strategy
max_value, best_solution = knapsack(weights, values, capacity)

# Print the maximum value and best solution
print("Maximum value:", max_value)
print("Best solution:", best_solution)