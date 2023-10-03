def isAnagram(String1, String2):
    if sorted(String1) == sorted(String2):
        return True
    else:
        return False

print(isAnagram("listen", "silent"))
print(isAnagram("triangle", "integral"))
print(isAnagram("cat", "dog"))
print(isAnagram("earth", "heart"))
print(isAnagram("bruh", "lmao"))