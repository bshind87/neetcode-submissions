class Solution:
    def isPalindrome(self, s: str) -> bool:
        #c = (s.replace(" ", "")).lower()
        c = "".join(ch for ch in s.lower() if ch.isalnum())
        if c == c[::-1]:
            return True
        else:
            return False
        