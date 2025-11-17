import itertools

# ---------------------------
#  Convert sentence to CNF (simple)
# ---------------------------
def parse_clause(clause):
    """
    Parses clause of form:
       A v B v ~C
    Returns a set: {"A", "B", "~C"}
    """
    parts = clause.replace(" ", "").split("v")
    return set(parts)

# ---------------------------
# Resolution rule
# ---------------------------
def resolve(ci, cj):
    resolvents = []
    for di in ci:
        if di.startswith("~"):
            complementary = di[1:]
        else:
            complementary = "~" + di

        if complementary in cj:
            new_clause = (ci - {di}) | (cj - {complementary})
            resolvents.append(new_clause)

    return resolvents


# ---------------------------
# Resolution Algorithm
# ---------------------------
def resolution(kb, query):
    # Negate query and add into KB
    negated_query = "~" + query if not query.startswith("~") else query[1:]
    kb.append(parse_clause(negated_query))

    print("\nNegated Query added to KB:", parse_clause(negated_query))

    new = set()

    while True:
        pairs = list(itertools.combinations(kb, 2))

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)

            for resolvent in resolvents:
                print("Resolving:", ci, "and", cj, "=>", resolvent)

                if len(resolvent) == 0:
                    print("\n==== EMPTY CLAUSE GENERATED ====")
                    print("✔ Query is TRUE (entailed by KB).")
                    return True

                new_clause = frozenset(resolvent)
                new.add(new_clause)

        # If no new clauses → cannot prove
        new_kb_clauses = [frozenset(c) for c in kb]
        if new.issubset(new_kb_clauses):
            print("\n❌ No new clauses produced.")
            print("✘ Query cannot be proven from KB.")
            return False

        for c in new:
            if c not in new_kb_clauses:
                kb.append(set(c))


# --------------------------------------------------------
# MAIN: USER INPUT
# --------------------------------------------------------
print("Enter number of clauses in Knowledge Base:")
n = int(input("> "))

kb = []
print("\nEnter each clause in CNF form (use v for OR, ~ for NOT):")
print("Example: A v ~B v C")

for i in range(n):
    clause = input(f"Clause {i+1}: ")
    kb.append(parse_clause(clause))

print("\nEnter the query to prove:")
query = input("> ").strip()

print("\n========== Knowledge Base ==========")
for c in kb:
    print(c)

print("\nQuery:", query)
print("\n=========== RESOLUTION ============")
resolution(kb, query)
