# It is dynamic programing approach to solve all-Pairs shortest path Problem. It is used to find the shortest path between all pairs of vertices in a weighted graph.
# It works for both directed and undirected graphs.

# Creating an Adjacency Matrix
# The edges are : a, b, c
import math


# Creating a linked list to track paths
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PathLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
            return

        position = 0
        currentNode = self.head
        while currentNode != None and position < index:
            position = position + 1
            currentNode = currentNode.next
        if currentNode != None:
            new_node = Node(data)
            new_node.next = currentNode.next
            currentNode.next = new_node
        else:
            print("invalid index")

    def print(self):
        print(self)
        # currentNode = self.head
        # while currentNode:
        #     print(currentNode.data, end=" ")
        #     currentNode = currentNode.next
        # print("")

    def __str__(self):  # Override str() for better printing
        result = []
        currentNode = self.head
        while currentNode:
            result.append(str(currentNode.data))
            currentNode = currentNode.next
        return " -> ".join(result) if result else "Empty"


edges = ["a", "b", "c"]
Weight = [[0, 4, 11], [6, 0, 2], [3, math.inf, 0]]
print(Weight)

# for edge in edges: *ERR - 1
#     edge = PathLinkedList()

paths = [
    PathLinkedList() for _ in edges
]  # _ is throwaway variable, the var whose value we don't need
print("paths ", paths[0])


for k in range(len(edges)):  # through this edge
    for i in range(len(edges)):  # starting edge
        for j in range(len(edges)):  # ending edge
            if i == j:
                Weight[i][j] = 0
            else:
                new_distance = Weight[i][k] + Weight[k][j]
                if new_distance < Weight[i][j]:
                    Weight[i][j] = new_distance
                    paths[i].insertAtBeginning(edges[j])

                # Weight[i][j] = min(Weight[i][j], Weight[i][k] + Weight[k][j])
                # paths[i].insertAtIndex(Weight[i][j], j - 1) #*ERR - 1 didn't work


print("The Shortest Path Matrix is:")
# print(Weight)
for row in Weight:
    print(row)
print("The Shortest Path is: ")
for index, path in enumerate(
    paths
):  # NOTE adds an index to each element in the paths list while iterating
    print(f"From {edges[index]}:", end="")
    path.print()
