'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
# -*- coding:utf-8 -*-

def twoSum(nums,target):
    hashmap={}
    for i,n in enumerate(nums):
        if target-n in hashmap:
            return [hashmap[target-n],i]
        hashmap[n]=i

if __name__=='__main__':
    nums=[2,7,11,15]
    target=9
    print(twoSum(nums,target))