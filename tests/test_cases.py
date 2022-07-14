
import pytest
from test_json.team_rcb_json import *
from team_check.player_count import *


@pytest.fixture()
def load_team_data():
    team = load_json_data()
    return team


def test_foreign_player_count(load_team_data):
    player_count = count_foreign_players(load_team_data)
    assert player_count == 4, "Team cannot have more or less than 4 foreign players"
    print("Team has only 4 foreign players")


def test_one_keeper(load_team_data):
    player_count = count_wicketkeeper(load_team_data)
    assert player_count >= 1, "Team should have at least one WK"
    print("Team has at least one wicket keeper")
