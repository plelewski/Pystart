from random import choice

def play_game(p_choice: str, c_choice: str) -> int:
    if p_choice == c_choice:
        return 0
    if (p_choice == 'papier' and c_choice == 'kamień') or (p_choice == 'kamień' and c_choice == 'nożyce') or (
            p_choice == 'nożyce' and c_choice == 'papier'):
        return 1
    return 2


def test_draw():
    assert play_game('papier', 'papier') == 0
    assert play_game('nożyce', 'nożyce') == 0
    assert play_game('kamień', 'kamień') == 0


def test_p_win():
    assert play_game('papier', 'kamień') == 1


def test_c_win():
    assert play_game('papier', 'nożyce') == 2


if __name__ == '__main__':
    player = input('Wybierz: kamień, papier, nożyce ')
    computer = choice(['kamień', 'papier', 'nożyce'])

    print(f'Player wybrał: {player}')
    print(f'Computer zalosował: {computer}')
    print(f'wynik: {play_game(player, computer)}')
    # tu można oczywiście if/elif/else aby wyświetlić zwycięzce
