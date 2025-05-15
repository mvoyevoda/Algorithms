class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, combo, remainder):
            if len(combo) > k or remainder < 0: return -1
            if len(combo) == k and remainder == 0:
                output.append(combo.copy())
                return
            for num in range(start, 10):
                combo.append(num)
                backtrack(num+1, combo, remainder-num)
                combo.pop()

        output = []
        backtrack(1, [], n)
        return output