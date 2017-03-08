# search.py
# ---------
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
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).

Name: Raymond Deng
Section: COMP3770-01 (Intro To AI)
Assignment: Homework 4 (Search)
"""

import util
import sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def graphSearch(problem, frontier):
    """
    Once your DFS, BFS, and UCS algorithms work, unify them
    into a single, iterative graphSearch algorithm that
    requires only an object to manage the fringe.
    """
    "*** YOUR CODE HERE ***"
    # Build the initial node
    # Push this into the frontier
    closed = set()
    initialState = (list(), 0, problem.getStartState())
    frontier.push(initialState)
    while True:
        if frontier.isEmpty():
            print "No solution"
            return None

        currentActionList, currentCost, currentState = frontier.pop()
        # Check if the current state is the goal state
        if problem.isGoalState(currentState):
            return currentActionList

        # Check if been to this state location
        if currentState not in closed:

            # Add it to the closed loop
            # Prevents coming back to an old state
            closed.add(currentState)
            successorStates = problem.getSuccessors(currentState)

            # Generate new successor nodes
            # Add it to the current list of actions
            # Append it to the frontier
            for nextState, nextAction, nextCost in successorStates:
                # Build the cumulative action list
                tempActionList = currentActionList[:]
                tempActionList.append(nextAction)

                # Build the cumulative cost to get to successor state
                tempCostList = currentCost
                tempCostList += nextCost

                # Insert the node
                insertedNode = (tempActionList, tempCostList, nextState)
                frontier.push(insertedNode)

                # util.raiseNotDefined()


def depthFirstSearch(problem):
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
    # inputStructure = util.PriorityQueueWithFunction(lambda node: node[3] * -1)

    return graphSearch(problem, inputStructure)

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Uses Queue
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"

    inputStructure = util.Queue()

    # UNCOMMENT TO RUN EXTRA CREDIT PROBLEM
    # inputStructure = util.PriorityQueueWithFunction(lambda node: node[3])

    return graphSearch(problem, inputStructure)

    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """
    Uses a Priority Queue
    Call this with PriorityQueueWith() in Util.Py
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"

    inputPriorityQueue = util.PriorityQueueWithFunction(lambda node: node[1])
    return graphSearch(problem, inputPriorityQueue)

    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    # Create the heuristic function
    # Call graphSearch with the priorityQueue
    inputPriorityQueue = util.PriorityQueueWithFunction(lambda node: node[1] + heuristic(node[2], problem))
    return graphSearch(problem, inputPriorityQueue)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
