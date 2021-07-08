def productExceptSelf(nums):
    except_i = [1 for _ in range(len(nums))]
    acc_mul = 1
    for i in range(0, len(nums)-1):
        acc_mul *= nums[i]
        except_i[i+1] = acc_mul

    acc_mul = 1
    for i in range(len(nums)-1, 0, -1):
        acc_mul *= nums[i]
        except_i[i-1] *= acc_mul

    return except_i


nums = [1,2,3,4]
productExceptSelf(nums)