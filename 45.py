class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        jumps = 0
        i = 0
        while i < len(nums):
            jump_limit = nums[i]
            if i + jump_limit >= len(nums)-1:
                return jumps+1

            best_option = (0, -1)
            for j in range(i+1, i+jump_limit+1):
                if j+nums[j] >= best[0]:
                    best = (j+nums[j], j)
            best_jump = best_option[1]
            i = best_jump if best_jump > 0 else i+1

            jumps += 1


        return jumps