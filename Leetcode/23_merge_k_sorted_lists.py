from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        string = ''
        p = self
        while p is not None:
            string += str(p.val) + '\n'
            p = p.next
        return string


# 我的解法1
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if not lists:
#             return None
#
#         hashmap = {}
#         for i in range(len(lists)):
#             if lists[i] is not None:
#                 hashmap[str(i)] = lists[i].val
#                 lists[i] = lists[i].next
#
#         result = None
#         tail_p = result
#         while len(hashmap.keys()) > 0:
#             min_pos = int(list(hashmap.keys())[0])
#             min_val = hashmap.get(str(min_pos))
#             for key in hashmap.keys():
#                 if hashmap.get(key) < min_val:
#                     min_val = hashmap.get(key)
#                     min_pos = int(key)
#             if result is None:
#                 result = ListNode(min_val)
#                 result.next = None
#                 tail_p = result
#             else:
#                 tail_p.next = ListNode(min_val)
#                 tail_p.next.next = None
#                 tail_p = tail_p.next
#             hashmap.pop(str(min_pos))
#
#             if lists[min_pos] is not None:
#                 hashmap[str(min_pos)] = lists[min_pos].val
#                 lists[min_pos] = lists[min_pos].next
#
#         return result

# 我的解法2
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#
#         index = len(lists) - 1
#         while index >= 0:
#             if lists[index] is None:
#                 lists.pop(index)
#             index -= 1
#
#         if not lists:
#             return None
#
#         result = None
#         p = result
#
#         while True:
#             if not lists:
#                 break
#
#             min_pos = 0
#             min_val = lists[0].val
#
#             for i in range(len(lists)):
#                 if lists[i] is not None and lists[i].val < min_val:
#                     min_pos = i
#                     min_val = lists[i].val
#
#             if result is None:
#                 result = ListNode(min_val)
#                 result.next = None
#                 p = result
#             else:
#                 p.next = ListNode(min_val)
#                 p.next.next = None
#                 p = p.next
#
#             lists[min_pos] = lists[min_pos].next
#             if lists[min_pos] is None:
#                 lists.remove(lists[min_pos])
#
#         return result

# 暴力法 时间复杂度O(NlogN) N为节点总个数
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         result = []
#
#         for listnode in lists:
#             while listnode:
#                 result.append(listnode.val)
#                 listnode = listnode.next
#
#         if not result:
#             return None
#
#         sorted_result = sorted(result)
#         head = ListNode(sorted_result[0])
#         p = head
#         for node in sorted_result[1:]:
#             p.next = ListNode(node)
#             p = p.next
#
#         return head

# 分治法 时间复杂度 O(Nlogk) n为节点总个数，k为链表个数
class Solution:
    def merge2Lists(self, listl, listr):
        pl = listl
        pr = listr
        result = ListNode(0)
        p = result

        while pl is not None and pr is not None:
            if pl.val < pr.val:
                p.next = ListNode(pl.val)
                p = p.next
                pl = pl.next
            else:
                p.next = ListNode(pr.val)
                p = p.next
                pr = pr.next

        while pl is not None:
            p.next = ListNode(pl.val)
            p = p.next
            pl = pl.next

        while pr is not None:
            p.next = ListNode(pr.val)
            p = p.next
            pr = pr.next

        return result.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        len_list = len(lists)
        interval = 1

        while interval < len_list:
            for i in range(0, len_list - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        if not lists:
            return None
        else:
            return lists[0]


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    list3 = ListNode(2)
    list3.next = ListNode(6)

    listnodes1 = [None]
    listnodes2 = [None, list3]
    listnodes3 = [list1, list2, list3]
    listnodes4 = []
    # print(len(listnodes))

    sln = Solution()
    res = sln.mergeKLists(listnodes2)
    print(res)
