# RL-COCO

## Getting Started

This project uses **uv** for dependency management and packaging. It replaces tools like pip, poetry, and virtualenv with a single, high-performance executable.

### 1. Install uv

If you do not have `uv` installed, install it via the official standalone installer:

**macOS / Linux:**
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

*Alternatively, if you already have Python installed, you can run `pip install uv`.*

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 3. Sync Dependencies

Initialize the environment and install dependencies. This command automatically creates a virtual environment and syncs it with the lockfile (`uv.lock`).

```bash
uv sync
```