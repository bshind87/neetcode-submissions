class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        req = Counter(t)
        required = len(req)
        cur = {}
        formed = 0
        
        left = 0
        best_len = float('inf')
        best_left, best_right = 0, 0
        
        for right, ch in enumerate(s):
            if ch in req:
                cur[ch] = cur.get(ch, 0) + 1
                if cur[ch] == req[ch]:
                    formed += 1
            
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left, best_right = left, right
                
                left_ch = s[left]
                if left_ch in req:
                    cur[left_ch] -= 1
                    if cur[left_ch] < req[left_ch]:
                        formed -= 1
                left += 1
        return "" if best_len == float('inf') else s[best_left:best_right + 1]