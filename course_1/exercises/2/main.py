def convert(originStr, card):
    result = ''

    for x in originStr:
        result += card[x]

    return result

origin = input()
cipher = input()
toCipher = input()
toOrigin = input()

cipherCard = {}
decipherCard = {}

for i, sym in enumerate(origin):
    cipherCard[sym] = cipher[i]
    decipherCard[cipher[i]] = sym

print(convert(toCipher, cipherCard))
print(convert(toOrigin, decipherCard))
