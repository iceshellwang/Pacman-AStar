# challenge_search.py
# -------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

"""

Name: Raymond Deng
Section: COMP3770-01 (Intro To AI)
Assignment: Challenge Lab Search
"""
import heapq

# Import your graph here
graph = {
    'A': [False, 3, [('H', 6), ('E', 5)]],
    'D': [False, 3, [('E', 2)]],
    'E': [False, 2, [('F', 3), ('D', 1)]],
    'F': [False, 1, [('G', 2)]],
    'G': [True, 0, []],
    'H': [False, 1, [('I', 2), ('G', 5)]],
    'I': [False, 10, []],
}

"""
 Data structures useful for implementing SearchAgents
"""
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """

    def __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction  # store the priority function
        PriorityQueue.__init__(self)  # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


"""End Structures"""


def graphSearch(frontier):
    """
    Once your DFS, BFS, and UCS algorithms work, unify them
    into a single, iterative graphSearch algorithm that
    requires only an object to manage the fringe.
    """
    "*** YOUR CODE HERE ***"
    # Set a counter for order of visited nodes
    visitCounter = 1
    closed = set()

    # Format of nodes is (actions, cumulativeCost, node/state, visitCount)
    # Node consists of (isGoalTest, heuristic (list of successors))
    initialState = (list(graph.keys()[0]), 0, graph.items()[0], visitCounter)
    frontier.push(initialState)

    while True:

        # Print the contents of the frontier
        # With the priority
        print "\n== Frontier =="
        for item in frontier.heap:
            print item[2][0], "(", item[0], ")"

        # Check if the frontier is empty
        if frontier.isEmpty():
            print "No solution"

        # Unpack frontier
        currentActionList, cumulativeCost, currentGraphItem, currentCount = frontier.pop()
        currentState, currentValues = currentGraphItem

        # Print pop and unpack values from node
        print "\n== Popped =="
        print currentActionList, "(", cumulativeCost, ")"
        isGoal, currentHeuristic, currentSuccessors = currentValues

        # Check if the current state is the goal state
        if isGoal:
            print "\nGOAAAAAAAALLLLL!!!"
            return currentActionList, cumulativeCost

        # Check if been to this state location
        if currentState not in closed:

            # Add it to the closed loop
            # Prevents coming back to an old state
            closed.add(currentState)

            # Generate new successor nodes
            # Add it to the current list of actions
            # Append it to the frontier
            print "\n== Successors =="
            for nextState, nextCost in currentSuccessors:
                # Build the cumulative action list
                tempActionList = currentActionList[:]
                tempActionList.append(nextState)

                # Build the cumulative cost to get to successor state
                tempCostList = cumulativeCost
                tempCostList += nextCost

                # Get the item from the dictionary
                # Increment the visited counter

                print tempActionList
                graphItem = graph.get(nextState)
                visitCounter += 1

                # Insert the node
                insertedNode = (tempActionList, tempCostList, (nextState, graphItem), visitCounter)
                frontier.push(insertedNode)

                # util.raiseNotDefined()


""" SEARCH ALGORITHM DEFINITIONS """
def depthFirstSearch():
    """
    Uses Stack

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # inputStructure = util.Stack()
    # Priority is set by the last node being popped first (LIFO)
    inputStructure = PriorityQueueWithFunction(lambda node: node[3] * -1)
    return graphSearch(inputStructure)
    # util.raiseNotDefined()


def breadthFirstSearch():
    """
    Uses Queue
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    # inputStructure = util.Queue()
    # Priority is set by order of entry (FIFO)
    inputStructure = PriorityQueueWithFunction(lambda node: node[3])
    return graphSearch(inputStructure)

    # util.raiseNotDefined()


def uniformCostSearch():
    """
    Uses a Priority Queue
    Call this with PriorityQueueWith() in Util.Py
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    # Priority is set by least cumulative cost
    inputPriorityQueue = PriorityQueueWithFunction(lambda node: node[1])
    return graphSearch(inputPriorityQueue)

    # util.raiseNotDefined()


def greedySearch():
    # Priority is set by lowest heuristic
    inputStructure = PriorityQueueWithFunction(lambda node: node[2][1][1])
    return graphSearch(inputStructure)


def id_dfs():
    # FIXME: Write algorithm to iterate depth, write priority in costOfActionIDDFS
    depth = 0
    while True:
        result = depthLimitedSearch(graph, depth)
        if result != False:
            return result
        # No solution at all
        elif result == None:
            return None

        depth +=1

    # inputStructure = PriorityQueueWithFunction(lambda node: node[3] * -1)
    # return graphSearch(inputStructure)

def depthLimitedSearch(problem, depth):
    return recursiveDLS(list(graph.keys()[0]), 0, graph.items()[0])


def recursiveDLS(problem, state, depth):
    print 5

def a_star():
    inputStructure = PriorityQueueWithFunction(lambda node: node[2][1][1] + node[1])
    return graphSearch(inputStructure)


""" END SEARCH ALGORITHM DEFINITION """

print id_dfs()

# print "******************DFS******************\n"
# print depthFirstSearch()
# print "******************ID-DFS******************\n"
# print id_dfs()
# print "******************BFS******************\n"
# print breadthFirstSearch()
# print "******************UCS******************\n"
# print uniformCostSearch()
# print "******************GREEDY******************\n"
# print greedySearch()
# print "******************A STAR******************\n"
# print a_star()

