bids = {}
next_bidder = 'yes'
while(next_bidder == 'yes'):
    name = input("What is your name?: ")
    bid = int(input("What is your name?: $"))
    bids[name] = bid
    next_bidder = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
maxs = max(bids.values())
for i,j in bids.items():
    if j == maxs:
        print(f"The winner is {i} with a bid of {j}")