

class Solution:
    def myAtoi(self, str: str) -> int:
        if str=="":
            return 0
        i=0
        length=len(str)
        num=""
        sign=False
        while i<length:
            if str[i]==' ' and num=="":
                i=i+1
                continue
            elif sign==False and (str[i]=='+' or str[i]=='-'):
                sign=True
                num=num+str[i]
            elif ord(str[i])>ord('0')-1 and ord(str[i])<ord('9')+1:
                sign=True
                num = num + str[i]
            else:
                if num=="":
                    return  0
                else:
                    break

            i=i+1
        digit=0
        length=len(num)
        i = length-1
        po=pow(10,i)
        while i>-1:
            if num[i]=='+':
                break
            elif num[i] =='-':
                digit=-1*digit
            else:
                digit=digit+int(num[i])*pow(10,length-1-i)
            i=i-1
        if digit<-pow(2,31):
            digit=-pow(2,31)
        elif digit>pow(2,31)-1:
            digit=pow(2,31)-1
        return digit
    def myAtoi2(self, str: str) -> int:
        if str=="":
            return 0
        i=0
        length=len(str)
        num=""
        state='s'
        while i<length:
            if state=='s':
                if str[i]==' ':
                    i = i + 1
                    continue
                elif str[i]=='+' or str[i]=='-' or (ord(str[i])>ord('0')-1 and ord(str[i])<ord('9')+1):
                    num=num+str[i]
                    i = i + 1
                    state='n'
                    continue
                else:
                    return 0
            elif state=='n':
                if ord(str[i])>ord('0')-1 and ord(str[i])<ord('9')+1:
                    num=num+str[i]
                    i = i + 1
                else:
                    break

        digit=0
        length=len(num)
        i = length-1
        po=pow(10,i)
        while i>-1:
            if num[i]=='+':
                break
            elif num[i] =='-':
                digit=-1*digit
            else:
                digit=digit+int(num[i])*pow(10,length-1-i)
            i=i-1
        if digit<-pow(2,31):
            digit=-pow(2,31)
        elif digit>pow(2,31)-1:
            digit=pow(2,31)-1
        return digit


s=Solution()
st="+-1"
result=s.myAtoi2(st)
print(result)
