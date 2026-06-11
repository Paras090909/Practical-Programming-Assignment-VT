import random
import os
import matplotlib.pyplot as plt

def get_theoretical_probabilities():
    """Calculate the theoretical probability for each sum 2-12 of rolling two 6-sided dice."""
    outcomes = {}
    total_outcomes = 36
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            s = d1 + d2
            outcomes[s] = outcomes.get(s, 0) + 1
    return {s: count / total_outcomes for s, count in outcomes.items()}

def run_dice_simulation():
    print("=" * 60)
    print(" QUESTION 6: DICE ROLL SIMULATION (10,000 ROLLS) ")
    print("=" * 60)

    num_rolls = 10000
    print(f"Simulating {num_rolls:,} rolls of two dice...")

    # Simulation
    sums_frequency = {s: 0 for s in range(2, 13)}
    for _ in range(num_rolls):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        sums_frequency[d1 + d2] += 1

    experimental_probs = {s: count / num_rolls for s, count in sums_frequency.items()}
    theoretical_probs = get_theoretical_probabilities()

    # Create folder for plots if it doesn't exist
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q6_dice_roll.png"))

    # Matplotlib plotting
    sums = list(range(2, 13))
    exp_values = [experimental_probs[s] for s in sums]
    theo_values = [theoretical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    x = [s - 0.2 for s in sums]
    y = [s + 0.2 for s in sums]
    
    plt.bar(x, exp_values, width=0.4, label='Experimental (Simulated)', color='#3F51B5', alpha=0.85)
    plt.bar(y, theo_values, width=0.4, label='Theoretical (Calculated)', color='#FF5722', alpha=0.85)
    
    plt.title(f'Probability Distribution of Dice Roll Sums ({num_rolls:,} Rolls)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sum of Two Dice', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.legend(fontsize=11)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    # Terminal ASCII Tabular Report
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
    import stats_utils # reuse print_table helper if possible

    headers = ["Sum", "Frequency", "Experimental P(S)", "Theoretical P(S)", "Abs Diff %"]
    rows = []
    for s in sums:
        f = sums_frequency[s]
        ep = experimental_probs[s]
        tp = theoretical_probs[s]
        diff_pct = abs(ep - tp) * 100
        rows.append([s, f"{f:,}", f"{ep:.4f}", f"{tp:.4f}", f"{diff_pct:.2f}%"])

    stats_utils.print_table(headers, rows, title="Dice Roll Simulation Comparison Table")
    print(f"\nBar chart successfully generated and saved to:")
    print(f"-> [q6_dice_roll.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_dice_simulation()
