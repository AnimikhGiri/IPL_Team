# function to count foreign players
def count_foreign_players(team_data):
    foreign_count = 0
    for i in team_data['player']:
        if i['country'] != 'India':
            foreign_count += 1
    return foreign_count


# function to count wicketkeeper
def count_wicketkeeper(team_data):
    wk_count = 0
    for i in team_data['player']:
        if i['role'] == 'Wicket-keeper':
            wk_count += 1
    return wk_count
