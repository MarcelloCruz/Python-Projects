import random

def generate_number():
    digits = "0123456789"
    first = random.choice(digits[1:])
    rest = random.sample([d for d in digits if d != first], 3)
    return first + ''.join(rest)

def checkn(number, guess):
    nlist = list(number)
    glist = list(guess)
    runner, reporter = 0, 0

    if number == guess:
        return 0 , 4

    for i in range(len(nlist)):
        if nlist[i] == glist[i]:
            reporter += 1

    for d in set(glist):
        runner += min(glist.count(d), nlist.count(d))

    runner -= reporter

    return runner, reporter

