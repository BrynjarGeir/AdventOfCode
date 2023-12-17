from utils.util import getLines

inpt = "./data/day4/input.txt"
test = "./data/day4/test.txt"

def getNumbers(numbers: str) -> tuple[set[int]]:
    winning_numbers, my_numbers = numbers.split("|")
    
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    winning_numbers = set([int(winning_number) for winning_number in winning_numbers])
    my_numbers = set([int(my_number) for my_number in my_numbers])

    return winning_numbers, my_numbers

def getCardValue(card: str) -> int:
    card_number, numbers = card.split(":")
    winning_numbers, my_numbers = getNumbers(numbers)

    res = len(winning_numbers.intersection(my_numbers))

    if res == 0:
        return 0

    return 2**(res-1)

def getNumberOfCards(card: str) -> tuple[int, list[int]]:
    card_number, numbers = card.split(":")

    card, number = card_number.split()

    number = int(number)

    winning_numbers, my_numbers = getNumbers(numbers)

    res = len(winning_numbers.intersection(my_numbers))

    return number, [n for n in range(number, number+res)]

def getNumberOfWinnings(card: str) -> int:
    card_number, numbers = card.split(":")

    card, number = card_number.split()

    number = int(number)

    winning_numbers, my_numbers = getNumbers(numbers)

    res = len(winning_numbers.intersection(my_numbers))
    return res

def part1(filePath: str = inpt) -> int:

    cards = getLines(filePath)
    res = 0

    for card in cards:
        res += getCardValue(card)

    print(f"The answer to part 1 is {res}")
    
    return res

def part2(filePath: str = inpt) -> int:
    cards = getLines(filePath)
    n = len(cards)
    winnings_on_cards = [None for _ in range(n)]
    res = [1 for _ in range(n)]

    for i, card in enumerate(cards):
        c = getNumberOfWinnings(card)
        winnings_on_cards[i] = c
        for j in range(i+1, i+1+c):
                res[j] += res[i]
    res = sum(res)

    print(f"The answer to part2 is {res}")

    return res

part1()
part2()