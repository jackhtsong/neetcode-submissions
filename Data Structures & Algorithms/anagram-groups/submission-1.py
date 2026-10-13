class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for current in strs:
            key = "".join(sorted(current))
            if key in hashTable:
                hashTable[key].append(current)
            else:
                hashTable[key] = [current]

        solution = []
        for key in hashTable.keys():
            solution.append(hashTable[key])
        return solution

