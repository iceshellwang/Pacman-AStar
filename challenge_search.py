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
import util

# Import your graph here
# insertedGraph = {
#     'A': [False, 3, [('H', 6), ('E', 5)]],
#     'D': [False, 3, [('E', 2)]],
#     'E': [False, 2, [('F', 3), ('D', 1)]],
#     'F': [False, 1, [('G', 2)]],
#     'G': [True, 0, []],
#     'H': [False, 1, [('I', 2), ('G', 5)]],
#     'I': [False, 10, []],
# }

insertedGraph = {
    'A': [False, 7, [('G', 5), ('S', 1)]],
    'S': [False, 6, [('G', 3)]],
    'G': [True, 0, []]
}

# insertedGraph = {
#     'A': [False, 2, [('S', 1), ('B', 1)]],
#     'S': [False, 4, [('C', 1)]],
#     'B': [False, 1, [('C', 2)]],
#     'C': [False, 1, [('G', 3)]],
#     'G': [True, 0, []]
# }



def graphSearch(graph, frontier):
    """
    Once your DFS, BFS, and UCS algorithms work, unify them
    into a single, iterative graphSearch algorithm that
    requires only an object to manage the fringe.
    """
    "*** YOUR CODE HERE ***"
    # Set a counter for order of visited nodes
    visitCounter = 1
    closed = set()

    # Format of nodes is (ActionList, cumulativeCost, node/state, visitCount)
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
            return None

        # Unpack frontier
        currentActionList, cumulativeCost, currentGraphItem, currentCount = frontier.pop()
        currentState, currentValues = currentGraphItem
        isGoal, currentHeuristic, currentSuccessors = currentValues

        # Print pop and unpack values from node
        print "\n== Popped =="
        print currentActionList, "(", cumulativeCost, ")"

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
def depthFirstSearch(inputGraph):
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
    inputStructure = util.PriorityQueueWithFunction(lambda node: node[3] * -1)
    return graphSearch(inputGraph, inputStructure)
    # util.raiseNotDefined()


def breadthFirstSearch(inputGraph):
    """
    Uses Queue
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    # inputStructure = util.Queue()
    # Priority is set by order of entry (FIFO)
    inputStructure = util.PriorityQueueWithFunction(lambda node: node[3])
    return graphSearch(inputGraph, inputStructure)

    # util.raiseNotDefined()


def uniformCostSearch(inputGraph):
    """
    Uses a Priority Queue
    Call this with PriorityQueueWith() in Util.Py
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    # Priority is set by least cumulative cost
    inputPriorityQueue = util.PriorityQueueWithFunction(lambda node: node[1])
    return graphSearch(inputGraph, inputPriorityQueue)

    # util.raiseNotDefined()


def greedySearch(inputGraph):
    # Priority is set by lowest heuristic
    inputStructure = util.PriorityQueueWithFunction(lambda node: node[2][1][1])
    return graphSearch(inputGraph, inputStructure)


def id_dfs(inputGraph):
    inputStructure = util.PriorityQueueWithFunction(lambda node: node[3] * -1)
    depth = 1

    while True:
        print "\nDepth Limit: ", depth
        result = depthLimitedSearch(inputGraph, depth, inputStructure)
        if result is not None:
            print "Found a solution"
            return result
        depth += 1

    # inputStructure = PriorityQueueWithFunction(lambda node: node[3] * -1)
    # return graphSearch(inputStructure)


def depthLimitedSearch(problem, maxDepth, frontier):
    # Set a counter for order of visited nodes
    visitCounter = 1
    closed = set()

    # Format of nodes is (ActionList, cumulativeCost, node/state, visitCount, depthOfTheNode)
    # Node consists of (isGoalTest, heuristic (list of successors))
    initialState = (list(problem.keys()[0]), 0, problem.items()[0], visitCounter, 0)
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
            return None

        # Unpack frontier
        currentActionList, cumulativeCost, currentGraphItem, currentCount, depthOfNode = frontier.pop()
        currentState, currentValues = currentGraphItem
        isGoal, currentHeuristic, currentSuccessors = currentValues

        # Print pop and unpack values from node
        print "\n== Popped =="
        print currentActionList, "(", cumulativeCost, ")"

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
        if depthOfNode < maxDepth:
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
                graphItem = problem.get(nextState)
                visitCounter += 1
                newDepth = depthOfNode + 1

                # Insert the node
                insertedNode = (tempActionList, tempCostList, (nextState, graphItem), visitCounter, newDepth)
                frontier.push(insertedNode)


def a_star(inputGraph):
    inputStructure = util.PriorityQueueWithFunction(lambda node: node[2][1][1] + node[1])
    return graphSearch(inputGraph, inputStructure)


def checkAdmissiblity(inputGraph):

    # Check if each nodes path to the goal
    for i in range(len(inputGraph)):
        inputStructure = util.PriorityQueueWithFunction(lambda node: node[2][1][1] + node[1])
        currentState = inputGraph.keys()[i]
        currentStateItems = inputGraph.items()[i]
        currentHeuristic = currentStateItems[1][1]
        initialState = (list(currentState), 0, currentStateItems)
        pathToSolution, costToSolution = graphSearchCheckAdmissiblity(inputGraph, inputStructure, initialState)
        # print "Heuristic: ", currentHeuristic, "State: ", currentState, \
        #     " costToSolution: ", costToSolution, "PathToSolution: ", pathToSolution

        if currentHeuristic > costToSolution and costToSolution:
            print currentState, " ", currentHeuristic, " ", " vs. ", pathToSolution, " ", costToSolution
            return False

    return True


def checkConsistency(inputGraph):
    """
    Used to check if a heuristic is consistent
    Satisfies the equation:
        heuristic(successor) <= cost(current, successor) + heuristic(current)
    """
    if not checkAdmissiblity(inputGraph):
        return False
    for j in range(len(inputGraph)):
        currentState = inputGraph.keys()[j]
        isGoal, currentHeuristic, currentSuccessors = inputGraph.items()[j][1]
        for successorState, costToSuccessor in currentSuccessors:
            # Get the successors heuristic
            fullSuccessorNode = inputGraph.get(successorState)
            successorHeuristic = fullSuccessorNode[1]
            if currentHeuristic - successorHeuristic > costToSuccessor:
                print currentState, "(", currentHeuristic, ") -", costToSuccessor, \
                    "->", successorState, "(", successorHeuristic, ")"
                return False
    return True


"Helper function to Check Admissiblity of a Heuristic"
def graphSearchCheckAdmissiblity(inputGraph, frontier, initialNode):
    """
    Used to check the admissibility of a heuristic
    Finds the least path cost to the goal from a given node
    Returns None, None if no path to goal or actions to goal and cost to goal
    Satisfies equation: heuristic(currentNode) <= pathCost(currentNode, goal)
    """
    "*** YOUR CODE HERE ***"
    # Set a counter for order of visited nodes
    closed = set()

    # Format of nodes is (ActionList, cumulativeCost, node/state, visitCount)
    # Node consists of (isGoalTest, heuristic (list of successors))
    frontier.push(initialNode)
    while True:
        # Check if the frontier is empty
        # If empty return None, None
        if frontier.isEmpty():
            return None, None

        # Unpack frontier
        currentActionList, cumulativeCost, currentGraphItem = frontier.pop()
        currentState, currentValues = currentGraphItem
        isGoal, currentHeuristic, currentSuccessors = currentValues

        # Check if the current state is the goal state
        # Return the actions and cost of it
        if isGoal:
            return currentActionList, cumulativeCost

        # Check if been to this state location
        if currentState not in closed:

            # Add it to the closed loop
            # Prevents coming back to an old state
            closed.add(currentState)

            # Generate new successor nodes
            # Add it to the current list of actions
            # Append it to the frontier
            for nextState, nextCost in currentSuccessors:
                # Build the cumulative action list
                tempActionList = currentActionList[:]
                tempActionList.append(nextState)

                # Build the cumulative cost to get to successor state
                tempCostList = cumulativeCost
                tempCostList += nextCost

                # Get the item from the dictionary
                # Increment the visited counter

                # print tempActionList
                graphItem = inputGraph.get(nextState)

                # Insert the node
                insertedNode = (tempActionList, tempCostList, (nextState, graphItem))
                frontier.push(insertedNode)

                # util.raiseNotDefined()


""" END SEARCH ALGORITHM DEFINITION """

print "******************DFS******************\n"
print depthFirstSearch(insertedGraph)
print "******************ID-DFS******************\n"
print id_dfs(insertedGraph)
print "******************BFS******************\n"
print breadthFirstSearch(insertedGraph)
print "******************UCS******************\n"
print uniformCostSearch(insertedGraph)
print "******************GREEDY******************\n"
print greedySearch(insertedGraph)
print "******************A STAR******************\n"
print a_star(insertedGraph)


print "******************Checking admissiblity******************\n"
isAdmissible = checkAdmissiblity(insertedGraph)
print " Admissible: ", isAdmissible
print "******************Checking Consistency******************\n"
isConsistent = checkConsistency(insertedGraph)
print " Consistency: ", isConsistent

