"""
bingo_generator.py

A script to generate simple bingo cards using a list of concepts in a text file.
The given text file should contain words (the shorter the better) separated by new lines.

Usage:

    python bingo_generator.py

Arguments:
    --num_cards 12                  (create a set amount of cards)
    --concepts_file other_file.txt  (use a different list)
    --save_dir /your-dir/           (store to a different directory)
"""

import os
import random
import argparse
import matplotlib.pyplot as plt
import textwrap
import string

def read_concepts(file_name) -> list:
    with open(file_name, 'r') as file:
        concepts = file.readlines()
    return [concept.strip() for concept in concepts]

def generate_bingo_card(concepts, rows=5, cols=5):
    card = random.sample(concepts, rows * cols)
    card_matrix = [card[i:i+cols] for i in range(0, len(card), cols)]
    return card_matrix

def plot_bingo_card(card, save_dir) -> None:
    """
    Plot a single (simple) bingo card using matplotlib.

    :param card:        Matrix data for the card, obtained from generate_bingo_card
    :param save_dir:    Directory to store the result
    :return:
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.matshow([[0]*5]*5, cmap='Greys')  # to draw bingo grid
    for i in range(5):
        for j in range(5):
            text = '\n'.join(textwrap.wrap(card[i][j], width=12))  # Adjust width as needed
            ax.text(j, i, text, ha='center', va='center', fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(color='black', linestyle='-', linewidth=1)

    # Generate unique ID for the bingo card
    unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    file_path = os.path.join(save_dir, f'bingo_card_{unique_id}.png')
    plt.savefig(file_path)
    plt.close()
    print(f"Bingo card saved at: {file_path}")

def generate_bingo_cards(concepts_file, save_dir, num_cards=1):
    """
    Genereer een enkele bingo-kaart.

    :param concepts_file:   File met opties voor de bingo-kaart
    :param save_dir:        File om de bingokaart in op te slaan
    :param num_cards:       Aantal kaarten om te genereren
    :return:
    """
    concepts = read_concepts(concepts_file)
    os.makedirs(save_dir, exist_ok=True)
    for _ in range(num_cards):
        bingo_card = generate_bingo_card(concepts)
        plot_bingo_card(bingo_card, save_dir)


if __name__ == "__main__":
    """
    Only execute if we are using the script directly :)
    """
    parser = argparse.ArgumentParser(description="Generate Bingo cards")
    parser.add_argument("--concepts_file", type=str, default="concepts.txt", help="Path to the concepts file")
    parser.add_argument("--save_dir", type=str, default="Resources/Bingo", help="Directory to save bingo cards")
    parser.add_argument("--num_cards", type=int, default=1, help="Number of bingo cards to generate")
    args = parser.parse_args()

    generate_bingo_cards(args.concepts_file, args.save_dir, args.num_cards)
