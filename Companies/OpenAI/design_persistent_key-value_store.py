# You are designing a persistent key-value store that supports saving and restoring its data using a binary middleware medium. The system should store only string keys and string values and be able to serialize its entire state to a binary blob for durability across restarts.

# A storage interface called Medium is provided, allowing you to save and retrieve a single binary blob. The implementation is in InMemoryMedium.

# // This is a provided API interface.
# interface Medium {
#     /**
#      * Saves a byte array to the storage medium (e.g., file, in-memory).
#      * @param data The byte array to persist.
#      */
#     void saveBlob(byte[] data);

#     /**
#      * Retrieves the most recently saved byte array from the storage medium.
#      * @return The stored byte array, or null if nothing is saved.
#      */
#     byte[] getBlob();
# }
# You need to implement the KVStore class, ensuring that the binary serialization format can exactly recover all string keys and values, including those with Unicode characters or empty strings. Native object serialization (such as direct use of language-specific serialization, or JSON) is not allowed. You must construct your own serialization format.

# Implement the KVStore class:

# KVStore(Medium medium) Initializes a new, empty key-value store using the provided storage medium. The store only interacts with data via this medium.

# void put(String key, String value) Stores the specified value associated with the given key. If the key already exists, its value is updated.

# String get(String key) Returns the value associated with key. If the key is not present, it returns the empty string "".

# void shutdown() Serializes the current store into a custom binary format and writes it to the associated medium. After shutdown, the instance becomes closed, any subsequent get or put must fail and throw an error.

# void restore() Loads the key-value data from the binary blob saved in the medium, completely replacing the in-memory store. If the blob is missing or empty, the store should become empty.

# Constraints:

# Keys and values are arbitrary strings (may include Unicode and empty strings).
# After calling shutdown, the instance is permanently closed; further calls to get or put must fail.
# The restore method always replaces the in-memory state, discarding any unsaved changes.
# 1 ≤ number of keys ≤ 10⁴.
# Total size of all keys and values together ≤ 10⁶ characters.
# Each key and value is a string of length ≤ 10⁴.
# All methods are called in a valid order (e.g., shutdown is not called twice in a row).
# Example:

# Input:
# ["InMemoryMedium", "KVStore", "put", "put", "put", "get", "get", "shutdown", "KVStore", "get", "put", "restore", "get", "get", "get", "get"]
# [[], [], ["key1", "value1"], ["key2", "value2_is_longer"], ["key3", "value3"], ["key1"], ["key4"], [], [medium], ["key1"], ["key4", "value4"], [], ["key1"], ["key2"], ["key3"], ["key4"]]

# Output:
# [null, null, null, null, null, "value1", "", null, null, "", null, null, "value1", "value2_is_longer", "value3", ""]

# Explanation:

# Medium medium = new InMemoryMedium();
# KVStore store1 = new KVStore(medium); // Initializes a new store backed by medium.
# store1.put("key1", "value1"); // Stores "key1" -> "value1".
# store1.put("key2", "value2_is_longer"); // Stores "key2" -> "value2_is_longer".
# store1.put("key3", "value3"); // Stores "key3" -> "value3".
# store1.get("key1"); // Returns "value1".
# store1.get("key4"); // Returns "".
# store1.shutdown(); // Persists the current store and closes this instance.
# KVStore store2 = new KVStore(medium); // Creates a new store with same medium.
# store2.get("key1"); // Returns "", since nothing has been restored yet.
# store2.put("key4", "value4"); // Adds "key4" -> "value4" to store2's in-memory map.
# store2.restore(); // Loads the blob, replacing all in-memory data with what was persisted by store1.
# store2.get("key1"); // Returns "value1", loaded from persisted state.
# store2.get("key2"); // Returns "value2_is_longer".
# store2.get("key3"); // Returns "value3".
# store2.get("key4"); // Returns "", since "key4" was never persisted and was overwritten by restore.

import struct
from abc import ABC, abstractmethod
from io import BytesIO

# The Medium interface allows persisting and retrieving raw binary data.
class Medium(ABC):
    @abstractmethod
    def saveBlob(self, data):
        pass

    @abstractmethod
    def getBlob(self):
        pass

# An in-memory implementation of the Medium interface for testing purposes.
class InMemoryMedium(Medium):
    def __init__(self):
        self.storage = None

    def saveBlob(self, data):
        self.storage = data

    def getBlob(self):
        return self.storage

# Serializes a python dict to a bytes object
def serialize(data: dict[str, str]) -> bytes:
    buf = bytearray()
    for key, val in data.items():
        key_bytes = key.encode("utf-8")
        val_bytes = val.encode("utf-8")
        buf.extend(len(key_bytes).to_bytes(4, "big"))
        buf.extend(key_bytes)
        buf.extend(len(val_bytes).to_bytes(4, "big"))
        buf.extend(val_bytes)
    return bytes(buf)

# Deserializes a bytes object into a python dict
def deserialize(b: bytes) -> dict[str, str]:
    data = {}
    if b is None:
        return data

    buf = bytearray(b)
    idx = 0
    while idx < len(buf):
        key_size = int.from_bytes(buf[idx:idx+4], "big")
        idx += 4
        key = buf[idx:idx+key_size].decode("utf-8")
        idx += key_size
        val_size = int.from_bytes(buf[idx:idx+4], "big")
        idx += 4
        val = buf[idx:idx+val_size].decode("utf-8")
        idx += val_size
        data[key] = val
    return data

class KVStore:
    def __init__(self, medium):
        self.medium = medium
        self.data: dict[str, str] = {}
        self.is_closed = False

    def put(self, key, value):
        if self.is_closed:
            raise RuntimeError("Store Closed")
        self.data[key] = value

    def get(self, key):
        if self.is_closed:
            raise RuntimeError("Store Closed")
        return self.data.get(key, "")

    def shutdown(self):
        if self.is_closed:
            raise RuntimeError("Store Closed")
        self.medium.saveBlob(serialize(self.data))
        self.is_closed = True

    def restore(self):
        if self.is_closed:
            raise RuntimeError("Store Closed")

        self.data = deserialize(self.medium.getBlob())


    @staticmethod
    def main(args):
        KVStore.test1()
        KVStore.test2()
        KVStore.test3()

    @staticmethod
    def test1():
        print("===== Test 1 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("key1", "value1")
        store1.put("key2", "value2_is_longer")
        store1.put("key3", "value3")
        print(store1.get("key1"))  # Expected: "value1"
        print(store1.get("key4"))  # Expected: ""
        store1.shutdown()

        store2 = KVStore(medium)
        print(store2.get("key1"))  # Expected: ""
        store2.put("key4", "value4")

        store2.restore()
        print(store2.get("key1"))  # Expected: "value1"
        print(store2.get("key2"))  # Expected: "value2_is_longer"
        print(store2.get("key3"))  # Expected: "value3"
        print(store2.get("key4"))  # Expected: ""

    @staticmethod
    def test2():
        print("\n===== Test 2 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("counter", "1")
        store1.put("status", "active")
        print(store1.get("counter"))  # Expected: "1"
        print(store1.get("status"))  # Expected: "active"
        store1.shutdown()

        store2 = KVStore(medium)
        store2.restore()
        store2.put("counter", "2")
        store2.put("status", "inactive")
        store2.put("new_field", "added")
        print(store2.get("counter"))  # Expected: "2"
        print(store2.get("status"))  # Expected: "inactive"
        print(store2.get("new_field"))  # Expected: "added"
        store2.shutdown()

        store3 = KVStore(medium)
        store3.restore()
        print(store3.get("counter"))  # Expected: "2"
        print(store3.get("status"))  # Expected: "inactive"
        print(store3.get("new_field"))  # Expected: "added"

    @staticmethod
    def test3():
        print("\n===== Test 3 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("emoji_key_😊", "emoji_value_🎉")
        store1.put("unicode_key_中文", "unicode_value_日本語")
        store1.put("empty_value", "")
        print(store1.get("emoji_key_😊"))  # Expected: "emoji_value_🎉"
        print(store1.get("empty_value"))  # Expected: ""
        store1.shutdown()

        store2 = KVStore(medium)
        store2.restore()
        print(store2.get("emoji_key_😊"))  # Expected: "emoji_value_🎉"
        print(store2.get("unicode_key_中文"))  # Expected: "unicode_value_日本語"
        print(store2.get("empty_value"))  # Expected: ""
        print(store2.get("nonexistent_key"))  # Expected: ""

if __name__ == "__main__":
    KVStore.main([])