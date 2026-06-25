class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                num1 = st.pop()
                num2 = st.pop()
                if t == '+':
                    res = int(num1) + int(num2)
                elif t == '-':
                    res = int(num2) - int(num1)
                elif t == '*':
                    res = int(num2) * int(num1)
                elif t == '/':
                    res = int(num2) / int(num1)
                st.append(res)
            else:
                st.append(t)
        return int(st[0])

        