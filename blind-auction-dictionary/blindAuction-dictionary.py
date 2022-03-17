from asscciart import gavel
import os

os.system('clear')
print (gavel)
bids={} 
bidding_finished=False

def winner_finder(bid_rec):
    highest_bid=0
    winner=""
    for bidder in bid_rec:
        bid_amount=bid_rec[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
    name = input("What is your name?: ")
    price =float(input("What is your price?: $"))
    bids[name]=price
    to_be_continue=input("Are there any other bidder? Type 'yes' or 'no'\n")
    if to_be_continue=="no":
        bidding_finished=True
        winner_finder(bids)
    elif to_be_continue=='yes':
        os.system('cls')
