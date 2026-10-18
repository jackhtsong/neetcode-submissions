class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(":")",
            "{":"}",
            "[":"]"}
        opens = {"(", "{", "["}
        closes = {")", "}", "]"}
        for c in s:
            if c in opens:
                stack.append(c)
                continue
            elif c in closes:
                if len(stack) == 0:
                    return False
                elif pairs[stack.pop()] != c:
                    return False
        if len(stack) == 0:
            return True
        return False
            