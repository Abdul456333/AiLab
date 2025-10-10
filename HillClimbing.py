# ---------------------------------------
# Hill Climbing Algorithm for 4-Queens
# Starting State: [2, 1, 4, 3]
# ---------------------------------------

import itertools

def cost_function(state):
    """Count number of attacking queen pairs."""
    n = len(state)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal → attacking
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    """Generate neighbors by swapping any two columns."""
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)
    return neighbors

def hill_climb(initial_state):
    current = initial_state
    current_cost = cost_function(current)
    step = 0

    print(f"Initial State: {current}, Cost = {current_cost}\n")

    while True:
        neighbors = get_neighbors(current)
        neighbor_costs = [(n, cost_function(n)) for n in neighbors]
        
        # Pick the neighbor with minimum cost
        best_neighbor, best_cost = min(neighbor_costs, key=lambda x: x[1])

        print(f"Step {step}: Current = {current}, Cost = {current_cost}")
        for n, c in neighbor_costs:
            print(f"    Neighbor: {n}, Cost = {c}")
        print(f"  → Best neighbor: {best_neighbor}, Cost = {best_cost}\n")

        # Stop if no improvement
        if best_cost >= current_cost:
            print(f"Terminated. Local optimum reached at {current} with Cost = {current_cost}")
            break

        # Move to better neighbor
        current, current_cost = best_neighbor, best_cost
        step += 1

        # Stop if perfect solution found
        if current_cost == 0:
            print(f"Goal reached: {current}")
            break

    return current, current_cost

# Run the algorithm
initial_state = [2, 1, 4, 3]
final_state, final_cost = hill_climb(initial_state)
