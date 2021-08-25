class Solution:
    def canCompleteCircuit(self, gas, cost):
        subs, subs_sum = [], 0
        for n1, n2 in zip(gas, cost):
            sub = n1 - n2
            subs.append(sub)
            subs_sum += sub

        if subs_sum < 0:
            return -1

        ans_idx = 0
        cur_fuel = 0
        for idx, sub in enumerate(subs):
            if cur_fuel + sub < 0:
                ans_idx = idx+1
                cur_fuel = 0
            else:
                cur_fuel += sub

        return ans_idx

    # O(N^2)
    # def canCompleteCircuit(self, gas, cos):
        # subs = []
        # for n1, n2 in zip(gas, cost):
        #     subs.append(n1-n2)
        #
        # for i in range(len(subs)):
        #     can = True
        #     sums = 0
        #     for j in range(len(subs)):
        #         sums += subs[(i+j)%len(subs)]
        #         if sums < 0:
        #             can = False
        #             break
        #
        #     if can:
        #         return i
        #
        # return -1


s = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))
