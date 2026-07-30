class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # mini = float('inf')
        # res = []
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i] == list2[j]:
        #             if i + j < mini:

        #                 mini = i+j
        #                 res = [list1[i]]

        #             elif i + j == mini:
        #                 res.append(list1[i])

        # return res                
        mini = float('inf')
        common = {}
        res = []
        for i in range(len(list1)):
            common[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in common:
                indexSum = common[list2[j]] + j

                if indexSum < mini:
                    mini = indexSum
                    res = [list2[j]]

                elif indexSum == mini:
                    res.append(list2[j]) 

        return res                   

        
        