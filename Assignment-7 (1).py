class RoadNetwork:
    def __init__(self, num_intersections):
        self.num_intersections = num_intersections
        # Initialize an n x n adjacency matrix with 0s
        self.adj_matrix = [[0] * num_intersections for _ in range(num_intersections)]

    # Add an undirected edge (road) between two intersections
    def add_road(self, u, v):
        if 0 <= u < self.num_intersections and 0 <= v < self.num_intersections:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:
            print(f"Error: Invalid intersection indices ({u}, {v})")

    # Display the adjacency matrix
    def display_matrix(self):
        print("\nAdjacency Matrix:")
        # Header row
        header = "    " + " ".join(f"[{i}]" for i in range(self.num_intersections))
        print(header)
        for i in range(self.num_intersections):
            row_str = " ".join(f" {self.adj_matrix[i][j]} " for j in range(self.num_intersections))
            print(f"[{i}] {row_str}")

    # Recursive helper function for DFS
    def _dfs_util(self, vertex, visited, traversal_order):
        visited[vertex] = True
        traversal_order.append(vertex)

        for neighbor in range(self.num_intersections):
            # If an edge exists and the neighbor has not been visited
            if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                self._dfs_util(neighbor, visited, traversal_order)

    # Perform DFS traversal and display the order of visited intersections
    def dfs(self, start_intersection):
        if not (0 <= start_intersection < self.num_intersections):
            print(f"Invalid starting intersection: {start_intersection}")
            return

        visited = [False] * self.num_intersections
        traversal_order = []

        self._dfs_util(start_intersection, visited, traversal_order)

        print(f"\nDFS Traversal starting from intersection {start_intersection}:")
        print(" -> ".join(map(str, traversal_order)))


# --- Driver Code ---
if __name__ == "__main__":
    # Create a road network with 5 intersections (labeled 0 to 4)
    total_intersections = 5
    city_map = RoadNetwork(total_intersections)

    # Add bidirectional roads (edges)
    roads = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (3, 4)
    ]
    for u, v in roads:
        city_map.add_road(u, v)

    # 1. Display the Adjacency Matrix
    city_map.display_matrix()

    # 2. Perform DFS and display the visited order
    start_point = 0
    city_map.dfs(start_point)