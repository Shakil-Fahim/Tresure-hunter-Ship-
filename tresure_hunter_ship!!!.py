# -*- coding: utf-8 -*-
"""Tresure Hunter Ship!!!

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SPs6WaQjDCKjG8myRPA8EKrfV365qtQ8
"""

def display_board(board, player_x, player_y):
    for i in range(5):
        for j in range(5):
            if i == player_x and j == player_y:
                print("🚢 ", end="")
            else:
                print(board[i][j] + " ", end="")
        print()  # New line after each row
    print()

def play_level(board, treasure_x, treasure_y, level_num):
    player_x = 0
    player_y = 0
    moves = 0
    found_treasure = False

    while not found_treasure:
        display_board(board, player_x, player_y)
        print(f"Level {level_num} - Moves: {moves}")

        direction = input("Enter direction (up/down/left/right) or 'quit' to exit: ").lower()

        if direction == "quit":
            print("Game ended by player.")
            return False

        old_x = player_x
        old_y = player_y

        if direction == "up" and player_x > 0:
            player_x -= 1
        elif direction == "down" and player_x < 4:
            player_x += 1
        elif direction == "left" and player_y > 0:
            player_y -= 1
        elif direction == "right" and player_y < 4:
            player_y += 1
        else:
            print("Invalid move! Can't go that way!")
            continue

        moves += 1

        if player_x == treasure_x and player_y == treasure_y:
            found_treasure = True
            display_board(board, player_x, player_y)
            print(f"Level {level_num} completed in {moves} moves!")
            return True

def play_game():
    # Define multiple levels
    levels = [
        # Level 1: Simple layout
        {
            "board": [
                ["🌊", "🌊", "🏝️", "🌊", "🌊"],
                ["🌊", "🏝️", "🌊", "🏝️", "🌊"],
                ["🌊", "🌊", "🌊", "🌊", "🏝️"],
                ["🏝️", "🌊", "🌊", "💰", "🌊"],
                ["🌊", "🏝️", "🌊", "🌊", "🌊"]
            ],
            "treasure_x": 3,
            "treasure_y": 3
        },
        # Level 2: More islands
        {
            "board": [
                ["🌊", "🏝️", "🌊", "🏝️", "🌊"],
                ["🏝️", "🌊", "🏝️", "🌊", "🌊"],
                ["🌊", "🏝️", "🌊", "🌊", "🏝️"],
                ["🌊", "🌊", "🏝️", "💰", "🌊"],
                ["🏝️", "🌊", "🌊", "🏝️", "🌊"]
            ],
            "treasure_x": 3,
            "treasure_y": 3
        },
        # Level 3: Challenging layout
        {
            "board": [
                ["🌊", "🏝️", "🏝️", "🌊", "🏝️"],
                ["🏝️", "🌊", "🌊", "🏝️", "🌊"],
                ["🌊", "🏝️", "🏝️", "🌊", "🌊"],
                ["🏝️", "🌊", "🌊", "🌊", "💰"],
                ["🌊", "🏝️", "🏝️", "🌊", "🌊"]
            ],
            "treasure_x": 4,
            "treasure_y": 4
        }
    ]

    print("Welcome to Treasure Hunt!")
    print("Find the 💰 treasure in each level!")
    print("Your ship: 🚢")

    for level_num, level in enumerate(levels, 1):
        print(f"\nStarting Level {level_num}")
        success = play_level(level["board"], level["treasure_x"], level["treasure_y"], level_num)
        if not success:
            break
        if level_num < len(levels):
            input("Press Enter to continue to next level...")

    if success:
        print("Congratulations! You've completed all levels!")

if __name__ == "__main__":
    play_game()