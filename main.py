from art import logo
from game_rules import BlackJack

g_rules = BlackJack()


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(g_rules.deal_card())
        computer_cards.append(g_rules.deal_card())

    while not is_game_over:
        user_score = g_rules.calculate_score(user_cards)
        computer_score = g_rules.calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(g_rules.deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(g_rules.deal_card())
        computer_score = g_rules.calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(g_rules.compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    play_game()


