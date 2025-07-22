from typing import List

class Solution:
    @staticmethod
    def three_sum_triple_loop(nums: List[int]) -> List[List[int]]:
        """
        通过三重循环找出所有和为0的三元组（暴力解法）

        :param nums: 输入的整数列表
        :return: 包含所有和为0且不重复的三元组的列表
        """
        # 对列表进行排序
        nums.sort()
        # 存储符合条件的结果
        results = []
        # 如果元素个数小于3，无法找到三元组，直接返回空列表
        if len(nums) < 3:
            return results
        # 若唯一一组满足条件，直接加入结果
        elif len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                results.append([nums[0], nums[1], nums[2]])
        else:
            # 遍历数组中的每一个元素作为第一个数
            for i in range(len(nums)):
                # 从当前元素的下一个元素开始遍历作为第二个数
                for j in range(i+1, len(nums)):
                    # 从第二个数的下一个元素开始遍历作为第三个数
                    for k in range(j+1, len(nums)):
                        # 判断三数之和是否为0
                        if nums[i] + nums[j] + nums[k] == 0:
                            result = [nums[i], nums[j], nums[k]]
                            # 去重
                            if result not in results: results.append(result)

        return results

    @staticmethod
    def three_sum_two_points(nums: List[int]) -> List[List[int]]:
        """
        使用双指针法找出所有和为0的三元组

        :param nums: 输入的整数列表
        :return: 包含所有和为0且不重复的三元组的列表
        """
        # 对列表进行排序
        nums.sort()
        # 存储符合条件的结果
        results = []
        # 如果元素个数小于3，无法找到三元组，直接返回空列表
        if len(nums) < 3:
            return results
        # 若唯一一组满足条件，直接加入结果
        elif len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                results.append([nums[0], nums[1], nums[2]])
        else:
            for i in range(len(nums)):
                # 跳过重复值
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                # 左指针初始化为当前元素的下一个位置
                left = i + 1
                # 右指针初始化为数组末尾
                right = len(nums) - 1

                while left < right:
                    # 计算三数之和
                    total = nums[left] + nums[right] + nums[i]
                    # 如果和为0
                    if total == 0:
                        result = [nums[i], nums[left], nums[right]]
                        # 将结果加入列表
                        results.append(result)

                        # 跳过重复值
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # 移动左指针
                        left += 1
                        # 移动右指针
                        right -= 1
                    # 如果和大于0，右指针左移
                    elif total > 0:
                        right -= 1
                    # 如果和小于0，左指针右移
                    else:
                        left += 1
        # 返回所有符合条件的三元组
        return results


def test(func):
    # 标准输入
    assert func([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]) == [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]
    # 全为 0
    assert func([0, 0, 0]) == [[0, 0, 0]]
    # 无解的情况
    assert func([1, 2, 3]) == []
    # 数组长度不足
    assert func([1, 2]) == []
    # 包含重复解
    assert func([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]) == [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    print("所有测试通过！")

if __name__ == "__main__":
    # test(Solution.three_sum_triple_loop)
    test(Solution.three_sum_two_points)