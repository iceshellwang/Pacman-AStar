import util

graph = {
    'A': [False, 3, [('H', 6), ('E', 5)]],
    'D': [False, 3, [('E', 2)]],
    'E': [False, 2, [('F', 3), ('D', 1)]],
    'F': [False, 1, [('G', 2)]],
    'G': [True, 0, []],
    'H': [False, 1, [('I', 2), ('G', 5)]],
    'I': [False, 10, []],
}

def graphSearch(frontier):
    """
    Once your DFS, BFS, and UCS algorithms work, unify them
    into a single, iterative graphSearch algorithm that
    requires only an object to manage the fringe.
    """
    "*** YOUR CODE HERE ***"
    # Build the initial node
    # Push this into the frontier
    visitCounter = 1
    closed = set()
    # Format of nodes is (actions, cumulativeCost, node/state, visitCount)
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
        currentActionList, cumulativeCost, currentGraphItem, currentVisitCount = frontier.pop()
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
                print tempActionList

                # Build the cumulative cost to get to successor state
                tempCostList = cumulativeCost
                tempCostList += nextCost

                # Get the item from the dictionary
                # Increment the visited counter
                graphItem = graph.get(nextState)
                visitCounter += 1

                # Insert the node
                insertedNode = (tempActionList, tempCostList, (nextState, graphItem), visitCounter)
                frontier.push(insertedNode)

                # util.raiseNotDefined()

def costOfActionDFS(item):
    """
    Uses the order of what was inserted last as highest priority

    :param item: current item as a list (state, action, cost)
    :return: cost or priority of item
    """
    return item[3] * -1


def costOfActionBFS(item):
    """
    Uses the order of when it was inserted for higher priority
    FIFO

    :param item: current item as a list (state, action, cost)
    :return: cost or priority of item
    """
    return item[3]

def costOfActionUCS(item):
    """
    Uses the lowest cumulative cost for the higher priority
    """
    return item[1]


def costOfActionGreedy(item):
    """
    Uses lowest heuristic of item for highest priority
    :param item:
    :return:
    """
    return item[2][1][1]

def costofActionIDDFS(item):
    """

    Similar to DFS but only deepens to x depth
    :param item:
    :return:
    @TODO
    """

    return item[3] * -1




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

    inputStructure = util.Stack()

    # UNCOMMENT TO RUN EXTRA CREDIT PROBLEM
    inputStructure = util.PriorityQueueWithFunction(costOfActionDFS)
    return graphSearch(inputStructure)

    # util.raiseNotDefined()


def breadthFirstSearch():
    """
    Uses Queue
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    inputStructure = util.Queue()

    # UNCOMMENT TO RUN EXTRA CREDIT PROBLEM
    inputStructure = util.PriorityQueueWithFunction(costOfActionBFS)
    return graphSearch(inputStructure)

    # util.raiseNotDefined()


def uniformCostSearch():
    """
    Uses a Priority Queue
    Call this with PriorityQueueWith() in Util.Py
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"

    inputPriorityQueue = util.PriorityQueueWithFunction(costOfActionUCS)
    return graphSearch(inputPriorityQueue)

    # util.raiseNotDefined()

def greedySearch():
    inputStructure = util.PriorityQueueWithFunction(costOfActionGreedy)
    return graphSearch(inputStructure)


def id_dfs():
    # FIXME: Write algorithm to iterate depth, write priority in costOfActionIDDFS
    inputStructure = util.PriorityQueueWithFunction(costofActionIDDFS)
    return graphSearch(inputStructure)



print "******************DFS******************\n"
print depthFirstSearch()
print "******************ID-DFS******************\n"
print id_dfs()
print "******************BFS******************\n"
print breadthFirstSearch()
print "******************UCS******************\n"
print uniformCostSearch()
print "******************GREEDY******************\n"
print greedySearch()
