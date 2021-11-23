import sys


def solve():
    global n, nums

    if n == 1:
        nums.sort()
        print(sum(nums[:5]))

    elif n == 2:
        num_two = get_two_face_min_sum() * 4
        num_three = get_three_face_min_sum() * 4

        print(num_two + num_three)

    else:
        num_one = min(nums) * (pow((n-2), 2) * 5 + (n-2) * 4)
        num_two = get_two_face_min_sum() * ((n-2) * 8 + 4)
        num_three = get_three_face_min_sum() * 4

        print(num_one + num_two + num_three)


def get_two_face_min_sum():
    global nums, A, B, C, D, E, F

    return min(
        nums[A] + nums[B],
        nums[A] + nums[C],
        nums[A] + nums[D],
        nums[A] + nums[E],
        nums[B] + nums[C],
        nums[B] + nums[D],
        nums[B] + nums[F],
        nums[C] + nums[E],
        nums[C] + nums[F],
        nums[D] + nums[E],
        nums[D] + nums[F],
        nums[E] + nums[F]
    )


def get_three_face_min_sum():
    global nums, A, B, C, D, E, F

    return min(
        nums[A] + nums[B] + nums[C],
        nums[A] + nums[B] + nums[D],
        nums[A] + nums[C] + nums[E],
        nums[A] + nums[D] + nums[E],
        nums[B] + nums[C] + nums[F],
        nums[B] + nums[D] + nums[F],
        nums[C] + nums[E] + nums[F],
        nums[D] + nums[E] + nums[F]
    )


A, B, C, D, E, F = 0, 1, 2, 3, 4, 5
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()
# 2
# 1 2 10 11 12 3