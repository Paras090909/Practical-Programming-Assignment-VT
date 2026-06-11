import sys
import os
import random

# Adjust path to find stats_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import stats_utils

def calculate_quartiles(data):
    """Calculate the first quartile (Q1), second quartile (Q2/median), and third quartile (Q3)."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # Using method similar to standard quartile calculation (hinges)
    def get_median_segment(lst):
        m = len(lst)
        mid = m // 2
        if m % 2 == 1:
            return lst[mid]
        else:
            return (lst[mid - 1] + lst[mid]) / 2

    q2 = get_median_segment(sorted_data)
    
    # Split the dataset
    if n % 2 == 0:
        lower_half = sorted_data[:n//2]
        upper_half = sorted_data[n//2:]
    else:
        # Include median or exclude? Standard standard is to exclude median
        lower_half = sorted_data[:n//2]
        upper_half = sorted_data[n//2 + 1:]
        
    q1 = get_median_segment(lower_half)
    q3 = get_median_segment(upper_half)
    
    return q1, q2, q3

def run_random_analysis():
    print("=" * 60)
    print(" QUESTION 3: RANDOM DATASET STATISTICAL ANALYSIS ")
    print("=" * 60)
    
    size_input = input("Enter number of random values to generate (minimum 100, default is 150): ").strip()
    try:
        size = int(size_input) if size_input else 150
        if size < 100:
            print("Size must be at least 100. Using 100.")
            size = 100
    except ValueError:
        print("Invalid size. Using default 150.")
        size = 150

    print("\nChoose distribution for the random data:")
    print("1. Normal Distribution (Mean = 50, SD = 15)")
    print("2. Uniform Distribution (Min = 10, Max = 90)")
    dist_choice = input("Enter choice (1 or 2, default is 1): ").strip()
    
    if dist_choice == "2":
        data = [random.uniform(10, 90) for _ in range(size)]
        dist_name = f"Uniform Distribution [10, 90]"
    else:
        data = [random.normalvariate(50, 15) for _ in range(size)]
        dist_name = "Normal Distribution (mu=50, sigma=15)"

    # Calculations
    mean_val = stats_utils.calculate_mean(data)
    median_val = stats_utils.calculate_median(data)
    modes, count = stats_utils.calculate_mode([round(x, 1) for x in data]) # Rounding to find meaningful modes in floats
    var_val = stats_utils.calculate_variance(data)
    std_val = stats_utils.calculate_std_dev(data)
    
    min_val = min(data)
    max_val = max(data)
    val_range = max_val - min_val
    
    q1, q2, q3 = calculate_quartiles(data)
    iqr = q3 - q1

    # Format Mode Output
    if not modes:
        mode_str = "No duplicate rounded values"
    else:
        # Show first 3 modes if many exist
        mode_sample = ", ".join(map(str, modes[:3]))
        if len(modes) > 3:
            mode_sample += f" ... (+{len(modes)-3} more)"
        mode_str = f"{mode_sample} (Freq: {count} on 1-decimal rounding)"

    headers = ["Measure Type", "Statistical Metric", "Value"]
    rows = [
        ["Dataset Info", "Sample Size (N)", size],
        ["Dataset Info", "Source Distribution", dist_name],
        ["Central Tendency", "Mean", f"{mean_val:.4f}"],
        ["Central Tendency", "Median (Q2)", f"{median_val:.4f}"],
        ["Central Tendency", "Mode (rounded to 1 decimal)", mode_str],
        ["Dispersion", "Minimum", f"{min_val:.4f}"],
        ["Dispersion", "Maximum", f"{max_val:.4f}"],
        ["Dispersion", "Range", f"{val_range:.4f}"],
        ["Dispersion", "Sample Variance", f"{var_val:.4f}"],
        ["Dispersion", "Standard Deviation", f"{std_val:.4f}"],
        ["Dispersion", "First Quartile (Q1)", f"{q1:.4f}"],
        ["Dispersion", "Third Quartile (Q3)", f"{q3:.4f}"],
        ["Dispersion", "Interquartile Range (IQR)", f"{iqr:.4f}"],
    ]

    stats_utils.print_table(headers, rows, title=f"Statistical Analysis of Generated Dataset")
    
    # Print sample values
    print("\nFirst 10 values in dataset:")
    print([round(x, 4) for x in data[:10]])
    print("=" * 60)

if __name__ == "__main__":
    run_random_analysis()
