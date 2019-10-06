from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.map = defaultdict(defaultdict)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.map[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if i in self.map:
                if index in self.map[i]:
                    return self.map[i][index]
        return 0


snapshotArr = SnapshotArray(100)
snapshotArr.set(0,5)
snapshotArr.set(2,14)
print(snapshotArr.snap())
snapshotArr.set(0,6)
print(snapshotArr.snap())
print(snapshotArr.get(2,2))
print(snapshotArr.map)