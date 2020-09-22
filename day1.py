# Contains duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set from our list
        # compare length of set to length of orig. list
        # if set is shorter, duplicates were removed - return True
        # if list and set are equal length, no dups - return False
        # we can do that all in one line! (so why the five lines of comments?)
        return len(set(nums)) < len(nums)


class Solution:
    def addTwoNumvers(self, l1: ListNode, l2: ListNode) ->
ListNode:
    # Initialize current node to dummy head of the returning list.
    # Initialize carry to 00.
    # Initialize pp and qq to head of l1l1 and l2l2 respectively.
    # Loop through lists l1l1 and l2l2 until you reach both ends.
    # Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
    # Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
    # Set sum = x + y + carrysum = x+y+carry.
    # Update carry = sum / 10carry = sum/10.
    # Create a new node with the digit value of(sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
    # Advance both pp and qq.
    # Check if carry = 1carry = 1, if so append a new node with digit 11 to the returning list.
    # Return dummy head's next node.
    carry = 0
    head = curr = ListNode()
    while l1 and l2:
		total = l1.val + l2.val + carry
		curr.next = ListNode(total % 10)
		carry = total // 10
		l1, l2, curr = l1.next, l2.next, curr.next

	while l1:
		total = l1.val + carry
		curr.next = ListNode(total % 10)
		carry = total // 10
		l1, curr = l1.next, curr.next

	while l2:
		total = l2.val + carry
		curr.next = ListNode(total % 10)
		carry = total // 10
		l2, curr = l2.next, curr.next

	if carry > 0:        
		curr.next = ListNode(carry)

	return head.next
