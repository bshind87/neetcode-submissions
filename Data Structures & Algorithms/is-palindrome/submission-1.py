class Solution:
    def isPalindrome(self, s: str) -> bool:
        cln = "".join(ch for ch in s.lower() if ch.isalnum())
        #print(cln)
        if cln == cln[::-1]:
            return True
        else:
            return False
        