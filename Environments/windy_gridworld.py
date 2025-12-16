import numpy as np

# Actions: up, right, down, left
ACTIONS = np.array([
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
])

class WindyGridworld:
    """Simple Windy Gridworld environment.

    Attributes
    ----------
    R : int
        Number of rows (7).
    C : int
        Number of columns (10).
    wind : numpy.ndarray
        1D array of length `C` containing vertical wind strengths per column.
    start : tuple[int, int]
        Starting cell as (row, col).
    goal : tuple[int, int]
        Goal cell as (row, col).
    state : tuple[int, int] | None
        Current agent position.
    """
    # Actions: up, right, down, left
    ACTIONS = np.array([
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
    ])
    
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
        """Reset the environment and return the start state.

        Returns
        -------
        tuple[int, int]
            The starting `(row, col)` position.
        """

        self.state = self.start
        return self.state

    def step(self, action):
        """Apply an action and return (next_state, reward, done).

        Parameters
        ----------
        action : int
            Index into `ACTIONS` (0: up, 1: right, 2: down, 3: left).

        Returns
        -------
        tuple[tuple[int, int], int, bool]
            `(next_state, reward, done)` where `next_state` is `(row, col)`,
            `reward` is -1 for a normal step and 0 when reaching the goal,
            and `done` is True if the goal was reached.
        """

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
    
    def viz(self, ax=None, show=True):
        """Visualize the current grid using Matplotlib.

        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            If provided, draw into this axes. Otherwise a new figure and
            axes are created.
        show : bool, optional
            If True (default), call ``plt.show()`` for interactive display.

        Returns
        -------
        tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]
            The `(fig, ax)` used to render the visualization.
        """

        # Inline import to avoid requiring matplotlib at module import time.
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap

        grid = np.zeros((self.R, self.C), dtype=int)

        # Mark start, goal and agent with distinct integer codes
        sr, sc = self.start
        gr, gc = self.goal
        if self.state is None:
            ar, ac = sr, sc
        else:
            ar, ac = self.state

        # Codes: 0 empty, 1 start, 2 goal, 3 agent
        grid[:, :] = 0
        grid[sr, sc] = 1
        grid[gr, gc] = 2
        grid[ar, ac] = 3

        cmap = ListedColormap(["#ffffff", "#7fc97f", "#fb8072", "#80b1d3"])

        created_fig = False
        if ax is None:
            fig, ax = plt.subplots(figsize=(self.C * 0.4, self.R * 0.4))
            created_fig = True
        else:
            fig = ax.figure

        ax.imshow(grid, cmap=cmap, origin="upper", interpolation="none")

        # Draw grid lines and remove ticks
        ax.set_xticks(np.arange(-0.5, self.C, 1.0))
        ax.set_yticks(np.arange(-0.5, self.R, 1.0))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(color="gray", linestyle="-", linewidth=0.5)
        ax.set_xlim(-0.5, self.C - 0.5)
        ax.set_ylim(self.R - 0.5, -0.5)
        ax.set_aspect("equal")

        # Annotate S/G/A and wind strengths
        for r in range(self.R):
            for c in range(self.C):
                if (r, c) == (sr, sc):
                    ax.text(c, r, "S", ha="center", va="center", fontsize=10, weight="bold")
                elif (r, c) == (gr, gc):
                    ax.text(c, r, "G", ha="center", va="center", fontsize=10, weight="bold")
                elif (r, c) == (ar, ac):
                    ax.text(c, r, "A", ha="center", va="center", fontsize=10, weight="bold")

        # Wind values above each column
        for c, w in enumerate(self.wind):
            ax.text(c, -0.35, str(int(w)), ha="center", va="bottom", fontsize=8)

        if show and created_fig:
            plt.show()

        return fig, ax
