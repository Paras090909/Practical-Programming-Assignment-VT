import os
import sys
import subprocess

# Define mapping from key to file path and description
QUESTIONS = {
    # Part A
    "1": ("part_a/q1_stats_calculator.py", "Statistics Calculator (Mean, Median, Mode, Var, SD)"),
    "2": ("part_a/q2_zscore_outliers.py", "Z-Score Outlier Detector"),
    "3": ("part_a/q3_random_analysis.py", "Random Dataset Statistical Analysis"),
    "4": ("part_a/q4_pearson_correlation.py", "Pearson Correlation Coefficient"),
    "5": ("part_a/q5_variability_comparison.py", "Dataset Variability Comparator"),
    
    # Part B
    "6": ("part_b/q6_dice_roll_simulation.py", "Dice Roll Simulator (10k rolls) + Bar Chart"),
    "7": ("part_b/q7_coin_toss_simulation.py", "Coin Toss Simulator (10k flips) + Convergence Chart"),
    "8": ("part_b/q8_conditional_probability.py", "Conditional Probability & Bayes Calculator"),
    "9": ("part_b/q9_card_probability.py", "Card Draw Simulator (10k draws)"),
    "10": ("part_b/q10_lottery_simulation.py", "Lottery Simulation & Win Estimator"),
    
    # Part C
    "11": ("part_c/q11_matrix_ops_scratch.py", "Matrix Add/Sub/Mul from scratch"),
    "12": ("part_c/q12_matrix_transpose.py", "Matrix Transpose & Verification"),
    "13": ("part_c/q13_matrix_determinant.py", "Determinant of 2x2 & 3x3 Matrices"),
    "14": ("part_c/q14_matrix_inverse.py", "Matrix Inverse via NumPy & Verification"),
    "15": ("part_c/q15_linear_equations.py", "System of Linear Equations Solver (Gaussian)"),
    
    # Part D
    "16": ("part_d/q16_random_plots.py", "Random Dataset Viz (Hist, Box, Freq Dist)"),
    "17": ("part_d/q17_scatter_correlation.py", "Scatter Plot & Trendline Correlation"),
    "18": ("part_d/q18_normal_distribution.py", "Normal Distribution PDF Curve & SD Shading"),
    "19": ("part_d/q19_dashboard.py", "Mini Data Analysis Dashboard (HTML + Plot)"),
    "20": ("part_d/q20_student_eda.py", "Student Performance EDA (Descriptive & Correlation)")
}

# Map alias keys like A1, B6, etc.
ALIAS_MAP = {}
for k in range(1, 21):
    path, desc = QUESTIONS[str(k)]
    part = "A" if k <= 5 else "B" if k <= 10 else "C" if k <= 15 else "D"
    q_num = k if k <= 5 else k - 5 if k <= 10 else k - 10 if k <= 15 else k - 15
    ALIAS_MAP[f"{part}{q_num}"] = str(k)
    ALIAS_MAP[f"{part.lower()}{q_num}"] = str(k)

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 75)
    print("      STATISTICS, PROBABILITY, LINEAR ALGEBRA & VISUALIZATION SUITE      ")
    print("=" * 75)
    
    print("\n PART A: STATISTICS & DATA ANALYSIS")
    print("  [1] Q1. Dataset Statistics Calculator (Mean, Median, Mode, Var, SD)")
    print("  [2] Q2. Z-Score Outlier Detector")
    print("  [3] Q3. Random Dataset Statistical Analysis (N >= 100)")
    print("  [4] Q4. Pearson Correlation Coefficient & Interpretation")
    print("  [5] Q5. Dataset Variability Comparator (SD vs CV)")
    
    print("\n PART B: PROBABILITY & SIMULATION")
    print("  [6] Q6. Dice Roll Simulator (10,000 rolls with Bar Chart)")
    print("  [7] Q7. Coin Toss Simulator (10,000 flips with Convergence Line)")
    print("  [8] Q8. Conditional Probability & Bayes' Theorem Calculator")
    print("  [9] Q9. Card Selection Draw Probability (Ace, King, Queen, Face, Red)")
    print("  [10] Q10. Lottery Simulation Jackpot & Match Probability Estimator")

    print("\n PART C: LINEAR ALGEBRA")
    print("  [11] Q11. Custom Matrix Operations (Addition, Subtraction, Multiplication)")
    print("  [12] Q12. Custom Matrix Transpose and Axiom Verifications")
    print("  [13] Q13. Custom Determinant Calculator (2x2 & 3x3 Matrices)")
    print("  [14] Q14. NumPy Matrix Inverse Calculator & Identity Matrix Verification")
    print("  [15] Q15. Linear System Solver (Step-by-Step Gaussian Elimination)")

    print("\n PART D: DATA VISUALIZATION")
    print("  [16] Q16. Random Dataset Viz (Histogram + KDE, Box Plot, Freq Table)")
    print("  [17] Q17. Scatter Plot with Trendline & Correlation strength")
    print("  [18] Q18. Normal Distribution Curve and Standard Deviation Zones Shaded")
    print("  [19] Q19. Mini Data Analysis Dashboard (HTML Report + 2x2 Plots)")
    print("  [20] Q20. Student Performance EDA (Grades, Trends, Study Hours Correlation)")
    
    print("\n [0] Exit Program")
    print("=" * 75)

def main():
    while True:
        print_menu()
        choice = input("\nEnter Question Number (1-20), Section Key (e.g. A1, B6, C11, D16) or 0 to exit: ").strip()
        
        if choice == "0":
            print("\nExiting program. Goodbye!\n")
            break
            
        # Resolve alias mapping
        resolved_choice = choice
        if choice in ALIAS_MAP:
            resolved_choice = ALIAS_MAP[choice]
            
        if resolved_choice not in QUESTIONS:
            input("\nInvalid choice. Press Enter to try again...")
            continue
            
        script_path, description = QUESTIONS[resolved_choice]
        script_full_path = os.path.abspath(script_path)
        
        print("\n" + "=" * 70)
        print(f" RUNNING: {description.upper()}")
        print(f" FILE: {script_path}")
        print("=" * 70 + "\n")
        
        try:
            # Run using the same python executable to ensure environment carries over
            subprocess.run([sys.executable, script_full_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"\nExecution failed with error: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            
        input("\nExecution completed. Press Enter to return to menu...")

if __name__ == "__main__":
    main()
