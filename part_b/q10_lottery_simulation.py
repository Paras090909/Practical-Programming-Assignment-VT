import random
import sys
import os
import math

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

def combination(n, k):
    """Calculate combination (n choose k)."""
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def get_theoretical_lottery_probs():
    """Calculate the theoretical probability of matching k numbers in a 6/49 lottery."""
    probs = {}
    total_combinations = combination(49, 6) # 13,983,816
    for k in range(7):
        # Ways to choose k winning numbers from the 6 winning numbers: comb(6, k)
        # Ways to choose remaining (6-k) numbers from the 43 non-winning numbers: comb(43, 6-k)
        ways = combination(6, k) * combination(43, 6 - k)
        probs[k] = ways / total_combinations
    return probs

def run_lottery_simulation():
    print("=" * 60)
    print(" QUESTION 10: LOTTERY SIMULATION SYSTEM ")
    print("=" * 60)
    
    # We will simulate a standard 6/49 lottery
    # Choose 6 distinct numbers from 1 to 49
    print("Rules: Match 6 numbers from a pool of 1 to 49.")
    print("Theoretical Jackpot Odds: 1 in 13,983,816 (approx 0.00000715%)")
    
    trials_input = input("\nEnter number of simulation trials (default 100,000, max 500,000): ").strip()
    try:
        num_trials = int(trials_input) if trials_input else 100000
        if num_trials < 1:
            num_trials = 100000
        elif num_trials > 500000:
            print("Limiting to 500,000 trials for performance.")
            num_trials = 500000
    except ValueError:
        print("Invalid input. Using default 100,000 trials.")
        num_trials = 100000

    # User's ticket (or a random player ticket)
    player_numbers = set(sorted(random.sample(range(1, 50), 6)))
    print(f"\nYour Ticket Numbers: {sorted(list(player_numbers))}")
    print(f"Running simulation of {num_trials:,} draws...")

    # Frequency tracker for matches
    match_counts = {k: 0 for k in range(7)}

    # Optimization: pre-generate winning numbers is not needed, set intersection is very fast in python
    for _ in range(num_trials):
        # Draw 6 random numbers
        winning_draw = set(random.sample(range(1, 50), 6))
        # Find matching numbers
        matches = len(player_numbers & winning_draw)
        match_counts[matches] += 1

    theoretical_probs = get_theoretical_lottery_probs()

    # Create summary table
    headers = ["Match", "Frequency", "Experimental Prob", "Theoretical Prob", "Theoretical Odds"]
    rows = []
    for k in range(7):
        freq = match_counts[k]
        exp_p = freq / num_trials
        theo_p = theoretical_probs[k]
        
        # Format odds string
        if theo_p > 0:
            odds_str = f"1 in {int(1/theo_p):,}"
        else:
            odds_str = "N/A"
            
        rows.append([
            f"Match {k}",
            f"{freq:,}",
            f"{exp_p:.8f}",
            f"{theo_p:.8f}",
            odds_str
        ])

    stats_utils.print_table(headers, rows, title=f"Lottery Simulation Results ({num_trials:,} Trials)")

    # Print interesting observations
    print("\nSimulation Observations:")
    print("-" * 60)
    print(f"- Total Tickets Purchased: {num_trials:,}")
    cost_per_ticket = 2 # Assume $2 per ticket
    total_spent = num_trials * cost_per_ticket
    print(f"- Total Cost (at ${cost_per_ticket} per ticket): ${total_spent:,}")
    
    # Simple prize structure: Match 3 = $10, Match 4 = $100, Match 5 = $2000, Match 6 = $5,000,000
    prizes = {0: 0, 1: 0, 2: 3, 3: 10, 4: 100, 5: 2000, 6: 5000000}
    total_winnings = sum(match_counts[k] * prizes[k] for k in range(7))
    net_profit = total_winnings - total_spent
    
    print(f"- Total Prize Money Won: ${total_winnings:,}")
    print(f"- Net Profit/Loss: ${net_profit:+,}")
    if net_profit < 0:
        print("  Status: Net Loss (expected outcome for lottery play).")
    else:
        print("  Status: Net Profit (extremely lucky!)")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    run_lottery_simulation()
