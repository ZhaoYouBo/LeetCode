from typing import List

class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        """
        寻找数组中两个数的和等于目标值 target，并返回它们的索引。

        :param nums: 整数列表，表示待查找的数组
        :param target: 整数，表示目标和
        :return: 包含两个索引的列表，这两个数的和等于目标值；如果没有符合条件的数对，返回空列表
        """
        for i in range(len(nums)): # 外层循环遍历数组中的每一个元素
            for j in range(i+1, len(nums)): # 内层循环从当前元素的下一个元素开始遍历
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

def test():
    assert Solution.two_sum([2,7,11,15], 9) == [0,1] # 标准情况
    assert Solution.two_sum([-1, -2, -3, -4], -7) == [2,3] # 包含负数
    assert Solution.two_sum([3, 2, 4, 3], 6) in [[0,3], [2,1]] # 多个解，只需要返回一个
    assert Solution.two_sum([1, 2, 3], 10) == [] # 无解的情况
    assert Solution.two_sum([5, 5], 10) == [0,1] # 只有两个元素的情况
    assert Solution.two_sum([], 0) == [] # 边界情况，空列表或只有一个元素
    assert Solution.two_sum([1], 1) == []

    print("所有测试通过！")

if __name__ == "__main__":
    test()