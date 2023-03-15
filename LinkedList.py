class Node:

    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    def print_list_items(self):
        if self.head is None:
            print("Empty")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print()

    def count_nodes(self):
        count = 0
        runner = self.head

        while runner is not None:
            count += 1
            runner = runner.next

        return count

    def find_node(self, target_value):
        runner = self.head
        while runner is not None:
            if runner.value == target_value:
                return True
            else:
              runner = runner.next

        return False

    def delete_node(self, target_value):
        if self.head is None:
            return False
        elif self.head.value == target_value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (target_value > runner.value):
                previous = runner
                runner = runner.next

            if (runner is not None) and runner.value == target_value:
                previous.next = runner.next
                return True
            else:
                return False


my_linked_list = LinkedList()

my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(15)

# 1st: 9
#2nd: 3 -> 9
#3nd: 3 -> 6 -> 9
#4nd: 3 -> 6 -> 9 -> 15



print(my_linked_list.find_node(6))
print(my_linked_list.print_list_items())
print(my_linked_list.count_nodes())
print(my_linked_list.find_node(3))
