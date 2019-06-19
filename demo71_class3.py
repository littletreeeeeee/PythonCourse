#encoding=utf-8
class Team:
    name = 'Normal Team'


team1 = Team()
print team1.name
team1.name = 'R&D Team'
team2 = Team()
print team1.name, team2.name, Team.name
del team1.name  #刪除變量，解除team1對name的使用 (回Default)
print team1.name, team2.name, Team.name
team1.member = 9
print team1.name, team1.member