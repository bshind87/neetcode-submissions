class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            n = len(s)
            ret += str(n) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            slen = int(s[i:j])
            start_str = j + 1
            end_str = start_str + slen
            cur_str = s[start_str:end_str]
            ret.append(cur_str)
            i = end_str
        return ret
