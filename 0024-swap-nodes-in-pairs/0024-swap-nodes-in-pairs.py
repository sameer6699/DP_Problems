class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next            
            first.next = second.next
            second.next = first
            current.next = second
            current = first
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
    head = list_to_linkedlist([1, 2, 3, 4])
    swapped = solution.swapPairs(head)
    print(linkedlist_to_list(swapped))
    head = list_to_linkedlist([])
    swapped = solution.swapPairs(head)
    print(linkedlist_to_list(swapped))
    head = list_to_linkedlist([1])
    swapped = solution.swapPairs(head)
    print(linkedlist_to_list(swapped)) 