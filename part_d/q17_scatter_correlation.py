import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

def run_scatter_correlation():
    print("=" * 60)
    print(" QUESTION 17: SCATTER PLOT & CORRELATION ")
    print("=" * 60)

    # Generate correlated data
    np.random.seed(42)
    n_samples = 150
    # X: Study Hours (range 2 to 25 hours per week)
    x = np.random.uniform(2, 25, n_samples)
    # Y: Exam Score (linear relation with study hours + normal noise)
    noise = np.random.normal(0, 6, n_samples)
    y = 40 + 2.2 * x + noise
    # Clip exam scores to maximum of 100
    y = np.clip(y, 0, 100)

    print(f"Generated {n_samples} samples representing Study Hours (X) vs. Exam Score (Y).")

    # Calculate Pearson's r
    r = stats_utils.calculate_pearson_correlation(x.tolist(), y.tolist())
    r_squared = r ** 2

    # Fit linear regression line (y = mx + c)
    m, c = np.polyfit(x, y, 1)

    # Plotting
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q17_scatter_correlation.png"))

    sns.set_theme(style="ticks")
    plt.figure(figsize=(10, 6))
    
    # Draw scatter points
    plt.scatter(x, y, color="#E91E63", edgecolors="black", alpha=0.75, s=60, label="Student Records")
    
    # Draw trendline
    x_line = np.linspace(min(x), max(x), 100)
    y_line = m * x_line + c
    plt.plot(x_line, y_line, color="#2196F3", linestyle="-", linewidth=2.5, 
             label=f"Regression Line (y = {m:.2f}x + {c:.2f})")

    plt.title("Relationship Between Study Hours and Exam Scores", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Study Hours per Week", fontsize=12)
    plt.ylabel("Exam Score (out of 100)", fontsize=12)
    plt.grid(True, linestyle=":", alpha=0.6)
    
    # Add stats text box
    stats_text = f"Correlation (r): {r:.4f}\nR² (Coeff of Det): {r_squared:.4f}"
    plt.gca().text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=11,
                  verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#E0E0E0'))
    
    plt.legend(loc="lower right", fontsize=11)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    # Interpretation
    print("\nRELATIONSHIP INTERPRETATION:")
    print("-" * 60)
    print(f"Pearson Correlation Coefficient (r) = {r:.4f}")
    print(f"Coefficient of Determination (R²)   = {r_squared:.4f}")
    
    print("\nDirection:")
    if r > 0:
        print("  - The relationship is POSITIVE. As study hours increase, exam scores tend to increase.")
    elif r < 0:
        print("  - The relationship is NEGATIVE. As study hours increase, exam scores tend to decrease.")
    else:
        print("  - The relationship is NEUTRAL (No linear relationship).")

    print("\nStrength:")
    abs_r = abs(r)
    if abs_r > 0.7:
        print(f"  - The strength is VERY STRONG. (r = {r:.4f})")
    elif abs_r > 0.5:
        print(f"  - The strength is MODERATE. (r = {r:.4f})")
    else:
        print(f"  - The strength is WEAK. (r = {r:.4f})")

    print("\nInsight:")
    print(f"  - A slope of {m:.2f} implies that for every additional hour studied per week,")
    print(f"    a student's score increases by approximately {m:.2f} points on average.")
    print(f"  - The R² value of {r_squared:.2f} means that {r_squared*100:.1f}% of the variance in exam scores")
    print("    can be explained by the number of study hours.")
    print("-" * 60)
    print(f"\nScatter plot successfully generated and saved to:")
    print(f"-> [q17_scatter_correlation.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_scatter_correlation()
