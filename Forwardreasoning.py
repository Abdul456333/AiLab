from copy import deepcopy

# ---------- Unification (from previous step) ----------

def is_variable(x):
    return isinstance(x, str) and x[0].islower()

def is_compound(x):
    return isinstance(x, tuple) and len(x) > 1

def get_functor(x):
    return x[0]

def get_args(x):
    return x[1:]

def occurs_check(var, x, theta):
    if var == x:
        return True
    elif is_variable(x) and x in theta:
        return occurs_check(var, theta[x], theta)
    elif is_compound(x):
        return any(occurs_check(var, arg, theta) for arg in get_args(x))
    return False

def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if theta is False:
        return False
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif is_compound(x) and is_compound(y):
        if get_functor(x) != get_functor(y) or len(get_args(x)) != len(get_args(y)):
            return False
        return unify(get_args(x), get_args(y), theta)
    elif isinstance(x, (list, tuple)) and isinstance(y, (list, tuple)):
        if len(x) != len(y):
            return False
        if not x:
            return theta
        first_unify = unify(x[0], y[0], theta)
        return unify(x[1:], y[1:], first_unify)
    else:
        return False

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif is_variable(x) and x in theta:
        return unify(var, theta[x], theta)
    elif occurs_check(var, x, theta):
        return False
    else:
        new_theta = deepcopy(theta)
        new_theta[var] = x
        return new_theta

# ---------- Forward Chaining ----------

def substitute(expr, theta):
    """Substitute variables in expr according to theta."""
    if isinstance(expr, str):
        return theta.get(expr, expr)
    elif isinstance(expr, tuple):
        return tuple(substitute(arg, theta) for arg in expr)
    return expr

def forward_chain(KB, query):
    """Prove query using forward chaining."""
    known_facts = set(KB['facts'])
    rules = KB['rules']
    new_inferred = True

    print("Initial facts:", known_facts)

    while new_inferred:
        new_inferred = False
        for rule in rules:
            premises, conclusion = rule
            for theta in match_rule(premises, known_facts):
                new_fact = substitute(conclusion, theta)
                if new_fact not in known_facts:
                    print("Derived:", new_fact)
                    known_facts.add(new_fact)
                    new_inferred = True
                if unify(new_fact, query) is not False:
                    print("\n✅ Query", query, "proved!")
                    return True
    print("\n❌ Query", query, "cannot be proved.")
    return False

def match_rule(premises, facts):
    """Find all substitutions making all premises true."""
    if not premises:
        return [{}]

    first, rest = premises[0], premises[1:]
    matches = []

    for fact in facts:
        theta = unify(first, fact)
        if theta is not False:
            for theta_rest in match_rule([substitute(p, theta) for p in rest], facts):
                merged = deepcopy(theta)
                merged.update(theta_rest)
                matches.append(merged)
    return matches

# ---------- Example ----------

if __name__ == "__main__":
    # Knowledge Base
    KB = {
        'facts': {('Human', 'Socrates')},
        'rules': [
            ([('Human', 'x')], ('Mortal', 'x'))  # Mortal(x) ← Human(x)
        ]
    }

    query = ('Mortal', 'Socrates')

    print("Proving query:", query)
    result = forward_chain(KB, query)
    print("Result:", result)
