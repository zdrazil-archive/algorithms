# Write code to remove duplicates from an unsorted linked list
# Follow up: How would you solve this problem if a temproray buffer is not allowed


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def delete_node(self, input):
        head = self
        if head.cargo == input:
            return self.next
        while head.next is not None:
            if head.next.cargo == input:
                head.next = head.next.next
                return self
            head = head.next
        return self

    def delete_duplicates(self):
        table = HashTable()
        head = self
        while head.next is not None:
            if table.containsKey(head.cargo):
                head.delete_node(head.cargo)
            else:
                table.insert(head.cargo)
        return head


def print_list(node):
    while node:
        print(node.cargo)
        node = node.next
    return


def print_backward(list):
    if list is None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print(head)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# printList(node1)
# printBackward(node1)
node1 = node1.delete_node(2)
print_list(node1)