# Part 23: GitHub Actions — Introduction

---

## 23.1 What is CI/CD?

| Term | Full Name | Meaning |
|---|---|---|
| **CI** | Continuous Integration | Automatically test code when changes are pushed |
| **CD** | Continuous Deployment | Automatically deploy code after tests pass |

**GitHub Actions** is GitHub's built-in CI/CD tool. It runs automated tasks (called **workflows**) whenever certain events happen (push, PR, etc.).

---

## 23.2 Key Terms

| Term | Meaning |
|---|---|
| **Workflow** | An automated process defined in a YAML file |
| **Job** | A set of steps that run on the same machine |
| **Step** | A single task within a job (run a command, use an action) |
| **Trigger** | The event that starts the workflow (push, pull_request, etc.) |
| **Runner** | The virtual machine that executes your workflow |

---

## 23.3 Create a Simple Workflow

First, create a test file for our project. Create `test_tasks.py`:

```python
import unittest
from tasks import tasks, add_task, view_tasks, mark_done, delete_task

class TestTaskTracker(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Test task")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test task")
        self.assertFalse(tasks[0]["done"])

    def test_mark_done(self):
        add_task("Test task")
        mark_done(1)
        self.assertTrue(tasks[0]["done"])

    def test_mark_done_invalid(self):
        add_task("Test task")
        mark_done(5)  # Should print error, not crash
        self.assertFalse(tasks[0]["done"])

    def test_delete_task(self):
        add_task("Task 1")
        add_task("Task 2")
        delete_task(1)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Task 2")

if __name__ == "__main__":
    unittest.main()
```

Commit the test file:

```bash
git add test_tasks.py
git commit -m "Add unit tests for task functions"
git push
```

---

Now create the GitHub Actions workflow file:

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/test.yml`:

```yaml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Run tests
        run: python -m unittest test_tasks.py -v
```

### What this does:

1. **Triggers** on every push to `main` or PR targeting `main`
2. **Checks out** your code on a fresh Ubuntu machine
3. **Installs** Python
4. **Runs** your tests

---

## 23.4 Deploy It

```bash
git add .github/workflows/test.yml
git commit -m "Add GitHub Actions CI workflow"
git push
```

Go to your repo on GitHub → **Actions** tab. You'll see your workflow running!

A ✅ green check means all tests passed. A ❌ red X means something failed.

---

## 23.5 Try it

1. Create `test_tasks.py` and `.github/workflows/test.yml` as shown above
2. Push to GitHub
3. Go to the **Actions** tab and watch the workflow run
4. Try making a test fail (change an assertion), push, and see it fail in Actions
5. Fix it and push again — green check!

---

---

# Part 24: Git Aliases & Useful Commands

---

## 24.1 Useful Commands You Should Know

### Visual Log

```bash
git log --oneline --graph --all
```

Shows a beautiful ASCII graph of your branch history. Add `--all` to see all branches.

```text
* d4e5f6a (HEAD -> main) Add CI workflow
* b2c3d4e Merge feature-priority
|\
| * a1b2c3d Add task priority levels
|/
* 9e8f7g6 Add task export feature
* 7c6d5e4 Merge feature-search
```

### See All Branches (Including Remote)

```bash
git branch -a
```

### Check Remote URLs

```bash
git remote -v
```

### See Changes Between Branches

```bash
git diff main..feature-branch
```

### See Who Changed Each Line

```bash
git blame filename.py
```

Shows who last modified each line — useful for tracking down when a bug was introduced.

### Find a Bug with Bisect

```bash
git bisect start
git bisect bad          # Current commit is broken
git bisect good a1b2c3d # This old commit was working
# Git checks out a middle commit, you test, and tell it good/bad
# Repeat until Git finds the exact commit that introduced the bug
git bisect reset
```

---

## 24.2 Git Aliases

Tired of typing long commands? Create shortcuts:

```bash
git config --global alias.s "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.cm "commit -m"
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 HEAD"
```

Now you can use:

```bash
git s          # instead of git status
git lg         # instead of git log --oneline --graph --all
git cm "msg"   # instead of git commit -m "msg"
git last       # show the last commit
```

---

## 24.3 Try it

1. Run `git log --oneline --graph --all` on your project
2. Set up at least 2 aliases from above
3. Use your aliases — `git s`, `git lg`
4. Run `git blame main.py` to see the annotation

---

---

# Part 25: Real-World Project Summary

---

## 25.1 What You Built

Throughout this tutorial, you built **TaskTracker** — a Python CLI task manager. Here's everything you practiced:

| # | Concept | What You Did |
|---|---|---|
| 1 | Create project | Created `tasktracker` folder with `main.py` |
| 2 | Initialize Git | `git init` |
| 3 | Configure Git | Set name and email |
| 4 | Create .gitignore | Added Python-specific ignore rules |
| 5 | Create README | Wrote a professional README.md |
| 6 | Stage & commit | `git add` → `git commit` multiple times |
| 7 | Inspect history | `git log`, `git diff`, `git show` |
| 8 | Create GitHub repo | Set up remote repository |
| 9 | Push to GitHub | `git push -u origin main` |
| 10 | Clone | `git clone` (simulated second machine) |
| 11 | Create branches | `feature-delete-task`, `feature-search`, etc. |
| 12 | Make changes on branches | Added features on isolated branches |
| 13 | Merge | Combined feature branches into main |
| 14 | Merge conflict | Intentionally created and resolved a conflict |
| 15 | Stash | Saved half-done work, switched branches, restored |
| 16 | Rebase | Practiced linear history |
| 17 | Cherry-pick | Copied a specific commit |
| 18 | Create a PR | Full GitHub Pull Request workflow |
| 19 | Create an Issue | Bug report / feature request |
| 20 | Tag a release | `v1.0.0` |
| 21 | GitHub Actions | Automated testing on push |
| 22 | Amend commits | Fixed commit messages |
| 23 | Undo changes | `restore`, `revert`, `reset` |

---

## 25.2 Final Project Structure

```text
tasktracker/
├── .git/
├── .github/
│   └── workflows/
│       └── test.yml
├── .gitignore
├── README.md
├── main.py
├── tasks.py
├── export.py
└── test_tasks.py
```

---

## 25.3 The Complete Developer Workflow

This is the workflow you'll use in real jobs and projects:

```text
1. Create/Clone Repository
         ↓
2. Create a Feature Branch
         ↓
3. Make Changes
         ↓
4. Stage Changes (git add)
         ↓
5. Commit (git commit)
         ↓
6. Push Branch (git push)
         ↓
7. Create Pull Request
         ↓
8. Code Review
         ↓
9. Merge into Main
         ↓
10. Tag a Release
         ↓
11. Deploy / Celebrate 🎉
```

---

You now have the skills to use Git and GitHub confidently in any project. Keep practicing — the more you use these commands, the more natural they become.
