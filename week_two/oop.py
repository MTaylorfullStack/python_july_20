class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#create some nodes

node_one = Node(7)
node_two = Node(8)
node_three = Node(9)

print(f"Node one's pointer: {node_one.next}")

node_one.next = node_two

print(f"Node one's pointer: {node_one.next}")

node_two.next = node_three

print(node_one.value, node_one.next.value, node_one.next.next.value)

class SLL:
    def __init__(self, value):
        self.head = Node(value)
    # adding nodes to the end of our list
    def add_node(self, value):
        runner = self.head
        while(runner.next):
            runner = runner.next
        runner.next = Node(value)
        return self
    # print sll node values
    def display(self):
        monkey = self.head
        count = 1
        while(monkey):
            print(f"This is Node {count}, the value stored is {monkey.value}")
            count += 1
            monkey = monkey.next
        return self

first_sll = SLL(6)
print(first_sll.head.next)
first_sll.add_node(7).add_node(8).add_node(9).add_node(10).display()