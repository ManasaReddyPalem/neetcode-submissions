from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Empty cells are represented by "." and can be skipped
                if val == ".":
                    continue

                # Check if the number already exists in current row, column, or 3x3 box
                box_key = (r // 3, c // 3)
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_key]):
                    return False

                # Record the number in the sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True