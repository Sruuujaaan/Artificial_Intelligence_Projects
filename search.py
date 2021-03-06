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
"""

import util

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

def depthFirstSearch(problem):
    """
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
    root = problem.getStartState()
    node = dict()
    visited_list = []
    action = []
    stack = util.Stack()    # Initialize Stack
    node["0"] = root        # root or start state
    node["1"] = None        # path
    node["2"] = None        # parent
    stack.push(node)        # state,path,parent
    while not stack.isEmpty():  # Traverse till there are no elements left in the stack
        node = stack.pop()        # Retrieve first element
        location = node["0"]
        if problem.isGoalState(location):
            break
        if location not in visited_list:
            visited_list.append(location)           # Add location to list of visited nodes
            for x, y, z in problem.getSuccessors(location):  # x=location, y=path, z=parent
                if x not in visited_list:
                    nn = dict()
                    nn["0"] = x
                    nn["1"] = y
                    nn["2"] = node
                    stack.push(nn)
    while node["1"] is not None:
        action.insert(0, node["1"])  # Print the path
        node = node["2"]  # Make parent node the next node
    return action

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    root = problem.getStartState()
    node = dict()
    visited_list = []
    action = []
    queue = util.Queue()    # Initialize Stack
    node["0"] = root        # root or start state
    node["1"] = None        # path
    node["2"] = None        # parent
    queue.push(node)        # state,path,parent
    while not queue.isEmpty():  # Traverse till there are no elements left in the queue
        node = queue.pop()        # Retrieve first element
        location = node["0"]
        if problem.isGoalState(location):
            break
        if location not in visited_list:
            visited_list.append(location)           # Add location to list of visited nodes
            for x, y, z in problem.getSuccessors(location):  # x=location, y=path, z=parent
                if x not in visited_list:
                    nn = dict()
                    nn["0"] = x
                    nn["1"] = y
                    nn["2"] = node
                    queue.push(nn)
    while node["1"] is not None:
        action.insert(0, node["1"])  # To print the path
        node = node["2"]   # Make parent node the next node
    return action

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    node = dict()
    root = problem.getStartState()
    visited_list = []
    action = []
    pQueue = util.PriorityQueue()   # Initialize PriorityQueue
    node["0"] = root                # root or start state
    node["1"] = None                # path
    node["2"] = None                # parent
    node["3"] = 0                   # Cost specified
    pQueue.push(node, node["3"])  # state,path,parent,cost is pushed onto the PQueue
    while not pQueue.isEmpty():
        node = pQueue.pop()     # Retrieve element
        location = node["0"]
        if problem.isGoalState(location):   # Check for goal state
            break
        if location not in visited_list:
            visited_list.append(location)
            for x, y, z in problem.getSuccessors(location):  # update root, path, parent and cost
                if x not in visited_list:
                    nn = dict()  # updating each new node
                    nn["0"] = x
                    nn["1"] = y
                    nn["2"] = node
                    nn["3"] = z + node["3"]
                    pQueue.push(nn, nn["3"])
    while node["1"] is not None:
        action.insert(0, node["1"])  # Path will be calculated
        node = node["2"]
    return action

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    node = dict()
    root = problem.getStartState()
    visited_list = []
    action = []
    pQueue = util.PriorityQueue()
    node["0"] = root
    node["1"] = None
    node["2"] = None
    node["3"] = 0
    node["4"] = heuristic(node["0"], problem)  # heuristic used to calculate actual distance from goal
    pQueue.push(node, node["3"] + node["4"])  # state,path,parent,cost,heuristic(push values onto the PriorityQueue)
    while not pQueue.isEmpty():
        node = pQueue.pop()
        location = node["0"]
        if problem.isGoalState(location):
            break                          # Goal State reached break
        if location not in visited_list:
            visited_list.append(location)
            for x, y, z in problem.getSuccessors(location):
                if x not in visited_list:
                    nn = dict()
                    nn["0"] = x
                    nn["1"] = y
                    nn["2"] = node
                    nn["3"] = z + node["3"]  # update cost
                    nn["4"] = heuristic(x, problem)  # update heuristic
                    pQueue.push(nn, nn["3"] + nn["4"])

    while node["1"] is not None:
        action.insert(0, node["1"])
        node = node["2"]                # Make parent node the next node
    return action



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
