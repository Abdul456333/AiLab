import itertools

# Evaluate propositional logic expressions
def pl_true(expr, model):
    if isinstance(expr, str):
        return model[expr]
    op = expr[0]
    if op == 'not':
        return not pl_true(expr[1], model)
    elif op == 'and':
        return pl_true(expr[1], model) and pl_true(expr[2], model)
    elif op == 'or':
        return pl_true(expr[1], model) or pl_true(expr[2], model)
    elif op == 'implies':
        return (not pl_true(expr[1], model)) or pl_true(expr[2], model)
    elif op == 'iff':
        return pl_true(expr[1], model) == pl_true(expr[2], model)
    else:
        raise ValueError("Unknown operator: " + op)

# Extract all symbols used
def extract_symbols(*exprs):
    symbols = set()
    for expr in exprs:
        if isinstance(expr, str):
            symbols.add(expr)
        elif isinstance(expr, tuple):
            for e in expr[1:]:
                symbols.update(extract_symbols(e))
    return symbols

# Truth table entailment check
def tt_entails(kb, query):
    symbols = list(extract_symbols(kb, query))
    all_models = list(itertools.product([False, True], repeat=len(symbols)))

    print(f"{' | '.join(symbols)} | KB | Query | Considered?")
    print("-" * 40)

    all_true = True
    for vals in all_models:
        model = dict(zip(symbols, vals))
        kb_val = pl_true(kb, model)
        query_val = pl_true(query, model)
        considered = "✓" if kb_val else "-"
        print(f"{' | '.join(['T' if v else 'F' for v in vals])} | "
              f"{'T' if kb_val else 'F'} | "
              f"{'T' if query_val else 'F'} | {considered}")

        # If KB is true but query is false → entailment fails
        if kb_val and not query_val:
            all_true = False

    return all_true

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Knowledge Base: (P => Q) and P
    kb = ('and', ('implies', 'P', 'Q'), 'P')
    query = 'Q'

    result = tt_entails(kb, query)
    print("\nDoes KB entail Query?", result)
