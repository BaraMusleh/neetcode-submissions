class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = {'{': '}', '[': ']', '(': ')'}

        for i in range(len(s)):
            if s[i] in store:
                stack.append(s[i])
            else:
                if not stack or store[stack[-1]] != s[i]:
                    return False
                stack.pop()
            
        return len(stack) == 0