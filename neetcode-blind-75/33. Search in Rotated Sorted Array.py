class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 1
            if (target == nums[mid]):
                return mid
            
            # if the first half is sorted
            if(nums[mid] > nums[l]):
                if(target > nums[mid] or target < nums[l]):
                    l = mid + 1
                else:
                    r = mid - 1
            
            #if the second half is sorted
            else:
                if(target < nums[mid] or target > nums[r]):
                    r = mid - 1
                else: 
                    l = mid + 1
        return -1