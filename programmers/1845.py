
def solution(nums):
    pon_dict = {}
    for num in nums:
        pon_dict[num] = 1
    
    return min(len(nums) // 2, len(pon_dict))
