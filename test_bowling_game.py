import pytest

from bowling_game import BowlingGame


@pytest.fixture
def game():
    return BowlingGame()


def test_gutter_game(game):
    roll_many(game, count=20, pins=0)

    assert game.score() == 0


def test_all_ones(game):
    roll_many(game, count=20, pins=1)

    assert game.score() == 20


def test_spare(game):
    roll_spare(game)
    game.roll(1)

    roll_many(game, count=17, pins=0)

    assert game.score() == 12


def test_strike(game):
    roll_strike(game)
    game.roll(1)
    game.roll(2)

    roll_many(game, count=17, pins=0)

    assert game.score() == 16


def roll_strike(game):
    game.roll(10)


def roll_spare(game):
    game.roll(5)
    game.roll(5)


def roll_many(game, count, pins):
    for roll in range(count):
        game.roll(pins)
