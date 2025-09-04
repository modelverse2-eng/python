"""您将获得两个排序链接列表list1和list2的负责人。

将两个列表合并为一个排序的列表。列表应该通过将前两个列表的节点拼接在一起来制作。

返回合并链接列表的负责人。"""



"""思路：1，两个有序序列 2，依次比较头部元素 3，谁小就取谁 4，指针后移。
我们可以用 双指针 来完成“”“




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 创建一个虚拟头节点，方便处理边界
        dummy = ListNode(-1)
        cur = dummy

        # 同时遍历两个链表，按大小拼接节点
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 把剩余的链表接上
        cur.next = list1 if list1 else list2

        return dummy.next
