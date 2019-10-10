# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show(self):
        ptr = self
        while ptr is not None:
            print(str(ptr.val), end='')
            ptr = ptr.next
        print()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr = l1
        list_l1 = ''
        while ptr is not None:
            list_l1 += str(ptr.val)
            ptr = ptr.next
        list_l1 = int(list_l1[::-1])

        ptr = l2
        list_l2 = ''
        while ptr is not None:
            list_l2 += str(ptr.val)
            ptr = ptr.next
        list_l2 = int(list_l2[::-1])

        res = str(list_l1 + list_l2)[::-1]
        ptr = None
        res_list = None
        print(res)
        for i in res:
            if res_list is None:
                res_list = ListNode(i)
                ptr = res_list
            elif ptr.next is None:
                ptr.next = ListNode(i)
                ptr = ptr.next

        return res_list


if __name__ == '__main__':
    node = ListNode(2)
    node.next = ListNode(4)
    node.next.next = ListNode(3)
    list1 = node

    node = ListNode(5)
    node.next = ListNode(6)
    node.next.next = ListNode(4)
    list2 = node

    print('List1 : ', end='')
    list1.show()
    print('List2 : ', end='')
    list2.show()

    sln = Solution()
    list3 = sln.addTwoNumbers(list1, list2)
    print('List3 : ', end='')
    # print(list3)
    print(type(list3))
    list3.show()
