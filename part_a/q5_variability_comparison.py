import sys
import os

# Adjust path to find stats_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import stats_utils

def calculate_cv(data):
    """Calculate the Coefficient of Variation (CV) as a percentage."""
    mean_val = stats_utils.calculate_mean(data)
    if mean_val == 0:
        raise ValueError("Cannot calculate CV for a dataset with a mean of zero.")
    std_val = stats_utils.calculate_std_dev(data)
    return (std_val / mean_val) * 100

def run_variability_comparison():
    print("=" * 60)
    print(" QUESTION 5: DATASET VARIABILITY COMPARATOR ")
    print("=" * 60)
    print("Enter two datasets to compare their variability.")
    
    user_a = input("\nEnter Dataset A (comma or space separated, or press Enter for sample): ").strip()
    if not user_a:
        print("Using sample datasets of different scales:")
        # Dataset A: Test Scores (scale 0-100)
        data_a = [75, 82, 78, 85, 90, 71, 88, 80, 84, 79]
        # Dataset B: Product Weights (scale in grams, e.g., around 10g)
        data_b = [9.5, 10.2, 9.8, 10.5, 11.0, 9.1, 10.8, 10.0, 10.4, 9.9]
        print(f"Dataset A (Test Scores):   {data_a}")
        print(f"Dataset B (Product Weights): {data_b}")
    else:
        user_b = input("Enter Dataset B (same format): ").strip()
        data_a = [float(val) for val in user_a.replace(",", " ").split() if val]
        data_b = [float(val) for val in user_b.replace(",", " ").split() if val]
        
        if not data_a or not data_b:
            print("Error: Both datasets must contain valid numbers. Exiting.")
            return

    # Calculations for A
    mean_a = stats_utils.calculate_mean(data_a)
    range_a = max(data_a) - min(data_a)
    var_a = stats_utils.calculate_variance(data_a)
    std_a = stats_utils.calculate_std_dev(data_a)
    cv_a = calculate_cv(data_a)

    # Calculations for B
    mean_b = stats_utils.calculate_mean(data_b)
    range_b = max(data_b) - min(data_b)
    var_b = stats_utils.calculate_variance(data_b)
    std_b = stats_utils.calculate_std_dev(data_b)
    cv_b = calculate_cv(data_b)

    # Tabular Comparison
    headers = ["Metric", "Dataset A", "Dataset B", "Higher Variability"]
    
    rows = [
        ["Count (N)", len(data_a), len(data_b), "N/A"],
        ["Mean (μ)", f"{mean_a:.4f}", f"{mean_b:.4f}", "N/A"],
        ["Range", f"{range_a:.4f}", f"{range_b:.4f}", "Dataset A" if range_a > range_b else "Dataset B"],
        ["Variance (s²)", f"{var_a:.4f}", f"{var_b:.4f}", "Dataset A" if var_a > var_b else "Dataset B"],
        ["Std Dev (s)", f"{std_a:.4f}", f"{std_b:.4f}", "Dataset A" if std_a > std_b else "Dataset B"],
        ["Coeff of Variation (CV %)", f"{cv_a:.2f}%", f"{cv_b:.2f}%", "Dataset A" if cv_a > cv_b else "Dataset B"]
    ]
    
    stats_utils.print_table(headers, rows, title="Variability Comparison Report")

    # Conclusion logic
    print("\nCONCLUSION:")
    print("-" * 60)
    print(f"1. Absolute Variability (Standard Deviation):")
    if std_a > std_b:
        print(f"   Dataset A has a higher standard deviation ({std_a:.4f} vs {std_b:.4f}).")
    elif std_b > std_a:
        print(f"   Dataset B has a higher standard deviation ({std_b:.4f} vs {std_a:.4f}).")
    else:
        print("   Both datasets have the same standard deviation.")

    print(f"\n2. Relative Variability (Coefficient of Variation - CV):")
    print("   CV adjusts standard deviation by the mean, making it a unitless percentage.")
    print("   This is the mathematically correct metric for comparing variability across different scales.")
    if cv_a > cv_b:
        print(f"   Dataset A exhibits higher relative variability ({cv_a:.2f}% vs {cv_b:.2f}%).")
    elif cv_b > cv_a:
        print(f"   Dataset B exhibits higher relative variability ({cv_b:.2f}% vs {cv_a:.2f}%).")
    else:
        print("   Both datasets have identical relative variability.")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    run_variability_comparison()
