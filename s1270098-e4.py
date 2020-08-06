
import random

l = ["Heads", "Tails"]
head = 0
tail = 0

print('Who are you?')
name = input('> ')
print('Hello, ' + name + '!')

print("Tossing a coin...")
for i in range(3):
    j = random.choice(l)
    print("Round {}: {}".format(i+1,j))
    if j == "Heads":
        head += 1
    else:
        tail += 1
print("Heads: {}, Tails: {}".format(head,tail))

if head > tail:
    print(name + " won!")
else:
    print(name + " lost!")
