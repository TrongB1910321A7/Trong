import re
f = open("test.txt")
s = f.read().split("\n")
for e in s:
    result = re.search(r"(?<=\b@)[a-zA-Z0-9_.]+\.[a-zA-Z0-9_.]{1,}\b", e)
    if result:
        print(result.group())
f.close()
