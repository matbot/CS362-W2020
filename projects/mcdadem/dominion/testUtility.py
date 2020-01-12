# -*- coding: utf-8 -*-
"""
Author: Mathew McDade
@author: mcdadem
Date: 1/12/20
"""

import random
from collections import defaultdict

import projects.mcdadem.dominion.Dominion as Dominion

# BUILD GAME FUNCTIONS
# ---------------------------------------------------------------------------- #
# Return a list of player objects.
def build_players(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

# Return quantity of curse cards and victory cards.
def get_curse_victory_card_quantities(num_players):
    curse_card_quantity = -10 + 10 * num_players
    if num_players > 2:
        victory_card_quantity = 12
    else:
        victory_card_quantity = 8
    return curse_card_quantity, victory_card_quantity

# Return a standard box of cards.
def get_card_box(victory_card_quantity):
    return {
        "Woodcutter": [Dominion.Woodcutter()] * 10,
        "Smithy": [Dominion.Smithy()] * 10,
        "Laboratory": [Dominion.Laboratory()] * 10,
        "Village": [Dominion.Village()] * 10,
        "Festival": [Dominion.Festival()] * 10,
        "Market": [Dominion.Market()] * 10,
        "Chancellor": [Dominion.Chancellor()] * 10,
        "Workshop": [Dominion.Workshop()] * 10,
        "Moneylender": [Dominion.Moneylender()] * 10,
        "Chapel": [Dominion.Chapel()] * 10,
        "Cellar": [Dominion.Cellar()] * 10,
        "Remodel": [Dominion.Remodel()] * 10,
        "Adventurer": [Dominion.Adventurer()] * 10,
        "Feast": [Dominion.Feast()] * 10,
        "Mine": [Dominion.Mine()] * 10,
        "Library": [Dominion.Library()] * 10,
        "Gardens": [Dominion.Gardens()] * victory_card_quantity,
        "Moat": [Dominion.Moat()] * 10,
        "Council Room": [Dominion.Council_Room()] * 10,
        "Witch": [Dominion.Witch()] * 10,
        "Bureaucrat": [Dominion.Bureaucrat()] * 10,
        "Militia": [Dominion.Militia()] * 10,
        "Spy": [Dominion.Spy()] * 10,
        "Thief": [Dominion.Thief()] * 10,
        "Throne Room": [Dominion.Throne_Room()] * 10
    }

# Return prices for supply cards.
def get_supply_prices():
    return {
        0: ['Curse', 'Copper'],
        2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
        3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
        4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
            'Throne Room'],
        5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
        6: ['Gold', 'Adventurer'],
        8: ['Province']
    }

# Return a random selection of 10 supply cards from a card box.
def get_random_supply_cards(card_box):
    boxlist = [k for k in card_box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    return defaultdict(list, [(k, card_box[k]) for k in random10])

# Set the default supply level of essential cards.
def set_default_supply(supply, num_players, curse_card_quantity, victory_card_quantity):
    supply["Copper"] = [Dominion.Copper()] * (60 - num_players * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * victory_card_quantity
    supply["Duchy"] = [Dominion.Duchy()] * victory_card_quantity
    supply["Province"] = [Dominion.Province()] * victory_card_quantity
    supply["Curse"] = [Dominion.Curse()] * curse_card_quantity
    return

def build_supply(num_players, curse_card_quantity, victory_card_quantity):
    box = get_card_box(victory_card_quantity)
    supply = get_random_supply_cards(box)
    set_default_supply(supply, num_players, curse_card_quantity, victory_card_quantity)
    return supply


# PLAY GAME FUNCTIONS
# ---------------------------------------------------------------------------- #
# Print the available supply of cards at each price point.
def print_supply(supply, supply_prices):
    print("\r")
    for price in supply_prices:
        print(price)
        for card in supply_prices[price]:
            if card in supply:
                print(card, len(supply[card]))
    print("\r")
    return

# Print the player names and current scores.
def print_players(players):
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\r")
    return

# Have each player take a their turn.
def play_turn(players, supply, trash):
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)
    return


# FINAL SCORE FUNCTIONS
# ---------------------------------------------------------------------------- #
# Get a list of winners based on calculated player card summaries.
def get_winners(players):
    dcs = Dominion.cardsummaries(players)
    vp = dcs.loc['VICTORY POINTS']
    vpmax = vp.max()
    winners = []
    for i in vp.index:
        if vp.loc[i] == vpmax:
            winners.append(i)
    return winners, dcs

# Print the winners and the card summaries.
def print_winners(winners, dcs):
    if len(winners) > 1:
        winstring = ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0], 'wins!'])
    print("\nGAME OVER!!!\n" + winstring + "\n")
    print(dcs)
    return
