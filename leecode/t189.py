nums = [1, 2, 3, 4,5,6,7,8,9,10]
k = 5
cnt = len(nums)
k = k % cnt


def reverse(start, end):
    last = end
    for i in range(start, end):
        if i < last:
            tmp = nums[i]
            nums[i] = nums[last]
            nums[last] = tmp
            last -= 1
        else:
            break
    #print(nums)


def rotate():
    #先转前半部分
    reverse(0, cnt - 1 - k)
    #再转后半部分
    reverse(cnt - k, cnt - 1)
    #全体转
    reverse(0, cnt - 1)


rotate()
print(nums)