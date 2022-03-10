class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        while next_node.next is not None:
            node.val = next_node.val
            node = node.next
            next_node = next_node.next
        node.next = None