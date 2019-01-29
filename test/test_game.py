import pytest
from py2048.game import Game2048


@pytest.mark.parametrize(
    'four, expected_four',
    [
        (
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ),
        (
            [2, 4, 2, 0],
            [0, 2, 4, 2]
        ),
        (
            [0, 2, 2, 0],
            [0, 0, 0, 4]
        ),
        (
            [256, 256, 128, 128],
            [0, 0, 512, 256]
        ),
        (
            [2, 2, 2, 0],
            [0, 0, 2, 4]
        ),
        (
            [2, 8, 2, 4],
            [2, 8, 2, 4]
        ),
    ]
)
def test_squash_four(four, expected_four):
    game2048 = Game2048()
    assert game2048.squash_four(four) == expected_four



@pytest.mark.parametrize(
    'board, expected_board',
    [
        (
            [
                2, 4, 2, 0,
                256, 256, 128, 128,
                2, 2, 2, 0,
                2, 8, 2, 4
            ],
            [
                0, 2, 4, 2,
                0, 0, 512, 256,
                0, 0, 2, 4,
                2, 8, 2, 4
            ],
        )
    ]
)
def test_swipe_right(board, expected_board):
    game = Game2048(board=board)
    game.swipe_right()
    assert game.game_board == expected_board
