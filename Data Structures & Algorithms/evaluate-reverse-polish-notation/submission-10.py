class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                match t:
                    case "+":
                        res = num1 + num2
                    case "-":
                        res = num1 - num2
                    case "*":
                        res = num1 * num2
                    case "/":
                        res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()
