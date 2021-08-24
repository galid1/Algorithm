class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda person: (-person[0], person[1]))

        ans = []
        for person in people:
            ans.insert(person[1], person)

        return ans


s = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(s.reconstructQueue(people))
