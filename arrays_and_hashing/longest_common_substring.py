def longestCommonSubsequence(text1: str, text2: str) -> int:

    if len(text1) >= len(text2):
        s = text1
        t = text2
    else:
        s = text2
        t = text1

    race = [0 for _ in range(len(t))]
    counters = [i for i in range(len(t))]


    for i in range(len(s)):
        for j in range(len(counters)):
            if counters[j] == len(counters):
                continue
            if s[i] == t[counters[j]]:
                race[j] +=1
                counters[j] +=1

    return max(race)

text1 = "ezupkr"
text2 = "ubmrapg"
print(longestCommonSubsequence(text1,text2))