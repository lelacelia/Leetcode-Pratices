class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_rec = {}
        j = 0 
        max_fruits = 0

        for i in range(len(fruits)):
            fruit_type = fruits[i]

            fruit_rec[fruit_type] = fruit_rec.get(fruit_type, 0) + 1

            while len(fruit_rec) > 2:
                left_fruit = fruits[j]

                fruit_rec[left_fruit] -= 1

                if fruit_rec[left_fruit] == 0:
                    del fruit_rec[left_fruit]
                
                j += 1
            max_fruits = max(max_fruits, i-j+1)
    
        return max_fruits

        
        

