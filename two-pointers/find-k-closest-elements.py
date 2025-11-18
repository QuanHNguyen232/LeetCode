class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # return self.sln_heap(arr, k, x)
        return self.sln_binary_search(arr, k, x)
    
    def sln_binary_search(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]

    def sln_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        ans = []
        
        for num in arr:
            # add min heap of diff from num to x
            heappush(heap, (abs(num - x), num))
        
        for i in range(k):
            ans.append(heappop(heap)[1])

        ans.sort()
        return ans