import sys
import os

# Adjust path to find stats_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import stats_utils

def interpret_correlation(r):
    """Interpret the strength and direction of Pearson correlation coefficient."""
    abs_r = abs(r)
    
    if abs_r < 0.1:
        strength = "Negligible / No correlation"
    elif abs_r < 0.3:
        strength = "Weak correlation"
    elif abs_r < 0.5:
        strength = "Moderate correlation"
    elif abs_r < 0.7:
        strength = "Strong correlation"
    else:
        strength = "Very strong correlation"
        
    if r > 0.05:
        direction = "Positive"
        interpretation = f"As Variable X increases, Variable Y tends to increase. ({strength})"
    elif r < -0.05:
        direction = "Negative"
        interpretation = f"As Variable X increases, Variable Y tends to decrease. ({strength})"
    else:
        direction = "None"
        interpretation = "There is no apparent linear relationship between Variable X and Variable Y."
        
    return direction, strength, interpretation

def run_correlation_calculator():
    print("=" * 60)
    print(" QUESTION 4: PEARSON CORRELATION CALCULATOR ")
    print("=" * 60)
    print("Enter two equal-sized datasets (comma or space separated).")
    
    user_x = input("\nEnter Variable X values (or press Enter for sample): ").strip()
    if not user_x:
        print("Using sample dataset (e.g., Study Hours vs. Exam Scores):")
        # Strong positive correlation
        x_data = [2.0, 3.5, 5.0, 8.0, 9.0, 1.5, 4.0, 6.0, 7.5, 10.0]
        y_data = [45,  52,  61,  80,  85,  40,  55,  68,  78,  95]
        print(f"X (Study Hours): {x_data}")
        print(f"Y (Exam Score):  {y_data}")
    else:
        user_y = input("Enter Variable Y values (same length as X): ").strip()
        
        # Parse inputs
        x_data = [float(val) for val in user_x.replace(",", " ").split() if val]
        y_data = [float(val) for val in user_y.replace(",", " ").split() if val]
        
        if len(x_data) != len(y_data):
            print(f"Error: Datasets must be of equal size (X has {len(x_data)} items, Y has {len(y_data)} items).")
            return
        if not x_data:
            print("Error: Datasets are empty. Exiting.")
            return

    # Calculations
    try:
        r = stats_utils.calculate_pearson_correlation(x_data, y_data)
        direction, strength, desc = interpret_correlation(r)
    except Exception as e:
        print(f"Error calculating correlation: {e}")
        return

    # Table formatting
    headers = ["Metric", "Value", "Meaning / Interpretation"]
    rows = [
        ["Pearson's r", f"{r:.6f}", f"Range is [-1, 1]"],
        ["Relationship Direction", direction, f"Sign of r shows the direction"],
        ["Relationship Strength", strength, f"Magnitude of r shows the strength"],
    ]
    
    stats_utils.print_table(headers, rows, title="Correlation Analysis Results")
    
    print("\nDetailed Explanation:")
    print(f"- {desc}")
    print(f"- Coefficient of Determination (r²): {r**2:.4f}")
    print(f"  (This means {r**2*100:.1f}% of the variance in Y is predictable from X.)\n")

if __name__ == "__main__":
    run_correlation_calculator()
