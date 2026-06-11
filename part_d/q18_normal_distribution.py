import numpy as np
import os
import matplotlib.pyplot as plt

def run_normal_distribution():
    print("=" * 60)
    print(" QUESTION 18: NORMAL DISTRIBUTION VISUALIZATION ")
    print("=" * 60)

    # Let's model IQ scores (Mean = 100, Standard Deviation = 15)
    mu = 100
    sigma = 15
    np.random.seed(100)
    sample_size = 2000
    data = np.random.normal(mu, sigma, sample_size)

    sample_mean = np.mean(data)
    sample_std = np.std(data)

    print(f"Parameters: Theoretical Mean = {mu}, SD = {sigma}")
    print(f"Sample Stats (N={sample_size}): Mean = {sample_mean:.2f}, SD = {sample_std:.2f}")

    # Plotting
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q18_normal_distribution.png"))

    plt.figure(figsize=(12, 7))
    
    # 1. Plot histogram of simulated data (normalized density)
    count, bins, ignored = plt.hist(data, bins=40, density=True, alpha=0.35, color='#78909C', label='Sample Data Density')

    # 2. Plot smooth theoretical PDF curve
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    plt.plot(x, pdf, color='#1565C0', linewidth=2.5, label='Theoretical PDF (Bell Curve)')

    # 3. Shade standard deviation zones (68-95-99.7 Rule)
    # Zone 1: ±1 SD (68.27% of data)
    plt.fill_between(x, pdf, where=(x >= mu - sigma) & (x <= mu + sigma), 
                     color='#2196F3', alpha=0.25, label='±1 Std Dev (~68.3%)')
    
    # Zone 2: ±2 SD (95.45% of data)
    plt.fill_between(x, pdf, where=((x >= mu - 2*sigma) & (x < mu - sigma)) | ((x > mu + sigma) & (x <= mu + 2*sigma)), 
                     color='#4CAF50', alpha=0.15, label='±2 Std Dev (~95.4%)')
    
    # Zone 3: ±3 SD (99.73% of data)
    plt.fill_between(x, pdf, where=((x >= mu - 3*sigma) & (x < mu - 2*sigma)) | ((x > mu + 2*sigma) & (x <= mu + 3*sigma)), 
                     color='#FF9800', alpha=0.10, label='±3 Std Dev (~99.7%)')

    # Add vertical lines for mean and standard deviations
    plt.axvline(mu, color='#B71C1C', linestyle='-', linewidth=2, label=f'Mean (μ) = {mu}')
    plt.axvline(mu - sigma, color='#1565C0', linestyle=':', linewidth=1.5)
    plt.axvline(mu + sigma, color='#1565C0', linestyle=':', linewidth=1.5)
    plt.axvline(mu - 2*sigma, color='#2E7D32', linestyle=':', linewidth=1.5)
    plt.axvline(mu + 2*sigma, color='#2E7D32', linestyle=':', linewidth=1.5)
    plt.axvline(mu - 3*sigma, color='#EF6C00', linestyle=':', linewidth=1.5)
    plt.axvline(mu + 3*sigma, color='#EF6C00', linestyle=':', linewidth=1.5)

    # Annotate labels for clarity
    plt.text(mu, max(pdf)*0.8, 'μ', color='#B71C1C', fontsize=14, horizontalalignment='center', weight='bold')
    plt.text(mu + sigma, max(pdf)*0.4, '+1σ', color='#1565C0', fontsize=12, horizontalalignment='center')
    plt.text(mu - sigma, max(pdf)*0.4, '-1σ', color='#1565C0', fontsize=12, horizontalalignment='center')
    plt.text(mu + 2*sigma, max(pdf)*0.15, '+2σ', color='#2E7D32', fontsize=12, horizontalalignment='center')
    plt.text(mu - 2*sigma, max(pdf)*0.15, '-2σ', color='#2E7D32', fontsize=12, horizontalalignment='center')

    plt.title('Normal Distribution of IQ Scores (μ=100, σ=15) with Empirical Rule Shading', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('IQ Score Value', fontsize=12)
    plt.ylabel('Probability Density', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    print("\nTHE EMPIRICAL RULE (68-95-99.7 RULE):")
    print("-" * 60)
    print(f"For a perfectly normal distribution:")
    print(f"1. Approx. 68.27% of all values lie within ±1 SD from the mean (between {mu-sigma} and {mu+sigma})")
    print(f"2. Approx. 95.45% of all values lie within ±2 SD from the mean (between {mu-2*sigma} and {mu+2*sigma})")
    print(f"3. Approx. 99.73% of all values lie within ±3 SD from the mean (between {mu-3*sigma} and {mu+3*sigma})")
    
    # Check sample data matches the empirical rule
    in_1sd = sum((x >= sample_mean - sample_std) and (x <= sample_mean + sample_std) for x in data) / sample_size
    in_2sd = sum((x >= sample_mean - 2*sample_std) and (x <= sample_mean + 2*sample_std) for x in data) / sample_size
    in_3sd = sum((x >= sample_mean - 3*sample_std) and (x <= sample_mean + 3*sample_std) for x in data) / sample_size
    
    print(f"\nObserved Sample Percentages (N={sample_size}):")
    print(f"  - Within ±1 Standard Deviation: {in_1sd*100:.2f}% (Theoretical: 68.27%)")
    print(f"  - Within ±2 Standard Deviations: {in_2sd*100:.2f}% (Theoretical: 95.45%)")
    print(f"  - Within ±3 Standard Deviations: {in_3sd*100:.2f}% (Theoretical: 99.73%)")
    print("-" * 60)
    print(f"\nBell curve graph successfully generated and saved to:")
    print(f"-> [q18_normal_distribution.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_normal_distribution()
