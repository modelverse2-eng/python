“”“给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。“”“


”“”思路：每次找 k 个节点，断开，翻转指针，再接回去；不足 k 的部分不动“”“

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:  # 不足 k 个节点
                    return dummy.next

            next_group = tail.next
            head_group = prev.next

            # 翻转 [head_group, tail]
            new_head, new_tail = self.reverse(head_group, tail)

            # 接回去
            prev.next = new_head
            new_tail.next = next_group

            # 移动 prev
            prev = new_tail

    def reverse(self, head: ListNode, tail: ListNode):
        """反转链表区间 [head, tail]，返回新头和新尾"""
        prev = tail.next
        cur = head
        while prev != tail:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return tail, head
