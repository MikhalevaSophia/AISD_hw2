class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None and self.table[index] != (None, None):
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (None, None)
                return
            index = (index + 1) % self.size
            if index == original_index:
                break


print('Enter hash-table size')
size = int(input())
table = HashTableOpenAddressing(size)
print('Enter keys and values')
while True:
    item = input()
    if not item:
        break
    k, v = item.split()
    table.insert(int(k), v)
def help():
    print('Write down what you want to do: \nDelete, if you want to delete an element \nSearch, if you want to find an element \nShow, if you want to watch how look hash-table now \nEnter, if you do not do do anything')
help()
while True:
    move = input()
    if move == 'Delete':
        print('Enter the key of element to delete')
        number = int(input())
        table.delete(number)
    elif move == 'Search':
        print('Enter the key of element to find')
        number = int(input())
        print(table.search(number))
    elif move == 'Show':
        print(table.table)
    elif move == 'Enter':
        break
    elif move == 'Insert':
        print('Enter the key and value of new element')
        k, v = input().split()
        table.insert(int(k), v)
    else:
        print('Invalid command')
        help()