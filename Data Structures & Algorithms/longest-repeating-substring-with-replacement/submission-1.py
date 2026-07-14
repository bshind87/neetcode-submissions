class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        #for ch in s:
        #    pd[ch] = pd[ch] + 1 if ch in pd else 1
        
        res = 0
        left = 0
        for ch in s:
            #d = pd
            #print(ch)
            
            d[ch] = d[ch] + 1 if ch in d else 1
            mx = max(d.values())
            sm = sum(d.values())
            while sm - k > mx:
                d[s[left]] -= 1
                left += 1
                mx = max(d.values())
                sm = sum(d.values())
            res = max(res, sum(d.values()))
            print(mx, " ", sm)
        print(d, " ", mx, " ", sm, " ", res)
        return res

        



        