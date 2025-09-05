"""给定链接列表的head，从列表末尾删除第nth节点并返回其头部"""


"""思路：在头节点前创建一个临时节点防止要删除的是头节点，读取一遍链表长度 ，找到要删除节点的前一节点n-1 ，让n-1直接跳到n+1 ,返回虚拟节点的后一个节点






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        cur = head

        # 先求链表长度
        while cur:
            length += 1
            cur = cur.next

        # 找到要删除节点的前一个，严格来说是跳过
        cur = dummy
        for _ in range(length - n):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next
