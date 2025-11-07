def occur_check(var, expr):
    """Checks if variable occurs in expression (to avoid infinite recursion)."""
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occur_check(var, subexpr) for subexpr in expr)
    else:
        return False

def unify(x, y, subst=None):
    """Unify two expressions Ψ1 and Ψ2."""
    if subst is None:
        subst = {}

    # Step 1: If Ψ1 or Ψ2 is a variable or constant
    if isinstance(x, str) and x.islower():  # variable (e.g., x, y)
        if x in subst:
            return unify(subst[x], y, subst)
        elif occur_check(x, y):
            return None  # FAILURE
        else:
            subst[x] = y
            return subst

    elif isinstance(y, str) and y.islower():
        if y in subst:
            return unify(x, subst[y], subst)
        elif occur_check(y, x):
            return None  # FAILURE
        else:
            subst[y] = x
            return subst

    # Step 2: If both are identical constants
    elif x == y:
        return subst

    # Step 3: If one is a predicate (list form)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None  # FAILURE (different number of arguments)
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst

    # Step 4: Else failure
    else:
        return None


# ---------- Example Tests ----------
print(unify(['P', 'x', 'y'], ['P', 'a', 'b']))    # {'x': 'a', 'y': 'b'}
print(unify(['Q', 'x', 'x'], ['Q', 'a', 'b']))    # None (failure)
print(unify(['Knows', 'John', 'x'], ['Knows', 'y', 'Bill']))  # {'x': 'Bill', 'y': 'John'}
print(unify('x', 'John'))                         # {'x': 'John'}
