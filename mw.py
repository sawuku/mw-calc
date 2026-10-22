#!/usr/bin/env python3
"""Compute the molecular weight of a chemical formula.

Usage: python3 mw.py <formula>
"""
import re
import sys

# Step 1: atomic weights (g/mol)
ATOMIC_WEIGHTS = {
    "H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999,"F": 18.998, "Na": 22.990, "P": 30.974, "S": 32.06, "Cl": 35.45, "Br": 79.904, "Ca": 40.078
    # TODO: add F, Na, P, S, Cl, Br, Ca (look up their weights)
}

# Step 2: turn "C6H12O6" into [("C", 6), ("H", 12), ("O", 6)]
def parse_formula(formula):
    stack = [[]]
    for element, count, open_p, close_p, group in re.findall(r"([A-Z][a-z]?)(\d*)|(\()|(\))(\d*)", formula):
        if element:
            stack[-1].append((element, int(count) if count else 1))
        elif open_p:
            stack.append([])
        elif close_p:
            multiplier = int(group) if group else 1
            inner = stack.pop()
            stack[-1].extend((e, c * multiplier) for e, c in inner)
    return stack[0]


# Step 3: add up weight x count for every element
def molecular_weight(formula):
    total = 0.0
    # TODO: loop over parse_formula(formula)
    # TODO: if an element isn't in ATOMIC_WEIGHTS, raise ValueError
    for element, count in parse_formula(formula):
        if element not in ATOMIC_WEIGHTS:
            raise ValueError("Unknown element: " + element)
        total = total + ATOMIC_WEIGHTS[element] * count

    return total


# Step 4: read the formula from the command line and print the result
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 mw.py <formula>")
        sys.exit(1)
    formula = sys.argv[1]
    print(f"{molecular_weight(formula):.3f}")
    # TODO: sys.argv is a list: ["mw.py", "C6H12O6"]
    # If it doesn't have exactly 2 items, print a usage message and exit.
    # Otherwise print molecular_weight(...) to 3 decimal places.
    pass


if __name__ == "__main__":
    main()
