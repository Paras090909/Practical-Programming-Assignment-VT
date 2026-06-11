import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

def run_random_visualization():
    print("=" * 60)
    print(" QUESTION 16: RANDOM DATASET VISUALIZATION ")
    print("=" * 60)
    
    # Generate a right-skewed dataset (log-normal distribution)
    # This represents realistic skewed data like household incomes or call center durations
    np.random.seed(42) # Set seed for reproducibility
    data = np.random.lognormal(mean=2.5, sigma=0.6, size=500)
    
    print(f"Generated a right-skewed (log-normal) dataset of {len(data)} points.")
    
    # Calculate Summary Statistics
    mean_val = np.mean(data)
    median_val = np.median(data)
    std_val = np.std(data)
    min_val = np.min(data)
    max_val = np.max(data)
    
    # Calculate Frequency Distribution
    # Divide range into 10 bins
    counts, bin_edges = np.histogram(data, bins=10)
    
    # Print Frequency Distribution
    headers = ["Bin Interval", "Frequency", "Percentage", "Cumulative %"]
    rows = []
    cumulative_count = 0
    total = len(data)
    
    for i in range(len(counts)):
        bin_start = bin_edges[i]
        bin_end = bin_edges[i+1]
        freq = counts[i]
        cumulative_count += freq
        pct = (freq / total) * 100
        cum_pct = (cumulative_count / total) * 100
        bin_label = f"[{bin_start:.2f} - {bin_end:.2f})"
        rows.append([bin_label, f"{freq}", f"{pct:.1f}%", f"{cum_pct:.1f}%"])
        
    stats_utils.print_table(headers, rows, title="Frequency Distribution Table")

    # Create visualization
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q16_random_distribution.png"))

    # Matplotlib + Seaborn Style
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # 1. Histogram + KDE
    sns.histplot(data, bins=25, kde=True, ax=axes[0], color="#009688", edgecolor="white")
    axes[0].axvline(mean_val, color="#E91E63", linestyle="--", linewidth=2, label=f"Mean: {mean_val:.2f}")
    axes[0].axvline(median_val, color="#3F51B5", linestyle="-.", linewidth=2, label=f"Median: {median_val:.2f}")
    axes[0].set_title("Histogram & Kernel Density Estimate (KDE)", fontsize=13, fontweight='bold')
    axes[0].set_xlabel("Value")
    axes[0].set_ylabel("Count / Density")
    axes[0].legend(fontsize=10)

    # 2. Box Plot
    sns.boxplot(y=data, ax=axes[1], color="#FFEB3B", width=0.4)
    axes[1].set_title("Box Plot (Showing IQR & Outliers)", fontsize=13, fontweight='bold')
    axes[1].set_ylabel("Value")

    plt.suptitle("Statistical Analysis and Visualization of Skewed Data", fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    # Printed Observations
    print("\nVISUAL OBSERVATIONS & INSIGHTS:")
    print("-" * 60)
    print("1. Shape of Distribution (Histogram & KDE):")
    print("   - The distribution exhibits a strong positive (right) skew.")
    print("   - A long tail extends to the right, showing a concentration of lower values and rare high values.")
    print(f"   - Asymmetry is confirmed by the relation: Mean ({mean_val:.2f}) > Median ({median_val:.2f}).")
    
    print("\n2. Outliers and Dispersion (Box Plot):")
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    upper_fence = q75 + (1.5 * iqr)
    num_outliers = sum(x > upper_fence for x in data)
    print(f"   - The IQR box is compact, located between {q25:.2f} (Q1) and {q75:.2f} (Q3).")
    print(f"   - The upper whisker ends around {upper_fence:.2f}. Points beyond this are outliers.")
    print(f"   - We detected {num_outliers} outliers in the upper range, representing high-value extremes.")
    
    print("\n3. Frequency Distribution Summary:")
    print(f"   - Over {rows[0][2]} ({rows[0][1]} points) of the data falls in the very first bin ({rows[0][0]}).")
    print(f"   - {rows[2][3]} of the entire dataset lies below value {bin_edges[3]:.2f}, proving strong density concentration.")
    print("-" * 60)
    print(f"\nCharts successfully generated and saved to:")
    print(f"-> [q16_random_distribution.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_random_visualization()
