
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Create a set of numbers
        num_set = set(nums)
        longest_streak = 0

        # Step 2: Iterate through the numbers
        for num in num_set:
            # Step 3: Check if the current number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Step 4: Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Step 5: Update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak