import sys
import os

# Adjust path to find stats_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import stats_utils

def run_outlier_detector():
    print("=" * 60)
    print(" QUESTION 2: Z-SCORE OUTLIER DETECTOR ")
    print("=" * 60)
    print("Enter a dataset (separated by commas or spaces).")
    print("Example: 10, 12, 11, 10, 12, 95, 11, 12, 13, -45")
    user_input = input("\nEnter numbers (or press Enter to use default sample): ").strip()
    
    if not user_input:
        print("No input provided. Using default sample with outliers: [10, 12, 11, 9, 13, 110, 10, 12, 11, 9, -50, 12]")
        data = [10, 12, 11, 9, 13, 110, 10, 12, 11, 9, -50, 12]
    else:
        # Clean up input string
        cleaned_str = user_input.replace(",", " ")
        data = []
        for p in cleaned_str.split():
            try:
                data.append(float(p))
            except ValueError:
                pass
                
        if not data:
            print("Error: No valid numbers entered. Exiting.")
            return

    threshold_input = input("Enter Z-Score threshold for outliers (default is 2.0 for small samples, or 3.0 for standard): ").strip()
    try:
        threshold = float(threshold_input) if threshold_input else 2.0
    except ValueError:
        print("Invalid threshold. Using default 2.0.")
        threshold = 2.0

    try:
        mean_val = stats_utils.calculate_mean(data)
        std_val = stats_utils.calculate_std_dev(data, is_sample=True)
        z_scores = stats_utils.calculate_z_scores(data)
    except Exception as e:
        print(f"Error during calculations: {e}")
        return

    # Identify outliers
    outliers = []
    for i, (val, z) in enumerate(zip(data, z_scores)):
        if abs(z) > threshold:
            outliers.append((i, val, z))

    print(f"\nDataset size: {len(data)}")
    print(f"Mean: {mean_val:.4f} | Standard Deviation: {std_val:.4f}")
    print(f"Outlier Threshold: |Z-Score| > {threshold}")

    if not outliers:
        print("\nNo outliers detected in the dataset with the current threshold.")
    else:
        headers = ["Index", "Value", "Z-Score", "Deviation Direction"]
        rows = []
        for idx, val, z in outliers:
            direction = "Above Mean (High)" if z > 0 else "Below Mean (Low)"
            rows.append([idx, f"{val:.4f}", f"{z:.4f}", direction])
            
        stats_utils.print_table(headers, rows, title=f"Detected Outliers (|Z| > {threshold})")

    # Show all values with their Z-Scores for context
    show_all = input("Would you like to see the Z-Scores for all data points? (y/n): ").strip().lower()
    if show_all == 'y' or show_all == 'yes':
        all_headers = ["Index", "Value", "Z-Score", "Is Outlier?"]
        all_rows = []
        for i, (val, z) in enumerate(zip(data, z_scores)):
            is_out = "YES" if abs(z) > threshold else "NO"
            all_rows.append([i, f"{val:.4f}", f"{z:.4f}", is_out])
        stats_utils.print_table(all_headers, all_rows, title="Complete Dataset Z-Scores")

if __name__ == "__main__":
    run_outlier_detector()
