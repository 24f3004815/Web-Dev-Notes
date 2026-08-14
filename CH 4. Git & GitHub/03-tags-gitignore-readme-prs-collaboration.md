# Part 16: Tags & Releases

---

## 16.1 What are Tags?

Tags are **named markers** on specific commits. They're used to mark release versions — points in history you want to easily find later.

Think of them as bookmarks in your project's timeline.

---

## 16.2 Creating Tags

### Lightweight Tag

```bash
git tag v1.0.0
```

Marks the current commit as `v1.0.0`.

### Annotated Tag (Recommended)

```bash
git tag -a v1.0.0 -m "First stable release"
```

Annotated tags store extra info: the tagger's name, date, and a message.

### List All Tags

```bash
git tag
```

### Tag a Specific Commit

```bash
git tag -a v0.9.0 <commit-hash> -m "Beta release"
```

---

## 16.3 Push Tags to GitHub

Tags are **not pushed** by default. You must push them explicitly:

```bash
git push origin v1.0.0
```

Or push all tags at once:

```bash
git push origin --tags
```

---

## 16.4 GitHub Releases

On GitHub, you can create **Releases** from tags:

1. Go to your repo → **Releases** → **Create a new release**
2. Choose the tag `v1.0.0`
3. Add a title and description of what's in this release
4. Click **Publish release**

Releases are user-friendly — they provide download links and changelogs for your project.

---

## 16.5 Try it

1. Tag your current state: `git tag -a v1.0.0 -m "First release with all basic features"`
2. Push: `git push origin v1.0.0`
3. On GitHub, go to your repo → Releases → create a release from the tag

---

---

# Part 17: .gitignore

---

## 17.1 Why .gitignore?

Some files should **never** be committed:
- **Passwords, API keys, secrets** — security risk!
- **Virtual environments** (`venv/`) — too large, machine-specific
- **Cache/compiled files** (`__pycache__/`, `*.pyc`) — auto-generated
- **IDE settings** (`.vscode/`, `.idea/`) — personal preferences
- **OS files** (`.DS_Store`, `Thumbs.db`) — system junk

`.gitignore` tells Git to **ignore these files** completely.

---

## 17.2 Create .gitignore

Create a `.gitignore` file in your project root:

```text
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.egg-info/
dist/
build/

# Virtual environments
.venv/
venv/
env/

# Environment variables and secrets
.env
.env.local
*.key

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Output files
tasks.txt
```

---

## 17.3 Important Rules

1. **Add `.gitignore` early** — ideally in your first commit
2. `.gitignore` only affects **untracked** files. If a file is already tracked, adding it to `.gitignore` won't remove it. You need:
   ```bash
   git rm --cached filename
   ```
3. Each line in `.gitignore` is a pattern:
   - `*.pyc` — ignore all `.pyc` files
   - `logs/` — ignore the entire `logs` directory
   - `!important.log` — do NOT ignore this file (exception)

---

## 17.4 Critical Warning

> 🔴 **NEVER commit passwords, API keys, tokens, or secrets.** Once pushed to GitHub, they're exposed forever (even if you delete the file later, it remains in history). Use environment variables and `.env` files instead.

---

## 17.5 Try it

1. Create `.gitignore` with the content above
2. Create a test file: `echo "SECRET_KEY=abc123" > .env`
3. Run `git status` — `.env` should NOT appear (it's ignored!)
4. Commit `.gitignore`: `git add .gitignore && git commit -m "Add .gitignore"`
5. Push: `git push`

---

---

# Part 18: README.md

---

## 18.1 What Makes a Good README?

A README is the **front page** of your project on GitHub. It should quickly tell visitors:

| Section | Purpose |
|---|---|
| **Project name** | What is this? |
| **Description** | What does it do? |
| **Features** | What can it do? |
| **Installation** | How to set it up? |
| **Usage** | How to use it? |
| **Technologies** | What's it built with? |
| **License** | Can I use it? |

---

## 18.2 Create a README for TaskTracker

Create `README.md`:

```markdown
# TaskTracker 📋

A simple command-line task manager built with Python.

## Features

- ✅ Add tasks
- 📋 View all tasks
- ✔️ Mark tasks as done
- 🗑️ Delete tasks
- 🔍 Search tasks
- 📊 Task statistics
- 📤 Export tasks to file

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/tasktracker.git
cd tasktracker
python main.py
```

## Usage

```bash
$ python main.py

=== TaskTracker ===
1. Add Task
2. View Tasks
3. Mark Task Done
4. Delete Task
5. Exit

Choose an option:
```

## Technologies

- Python 3.x

## License

This project is open source and available under the [MIT License](LICENSE).
```

---

## 18.3 Try it

1. Create `README.md` with the content above (use your actual GitHub username)
2. Commit: `git add README.md && git commit -m "Add project README"`
3. Push: `git push`
4. Visit your GitHub repo — the README renders beautifully on the main page!

---

---

# Part 19: GitHub Issues

---

## 19.1 What are Issues?

GitHub Issues are a **built-in task tracker** for your project. They're used for:

- 🐛 **Bug reports** — "The app crashes when the task list is empty"
- 💡 **Feature requests** — "Add the ability to set task priorities"
- 📝 **Tasks/To-dos** — "Write unit tests for task functions"
- ❓ **Questions** — "How do I configure the export format?"

---

## 19.2 Creating an Issue

1. Go to your GitHub repo → **Issues** tab → **New issue**
2. Fill in:
   - **Title:** `Add task priority levels`
   - **Description:**
     ```
     ## Feature Request

     Allow users to assign priority levels to tasks (Low, Medium, High).

     ### Expected behavior
     - When adding a task, user can optionally set a priority
     - Tasks are displayed with their priority level
     - Tasks can be sorted by priority

     ### Additional context
     This will help users focus on the most important tasks first.
     ```
3. Optionally add:
   - **Labels** (e.g., `enhancement`, `bug`, `good first issue`)
   - **Assignees** (who should work on this)
4. Click **Submit new issue**

---

## 19.3 Closing Issues with Commits

You can automatically close an issue by referencing it in a commit message:

```bash
git commit -m "Add task priorities (closes #1)"
```

When this commit is merged into the default branch, GitHub automatically closes issue #1.

Keywords that close issues: `closes`, `fixes`, `resolves` (followed by `#issue-number`).

---

## 19.4 Try it

1. Create an issue on your `tasktracker` repo with the title "Add task priority levels"
2. Note the issue number (probably `#1`)
3. You'll reference this in a future commit

---

---

# Part 20: Pull Requests

---

## 20.1 What is a Pull Request?

A Pull Request (PR) is a **request to merge changes** from one branch into another. It's the core of team collaboration on GitHub because it allows:

- **Code review** — teammates can read your changes before they're merged
- **Discussion** — comments and suggestions on specific lines
- **Quality checks** — automated tests can run before merging

---

## 20.2 The Pull Request Workflow

```text
1. Create a branch
         ↓
2. Make changes & commit
         ↓
3. Push the branch to GitHub
         ↓
4. Create a Pull Request on GitHub
         ↓
5. Review (discussion, changes)
         ↓
6. Merge the PR
         ↓
7. Delete the branch
```

---

## 20.3 Practice: Create a Full PR

### Step 1: Create a Branch

```bash
git switch -c feature-priority
```

### Step 2: Make Changes

Update `tasks.py` — modify the `add_task` function:

```python
def add_task(title, priority="medium"):
    tasks.append({"title": title, "done": False, "priority": priority})
    print(f"Task added: {title} [{priority.upper()}]")
```

Update the `view_tasks` function to show priority:

```python
def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        pri = task.get("priority", "medium").upper()
        print(f"  {i}. [{status}] [{pri}] {task['title']}")
```

Update `main.py` in the "Add Task" section:

```python
        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (low/medium/high): ").strip() or "medium"
            add_task(title, priority)
```

### Step 3: Commit

```bash
git add .
git commit -m "Add task priority levels (closes #1)"
```

### Step 4: Push the Branch

```bash
git push -u origin feature-priority
```

### Step 5: Create the PR on GitHub

1. Go to your repo on GitHub
2. You'll see a banner: **"feature-priority had recent pushes — Compare & pull request"**
3. Click **Compare & pull request**
4. Fill in:
   - **Title:** `Add task priority levels`
   - **Description:** `Implements priority levels for tasks. Users can set low/medium/high priority when adding tasks. Closes #1.`
5. Click **Create pull request**

### Step 6: Review the PR

- Click on the **Files changed** tab to see all code changes
- You (or a teammate) can leave comments on specific lines
- You can request changes or approve

### Step 7: Merge the PR

1. Click **Merge pull request** → **Confirm merge**
2. Click **Delete branch** (on GitHub)

### Step 8: Update Local

```bash
git switch main
git pull
git branch -d feature-priority
```

---

## 20.4 Try it

Follow all the steps above to create your first Pull Request. This is the workflow you'll use in every professional project.

---

---

# Part 21: Forking & Open Source

---

## 21.1 What is Forking?

A **fork** is a **personal copy** of someone else's repository on your GitHub account. You can modify your fork freely without affecting the original project.

---

## 21.2 The Open Source Contribution Workflow

```text
1. Fork the project on GitHub
         ↓
2. Clone YOUR fork to your computer
         ↓
3. Create a feature branch
         ↓
4. Make changes & commit
         ↓
5. Push to YOUR fork
         ↓
6. Create a Pull Request to the ORIGINAL repo
         ↓
7. Maintainer reviews and merges
```

### Commands

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/some-project.git
cd some-project

# Add the original repo as "upstream"
git remote add upstream https://github.com/ORIGINAL_OWNER/some-project.git

# Create a branch
git switch -c fix-typo

# Make changes, commit
git add .
git commit -m "Fix typo in README"

# Push to YOUR fork
git push origin fix-typo

# Then create a PR on GitHub from your fork to the original repo
```

### Keep Your Fork Updated

```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

---

## 21.3 Try it

1. Find a public repository on GitHub (or use a friend's)
2. Fork it
3. Clone your fork
4. Create a branch, make a small change, commit, push
5. Create a Pull Request to the original repo

---

---

# Part 22: GitHub Collaboration

---

## 22.1 Team Workflow

In a professional team, the workflow looks like this:

```text
main (protected)
  ↓
developer creates feature branch
  ↓
development work + commits
  ↓
push branch to GitHub
  ↓
create Pull Request
  ↓
code review by teammates
  ↓
address review comments
  ↓
PR approved
  ↓
merge into main
  ↓
delete feature branch
```

---

## 22.2 Key Concepts

### Code Review

Every PR should be reviewed by at least one other developer. Reviewers check for:
- Bugs and logic errors
- Code quality and readability
- Following project conventions
- Test coverage

### Protected Branches

Teams often **protect** the `main` branch so that:
- No one can push directly to `main`
- All changes must go through a Pull Request
- PRs require at least one approval before merging
- Automated tests must pass

You can set this up in GitHub → Settings → Branches → Branch protection rules.

### Keeping Branches Updated

Before merging a PR, update your branch with the latest `main`:

```bash
git switch feature-branch
git pull origin main
# or
git rebase main
```

This prevents merge conflicts in the PR.

### PR Comments

Reviewers can:
- Leave general comments
- Comment on specific lines of code
- Suggest code changes that the author can accept with one click
- Request changes (blocking the merge until addressed)

---

## 22.3 Try it

1. Invite a friend as a collaborator (Settings → Collaborators)
2. Have them clone the repo and create a branch
3. They push and create a PR
4. You review the PR, leave a comment, and merge it

(If no friend is available, practice by creating a PR and reviewing it yourself.)
