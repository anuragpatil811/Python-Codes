import math

# Function for solving recurrence using Recursion Tree method (Merge Sort Example)
def rec_tree(n):
    if n == 1:
        return 1  # Base case T(1) = 1
    cost_at_current_level = n  # Cost at the current level (O(n))
    subproblem_cost = 2 * rec_tree(n // 2)  # Cost of subproblems (2T(n/2))
    return cost_at_current_level + subproblem_cost  # Total cost

# Function for solving recurrence using Substitution method
# Guessing that T(n) = O(n log n)
def substitution_method(n):
    if n == 1:
        return 1  # Base case T(1) = 1
    return 2 * substitution_method(n // 2) + n  # Recurrence relation: T(n) = 2T(n/2) + n

# Main function
def main():
    # Change this for testing purposes, to bypass input() issue
    n = int(input("Enter the value of n (problem size): "))
    
    # If interactive input is an issue, replace it with: 
    # n = 8

    # Solving using Recursion Tree method
    result_rec_tree = rec_tree(n)
    print(f"Result using Recursion Tree method: {result_rec_tree}")

    # Solving using Substitution method
    result_substitution = substitution_method(n)
    print(f"Result using Substitution method: {result_substitution}")

if __name__ == "__main__":
    main()
