from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        len_buildings = len(buildings)

        if len_buildings == 0:
            return []
        if len_buildings == 1:
            building_start, building_end, building_height = buildings[0]
            return [[building_start, building_height], [building_end, 0]]

        left_skyline = self.getSkyline(buildings[:len_buildings // 2])
        right_skyline = self.getSkyline(buildings[len_buildings // 2:])

        result = self.merge_building(left_skyline, right_skyline)
        return result

    def merge_building(self, left: List[List], right: List[List]) -> List[List]:
        point_l = point_r = 0
        result = []
        current_l = current_r = 0

        while point_l < len(left) and point_r < len(right):
            left_x, left_h = left[point_l]
            right_x, right_h = right[point_r]

            if left_x < right_x:
                # 当前的点为左边大楼的点
                if (left_h > current_l and left_h > current_r) or (current_r <= left_h < current_l):
                    result.append([left_x, left_h])
                # left下降的趋势被right挡住了
                elif left_h < current_r < current_l:
                    result.append([left_x, current_r])
                current_l = left_h
                point_l += 1
            elif left_x > right_x:
                # 当前的点为右边大楼的点
                if (right_h > current_l and right_h > current_r) or (current_l <= right_h < current_r):
                    result.append([right_x, right_h])
                elif right_h < current_l < current_r:
                    result.append([right_x, current_l])
                current_r = right_h
                point_r += 1
            if left_x == right_x:
                left_dh = left_h - current_l
                right_dh = right_h - current_r

                if left_dh + right_dh != 0:
                    if left_dh > right_dh:
                        result.append([left_x, left_h])
                    else:
                        result.append([left_x, right_h])
                current_l = left_h
                current_r = right_h
                point_l += 1
                point_r += 1

        while point_l < len(left):
            result.append(left[point_l])
            point_l += 1

        while point_r < len(right):
            result.append(right[point_r])
            point_r += 1

        return result

if __name__ == '__main__':

    buildings_1 = [
        [2, 9, 10],
        [3, 7, 15],
        [5, 12, 12],
        [15, 20, 10],
        [19, 24, 8]
    ]
    buildings_2 = [
        [0, 2, 3],
        [2, 5, 3]
    ]
    buildings_3 = [
        [1, 2, 1],
        [1, 2, 2],
        [1, 2, 3]
    ]
    buildings_4 = [
        [3, 7, 8],
        [3, 8, 7],
        [3, 9, 6],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 3],
        [3, 13,  2],
        [3, 14, 1]
    ]

    sln = Solution()
    skyline = sln.getSkyline(buildings_4)
    print(skyline)
