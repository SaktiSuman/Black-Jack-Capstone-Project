import random


class BlackJack:

    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(self.cards)
        return card

    def calculate_score(self, cards):
        if sum(cards) == 20 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(self, user_score_compare, computer_score_compare):
        if user_score_compare == computer_score_compare:
            return "Draw 🙃"
        elif computer_score_compare == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score_compare == 0:
            return "Win with a Blackjack 😎"
        elif user_score_compare > 21:
            return "You went over. You lose 😭"
        elif computer_score_compare > 21:
            return "Opponent went over. You win 😁"
        elif user_score_compare > computer_score_compare:
            return "You win 😃"
        else:
            return "You lose 😤"
