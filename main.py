from itertools import zip_longest
import utils_kombat


def get_winner_kombat(dict_kombat):
    first_player, second_player = utils_kombat.whos_first_and_second_player(dict_kombat)
    print(f"First player: {first_player}")
    print(f"Second player: {second_player}")

    flag = False

    combinations_first_player = utils_kombat.get_combinations(dict_kombat[first_player]["movimientos"], dict_kombat[first_player]["golpes"])
    combinations_second_player = utils_kombat.get_combinations(dict_kombat[second_player]["movimientos"], dict_kombat[second_player]["golpes"])

    energia_first_player = 6
    energia_second_player = 6

    winner = ""

    for comb_first, comb_second in zip_longest(combinations_first_player, combinations_second_player):
        if comb_first:
            danio = utils_kombat.get_damage(first_player, comb_first)
            energia_second_player -= danio

            if energia_second_player <= 0:
                winner = first_player
                flag = True
                break

        if comb_second:
            danio = utils_kombat.get_damage(second_player, comb_second)
            energia_first_player -= danio

            if energia_first_player <= 0:
                winner = second_player
                flag = True
                break

        if flag:
            break


    if winner:
        if winner == 'player1':
            winner = 'Tonyn (player1)'
        else: winner = 'Arnaldor (player2)'
        print(f"Gana: {winner}")
    else:
        print("No hubo ganadores")


if __name__ == "__main__":
    try:
        dict_kombat = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
        get_winner_kombat(dict_kombat)
    except Exception as e:
        print(f'{type(e).__name__} => {e}')
# %%
