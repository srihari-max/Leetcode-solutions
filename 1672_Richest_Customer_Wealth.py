class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        res=[]
        for i in range(len(accounts)):
            c=0
            for j in range(len(accounts[i])):
                c+=accounts[i][j]
            res.append(c)
        return max(res)
            