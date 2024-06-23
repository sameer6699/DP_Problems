class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):   
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2       
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
    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    merged_list = solution.mergeTwoLists(list1, list2)
    print(linkedlist_to_list(merged_list))
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([])
    merged_list = solution.mergeTwoLists(list1, list2)
    print(linkedlist_to_list(merged_list))
    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([0])
    merged_list = solution.mergeTwoLists(list1, list2)
    print(linkedlist_to_list(merged_list))