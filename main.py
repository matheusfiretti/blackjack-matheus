import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards = []
dealer_cards = []
soma_dealer = 0
sua_soma = 0
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

jogando = True

while jogando:
    for i in range (2):
        carta_dealer = random.choice(cards)
        dealer_cards.append(carta_dealer)

        sua_carta = random.choice(cards)
        your_cards.append(sua_carta)

    soma_dealer = sum(dealer_cards)
    sua_soma = sum(your_cards)
    
    print(f'Suas cartas: {your_cards}. Cartas do dealer: {dealer_cards[0]}, ?')
    continuando = True

    while continuando:
        if sua_soma < 21:
            continua = input('Deseja outra carta? Digite "y" ou "n"\n')
            if continua == 'y':
                your_cards.append(random.choice(cards))
                print(your_cards)
                sua_soma += your_cards[-1]
                if sua_soma > 21:
                    print('Você estourou!')
                    continuando = False
                    jogando = False
            else:
                if soma_dealer < 16:
                    while soma_dealer <= 16:
                        dealer_cards.append(random.choice(cards))
                        soma_dealer += dealer_cards[-1]
                    if soma_dealer > 21:
                        print('Dealer estourou')
                        
                continuando = False
                print(f'Cartas do dealer: {dealer_cards}')

        elif sua_soma == 21:
            print('Blackjack')
            continuando = False
            jogando = False
            
    if soma_dealer > sua_soma and soma_dealer <= 21:
        print('Perdeu!')
    elif soma_dealer == sua_soma:
        print('Empate!')
    elif sua_soma > soma_dealer and sua_soma <= 21:
        print('Ganhou!')   

    jogando = False