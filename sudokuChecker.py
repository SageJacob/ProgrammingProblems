class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for row in range(9)]
        columns = [set() for column in range(9)]
        boxes = [[set() for boxes in range(3)] for layers in range(3)]
        for row in range(len(board)):
            for column in range(len(board[0])):
                number = board[row][column]
                if number == '.': continue
                if number in rows[row] or number in columns[column] or number in boxes[row//3]                   [column//3]: return False
                rows[row].add(number)
                columns[column].add(number)
                boxes[row//3][column//3].add(number)
        return True
                    