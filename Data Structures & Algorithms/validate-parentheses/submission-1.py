class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ['(', '{', '[']:
                st.append(c)
            elif c in [')', '}', ']'] and len(st) > 0:
                p = st.pop()
                if p+c not in ['[]', '()', '{}']:
                    return False
            else:
                return False
        if len(st) > 0:
            return False
        return True
                

        