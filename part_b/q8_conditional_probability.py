import sys
import os

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

def check_prob(val, name):
    """Validate that probability is between 0 and 1."""
    if val < 0.0 or val > 1.0:
        raise ValueError(f"Probability {name} must be between 0 and 1 (inclusive). Got {val}")

def calculate_conditional_basic():
    print("\n--- Basic Conditional Probability P(A|B) = P(A ∩ B) / P(B) ---")
    try:
        p_b = float(input("Enter P(B) - probability of event B occurring: "))
        check_prob(p_b, "P(B)")
        if p_b == 0:
            print("Error: P(B) cannot be 0 because we cannot divide by 0.")
            return
            
        p_a_and_b = float(input("Enter P(A ∩ B) - joint probability of A and B occurring: "))
        check_prob(p_a_and_b, "P(A ∩ B)")
        
        if p_a_and_b > p_b:
            print(f"Error: Joint probability P(A ∩ B) ({p_a_and_b}) cannot be greater than P(B) ({p_b}).")
            return
            
        # Calculation
        p_a_given_b = p_a_and_b / p_b
        
        # Display Result
        headers = ["Event Probability", "Expression", "Value"]
        rows = [
            ["Probability of B", "P(B)", f"{p_b:.4f}"],
            ["Joint Probability", "P(A ∩ B)", f"{p_a_and_b:.4f}"],
            ["Conditional Probability", "P(A|B)", f"{p_a_given_b:.4f}"]
        ]
        stats_utils.print_table(headers, rows, title="Conditional Probability Results")
        
        print("\nExplanation:")
        print(f"1. Formula: P(A|B) = P(A ∩ B) / P(B)")
        print(f"2. Calculation: {p_a_and_b:.4f} / {p_b:.4f} = {p_a_given_b:.4f}")
        print(f"3. Meaning: Given that event B has occurred, the probability of event A occurring is {p_a_given_b * 100:.2f}%.")
        
    except ValueError as e:
        print(f"Error: {e}")

def calculate_bayes():
    print("\n--- Bayes' Theorem P(A|B) = [ P(B|A) * P(A) ] / P(B) ---")
    try:
        p_a = float(input("Enter P(A) - prior probability of event A: "))
        check_prob(p_a, "P(A)")
        
        p_b_given_a = float(input("Enter P(B|A) - probability of B given A: "))
        check_prob(p_b_given_a, "P(B|A)")
        
        # Calculate P(B) or ask for it
        choice = input("Do you know the total probability P(B)? (y/n, default is n to calculate via partitions): ").strip().lower()
        
        if choice == 'y' or choice == 'yes':
            p_b = float(input("Enter total probability P(B): "))
            check_prob(p_b, "P(B)")
            if p_b == 0:
                print("Error: P(B) cannot be 0.")
                return
            if p_b_given_a * p_a > p_b:
                print(f"Error: Joint probability P(B|A)*P(A) ({p_b_given_a * p_a}) cannot exceed P(B) ({p_b}).")
                return
        else:
            print("\nTo calculate total P(B), we need P(B|not A) - probability of B given that A did NOT occur:")
            p_b_given_not_a = float(input("Enter P(B|not A): "))
            check_prob(p_b_given_not_a, "P(B|not A)")
            
            # Law of Total Probability
            # P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)
            p_not_a = 1.0 - p_a
            p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
            print(f"Calculated Total Probability P(B) = {p_b:.4f}")
            if p_b == 0:
                print("Error: Total probability P(B) resolved to 0. Cannot divide by 0.")
                return

        # Bayes' calculation
        p_a_given_b = (p_b_given_a * p_a) / p_b

        # Display Results
        headers = ["Probability Term", "Notation", "Value"]
        rows = [
            ["Prior Probability of A", "P(A)", f"{p_a:.4f}"],
            ["Probability of not A", "P(not A)", f"{1.0-p_a:.4f}"],
            ["Likelihood of B given A", "P(B|A)", f"{p_b_given_a:.4f}"],
            ["Total Probability of B", "P(B)", f"{p_b:.4f}"],
            ["Posterior Probability of A given B", "P(A|B)", f"{p_a_given_b:.4f}"]
        ]
        stats_utils.print_table(headers, rows, title="Bayes' Theorem Calculations")

        print("\nStep-by-Step Explanation:")
        print(f"1. Numerator (Joint Prob P(A ∩ B)): P(B|A) * P(A) = {p_b_given_a:.4f} * {p_a:.4f} = {p_b_given_a * p_a:.4f}")
        print(f"2. Denominator (Total Prob P(B)): {p_b:.4f}")
        print(f"3. Posterior Probability P(A|B): {p_b_given_a * p_a:.4f} / {p_b:.4f} = {p_a_given_b:.4f}")
        print(f"4. Meaning: Given that symptom/evidence B occurred, the probability that cause/hypothesis A is true rises to {p_a_given_b * 100:.2f}%.")

    except ValueError as e:
        print(f"Error: {e}")

def run_conditional_probability():
    print("=" * 60)
    print(" QUESTION 8: CONDITIONAL PROBABILITY CALCULATOR ")
    print("=" * 60)
    print("Choose calculation type:")
    print("1. Basic Conditional Probability: P(A|B) = P(A ∩ B) / P(B)")
    print("2. Bayes' Theorem: P(A|B) = [ P(B|A) * P(A) ] / P(B)")
    
    choice = input("\nEnter choice (1 or 2, default is 1): ").strip()
    if choice == "2":
        calculate_bayes()
    else:
        calculate_conditional_basic()

if __name__ == "__main__":
    run_conditional_probability()
