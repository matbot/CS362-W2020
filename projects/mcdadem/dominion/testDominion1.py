# -*- coding: utf-8 -*-
"""
Author: Mathew McDade
@author: mcdadem
Date: 1/12/20
"""
import projects.mcdadem.dominion.Dominion as Dominion
import projects.mcdadem.dominion.testUtility as tU

# BUILD GAME
# ---------------------------------------------------------------------------- #
# Set the player names.
player_names = ["Annie", "*Ben", "*Carla"]

# Construct the player objects.
players = tU.build_players(player_names)

# Build the supply deck.
supply = tU.build_supply(len(player_names))

# Get supply prices.
supply_order = tU.get_supply_prices()

# Initialize the trash.
trash = []


# PLAY GAME
# ---------------------------------------------------------------------------- #
#Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1

    tU.print_supply(supply, supply_order)
    tU.print_players(players)

    print("\rStart of turn " + str(turn))
    tU.play_turn(players, supply, trash)


# FINAL SCORE
# ---------------------------------------------------------------------------- #
# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)