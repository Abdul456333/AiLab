import random
import math

# -------------------- Helper Functions --------------------

# Compute number of conflicts for a given state
def compute_conflicts(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i+1, n):
            # Same column
            if state[i] == state[j]:
                conflicts += 1
            # Same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

# Generate a neighbor by moving a queen in one column
def generate_neighbor(state):
    n = len(state)
    new_state = state[:]
    col = random.randint(0, n-1)
    new_row = random.randint(0, n-1)
    new_state[col] = new_row
    return new_state

# -------------------- Simulated Annealing --------------------

def simulated_annealing(n, T=100.0, cooling_rate=0.99, max_steps=5000):
    # Random initial state
    state = [random.randint(0, n-1) for _ in range(n)]
    current_conflicts = compute_conflicts(state)

    for step in range(max_steps):
        if current_conflicts == 0:
            return state, step  # Solution found
        
        neighbor = generate_neighbor(state)
        neighbor_conflicts = compute_conflicts(neighbor)

        delta = neighbor_conflicts - current_conflicts

        # Accept move based on SA probability
        if delta < 0 or random.random() < math.exp(-delta / T):
            state = neighbor
            current_conflicts = neighbor_conflicts

        # Decrease temperature
        T *= cooling_rate

        # Temperature too low → stop
        if T < 0.0001:
            break

    return state, -1  # No exact solution found


# -------------------- MAIN PROGRAM --------------------

# User input
n = int(input("Enter number of queens (default 8): ") or 8)

solution, steps = simulated_annealing(n)

print("\nFinal Result:")
print("Board State (row positions of queens in each column):", solution)
print("Conflicts:", compute_conflicts(solution))

if steps != -1:
    print("Solved in", steps, "steps using Simulated Annealing!")
else:
    print("Could not find perfect solution, but best attempt shown.")

# Print board
print("\nChess Board:")
board = [["." for _ in range(n)] for _ in range(n)]
for col, row in enumerate(solution):
    board[row][col] = "Q"

for row in board:
    print(" ".join(row))
