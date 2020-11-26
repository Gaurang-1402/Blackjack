import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16

def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome

    :return: None
    """

    print("Let's Play Blackjack!\n")
    replay_prompt = "Y"
    while replay_prompt != "N":

        if replay_prompt == "Y":

            player_total = deal_cards_to_player()
            if player_total > BLACKJACK:
                print("YOU LOSE!\n")

            else:
                dealer_total = deal_cards_to_dealer()
                determine_outcome(player_total, dealer_total)

        replay_prompt = input("Play again (Y/N)? ")
        print()

    print("Goodbye.")


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.

    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    if BLACKJACK >= player_total > dealer_total or (dealer_total > BLACKJACK):
        print("YOU WIN!\n")
    else:
        print("YOU LOSE!\n")



def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total

    :return: the total value of the cards dealt
    """


    label_card_1 = deal_card()
    val_card_1 = get_card_value(label_card_1)
    label_card_2 = deal_card()
    val_card_2 = get_card_value(label_card_2)

    card_total = val_card_1 + val_card_2
    print("The dealer has {} and {}.\nDealer's total is {}.\n".format(label_card_1, label_card_2, card_total))

    while card_total <= DEALER_THRESHOLD:
        additional_label_card = deal_card()
        additional_val_card = get_card_value(additional_label_card)
        card_total = card_total + additional_val_card
        print("Dealer drew {}.\nDealer's total is {}.\n".format(additional_label_card, card_total))

    return card_total

def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total

    :return: the total value of the cards dealt
    """
    label_card_1 = deal_card()
    val_card_1 = get_card_value(label_card_1)
    label_card_2 = deal_card()
    val_card_2 = get_card_value(label_card_2)

    card_total = val_card_1 + val_card_2


    print("Player drew {} and {}.\nPlayer's total is {}.\n".format(label_card_1, label_card_2, card_total))

    while card_total <= BLACKJACK:
        player_action = input("Hit (h) or Stay (s)? ")
        print()
        if player_action == "h":

            additional_label_card = deal_card()
            additional_val_card = get_card_value(additional_label_card)
            card_total = card_total + additional_val_card
            print("Player drew {}.\nPlayer's total is {}.\n".format(additional_label_card, card_total))
        elif player_action == "s":
            break

    return card_total


def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)

    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value"""

    numbered_cards = "2345678910"
    if card_label in numbered_cards:
        card_int = int(card_label)
    elif card_label == "A":
        card_int = ACE_VALUE
    else:
        card_int = FACE_CARD_VALUE


    #print("Integer is", card_int)

    return card_int




def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple

    :return: a single- or double-character string representing a playing card
    """
    card_pick = random.choice(CARD_LABELS)


    return card_pick



####### DO NOT EDIT ABOVE ########

def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below


    play_blackjack()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
