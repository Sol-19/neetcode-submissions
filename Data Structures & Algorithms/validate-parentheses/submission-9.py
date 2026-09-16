class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(", "]":"[", "}":"{"}
        for key in s:
            if key in pair.values():
                stack.append(key)
            elif not stack and key in pair.keys():
                return False
            elif stack[-1] == pair[key]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
            