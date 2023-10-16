import pytest
from linked_list import LinkedListNode, LinkedList, OutOfBoundsException

def test_linked_list_node_init():
    node = LinkedListNode(1)
    assert node.value == 1
    assert node.next is None

def test_linked_list_node_next():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)

    node1.next = node2
    assert node1.next == node2

def test_linked_list_node_hasNext():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)

    assert node1.hasNext() is False
    node1.next = node2
    assert node1.hasNext() is True


def test_linked_list_init():
    ll = LinkedList()
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None
    assert ll.toList() == []

def test_linked_list_append():
    ll = LinkedList()
    ll.append(1)
    assert len(ll) == 1
    assert ll.head == 1
    assert ll.tail == 1
    assert ll.toList() == [1]

    ll.append(2)
    assert len(ll) == 2
    assert ll.head == 1
    assert ll.tail == 2
    assert ll.toList() == [1, 2]

def test_linked_list_insert():
    ll = LinkedList()
    ll.insert(1)
    assert len(ll) == 1
    assert ll.head == 1
    assert ll.tail == 1
    assert ll.toList() == [1]

    ll.insert(0)
    assert len(ll) == 2
    assert ll.head == 0
    assert ll.tail == 1
    assert ll.toList() == [0, 1]

def test_linked_list_removeFirst():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    v = ll.removeFirst()
    assert v == 1
    assert len(ll) == 2
    assert ll.head == 2
    assert ll.tail == 3
    assert ll.toList() == [2, 3]

def test_linked_list_getValueAt():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert ll.getValueAt(0) == 1
    assert ll.getValueAt(1) == 2
    assert ll.getValueAt(2) == 3

    with pytest.raises(OutOfBoundsException):
        ll.getValueAt(3)

def test_linked_list_toList():
    ll = LinkedList()
    assert ll.toList() == []

    ll.append(1)
    assert ll.toList() == [1]

    ll.append(2)
    ll.append(3)
    assert ll.toList() == [1, 2, 3]


def test_get_value_at():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert ll.getValueAt(0) == 1
    assert ll.getValueAt(1) == 2
    assert ll.getValueAt(2) == 3

    with pytest.raises(OutOfBoundsException):
        ll.getValueAt(3)

if __name__ == '__main__':
    pytest.main()
