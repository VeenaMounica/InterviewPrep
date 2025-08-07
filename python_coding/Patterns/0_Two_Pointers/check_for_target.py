def check_for_target(nums, target):
    sorted_nums = sorted(nums)
    left = 0
    right = len(sorted_nums)-1

    while left<right:
        current = sorted_nums[left] + sorted_nums[right]
        if current==target:
            print(f"{sorted_nums[left]} and {sorted_nums[right]} are the pair with target sum {target}")
            return True
        elif current < target:
            left += 1
        else:
            right -= 1
    print(f"Couldn't find the target {target} sum pair in {nums}")
    return False

check_for_target([1, 2, 6, 8, 4, 9, 14, 15], 13)

