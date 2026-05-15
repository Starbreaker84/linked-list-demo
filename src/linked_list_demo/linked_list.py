from __future__ import annotations
from typing import Generic, Optional, Iterator, TypeVar

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.next: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self._size = 0

    # ========= Базовые методы =========

    def append(self, value: T) -> None:
        """Добавить элемент в конец."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self._size += 1

    def prepend(self, value: T) -> None:
        """Добавить элемент в начало."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self._size += 1

    def insert(self, index: int, value: T) -> None:
        """Вставить элемент по индексу."""
        if index < 0 or index > self._size:
            raise IndexError("index out of range")

        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)

        current = self.head
        for _ in range(index - 1):
            assert current is not None
            current = current.next

        assert current is not None

        new_node.next = current.next
        current.next = new_node

        self._size += 1

    # ========= Удаление =========

    def remove(self, value: T) -> None:
        """Удалить первое вхождение значения."""
        if self.head is None:
            raise ValueError("list is empty")

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                self._size -= 1
                return

            prev = current
            current = current.next

        raise ValueError(f"{value!r} not found")

    def pop_first(self) -> T:
        """Удалить первый элемент."""
        if self.head is None:
            raise IndexError("pop from empty list")

        value = self.head.value
        self.head = self.head.next

        self._size -= 1
        return value

    def pop_last(self) -> T:
        """Удалить последний элемент."""
        if self.head is None:
            raise IndexError("pop from empty list")

        if self.head.next is None:
            value = self.head.value
            self.head = None

            self._size -= 1
            return value

        prev = self.head
        current = self.head.next

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None

        self._size -= 1
        return current.value

    # ========= Поиск =========

    def find(self, value: T) -> Optional[Node[T]]:
        """Найти узел по значению."""
        current = self.head

        while current is not None:
            if current.value == value:
                return current

            current = current.next

        return None

    def contains(self, value: T) -> bool:
        return self.find(value) is not None

    # ========= Служебные =========

    def clear(self) -> None:
        self.head = None
        self._size = 0

    def reverse(self) -> None:
        """Развернуть список."""
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # ========= Магические методы =========

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")

        current = self.head

        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None
        return current.value

    def __repr__(self) -> str:
        values = ", ".join(repr(v) for v in self)
        return f"LinkedList([{values}])"