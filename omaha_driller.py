import random

paired = True
suit_grp = ['ds', 'ss', 'rb']
suits = 'shdc'
suits = list(suits)
ranks = ['a', 2, 3, 4, 5, 6, 7, 8, 9, 't', 'j', 'q', 'k']


while True:

    #init
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(str(rank) + suit)
    pocket = []

    user_input = input("Enter:")

    if paired == True:
        suit_indices = list(range(4))
        random.shuffle(suit_indices)

        suit_index_1 = suit_indices.pop(0)
        suit_1 = suits[suit_index_1]
        rank_1 = random.choice(ranks)

        suit_index_2 = suit_indices.pop(0)
        suit_2 = suits[suit_index_2]

        ## make pair
        pocket.append(str(rank_1) + suit_1)
        pocket.append(str(rank_1) + suit_2)
        deck.remove(pocket[0])
        deck.remove(pocket[1])
        random.shuffle(deck)
        pocket.append(deck.pop(0))
        pocket.append(deck.pop(0))
    else:
        random.shuffle(deck)
        pocket.append(deck.pop(0))
        pocket.append(deck.pop(0))
        pocket.append(deck.pop(0))
        pocket.append(deck.pop(0))

    random.shuffle(pocket)
    print(' '.join(pocket))


