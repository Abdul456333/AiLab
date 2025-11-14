import math

# Alpha-Beta pruning function
def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # If leaf node:
    if depth == 0:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):  # binary tree
            val = alphabeta(depth - 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruning at MAX node: alpha={alpha}, beta={beta}")
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth - 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruning at MIN node: alpha={alpha}, beta={beta}")
                break
        return best


# -------------------------
#         USER INPUT
# -------------------------
depth = int(input("Enter depth of tree (e.g., 2 for 4 leaf nodes): "))

num_leaves = 2 ** depth
print(f"Enter {num_leaves} leaf values separated by space:")

values = list(map(int, input().split()))

if len(values) != num_leaves:
    print("Error: number of leaf values does not match 2^depth.")
else:
    result = alphabeta(depth, 0, True, values, -math.inf, math.inf)
    print("\nFinal minimax result with alpha-beta pruning:", result)
