import sys


class HashTable:
    def __init__(self):
        self.capacity = 8
        self.count = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        h = 0
        for char in key:
            h = (h * 131 + ord(char)) % 1000000007
        return h % self.capacity

    def _resize(self):
        old_table = self.table

        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]

        for bucket in old_table:
            for key, value in bucket:
                index = self._hash(key)
                self.table[index].append((key, value))

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)

        for k, value in self.table[index]:
            if k == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                value = bucket[i][1]
                bucket.pop(i)
                self.count -= 1
                return value

        return None

    def size(self):
        return self.count


def main():
    q = int(sys.stdin.readline())
    table = HashTable()
    result = []

    for _ in range(q):
        command = sys.stdin.readline().split()

        if command[0] == "put":
            table.put(command[1], int(command[2]))

        elif command[0] == "get":
            value = table.get(command[1])
            result.append(str(value) if value is not None else "Error")

        elif command[0] == "del":
            value = table.delete(command[1])
            result.append(str(value) if value is not None else "Error")

        elif command[0] == "size":
            result.append(str(table.size()))

    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()