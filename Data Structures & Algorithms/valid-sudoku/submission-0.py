class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCols = [set() for _ in range(9)]
        seenBoxes = [set() for _ in range(9)]
        for row, arr in enumerate(board): 
            seenRows = set()
            for col, num in enumerate(arr):
                if num == '.':
                    continue

                if num in seenRows:
                    return False
                seenRows.add(num)

                if num in seenCols[col]:
                    return False
                seenCols[col].add(num)

                boxIndex = row // 3 * 3 + col // 3
                if num in seenBoxes[boxIndex]:
                    return False
                seenBoxes[boxIndex].add(num)

        return True

