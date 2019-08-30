
class Solution(object):
    def isOneBitCharacter2(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits)==1:
            if bits[0]==0:
                return True
            else:
                return False
        elif len(bits)==2:
            if bits[0]==0 and bits[1]==0:
                return True
            else:
                return False
        else:
            if bits[0]==0:
                return self.isOneBitCharacter(bits[1:])
            else:
                return self.isOneBitCharacter(bits[2:])
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length=len(bits)
        i=0
        while i<length:
            if i<length-2:
                if bits[i]==0:
                    i=i+1
                else:
                    i=i+2
            elif i==length-1:
                if bits[i]==0:
                    return True
                else:
                    return False
            elif i==length-2:
                if bits[i]==0 and bits[i+1]==0:
                    return True
                else:
                    return False

bits=[1,0,0,1,0]
s=Solution()
if s.isOneBitCharacter(bits):
    print("True")
else:
    print("False")


