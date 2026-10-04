#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


# Create a VerboseList object
my_list = VerboseList()

# Test append
my_list.append("Apple")

# Test extend
my_list.extend(["Banana", "Orange", "Mango"])

# Test remove
my_list.remove("Banana")

# Test pop
my_list.pop()

# Display the final list
print("Final list:", my_list)
