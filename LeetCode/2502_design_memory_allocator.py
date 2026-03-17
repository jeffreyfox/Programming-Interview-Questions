# TAGS: design,array,hash table

# Core idea: Maintain a list of free memory blocks as (start, length) intervals and a hashmap mID → allocated blocks.

# Allocate:
# Scan free_blocks from left to right to find the leftmost block large enough.
# Allocate from the start of that block.
# Shrink or remove the free block accordingly.
# Record the allocated interval under mID.

# Free:
# Retrieve all blocks associated with mID.
# Add them back to free_blocks and sum freed units.
# Sort the free blocks and merge adjacent intervals to avoid fragmentation.

# Key properties:
# Supports multiple allocations per mID.
# Ensures future allocations can reuse freed space efficiently via merging.
# Time complexity is acceptable due to small constraints (≤1000 operations).

class Allocator:

    def __init__(self, n: int):
        self.id_to_blocks = {}
        # starting position and length. We should keep this sorted at all times
        self.free_blocks = [(0, n)]

    def allocate(self, size: int, mID: int) -> int:
        start = -1
        for idx, (start, length) in enumerate(self.free_blocks):
            if size <= length:
                self.id_to_blocks.setdefault(mID, []).append((start, size))
                if length == size:
                    self.free_blocks.pop(idx)
                else:
                    self.free_blocks[idx] = (start + size, length - size)
                return start

        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.id_to_blocks:
            return 0
        
        freed_units = 0
        for start, size in self.id_to_blocks[mID]:
            freed_units += size
            self.free_blocks.append((start, size))
        del self.id_to_blocks[mID]

        # sort the free blocks and also merge ajacent ones
        self.free_blocks.sort()
        
        merged = []
        for start, size in self.free_blocks:
            if not merged:
                merged.append((start, size))
                continue
            
            last_start, last_size = merged[-1]
            if last_start + last_size == start:
                    merged[-1] = (last_start, last_size + size)
            else:
                merged.append((start, size))
        self.free_blocks = merged
        return freed_units
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)