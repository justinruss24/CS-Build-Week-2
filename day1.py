# Contains duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set from our list
        # compare length of set to length of orig. list
        # if set is shorter, duplicates were removed - return True
        # if list and set are equal length, no dups - return False
        # we can do that all in one line! (so why the five lines of comments?)
        return len(set(nums)) < len(nums)
