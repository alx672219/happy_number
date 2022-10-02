class Solution:
    def isHappy(self, n: int) -> bool:
        dictionary = set()
        while not(n in dictionary):   # if it is a loop then, it never reaches 1. 
            dictionary.add(n)
            string = str(n)
            c = 0
            for i in string:       # each digit ** 2
                c += int(i) ** 2   # add 
            n = c

            if n == 1:   # happy number
                return True
        return False