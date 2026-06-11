import random
import os
import matplotlib.pyplot as plt

def run_coin_simulation():
    print("=" * 60)
    print(" QUESTION 7: COIN TOSS SIMULATION (10,000 TOSSES) ")
    print("=" * 60)

    num_tosses = 10000
    print(f"Simulating {num_tosses:,} coin tosses...")

    heads_count = 0
    tails_count = 0
    
    # We will record the experimental probability of heads at regular intervals for plotting
    trials = []
    exp_heads_probs = []
    
    for i in range(1, num_tosses + 1):
        outcome = random.choice(['Heads', 'Tails'])
        if outcome == 'Heads':
            heads_count += 1
        else:
            tails_count += 1
            
        # Record at step 1, 10, and then every 20 steps to avoid excessive data points
        if i == 1 or i == 10 or i % 20 == 0:
            trials.append(i)
            exp_heads_probs.append(heads_count / i)

    # Final probabilities
    exp_heads = heads_count / num_tosses
    exp_tails = tails_count / num_tosses
    theo_prob = 0.5

    # Create directory and save convergence plot
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q7_coin_toss_convergence.png"))

    plt.figure(figsize=(10, 5))
    plt.plot(trials, exp_heads_probs, color='#2196F3', linewidth=1.5, label='Experimental Probability')
    plt.axhline(y=theo_prob, color='#F44336', linestyle='--', linewidth=2, label='Theoretical Probability (0.5)')
    
    plt.title('Convergence of Coin Toss Probability (Law of Large Numbers)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Number of Tosses (Trials)', fontsize=11)
    plt.ylabel('Probability of Heads', fontsize=11)
    plt.ylim(0.35, 0.65) # Zoom in to see convergence details clearly
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    # Tabular report
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
    import stats_utils

    headers = ["Outcome", "Count", "Experimental Prob", "Theoretical Prob", "Absolute Error"]
    rows = [
        ["Heads", f"{heads_count:,}", f"{exp_heads:.4f}", f"{theo_prob:.4f}", f"{abs(exp_heads - theo_prob):.4f}"],
        ["Tails", f"{tails_count:,}", f"{exp_tails:.4f}", f"{theo_prob:.4f}", f"{abs(exp_tails - theo_prob):.4f}"]
    ]
    
    stats_utils.print_table(headers, rows, title="Coin Toss Simulation Results")
    print(f"\nConvergence graph successfully generated and saved to:")
    print(f"-> [q7_coin_toss_convergence.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_coin_simulation()
