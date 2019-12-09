class ListNode:
    def __init__(self, x, next_node):
        self.val = x
        self.next = next_node

    def __str__(self):
        res_str = ''
        p = self
        while p is not None:
            res_str += str(p.val) + '\n'
            p = p.next

        return res_str

class Solution:
    # 其实题目是移除倒数第n个节点
    # 时间复杂度O(n)，空间复杂度O(1)，n为链表长度
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        nth_before = head
        p = head
        index = 1
        while p is not None:
            if index > n+1:
                nth_before = nth_before.next
            p = p.next
            index += 1

        if index - 1 > n:
            nth_before.next = nth_before.next.next
        elif index - 1 == n:
            head = nth_before.next
        else:
            return None

        return head

if __name__ == '__main__':
    list_head_1 = None
    list_head_2 = ListNode(1, None)
    list_head_3 = ListNode(1, ListNode(2, None))
    list_head_4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

    print(list_head_4)
    sln = Solution()
    res = sln.removeNthFromEnd(list_head_4, 5)
    print(res)
