def countChars(strs):
    chars = {}
    for char in strs:
        if char in chars:
           chars[char] +=1
        else:
            chars[char] = 1
        return chars
st = input()
strSort = sorted(list(st))
chars = countChars(strSort)

for char, count in countChars(strSort).items():
         print(f"{char}: {count}")