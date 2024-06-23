class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse_linked_list(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev
        length = 0
        current = head
        while current:
            length += 1
            current = current.next        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy        
        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next            
            next_group_start = group_end.next
            reversed_group = reverse_linked_list(group_start, k)            
            prev_group_end.next = reversed_group
            group_start.next = next_group_start            
            prev_group_end = group_start
            length -= k        
        return dummy.next
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    solution = Solution()
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    k = 2
    reversed_list = solution.reverseKGroup(head, k)
    print(linkedlist_to_list(reversed_list))
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    k = 3
    reversed_list = solution.reverseKGroup(head, k)
    print(linkedlist_to_list(reversed_list))
    head = list_to_linkedlist([1])
    k = 1
    reversed_list = solution.reverseKGroup(head, k)
    print(linkedlist_to_list(reversed_list))