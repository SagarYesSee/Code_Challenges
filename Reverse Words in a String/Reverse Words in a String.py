class Solution:
    def reverseWords(self, s: str) -> str:
        arr = str()
        for i in s.split():
            word = i
            arr += ' '+word[::-1]
        return arr.strip()

s = "the input string"
sol = Solution()
print(sol.reverseWords(s))