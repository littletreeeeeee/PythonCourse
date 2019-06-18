#endcoding=UTF-8
left = ['A', 'K']
right = ['Q', 'J']
player1 = [left, right]
print player1
player2 = player1
import copy

player3 = copy.copy(player1) # duplicate parameter
player4 = copy.deepcopy(player1) #duplicate parameter and it's containing object
print hex(id(player1)), hex(id(player2)), hex(id(player3)), hex(id(player4))
print player1, player2, player3, player4
left[0] = 'JOKER' #改變List 中的List player3會改變(複製List，List中的List仍然是相同指向)，deepcopy的才會改變(整個複製)
print player1, player2, player3, player4
player1.append('10')#改變List 中的List player3會改變 因List是複製的
print player1, player2, player3, player4

print hex(id(player1[0])), hex(id(player2[0])), hex(id(player3[0])), hex(id(player4[0]))
