class Solution:
    def judgeCircle(self, moves: str) -> bool:
        stack = []
        for move in list(moves):
            stack.append(move)

            while len(stack) >= 2:
                prev_move, move = stack[-2], stack[-1]
                if (prev_move == "D" and move == "U"
                    or prev_move == "U" and move == "D"
                    or prev_move == "L" and move == "R"
                    or prev_move == "R" and move == "L"
                ):
                    stack.pop()
                    stack.pop()
                else:
                    break

        
        return len(stack)==0