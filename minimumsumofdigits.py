class Solution:
    def minimumSum(self, num: int) -> int:
         new_arr = []
         number1 = ""
         number2 = ""
         sum = 0
         num_str = str(num)
         for digit in num_str:
            new_arr.append(digit)
         new_arr.sort()
         number1 += new_arr[0]
         number1 += new_arr[2]
         number2 += new_arr[1] 
         number2 += new_arr[3]
         sum = int(number1) + int(number2)
         return sum
        