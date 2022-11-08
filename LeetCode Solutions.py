

class Solution:
    def reverseVowels(self, s: str) -> str:
        '''Given a string s, reverse only all the vowels in the string 
        and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and
        they can appear in both lower and upper cases, more than once.'''

        vowels = {'a','e','i','o','u'}

        word = {i for i in s if i}
        vowels = [[i,letter] for i, letter in enumerate(s) if letter.lower() in vowels]
        reversed_index = [i[0] for i in vowels][::-1]
        
        for i in enumerate(vowels):
            word[reversed_index[i[0]]] = i[1][1]
        return ''.join(word)    

    def letterCombinations(self, digits: str) -> list[str]:
        '''Given a string containing digits from 2-9 inclusive, return all 
        possible letter combinations that the number could represent. Return 
        the answer in any order.'''
        if not digits:
            return []
        letters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        combinations = ['']
        for digit in digits:
            combinations = [i+j for i in combinations for j in letters[digit]]
        return combinations
    
    def myPow(self, x: float, n: int) -> float:
        '''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).'''
        return x**n



