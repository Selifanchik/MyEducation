table_cards = ["A_S", "J_H", "7_S", "8_S", "10_D"]
hand_cards = ["J_S", "3_S"]
suits = dict.fromkeys(['S', 'H', 'D', 'C'], 0)
for elem in (table_cards + hand_cards):
    suits[elem[-1]] = suits.get(elem[-1]) + 1
if max(suits.values()) >= 5:
    print('Flush!')
else:
    print('No Flush!')
