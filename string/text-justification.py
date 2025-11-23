class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        data =[]
        curr_cnt = 0
        curr = []
        for word in words:
            
            if curr and curr_cnt + len(word) + len(curr) > maxWidth:
                data.append((curr_cnt, curr))
                curr = [word]
                curr_cnt = len(word)
            else:
                curr.append(word)
                curr_cnt += len(word)

        if curr:
            data.append(curr)

        ans = []
        for i, item in enumerate(data[:-1]):
            total_length, line = item
            num_space = len(line)-1
            remain_width = maxWidth - total_length
            # case: 1 word
            if len(line)==1:
                ans.append(line[0] + ' '*remain_width)
            # case: >1 words
            else:
                num_extra_space = (remain_width // num_space)
                num_remain_space = (remain_width % num_space)
                new_line = []
                for j, word in enumerate(line):
                    word += " "*num_extra_space
                    if num_remain_space > 0:
                        word += " "
                        num_remain_space -= 1

                    new_line.append(word)
                ans.append(''.join(new_line).strip())
        
        # case last line --> add space to end
        ans.append(' '.join(data[-1]))
        ans[-1] += " "*(maxWidth - len(ans[-1]))

        return ans

