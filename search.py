from util import Queue


def breadthFirstSearch(graph):
    state = 0
    nodes = Queue()
    usedstates = set()
    node = [state, [state]]
    nodes.push(node)
    while not nodes.isEmpty():
        node = nodes.pop()
        [s, actions] = node
        if not s in usedstates:
            usedstates.add(s)
            if graph.isGoalState(s):
                return node[1]
            for ns in graph.getSuccessors(s):
                new_actions = actions + [ns]
                nodes.push([ns, new_actions])
    return None
