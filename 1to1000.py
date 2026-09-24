num2word = {
    "base": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"},
    "teens": {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"},
    "tens": {        10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
}

def _(n):
    return len(str(n))
def tens(n):
    l = _(n)
    s = str(n)
    if n in num2word["tens"]:
        return (num2word["tens"][n])
    elif n in num2word["teens"]:
        return (num2word["teens"][n])
    elif l == 2:
        return (num2word["tens"][int(s[0] + "0")] + num2word["base"][int(s[1])])
def n2w(n):
    l = _(n)
    s = str(n)
    if n in num2word["base"]:
        return (num2word["base"][n])
    if l == 2:
        return (tens(n))
    if l == 3:
        if s[1] == "0" and s[2] == "0":
            return (num2word["base"][int(s[0])] + "hundred")
        elif s[1] == "0":
            return (num2word["base"][int(s[0])] + "hundredand" + num2word["base"][int(s[2])])
        else:
            return (num2word["base"][int(s[0])] + "hundredand" + tens(int(s[1:])))
    if l == 4:
        return "onethousand"
summ = 0    
for i in range(1, 1001):
    summ += len(n2w(i))
    print(n2w(i))
    
print(summ)