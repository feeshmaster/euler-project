alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

names = []


with open("0022_names.txt", "r") as f:
    names = f.read().replace('"', "").split(",")
    names.sort()

def score(name: str):
    s = 0
    for letter in name:
        s += alphabet.index(letter.lower()) + 1
    return  s * (names.index(name) + 1)
total = 0
for name in names:
    total += score(name)
print(total)