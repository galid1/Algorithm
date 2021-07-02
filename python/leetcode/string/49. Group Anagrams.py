def groupAnagrams(strs):
    ans = {}
    for s in strs:
        sorted_s = ''.join(sorted(list(s)))

        if sorted_s in ans.keys():
            ans[sorted_s].append(s)
        else:
            ans[sorted_s] = [s]

    return list(ans.values())


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)
# [["bat"],["nat","tan"],["ate","eat","tea"]]