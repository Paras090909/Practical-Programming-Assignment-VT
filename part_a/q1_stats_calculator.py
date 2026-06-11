import sys
import os

# Adjust path to find stats_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import stats_utils

def parse_input(input_str):
    """Parse comma-separated or space-separated numbers from a string."""
    # Clean up input string
    input_str = input_str.replace(",", " ")
    parts = input_str.split()
    data = []
    for p in parts:
        try:
            data.append(float(p))
        except ValueError:
            print(f"Warning: '{p}' is not a valid number. Skipping.")
    return data

def run_stats_calculator():
    print("=" * 60)
    print(" QUESTION 1: DATASET STATISTICS CALCULATOR ")
    print("=" * 60)
    print("Enter a dataset of numbers (separated by commas or spaces).")
    print("Example: 10, 15, 23, 10, 8, 12, 19, 10, 15, 22")
    user_input = input("\nEnter numbers (or press Enter to use default sample): ").strip()
    
    if not user_input:
        print("No input provided. Using default sample dataset: [12, 15, 12, 18, 20, 22, 15, 15, 18, 25]")
        data = [12, 15, 12, 18, 20, 22, 15, 15, 18, 25]
    else:
        data = parse_input(user_input)
        if not data:
            print("Error: No valid numbers entered. Exiting.")
            return

    # Calculations
    try:
        mean_val = stats_utils.calculate_mean(data)
        median_val = stats_utils.calculate_median(data)
        modes, count = stats_utils.calculate_mode(data)
        var_val = stats_utils.calculate_variance(data, is_sample=True)
        std_val = stats_utils.calculate_std_dev(data, is_sample=True)
    except Exception as e:
        print(f"Calculation Error: {e}")
        return

    # Formatting Mode Output
    if not modes:
        mode_str = "No Mode (all values unique)"
    else:
        mode_str = ", ".join(map(str, modes)) + f" (Freq: {count})"

    # Create Tabular Report
    headers = ["Statistic Metric", "Value"]
    rows = [
        ["Count (N)", len(data)],
        ["Mean", f"{mean_val:.4f}"],
        ["Median", f"{median_val:.4f}"],
        ["Mode(s)", mode_str],
        ["Sample Variance", f"{var_val:.4f}"],
        ["Standard Deviation", f"{std_val:.4f}"],
        ["Minimum", f"{min(data):.4f}"],
        ["Maximum", f"{max(data):.4f}"],
    ]
    
    stats_utils.print_table(headers, rows, title="Descriptive Statistics Report")
    print(f"\nAnalyzed Dataset: {data}\n")

if __name__ == "__main__":
    run_stats_calculator()
