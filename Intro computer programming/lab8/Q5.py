def LCS(s1,s2):
    len1, len2 = len(s1), len(s2)
    res = ""
    
    for i in range(len1):
        for j in range(len2):
            k = 0
            while (i + k < len1) and (j + k < len2) and (s1[i + k] == s2[j + k]):
                k += 1
            if k > len(res):
                res = s1[i:i + k]
    
    return res

print(LCS("Ingenious", "intelligent"))
print(LCS("intelligent", "inconsidered"))
print(LCS("russian", "ukranian"))
print(LCS("war", "love"))
print(LCS("romanian", "roman"))
print(LCS("philosophically", "zoophilous"))

        