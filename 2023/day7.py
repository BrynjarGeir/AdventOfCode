from utils.util import getLines

inpt = "./data/day7/input.txt"
test = "./data/day7/test.txt"
reddit_test = "./data/day7/reddit_LxsterGames_test.txt"

def getHands(lines: list[str]) -> list[(str, int)]:
    res = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        res.append((hand, bid))
    return res

def onlyOnce(res: dict[int]):
    seen2 = 0
    for key in res:
        if res[key] == 2:
            seen2 += 1
    return seen2 == 1

def posJ(cards: str) -> list[int]:
    res, n = [], len(cards)

    for i in range(n):
        if cards[i] == 'J':
            res.append(i)

    return res

def getHandType(hand: (str, int)) -> int:
    res = {}
    cards = hand[0]
    for card in cards:
        if card in res:
            res[card] += 1
        else:
            res[card] = 1
    mv = max(res.values())

    if mv in (4,5): # Four or five of a kind 5/6
        return mv + 1 
    if mv == 3 and 2 in res.values(): # Full house
        return 4
    if mv == 3: # Three of a kind
        return 3
    if mv == 2 and not onlyOnce(res): # two pair
        return 2
    if mv == 2: # one pair
        return 1
    return 0 # high card

def getHandTypeJokerPerm(cards: str) -> int:
    res = {}
    for card in cards:
        if card in res:
            res[card] += 1
        else:
            res[card] = 1
    mv = max(res.values())

    if mv in (4,5): # Four or five of a kind 5/6
        return mv + 1 
    if mv == 3 and 2 in res.values(): # Full house
        return 4
    if mv == 3: # Three of a kind
        return 3
    if mv == 2 and not onlyOnce(res): # two pair
        return 2
    if mv == 2: # one pair
        return 1
    return 0 # high card

def getHandTypeJoker(hand: (str, int)) -> int:
    res, lst = {}, ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards = hand[0]
    n = len(lst)
    if 'J' not in cards:
        return getHandType(hand)
    for card in cards:
        if card in res:
            res[card] += 1
        else:
            res[card] = 1
    
    if res['J'] == 4 or res['J'] == 5:
        return 6

    if res['J'] == 3:
        possible_cards = []
        a, b, c = posJ(cards)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    curr = cards[:a] + lst[i] + cards[a+1:b] + lst[j] + cards[b+1:c] + lst[k] + cards[c+1:]
                    possible_cards.append(curr)


        possible_cards = [(p, getHandTypeJokerPerm(p)) for p in possible_cards]

        possible_cards = sorted(possible_cards, key= lambda i: (i[1]), reverse=True)

        return possible_cards[0][1]
    if res['J'] == 2:
        possible_cards = []
        a, b = posJ(cards)

        for i in range(n):
            for j in range(n):
                curr = cards[:a] + lst[i] + cards[a+1:b] + lst[j] + cards[b+1:]
                possible_cards.append(curr)

        possible_cards = [(p, getHandTypeJokerPerm(p)) for p in possible_cards]

        possible_cards = sorted(possible_cards, key= lambda i: (i[1]), reverse=True)

        return possible_cards[0][1]
    
    possible_cards = []
    a = posJ(cards)[0]

    for i in range(n):
        curr = cards[:a] + lst[i] + cards[a+1:]
        possible_cards.append(curr)

    possible_cards = [(p, getHandTypeJokerPerm(p)) for p in possible_cards]

    possible_cards = sorted(possible_cards, key= lambda i: (i[1]), reverse=True)

    return possible_cards[0][1]
    
def handToValues(hand: str) -> list[int]:
    cards = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    res = [cards[card] for card in hand]

    return res

def handToValuesJoker(hand: str) -> list[int]:
    cards = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
    res = [cards[card] for card in hand]

    return res

def addHandType(hands: list[(str, int)]) -> list[(str, int, int)]:
    n = len(hands)

    for i in range(n):
        t = getHandType(hands[i])
        hands[i] = (hands[i][0], hands[i][1], t)
    return hands

def addHandTypeJoker(hands: list[(str, int)]) -> list[(str, int, int)]:
    n = len(hands)
    for i in range(n):
        t = getHandTypeJoker(hands[i])
        hands[i] = (hands[i][0], hands[i][1], t)
    return hands

def addValuesToHand(hands: list[(str, int, int)]) -> list[(str, int, int, list[int])]:
    n = len(hands)
    for i in range(n):
        hands[i] = (hands[i][0], hands[i][1], hands[i][2], handToValues(hands[i][0]))
    return hands
def addValuesToHandJoker(hands: list[(str, int, int)]) -> list[(str, int, int, list[int])]:
    n = len(hands)
    for i in range(n):
        hands[i] = (hands[i][0], hands[i][1], hands[i][2], handToValuesJoker(hands[i][0]))
    return hands

def sortedHands(hands: list[(str, int, int)]) -> list[(str, int, int)]:
    hands = sorted(sorted(hands, key= lambda i: (i[3]), reverse=True), key = lambda i: (i[2]))
    return hands

def getFinalValues(hands: list[tuple]) -> int:
    res, n = 0, len(hands)

    for i in range(n):
        res += hands[i][1] * (i+1)
    return res

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    hands = getHands(lines)

    hands = addHandType(hands)

    hands = addValuesToHand(hands)

    hands = sortedHands(hands)

    res = getFinalValues(hands)

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    hands = getHands(lines)

    hands = addHandTypeJoker(hands)

    hands = addValuesToHandJoker(hands)

    hands = sortedHands(hands)

    res = getFinalValues(hands)

    print(f"The answer to part 2 is {res}")

    return res
    
part1()

part2()