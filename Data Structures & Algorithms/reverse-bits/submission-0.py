class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = f"{n:032b}"
        reversed_str = binary_str[::-1]
        return int(reversed_str, 2)
        