class LRUCache:

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("capacity positive")
        self._capacity: int = capacity
        self._data: "dict[str, str]" = dict()

    def get(self, key: str) -> str:
        if key not in self._data:
            return ""
        value = self._data.pop(key)
        self._data[key] = value
        return value

    def set(self, key: str, value: str) -> None:

        if key in self._data:
            self._data.pop(key)
        elif len(self._data) >= self._capacity:
            first_key = next(iter(self._data))
            self._data.pop(first_key)
        self._data[key] = value


    def rem(self, key: str) -> None:

        self._data.pop(key, None)
