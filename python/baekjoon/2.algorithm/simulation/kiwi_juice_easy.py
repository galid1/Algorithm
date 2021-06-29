# top coder KiwiJuiceEasy srm 478

class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, fromId, toId):
        new_bottles = list(bottles)

        for i in range(len(fromId)):
            from_num = fromId[i]
            to_num = toId[i]

            move_mount = min(new_bottles[from_num], capacities[to_num] - new_bottles[to_num])

            new_bottles[from_num] -= move_mount
            new_bottles[to_num] += move_mount

        return new_bottles

capacities = (30, 20, 10)
bottles = (10, 5, 5)
fromId = (0, 1, 2)
toId = (1, 2, 0)
k = KiwiJuiceEasy()
print(k.thePouring(capacities, bottles, fromId, toId))