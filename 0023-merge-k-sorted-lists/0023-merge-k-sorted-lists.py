import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []      
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))        
        dummy = ListNode()
        current = dummy        
        while min_heap:
            val, index, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, index, node))        
        return dummy.next
def lists_to_linkedlists(lists):
    def list_to_linkedlist(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    return [list_to_linkedlist(lst) for lst in lists]
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    solution = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    linked_lists = lists_to_linkedlists(lists)
    merged_list = solution.mergeKLists(linked_lists)
    print(linkedlist_to_list(merged_list))
    lists = []
    linked_lists = lists_to_linkedlists(lists)
    merged_list = solution.mergeKLists(linked_lists)
    print(linkedlist_to_list(merged_list))
    lists = [[]]
    linked_lists = lists_to_linkedlists(lists)
    merged_list = solution.mergeKLists(linked_lists)
    print(linkedlist_to_list(merged_list))