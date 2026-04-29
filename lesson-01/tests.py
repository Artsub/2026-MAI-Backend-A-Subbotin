import pytest
from cache import LRUCache  # Укажите корректный путь к модулю


class TestLRUCache:
    # ─── Инициализация ───────────────────────────────────────────────────────
    def test_init_valid_capacity(self):
        cache = LRUCache(5)
        assert cache._capacity == 5

    def test_init_invalid_capacity(self):
        with pytest.raises(ValueError):
           LRUCache(0)
        with pytest.raises(ValueError):
           LRUCache(-10)

    # ─── Базовые операции ────────────────────────────────────────────────────
    def test_set_and_get(self):
        cache = LRUCache(2)
        cache.set("key1", "val1")
        assert cache.get("key1") == "val1"

    def test_get_missing_key(self):
        cache = LRUCache(2)
        assert cache.get("nonexistent") is ""

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.set("a", "1")
        cache.set("a", "2")
        assert cache.get("a") == "2"
        # Проверка, что размер не изменился
        cache.set("b", "3")
        assert cache.get("a") == "2"
        assert cache.get("b") == "3"

    # ─── Логика вытеснения LRU (самое важное) ────────────────────────────────
    def test_lru_eviction_on_overflow(self):
        """При добавлении (capacity + 1)-го элемента должен удаляться LRU"""
        cache = LRUCache(2)
        cache.set("1", "one")
        cache.set("2", "two")
        cache.set("3", "three")  # Вытесняет "1"

        assert cache.get("1") is ""
        assert cache.get("2") == "two"
        assert cache.get("3") == "three"

    def test_lru_eviction_after_access(self):
        """get() должен обновлять порядок доступа. LRU становится MRU"""
        cache = LRUCache(2)
        cache.set("A", "a")
        cache.set("B", "b")

        cache.get("A")  # "A" становится самым свежим
        cache.set("C", "c")  # Должен вытесниться "B" (он остался самым старым)

        assert cache.get("A") == "a"
        assert cache.get("B") is ""
        assert cache.get("C") == "c"

    def test_lru_eviction_after_update(self):
        """set() существующего ключа также обновляет порядок доступа"""
        cache = LRUCache(2)
        cache.set("X", "x")
        cache.set("Y", "y")

        cache.set("X", "x_new")  # "X" становится MRU
        cache.set("Z", "z")  # Вытесняется "Y"

        assert cache.get("X") == "x_new"
        assert cache.get("Y") is ""
        assert cache.get("Z") == "z"

    def test_remove_existing_key(self):
        cache = LRUCache(3)
        cache.set("a", "1")
        cache.set("b", "2")
        cache.rem("a")
        assert cache.get("a") is ""
        assert cache.get("b") == "2"

    def test_remove_nonexistent_key(self):
        cache = LRUCache(2)
        cache.rem("ghost")  # Не должно падать
        assert cache.get("ghost") is ""

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.set("first", "1")
        cache.set("second", "2")
        assert cache.get("first") is ""
        assert cache.get("second") == "2"

    def test_empty_cache_operations(self):
        cache = LRUCache(2)
        assert cache.get("anything") is ""
        cache.rem("anything")
        cache.set("only", "value")
        assert cache.get("only") == "value"