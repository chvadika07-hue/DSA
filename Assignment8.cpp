from collections import defaultdict, deque


class SocialNetwork:
    def __init__(self):
        # Represent friendships using an adjacency list
        self.adj_list = defaultdict(list)

    # Add a user (vertex) to the network
    def add_user(self, user):
        if user not in self.adj_list:
            self.adj_list[user] = []

    # Add an undirected friendship (edge) between two users
    def add_friendship(self, user1, user2):
        self.adj_list[user1].append(user2)
        self.adj_list[user2].append(user1)

    # Display the adjacency list representation
    def display_adj_list(self):
        print("--- Social Network Adjacency List ---")
        for user, friends in self.adj_list.items():
            print(f"{user} -> {', '.join(friends) if friends else 'No friends'}")

    # Perform BFS from a selected starting user
    def bfs(self, start_user):
        if start_user not in self.adj_list:
            print(f"Error: User '{start_user}' not found in the network.")
            return

        visited = set([start_user])
        queue = deque([start_user])
        visit_order = []

        print(f"\n--- BFS Traversal Level-by-Level (Starting from {start_user}) ---")
        level = 0

        while queue:
            level_size = len(queue)
            current_level_users = []

            for _ in range(level_size):
                curr_user = queue.popleft()
                visit_order.append(curr_user)
                current_level_users.append(curr_user)

                # Explore all friends (adjacent vertices)
                for friend in self.adj_list[curr_user]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)

            print(f"Level {level}: {', '.join(current_level_users)}")
            level += 1

        # Display users in the overall order they are visited
        print(f"\nOverall Visited Order: {' -> '.join(visit_order)}")


# --- Driver Code ---
if __name__ == "__main__":
    network = SocialNetwork()

    # Define users and friendships
    friendships = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David"),
        ("Charlie", "David"),
        ("Charlie", "Eve"),
        ("David", "Frank"),
    ]

    for u1, u2 in friendships:
        network.add_friendship(u1, u2)

    # 1. Display the Adjacency List
    network.display_adj_list()

    # 2. Perform BFS from a selected user
    start_user = "Alice"
    network.bfs(start_user)