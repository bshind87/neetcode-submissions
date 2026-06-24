class Solution:
    def reverse(self, x: int) -> int:
        max_sign = (1 << 31) - 1
        neg = True if x < 0 else False
        num = abs(x)
        y = str(num)[::-1]
        print(int(y))
        if int(y) > max_sign:
            return 0
        else:
            return -1 * int(y) if neg else int(y)