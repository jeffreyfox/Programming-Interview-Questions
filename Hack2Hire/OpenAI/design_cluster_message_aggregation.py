# You are implementing a message-based protocol for a distributed system organized as a rooted n-ary tree. Each node in this system represents a machine, identified by a unique string ID from 0 to n - 1. Each node also stores its parent's ID (-1 for the root) and a list of its children's IDs.

# Nodes communicate only with their immediate parent and children using a provided messaging API. Communication is bi-directional. You need to support the following two operations, both triggered by an external client sending a message to the root node:

# Counting all nodes in the cluster: Triggered by sending a "count" message to the root node.
# Reconstructing the cluster's topology as a string: Triggered by sending a "topology" message to the root node.
# The node structure is defined as follows:

# class Node {
#     String nodeId;
#     String parentId;
#     List<String> children; // List of child node IDs

#     /**
#      * This method is automatically invoked when a message is received by this node.
#      * You need to implement this method.
#      */
#     void receiveMessage(String fromId, String message);
# }
# You are also provided with the following asynchronous messaging API:

# class Cluster {
#    /**
#     * Sends a message asynchronously to the target node.
#     * This API is already implemented for you.
#     */
#     void sendAsyncMessage(String targetId, String message, String fromId);
# }
# You need to extend the Node class as necessary and implement the receiveMessage method:

# void receiveMessage(int fromId, String message)

# Invoked automatically when a message arrives at this node from the node specified by fromId.

# If the message is initiated by an external client (the initial command to the root), fromId will be -1.

# This method must handle two types of operations, both initiated at the root:

# "count" operation
# When the root receives the message "count", it should initiate a distributed counting process. When the process finishes, only the root node should print the final total node count.

# "topology" operation
# When the root receives the message "topology", it should initiate a process to reconstruct the tree's topology as a string. When the process finishes, only the root node should print the final reconstructed string. The required string format is:

# For a leaf node: its own ID (e.g., "4").
# For an internal node: "ID(<child1_topology>,<child2_topology>,...)".
# Children must be listed in the order provided in the children list.
# Note: All inter-node communication must be done via sendAsyncMessage and receiveMessage. Your solution should ensure that message passing, aggregation, and coordination are correctly managed for both operations.

# Constraints:

# 1 ≤ n ≤ 
# 10
# 4
# 10 
# 4
 
# Each nodeId is a unique string.
# The initial "count" or "topology" message is only sent to the root and has fromId as -1.
# Example:

# Input:

# ["sendAsyncMessage", "sendAsyncMessage"]
# [[1, "count", -1], [1, "topology", -1]]

# Output:
# [null, null]

# Explanation:

# sendAsyncMessage(1, "count", -1); // This action is expected to cause the root node (1) to print the total number of nodes: "7".
# sendAsyncMessage(1, "topology", -1); // This action is expected to cause the root node (1) to print the cluster topology: "1(2(4),3(5,6(7)))".

class Node:
    def __init__(self, id, parentId, childIds, cluster):
        self.id = id
        self.parentId = parentId
        self.childIds = childIds[:] if childIds is not None else []
        self.cluster = cluster

        self.subtreeCount = 0
        self.childCountsReceived = 0
        # not need to track topologies received
        self.subtreeTopos: dict[str, str] = {}

    def handleCountRequest(self, fromId):
        for childId in self.childIds:
            self.cluster.sendAsyncMessage(childId, "count", self.id)
        if not self.childIds:
            if self.parentId == -1:
                print("Total nodes: 1")
            else:
                # leaf node send result to parent (similar to return statement)
                self.cluster.sendAsyncMessage(self.parentId, "COUNT:1", self.id)
    
    def handleCountResponse(self, count):
        self.subtreeCount += count
        self.childCountsReceived += 1
        # received response from all child nodes
        if self.childCountsReceived == len(self.childIds):
            self.subtreeCount += 1
            if self.parentId == -1: # root
                print(f"Total nodes: {self.subtreeCount}")
            else:
                self.cluster.sendAsyncMessage(
                    self.parentId, f"COUNT:{self.subtreeCount}", self.id
                )

    def handleTopologyRequest(self, fromId):
        for childId in self.childIds:
            self.cluster.sendAsyncMessage(childId, "topology", self.id)
        if not self.childIds:
            if self.parentId == -1: # single root node
                print(f"Topology: {self.id}")
            else:
                # leaf node send result to parent (similar to return statement)
                self.cluster.sendAsyncMessage(
                    self.parentId, f"TOPOLOGY:{self.id}", self.id
                )
    
    def handleTopologyResponse(self, fromid, topo):
        self.subtreeTopos[fromid] = topo
        # received response from all child nodes
        if len(self.subtreeTopos) == len(self.childIds):
            result = f"{self.id}"
            if self.childIds:
                childTopos = [self.subtreeTopos[cid] for cid in self.childIds]
                result = result + "(" + ",".join(childTopos) + ")"

            if self.parentId == -1: # root
                print(f"Topology: {result}")
            else:
                self.cluster.sendAsyncMessage(
                    self.parentId, f"TOPOLOGY:{result}", self.id
                )

    # This method is automatically invoked when a message arrives.
    def receiveMessage(self, fromId, message):
        if message == "count":
            self.handleCountRequest(fromId)
        elif message.startswith("COUNT:"):
            count = int(message[len("COUNT:"):])
            self.handleCountResponse(count)
        elif message == "topology":
            self.handleTopologyRequest(fromId)
        elif message.startswith("TOPOLOGY:"):
            topo = message[len("TOPOLOGY:"):]
            self.handleTopologyResponse(fromId, topo)


class Cluster:
    def __init__(self, rootId):
        self.nodes = {}
        self.rootId = rootId

    def addNode(self, id, parentId, childIds):
        self.nodes[id] = Node(id, parentId, childIds, self)

    def sendAsyncMessage(self, targetId, message, fromId):
        """
        Provided API to simulate the process of sending a message to a target node
        asynchronously.
        """
        targetNode = self.nodes.get(targetId)
        if targetNode is not None:
            targetNode.receiveMessage(fromId, message)

    @staticmethod
    def main():
        Cluster.test1()
        Cluster.test2()
        Cluster.test3()
        Cluster.test4()

    @staticmethod
    def test1():
        print("================= Test 1 ===================")
        # Cluster topology:
        #
        #        1
        #      /   \
        #     2     3
        #    /     / \
        #   4     5   6
        #               \
        #                7
        cluster = Cluster(1)
        cluster.addNode(1, -1, [2, 3])
        cluster.addNode(2, 1, [4])
        cluster.addNode(3, 1, [5, 6])
        cluster.addNode(4, 2, [])
        cluster.addNode(5, 3, [])
        cluster.addNode(6, 3, [7])
        cluster.addNode(7, 6, [])

        print("--- Triggering Node Count ---")
        cluster.sendAsyncMessage(cluster.rootId, "count", -1)
        # Expected: 7

        print("\n--- Triggering Topology Reconstruction ---")
        cluster.sendAsyncMessage(cluster.rootId, "topology", -1)
        # Expected: "1(2(4),3(5,6(7)))"

    @staticmethod
    def test2():
        print("\n================= Test 2 ===================")
        # Cluster topology:
        #               1
        #          /    |    \
        #        2      3      4
        #      /  \     |   /  |  \
        #     5    6    7  8   9  10
        #    /          |      |
        #   11          12     13
        #                     /  \
        #                   14    15
        cluster = Cluster(1)
        cluster.addNode(1, -1, [2, 3, 4])
        cluster.addNode(2, 1, [5, 6])
        cluster.addNode(3, 1, [7])
        cluster.addNode(4, 1, [8, 9, 10])
        cluster.addNode(5, 2, [11])
        cluster.addNode(6, 2, [])
        cluster.addNode(7, 3, [12])
        cluster.addNode(8, 4, [])
        cluster.addNode(9, 4, [13])
        cluster.addNode(10, 4, [])
        cluster.addNode(11, 5, [])
        cluster.addNode(12, 7, [])
        cluster.addNode(13, 9, [14, 15])
        cluster.addNode(14, 13, [])
        cluster.addNode(15, 13, [])

        print("--- Triggering Node Count ---")
        cluster.sendAsyncMessage(cluster.rootId, "count", -1)
        # Expected: 15

        print("\n--- Triggering Topology Reconstruction ---")
        cluster.sendAsyncMessage(cluster.rootId, "topology", -1)
        # Expected: "1(2(5(11),6),3(7(12)),4(8,9(13(14,15)),10))"

    @staticmethod
    def test3():
        print("\n================= Test 3 ===================")
        # Cluster topology: Single node (100)
        cluster = Cluster(100)
        cluster.addNode(100, -1, [])

        print("--- Triggering Node Count ---")
        cluster.sendAsyncMessage(cluster.rootId, "count", -1)
        # Expected: 1

        print("\n--- Triggering Topology Reconstruction ---")
        cluster.sendAsyncMessage(cluster.rootId, "topology", -1)
        # Expected: "100"

    @staticmethod
    def test4():
        print("\n================= Test 4 ===================")
        # Cluster topology:
        # 10 -> 20 -> 30 -> 40 -> 50
        cluster = Cluster(10)
        cluster.addNode(10, -1, [20])
        cluster.addNode(20, 10, [30])
        cluster.addNode(30, 20, [40])
        cluster.addNode(40, 30, [50])
        cluster.addNode(50, 40, [])

        print("--- Triggering Node Count ---")
        cluster.sendAsyncMessage(cluster.rootId, "count", -1)
        # Expected: 5

        print("\n--- Triggering Topology Reconstruction ---")
        cluster.sendAsyncMessage(cluster.rootId, "topology", -1)
        # Expected: "10(20(30(40(50))))"


if __name__ == "__main__":
    Cluster.main()