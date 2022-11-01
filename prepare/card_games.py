def get_rounds(number):
    return [number,number+1,number+2]
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 +rounds_2
def list_contains_round(rounds, number):
    return number in rounds
def card_average(hand):
    return sum(hand) / len(hand)
def approx_average_is_average(hand):
    return card_average(hand) == hand[(len(hand) - 1) // 2] or card_average(hand) == card_average([hand[0], hand[-1]])
def average_even_is_average_odd(hand):
    avr_even = sum(hand[::2]) / len(hand[::2])
    avr_odd = sum(hand[1::2]) / len(hand[1::2])
    return avr_even == avr_odd
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
