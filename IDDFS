# ------------------------------------------------------
# Iterative Deepening Depth-First Search (IDDFS)
# Demonstration using a tree similar to the image
# ------------------------------------------------------

# Build the graph (adjacency list)
graph = {
    "123048758": ["103428756", "123408756", "123746056"],  # Depth 1
    "103428756": ["013428756", "123428756"],               # Depth 2
    "123408756": ["123458706", "123468756"],               # Depth 2
    "123746056": ["203746058", "203748056"],               # Depth 2
    "013428756": [], "123428756": [],                      # Depth 3 (leaf)
    "123458706": [], "123468756": [],                      # Depth 3 (leaf)
    "203746058": [], "203748056": []                       # Depth 3 (leaf)
}

# Depth-Limited Search (recursive)
def dls(node, goal, depth, path):
    print(f"Visiting: {node} | Depth remaining: {depth} | Path: {path + [node]}")
    if node == goal:
        return path + [node]
    if depth == 0:
        return None
    for child in graph.get(node, []):
        found = dls(child, goal, depth - 1, path + [node])
        if found:
            return found
    return None

# Iterative Deepening DFS
def iddfs(start, goal, max_depth):
    print(f"Starting IDDFS from {start} to reach goal {goal}\n")
    for depth in range(max_depth + 1):
        print(f"\n====== DEPTH LIMIT = {depth} ======")
        result = dls(start, goal, depth, [])
        if result:
            print(f"\nGoal found at depth {depth}")
            return result
    print("\nGoal not found within max depth")
    return None


# --- Main Program ---
if __name__ == "__main__":
    start_node = "123048758"     # root (Depth 0)
    goal_node  = "123468756"     # one of the nodes at depth 3
    max_depth  = 3               # just like the figure

    path = iddfs(start_node, goal_node, max_depth)
    print("\nFinal Path Found:", path)
