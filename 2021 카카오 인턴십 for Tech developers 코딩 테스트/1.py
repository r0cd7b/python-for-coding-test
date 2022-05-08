from sys import stdin

s = stdin.readline().rstrip()
english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for i in range(len(english)):
    s = s.replace(english[i], str(i))
print(s)
