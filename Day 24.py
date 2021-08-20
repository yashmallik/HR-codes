#  Objective
# Check out the Tutorial tab for learning materials and an instructional video!

# Task
# A Node class is provided for you in the editor. A Node object has an integer data field, Data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).

# A removeDuplicates function is declared in your editor, which takes a pointer to the head node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.

# Note: The head pointer may be null, indicating that the list is empty. Be sure to reset your next pointer when performing deletions to avoid breaking the list.

    def removeDuplicates(self,head):
      
        #Write your code here
         if head == None:
            return head;
        s = head
        while s.next != None:
            if s.data == s.next.data:
                s.next = s.next.next
            else :
                s = s.next

        return head;


# -------------------------------------------------------------------OR----------------------------------------------------------------------------------------------------------
    def removeDuplicates(self,head):
      
        #Write your code here
        if head == None :
           return head 
        itr = head
        stack = []
        while itr.next:
            stack.append(itr.data)
            # print(stack )
            if itr.next.data in stack :
                itr.next = itr.next.next
                continue
            itr = itr.next
              
        return head
