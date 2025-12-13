class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nrows = len(image)
        ncols = len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        start_color = image[sr][sc]
        visited = set()

        def isInBound(r, c):
            return (0 <= r < nrows) and (0 <= c < ncols)

        def dfs(r, c) -> None:
            # base
            if (r, c) in visited: return
            visited.add((r, c))
            
            # do sth
            image[r][c] = color
            
            # recursion
            for mr, mc in directions:
                new_r, new_c = r+mr, c+mc
                if (
                    isInBound(new_r, new_c)
                    and (new_r, new_c) not in visited
                    and image[new_r][new_c] == start_color
                ):
                    dfs(new_r, new_c)

        dfs(sr, sc)
        return image