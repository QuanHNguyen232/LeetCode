class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            curr_str = []
            if i % 3 == 0:
                curr_str.append("Fizz")
            if i % 5 == 0:
                curr_str.append("Buzz")
            ans.append(''.join(curr_str) if len(curr_str) > 0 else str(i))

        return ans