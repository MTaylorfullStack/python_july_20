import random
from number_players import players

print(players)

def determine_winner(players):
    max = players[0]['score']
    winner = players[0]
    for player in players:
        if player['score'] > max:
            max = player['score']
            winner = player
    return winner


def random_number_game(players):
    randy = int(random.random() * 10)
    for player in players:
        if player['guess'] > randy:
            player['score'] += 10
        elif player['guess'] < randy:
            player['score'] += 5
        else:
            player['score'] += 15
    the_winner = determine_winner(players)
    return f"Winner of round is {the_winner['name']} with a guess of {the_winner['guess']} and score of {the_winner['score']}!!!"

def play_rounds(players, rounds):
    for i in range(rounds):
        random_number_game(players)
    game_winner = determine_winner(players)
    return f"Winner of THE GAME is {game_winner['name']} with a guess of {game_winner['guess']} and score of {game_winner['score']}!!!"


print(play_rounds(players, 10))