from typing import List

class Solution():
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

    def letterCombinations(self, digits: str) -> List[str]:
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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''Given two sorted arrays nums1 and nums2 of size m and n respectively,
        return the median of the two sorted arrays.'''

        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2
        else:
            return nums1[len(nums1)//2]

    def plusOne(self, digits: List[int]) -> List[int]:
        '''Given a non-empty array of decimal digits representing a non-negative integer, 
        increment one to the integer. The digits are stored such that the most significant 
        digit is at the head of the list, and each element in the array contains a single 
        digit. You may assume the integer does not contain any leading zero, except the 
        number 0 itself.'''
        return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]

    def permute(self, nums: List[int]) -> List[List[int]]:
        '''Given an array nums of distinct integers, return all the possible permutations. 
        You can return the answer in any order.'''
        if len(nums) == 1:
            return [nums]
        else:
            return [[i] + j for i in nums for j in self.permute([x for x in nums if x != i])]