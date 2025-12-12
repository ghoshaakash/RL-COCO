import numpy as np

# Actions: up, right, down, left
ACTIONS = np.array([
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
])

class WindyGridworld:
    def __init__(self):
        # Grid shape fixed by the book
        self.R = 7
        self.C = 10
        
        # Wind strengths per column (Sutton & Barto Figure 6.5)
        self.wind = np.array([0,0,0,1,1,1,2,2,1,0])

        # Start and goal positions
        self.start = (3, 0)
        self.goal = (3, 7)

        self.state = None

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        r, c = self.state

        # Apply wind (vertical push up)
        r -= self.wind[c]

        # Apply chosen action
        dr, dc = ACTIONS[action]
        r += dr
        c += dc

        # Clip to grid boundaries
        r = min(max(0, r), self.R - 1)
        c = min(max(0, c), self.C - 1)

        self.state = (r, c)

        # Terminal?
        if (r, c) == self.goal:
            return (r, c), 0, True  # reward 0 at goal

        return (r, c), -1, False   # step cost everywhere else
    
    def viz(self):
        grid_chars = []

        for r in range(self.R):
            row = []
            for c in range(self.C):
                if (r, c) == self.state:
                    row.append("A")  # agent
                elif (r, c) == self.start:
                    row.append("S")
                elif (r, c) == self.goal:
                    row.append("G")
                else:
                    row.append(".")
            grid_chars.append(" ".join(row))

        # Print wind values under or above the grid
        wind_str = " ".join(str(w) for w in self.wind)

        print("\n".join(grid_chars))
        print("Wind:", wind_str)
        print()
