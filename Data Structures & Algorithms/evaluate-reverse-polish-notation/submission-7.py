class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.replace("-", "").isnumeric():
                t = int(t)
                stack.append(t)
            else:
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
                print(f"{num1} {t} {num2} = {res}")
                stack.append(res)
        return stack.pop()
