class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answers = dict()
        for i, n in enumerate(numbers):
            if n in answers:
                return [answers[n], i + 1]
            else:
                diff = target - n
                answers[diff] = i + 1
            

