class Element:
    def __init__(self, value=None, next_element=None):
        self.value = value
        self.next_element = next_element

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next_element
        return '  '.join(elements)

    def get(self, e):
        current = self.head
        while current:
            if current.value == e:
                return current.value
            current = current.next_element
        return None

    def delete(self, e):
        if self.head.value == e:
            self.head = self.head.next_element
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        current = self.head
        while current.next_element:
            if current.next_element.value == e:
                if current.next_element == self.tail:
                    self.tail = current
                current.next_element = current.next_element.next_element
                self.size -= 1
                return
            current = current.next_element

    def append(self, e, func=None):
        new_element = Element(e)

        if self.head is None:
            self.head = new_element
            self.tail = new_element
        elif func is None:
            if e >= self.tail.value:
                self.tail.next_element = new_element
                self.tail = new_element
            elif e <= self.head.value:
                new_element.next_element = self.head
                self.head = new_element
            else:
                current = self.head
                while current.next_element and e > current.next_element.value:
                    current = current.next_element
                new_element.next_element = current.next_element
                current.next_element = new_element
        else:
            if func(e, self.tail.value):
                self.tail.next_element = new_element
                self.tail = new_element
            elif func(self.head.value, e):
                new_element.next_element = self.head
                self.head = new_element
            else:
                current = self.head
                while current.next_element and not func(e, current.next_element.value):
                    current = current.next_element
                new_element.next_element = current.next_element
                current.next_element = new_element

        self.size += 1


def main():
    linked_list = MyLinkedList()

    linked_list.append(41)
    linked_list.append(12)
    linked_list.append(62)
    linked_list.append(3)
    linked_list.append(121)

    print(linked_list)

    element = linked_list.get(3)
    print(element)

    linked_list.delete(3)
    print(linked_list)


main()
