# BinarySearch
Binary search implementations

### Problem type 1 ###
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

## Solution in Swift: 
func binarySearch(nums: [Int], in target: Int)-> Int{
    if (nums.count == 0){
        return -1
    }
    
    var left = 0, right = nums.count - 1
    while(left <= right){
        // Prevent (left + right) overflow
        let mid = left + (right - left) / 2
        if(nums[mid] == target){ return mid }
        else if(nums[mid] < target) { left = mid + 1 }
        else { right = mid - 1 }
    }
    
    // End Condition: left > right
    return -1
}
