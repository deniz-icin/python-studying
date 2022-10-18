"""Some rules of Blackjack,
such as the way the game is played and scored.
"""
def value_of_card(card):
    face_cards = {"J","Q","K"}
    numericals = {"2","3","4","5","6","7","8","9","10"}
    if card in face_cards:
        return 10
    if card in numericals:
        return int(card)
    return 1 #"A" as ace_card
def higher_card(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one > value_card_two:
        return card_one
    if value_card_one == value_card_two:
        return card_one,card_two
    return card_two
def value_of_ace(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if card_one == "A" or card_two == "A":
        return 1
    if value_card_one + value_card_two > 10:
        return 1
    return 11
def is_blackjack(card_one, card_two):
    ten_points = {"10","J","Q","K"}
    if card_one == "A" and card_two in ten_points:
        return True
    if card_one in ten_points and card_two == "A":
        return True
    return False
def can_split_pairs(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one == value_card_two:
        return True
    return False
def can_double_down(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    if value_card_one + value_card_two in range(9,12):
        return True
    return False
