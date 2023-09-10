# Network Control Plane Simulator

This project simulates a basic network control plane using Dijkstra's shortest path algorithm. It allows users to understand how routing decisions are made in computer networks based on the shortest path between routers.

## Introduction

In computer networking, understanding the decision-making process for routing packets is crucial. The control plane, which is responsible for this task, lays out the rules and paths that data should follow. The actual data transmission is done over the data plane based on these rules.

This simulator illustrates the principles behind these routing decisions in a simplified manner, allowing beginners to grasp the foundational ideas behind network routing.

## Code Structure & Explanation

1. **Network Topology (`routers` dictionary)**:
   This dictionary defines the layout of our virtual network. Each router (like 'A', 'B', 'C'...) has neighboring routers it's connected to. The connection strength or cost is represented with a numerical value.
   
   For instance:
   ```python
   'A': {'B': 1, 'C': 2, 'E': 3}
   ```
   Router 'A' is connected to routers 'B', 'C', and 'E' with respective weights of 1, 2, and 3.

2. **Dijkstra's Algorithm (`dijkstra` function)**:
   This renowned algorithm helps find the shortest path from a starting router to all other routers in the network. It returns:
   - `distances`: The shortest distance from the starting router to every other router.
   - `predecessors`: Useful for retracing the chosen path.

3. **Path Determination (`get_path` function)**:
   With the results from Dijkstra's algorithm, we can determine the optimal path from a source router to a destination router. This is done by backtracking using the `predecessors` from the destination to the source.

4. **Main Execution**:
   At the end of the script, we've provided sample test cases to demonstrate the algorithm in action. This includes finding paths from router 'A' to 'H', 'D' to 'H', and 'B' to 'E'.

## Getting Started

To run the simulator:

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.
3. Navigate to the directory and run:
   ```bash
   python control_plane_simulator.py
   ```

Upon execution, the script will display the optimal paths for the sample test cases and their associated costs.

---

## Improvements and Extensions:

1. **Dynamic Topology**: Currently, our network topology is static (hard-coded). An improvement could be designing a user interface or a CLI prompt where users can input their own topology, adding or removing routers and connections on-the-fly.

2. **Visualization**: Implement a GUI that can visually depict the routers and their connections. As paths are determined, the optimal route can be highlighted, offering a clearer, more visual understanding of the path taken.

3. **Implement Different Algorithms**: Dijkstra's algorithm is a classic, but there are many routing algorithms out there, like the Bellman-Ford algorithm or A*. An extension could allow users to select from multiple algorithms and compare their results.

4. **Network Failures Simulation**: Add functionality to simulate network failures, like certain routers or connections going down. This would test the resilience of the routing algorithms and showcase alternate routes when the primary path is unavailable.

5. **Performance Metrics**: Include a system to time the execution of routing decisions and measure how different factors (like network size or complexity) might impact performance.

6. **Support for Additional Costs**: Apart from distance, other metrics such as bandwidth, congestion, or reliability can be considered as costs to determine the optimal path.

## Conclusion:

The Network Control Plane Simulator serves as a foundational tool for understanding the intricacies of routing decisions in computer networks. As the digital world continues to evolve, with networks becoming more complex, tools like this remain invaluable for students, professionals, and enthusiasts. With the proposed improvements, this simulator can be a versatile platform for advanced network simulations, performance testing, and algorithm comparison.

---
