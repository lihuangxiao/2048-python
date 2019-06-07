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
def test_right(board, expected_board):
    game = Game2048(board=board)
    game.right()
    assert game.game_board == expected_board



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
                2, 2, 256, 2,
                8, 2, 256, 4,
                2, 2, 128, 2,
                4, 0, 128, 0
            ],
        )
    ]
)
def test_rotation_90_right(board, expected_board):
    game = Game2048(board=board)
    game.rotation_90_right()
    assert game.game_board == expected_board


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
                2, 4, 2, 0,
                512, 256, 0, 0,
                4, 2, 0, 0,
                2, 8, 2, 4
            ],
        )
    ]
)
def test_left(board, expected_board):
    game = Game2048(board=board)
    game.left()
    assert game.game_board == expected_board


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
                2, 4, 2, 128,
                256, 256, 128, 4,
                4, 2, 4, 0,
                0, 8, 0, 0
            ],
        )
    ]
)
def test_up(board, expected_board):
    game = Game2048(board=board)
    game.up()
    assert game.game_board == expected_board


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
                0, 4, 0, 0,
                2, 256, 2, 0,
                256, 2, 128, 128,
                4, 8, 4, 4
            ],
        )
    ]
)
def test_down(board, expected_board):
    game = Game2048(board=board)
    game.down()
    assert game.game_board == expected_board
