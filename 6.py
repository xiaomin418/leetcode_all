

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if numRows==1:
            return s
        matrix = [[0 for i in range((numRows-1) * int(length / (2*numRows -2)) + numRows-1)] for j in range(numRows)]
        for k in range(1,length+1):
            if k%(2*numRows-2)>0 and k%(2*numRows-2)<numRows+1:
                # print(k,"index1",(numRows-1)*int(k/(2*numRows-2)),k%(2*numRows-2)-1)
                matrix[k%(2*numRows-2)-1][(numRows-1)*int(k/(2*numRows-2))]=s[k-1]
            elif k%(2*numRows-2)==0:
                # print(k, "index2", 1,(numRows - 1) * int(k / (2 * numRows - 2))  - 1)
                matrix[1][(numRows - 1) * int(k / (2 * numRows - 2)) - 1] = s[k - 1]
            else:
                # print(k,"index3",(numRows-1)-(k%(2*numRows-2)-numRows),(numRows-1)*int(k/(2*numRows-2))+(k%(2*numRows-2)-numRows)-1)
                matrix[(numRows-1)-(k%(2*numRows-2)-numRows)][(numRows-1)*int(k/(2*numRows-2))+(k%(2*numRows-2)-numRows)]=s[k-1]
        reorder=""
        for i in range(numRows):
            for j in range((numRows-1) * int(length / (2*numRows -2)) + numRows-1):
                if matrix[i][j] != 0:
                    reorder = reorder + matrix[i][j]
        return reorder

    def convert2(self, s: str, numRows: int) -> str:
        # No need to calculate if 1 row or more rows than characters
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]

        i = 0
        walkback = False
        for c in s:
            print("c",c)
            if walkback and i == 0:
                # Done walking back if we hit 0!
                walkback = False
            if i % numRows == 0 and i != 0:
                # We hit the end! Move backwards twice to
                # offset for incorrectly moving forward at
                # the end of the last iteration
                i -= 2

                # Don't walk back if we hit 0! (Only needed)
                # in the case that numRows == 2)
                walkback = (i != 0)

            rows[i] += c
            i += -1 if walkback else 1

        return "".join(rows)

    def convert3(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        cur_row, step = 0, 1
        nums = [''] * numRows
        for i in s:
            nums[cur_row] += i
            if cur_row == numRows - 1:
                step = -1
            if cur_row == 0:
                step = 1
            cur_row += step
        return ''.join(nums)



ex="LEETCODEISHIRING"
s=Solution()
result=s.convert3(ex,3)
print(result)