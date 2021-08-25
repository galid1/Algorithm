class Solution:
    def canCompleteCircuit(self, gas, cost):
        subs = []
        for n1, n2 in zip(gas, cost):
            subs.append(n1-n2)

        for i in range(len(subs)):
            can = True
            sums = 0
            for j in range(len(subs)):
                sums += subs[(i+j)%len(subs)]
                if sums < 0:
                    can = False
                    break

            if can:
                return i

        return -1


s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))
