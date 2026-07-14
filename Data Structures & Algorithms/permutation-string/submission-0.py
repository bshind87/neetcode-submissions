class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win = len(s1)
        s1d = Counter(s1)
        print(s1d)
        s2d = Counter(s2[:win])
        #print(s2d)
        if s1d == s2d:
            return True
        for i in range(win, len(s2)):
            s2d[s2[i-win]] -= 1
            s2d[s2[i]] = s2d[s2[i]] + 1 if s2[i] in s2 else 1
            print("s2d=", s2d, " i=", i)
            if s1d == s2d:
                return True
        return False


        