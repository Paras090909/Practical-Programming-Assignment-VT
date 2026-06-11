import random
import os
import sys

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.color = "Red" if suit in ["Hearts", "Diamonds"] else "Black"
        self.is_face = rank in ["Jack", "Queen", "King"]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

def build_deck():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    return [Card(rank, suit) for suit in suits for rank in ranks]

def run_card_simulator():
    print("=" * 60)
    print(" QUESTION 9: CARD SELECTION SIMULATOR (10,000 DRAWS) ")
    print("=" * 60)
    
    deck = build_deck()
    total_cards = len(deck)
    num_draws = 10000
    
    print(f"Standard deck initialized with {total_cards} cards.")
    print(f"Simulating {num_draws:,} random draws (with replacement to maintain probability consistency)...")

    # Counters
    draw_counts = {
        "Ace": 0,
        "King": 0,
        "Queen": 0,
        "Red Card": 0,
        "Face Card": 0
    }

    # Simulation
    for _ in range(num_draws):
        card = random.choice(deck)
        if card.rank == "Ace":
            draw_counts["Ace"] += 1
        if card.rank == "King":
            draw_counts["King"] += 1
        if card.rank == "Queen":
            draw_counts["Queen"] += 1
        if card.color == "Red":
            draw_counts["Red Card"] += 1
        if card.is_face:
            draw_counts["Face Card"] += 1

    # Theoretical calculations
    theoretical = {
        "Ace": 4 / 52,        # 4 Aces in deck
        "King": 4 / 52,       # 4 Kings in deck
        "Queen": 4 / 52,      # 4 Queens in deck
        "Red Card": 26 / 52,   # 26 Red cards (Hearts, Diamonds)
        "Face Card": 12 / 52,  # 12 Face cards (4 Jacks, 4 Queens, 4 Kings)
    }

    # Print comparative table
    headers = ["Card Category", "Draw Count", "Experimental P(E)", "Theoretical P(E)", "Difference"]
    rows = []
    for cat in ["Ace", "King", "Queen", "Red Card", "Face Card"]:
        count = draw_counts[cat]
        exp_p = count / num_draws
        theo_p = theoretical[cat]
        diff = abs(exp_p - theo_p)
        rows.append([
            cat,
            f"{count:,}",
            f"{exp_p:.4f}",
            f"{theo_p:.4f}",
            f"{diff:.4f}"
        ])

    stats_utils.print_table(headers, rows, title="Card Draw Probability Comparison")

    # Sample draws demo
    print("\nVisualizing 5 random sample draws:")
    for i in range(1, 6):
        c = random.choice(deck)
        props = []
        if c.rank == "Ace": props.append("Ace")
        if c.rank == "King": props.append("King")
        if c.rank == "Queen": props.append("Queen")
        if c.color == "Red": props.append("Red")
        if c.is_face: props.append("Face Card")
        props_str = f"({', '.join(props)})" if props else ""
        print(f"  Draw {i}: {c} {props_str}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_card_simulator()
