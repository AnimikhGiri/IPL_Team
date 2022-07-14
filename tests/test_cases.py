
import pytest
from test_json.team_rcb_json import *


@pytest.fixture()
def load_team_data():
    return load_json_data()


def test_foreign_player_count(load_team_data):
    team = load_team_data
    foreign_sum = 0
    for i in team['player']:
        if i['country'] != 'India':
            foreign_sum += 1
    assert foreign_sum == 4, "Team cannot have more or less than 4 foreign players"
    print("Team has only 4 foreign players")


def test_one_keeper(load_team_data):
    team = load_team_data
    count = 0

    for i in team['player']:
        if i['role'] == 'Wicket-keeper':
            count += 1
    assert count >= 1, "Team should have at least one WK"
    print("Team has at least one wicket keeper")
