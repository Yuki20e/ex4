import random

l = ["Heads", "Tails"]
head = 0
tail = 0

print("Tossing a coin...")
for i in range(3):
    j = random.choice(l)
    print("Round {}: {}".format(i+1,j))
    if j == "Heads":
        head += 1
    else:
        tail += 1
print("Heads: {}, Tails: {}".format(head,tail))
