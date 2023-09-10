# Network Control Plane Simulator

This project simulates a basic network control plane using both Dijkstra's shortest path algorithm and the Bellman-Ford algorithm. It allows users to understand how routing decisions are made in computer networks based on the shortest path between routers.

## Introduction

In computer networking, understanding the decision-making process for routing packets is essential. The control plane, responsible for this task, sets the rules and paths that data should follow. This simulator presents the principles behind these routing decisions, making it easier for beginners to grasp the foundational ideas of network routing.

## Code Structure & Explanation

### Common Components

1. **Network Topology (`routers` dictionary)**:
   This dictionary describes our virtual network's layout. Each router (like 'A', 'B', 'C'...) has neighboring routers it's connected to, with connection strengths or costs represented numerically.
   
   For instance:
   ```python
   'A': {'B': 1, 'C': 2, 'E': 3}
   ```
   Router 'A' connects to routers 'B', 'C', and 'E' with weights of 1, 2, and 3, respectively.

### Dijkstra's Algorithm

1. **Dijkstra's Algorithm Function (`dijkstra` function)**:
   This well-known algorithm finds the shortest path from a starting router to all other routers in the network. It returns:
   - `distances`: The shortest distance from the starting router to every other router.
   - `predecessors`: Used for retracing the chosen path.

2. **Path Determination (`get_path` function)**:
   This function determines the optimal path from a source to a destination router using Dijkstra's results, backtracking via the `predecessors` from the destination to the source.

### Bellman-Ford Algorithm

1. **Bellman-Ford Algorithm Function (`bellman_ford` function)**:
   Another essential algorithm in the networking realm, the Bellman-Ford algorithm determines the shortest path from a starting router to all others, accounting for possible negative-weight cycles. This function also returns distances and predecessors.

2. **Path Determination using Bellman-Ford (`get_path_bf` function)**:
   This function traces back the optimal path from source to destination using Bellman-Ford's results.

### Main Execution

Sample test cases at the end of each script demonstrate the algorithms in action. This includes finding paths between specified router pairs.

## Getting Started

To run the simulator:

1. Ensure Python is installed.
2. Clone this repository or download the scripts.
3. Navigate to the directory and run the appropriate script:
   - For Dijkstra's algorithm:
     ```bash
     python dijkstra_simulator.py
     ```
   - For Bellman-Ford's algorithm:
     ```bash
     python bellmanford_simulator.py
     ```

Executing the scripts will display optimal paths for sample test cases and their associated costs.

---

## Improvements and Extensions:

1. **Dynamic Topology**: Currently, our network topology is static (hard-coded). An improvement could be a UI or CLI prompt for users to input their own topology, modifying routers and connections dynamically.

2. **Visualization**: Design a GUI to visually depict routers and connections. Optimal routes can be highlighted as paths are determined, enhancing understanding.

3. **Multiple Algorithm Comparison**: Users could select from several algorithms (e.g., Dijkstra, Bellman-Ford, A*) and compare results.

4. **Network Failures Simulation**: Simulate network failures, such as particular routers or connections failing, to test routing algorithm resilience and highlight alternative routes when the primary is inaccessible.

5. **Performance Metrics**: Measure routing decision execution times, examining how factors like network size or complexity impact performance.

6. **Support for Additional Costs**: Beyond distance, metrics like bandwidth, congestion, or reliability could determine optimal paths.

## Conclusion:

The Network Control Plane Simulator serves as a foundational tool for delving into the intricacies of routing decisions in computer networks. As our digital landscape evolves and networks become more intricate, tools like this remain invaluable for students, professionals, and enthusiasts. Proposed improvements would further enhance this simulator into a platform for advanced network simulations, performance testing, and algorithm comparisons.
