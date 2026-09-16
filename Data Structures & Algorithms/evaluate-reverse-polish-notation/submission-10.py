class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        result = None
        for i in tokens:
            if i in ["+", "*", "-", "/"]:
                num1 = nums.pop()
                num2 = nums.pop()
                if i == "+":
                    result = int(num2) + int(num1)
                    nums.append(str(result))
                elif i == "-":
                    result = int(num2) - int(num1)
                   
                    nums.append(str(result))
                elif i == "*":
                    result = int(num2) * int(num1)
                    
                    nums.append(str(result))
                else:
                    result = int(num2) / int(num1)
                    result = int(result)
                    
                    nums.append(str(result))
            else:
                nums.append(i)
        return int(nums[-1])

