class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]

        for i in range(n+1):
            c=0

            while i>0:
                if i&1==1:
                    c+=1
                

                i=i>>1
            arr.append(c)
        
        return arr
        