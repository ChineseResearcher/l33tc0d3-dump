# number theory - medium
from collections import Counter
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getPrimeFactors(self, num):

        upper_bound = int(num ** 0.5) + 1
        search_space = [2] + list(range(3, upper_bound, 2))
    
        pf = []
        for d in search_space:
            while num % d == 0:
                pf.append(d)
                num = int(num / d)

        if num != 1:
            pf.append(num)

        return pf

    def getGCD(self, pf1, pf2):
        # given two dictionaries each representing the prime factor 
        # frequencies of num1 and num2, return the GCD
        gcd = [] # greatest common divisors
        for k,v in pf1.items():
            if k in pf2:
                gcd.extend([k] * min(pf1[k], pf2[k]))

        if len(gcd) >= 1:
            sumProduct = 1
            for x in gcd:
                sumProduct *= x
            return sumProduct
        elif len(gcd) == 0:
            return 1

    def insertGreatestCommonDivisors(self, head):
        
        currNode = head
        while True:
            if currNode is None:
                return head
            if currNode.next:
                nodeAfterInsert = currNode.next

                c1 = Counter(self.getPrimeFactors(currNode.val))
                c2 = Counter(self.getPrimeFactors(nodeAfterInsert.val))
                currNode.next = ListNode(val=self.getGCD(c1, c2))
                currNode.next.next = nodeAfterInsert
            
                currNode = nodeAfterInsert
            else:
                currNode = currNode.next

# helpers
def print_linked_list(head):
    current = head
    sequence = []
    
    while current is not None:
        sequence.append(current.val)
        current = current.next
        
    print(sequence)
        
def create_linked_list(python_list):
    # If the input list is empty, return None
    if not python_list:
        return None
    
    # Create the head node
    head = ListNode(python_list[0])
    current = head
    
    # Iterate through the rest of the elements in the list and create nodes
    for value in python_list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

# TC
head = [7]
head = [18,6,10,3]

print_linked_list(Solution().insertGreatestCommonDivisors(create_linked_list(head)))