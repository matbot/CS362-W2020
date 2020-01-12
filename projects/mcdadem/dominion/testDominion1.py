# -*- coding: utf-8 -*-
"""
Author: Mathew McDade
@author: mcdadem
Date: 1/12/20
"""

import projects.mcdadem.dominion.testUtility as tU

# Get player names.
player_names = tU.get_player_names()

# Construct the player objects.
players = tU.build_players(player_names)

# Get curses and victory card quantities.
nC, nV = tU.get_curse_victory_card_quantities(player_names)

# Get card box.
box = tU.get_card_box(nV)

# Get supply prices.
supply_order = tU.get_supply_prices()

# Put 10 random cards from box into the supply.
supply = tU.get_random_supply_cards(box)

# Put the default cards into the supply.
tU.set_default_supply(supply, player_names, nC, nV)

# Initialize the trash.
trash = []













#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)