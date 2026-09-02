class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # Check the row
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    if num in sub_boxes[i // 3][j // 3]:
                        return False
                    sub_boxes[i // 3][j // 3].add(num)
        return True