class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small_str = str1 if len(str1) == min(len(str1), len(str2)) else str2
        large_str = str2 if len(str1) == min(len(str1), len(str2)) else str1
        solution = []
        
        for i in range(1,len(small_str)+1):
            if len(small_str) % i == 0:
                temp = small_str[0:i]
                if temp in large_str:
                    solution.append(temp)
        
        solution = solution[::-1]

        if len(solution) == 0:
            return ""

        for sol in solution:
            diff = len(large_str) // len(sol)
            diff2 = len(small_str) // len(sol)

            if sol * diff == large_str and sol * diff2 == small_str:
                return sol
        
        return ""   

