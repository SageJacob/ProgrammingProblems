x = int(input())
for i in range(x):
    piles = input().split()
    piles.sort()
    alice = int(piles[0])
    bob = int(piles[1])
    pile = int(piles[2])
    alice += pile // 2
    bob += pile // 2
    if alice == bob:
        print(alice)
        break
    if pile % 2 == 1:
        alice += 1
    while alice != bob:
        bob -= 1
        alice += 1
        if alice > bob:
            alice -= 1
            break
    print(alice)
