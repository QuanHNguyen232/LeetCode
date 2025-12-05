class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # similar to convert decimal to binary or other bases
        res = []
        ALPHABET_LEN = 26
        def num_to_char(num: int):
            return chr(num + ord("A"))
        
        while columnNumber > 0:
            # columnNumber-1 since need to shift by 1: A=0, ..., Z=25
            curr_num = (columnNumber-1) % ALPHABET_LEN
            res.append(num_to_char(curr_num))
            columnNumber = (columnNumber-1) // ALPHABET_LEN

        return ''.join(res[::-1])