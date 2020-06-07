# from pprint import pprint
sentence = 'This is most common interview quistion'
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_Shorted = sorted(char_frequency.items(),
                      key=lambda kv: kv[1], reverse=True)

# pprint(char_frequency, width=1)
print(char_Shorted)
x, y = char_Shorted[0]
print(f"max={x} {y}")
