def maior_ponta(nums):
  if nums[0] >= nums [-1] :
    m = nums[0]
    for i in range(0,len(nums)) :
      nums[i] = m
    return nums
  if nums[-1] >= nums [0] :
    m = nums[-1]
    for i in range(0,len(nums)) :
      nums[i] = m
    return nums