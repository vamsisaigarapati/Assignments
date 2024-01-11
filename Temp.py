def optimal_winner(colors):
    while True:
        # Wendy's turn
        wendy_move = None
        for i in range(1, len(colors) - 1):
            if colors[i] == 'w' and colors[i - 1] == 'w' and colors[i + 1] == 'w':
                wendy_move = i
                break

        if wendy_move is not None:
            colors = colors[:wendy_move] + colors[wendy_move + 1:]
        else:
            return 'bob'  # Wendy can't make a move, Bob wins

        # Bob's turn
        bob_move = None
        for i in range(1, len(colors) - 1):
            if colors[i] == 'b' and colors[i - 1] == 'b' and colors[i + 1] == 'b':
                bob_move = i
                break

        if bob_move is not None:
            colors = colors[:bob_move] + colors[bob_move + 1:]
        else:
            return 'wendy'  # Bob can't make a move, Wendy wins

# Example usage
colors_example = 'wwwbbbbwww'
result = optimal_winner(colors_example)
print(result)
