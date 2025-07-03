import json, random, time

def adult_truth():
    with open("truth_adults.json", "r") as f:
        truths = json.load(f)
        truth = random.choice(truths)
        print("\n",truth)

def adult_dare():
    with open("dare_adults.json", "r") as f:
        dares = json.load(f)
        dare = random.choice(dares)
        print("\n",dare)

def kids_truth():
    with open("truth_kids.json", "r") as f:
        truths = json.load(f)
        truth = random.choice(truths)
        print("\n",truth)

def kids_dare():
    with open("dare_kids.json", "r") as f:
        dares = json.load(f)
        dare = random.choice(dares)
        print("\n",dare)


noofplayers = int(input("Total no of players: "))
players = []
for i in range(1, noofplayers+1):
    player = input(f"Name of {i} player: ")
    players.append(player)

while True:
    print("Select Mode:\n\nKids or Adults")
    mode = input("Choice : ").lower()
    if mode not in ["adults", "kids"]:
        print("Please select valid mode!")
        continue
    break

while True:
    mode2 = int(input("\nTruth/Dare should be randomized or selected by user:\n\n1. Selected by user\n2. Random"))
    if mode2 not in [1, 2]:
        print("Please select valid option (1 / 2)!")
        continue
    break
if mode2 == 2:
    options = ["truth", "dare"]

next = "next"
while True:
    if next == "next":
        user = random.choice(players)
        print(f"\n\n{user}'s Turn!")
        if mode2 == 1:
            while True:
                option = input("\nTruth or dare? ").lower()
                if option not in ["truth", "dare"]:
                    print("PLease select valid option (truth/dare)")
                    continue
                break
        else:
            option = random.choice(options)
        
        print(f"It's a {option}")

        if option == "truth" and mode == "kids":
            kids_truth()
        elif option == "truth" and mode == "adults":
            adult_truth()
        elif option == "dare" and mode == "kids":
            kids_dare()
        elif option == "dare" and mode == "adults":
            adult_dare()
    
    next = input("\n\n\nEnter 'next' for new round")

