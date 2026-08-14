# Part 5: Checking Changes & History

---

## 5.1 Check Status

You already know this one:

```bash
git status
```

It tells you:
- Which files are modified
- Which files are staged
- Which files are untracked

---

## 5.2 See What Changed — `git diff`

### Concept

`git diff` shows you **exactly what lines changed** in your working directory compared to the last commit. It's how you review changes before staging them.

### Setup

Edit `main.py` — update the `show_menu` function:

```python
# TaskTracker - A simple command-line task manager

from tasks import add_task, view_tasks

def show_menu():
    print("\n=== TaskTracker ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
```

### Command

```bash
git diff
```

### What happened?

Git shows you a line-by-line comparison:
- Lines starting with `-` (red) were **removed**
- Lines starting with `+` (green) were **added**

```diff
-    print("=== TaskTracker ===")
+    print("\n=== TaskTracker ===")
```

---

## 5.3 See Staged Changes — `git diff --staged`

After staging:

```bash
git add main.py
git diff
```

**Nothing shows!** `git diff` only compares **unstaged** changes.

To see **staged** changes (what will go into the next commit):

```bash
git diff --staged
```

| Command | Compares |
|---|---|
| `git diff` | Working directory vs staging area |
| `git diff --staged` | Staging area vs last commit |

---

## 5.4 View Commit History — `git log`

### Command

```bash
git log
```

### What happened?

```text
commit b4c5d6e... (HEAD -> main)
Author: Your Name <you@example.com>
Date:   Mon Aug 14 12:30:00 2026

    Add task management functions

commit a1b2c3d...
Author: Your Name <you@example.com>
Date:   Mon Aug 14 12:15:00 2026

    Initial commit: add main menu
```

Each entry shows the **commit hash**, author, date, and message.

### Compact View

```bash
git log --oneline
```

```text
b4c5d6e Add task management functions
a1b2c3d Initial commit: add main menu
```

Much cleaner for scanning history quickly.

---

## 5.5 Inspect a Specific Commit — `git show`

```bash
git show b4c5d6e
```

Shows the full details of that commit: the message, author, and the exact changes (diff) it introduced.

You can also use:

```bash
git show HEAD
```

This shows the **most recent** commit.

---

## 5.6 Practice

Now commit the changes to `main.py`:

```bash
git commit -m "Add interactive menu loop with user input"
```

### Try it

1. Run `git log --oneline` — you should see 3 commits
2. Pick any commit hash and run `git show <hash>`
3. Make a small change to any file, then run `git diff` to see the change
4. Stage the change, then run `git diff --staged`

---

---

# Part 6: Git Commits — Best Practices

---

## 6.1 What is a Commit?

A commit is a **permanent snapshot** of your project. Once committed, Git stores that exact state forever (unless you explicitly remove it). Each commit has:

- A unique **hash** (ID)
- An **author** and **timestamp**
- A **commit message** describing the change
- A **parent commit** (the commit before it)

---

## 6.2 Good vs Bad Commit Messages

Your commit message should explain **what** changed and **why**.

| ❌ Bad Messages | ✅ Good Messages |
|---|---|
| `fix` | `Fix crash when task list is empty` |
| `update` | `Add input validation to menu` |
| `stuff` | `Implement mark-task-done feature` |
| `asdfgh` | `Refactor task storage to use dictionary` |
| `changed some files` | `Add error handling for invalid menu options` |

### Rules of Thumb

1. Use **present tense** imperative: "Add feature" not "Added feature"
2. Keep the first line under **50 characters**
3. Be **specific** about what changed
4. One commit = **one logical change**

---

## 6.3 Small, Focused Commits

Don't wait until the end of the day and make one giant commit. Make **small, focused commits** as you complete each logical piece of work.

```text
Bad:  1 commit with 500 lines changed across 10 files
Good: 5 commits, each changing 1-2 files for a specific purpose
```

Why? Because small commits:
- Are easier to review
- Are easier to undo if something breaks
- Create a clear project history

---

## 6.4 Amending the Last Commit

### Concept

Made a typo in your last commit message? Forgot to include a file? `--amend` lets you **modify the most recent commit**.

### Command — Fix the Message

```bash
git commit --amend -m "Add interactive menu with user input handling"
```

### Command — Add a Forgotten File

```bash
git add forgotten_file.py
git commit --amend --no-edit
```

`--no-edit` keeps the original message unchanged.

> ⚠️ **Warning:** Only amend commits that haven't been pushed to a shared remote. Amending rewrites history, which can cause problems for collaborators.

---

## 6.5 Practice

Let's add the "mark done" feature. Add this to `tasks.py`:

```python
def mark_done(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Task {index} marked as done!")
    else:
        print("Invalid task number!")
```

Update `main.py` to import and use it:

```python
from tasks import add_task, view_tasks, mark_done
```

And add this to the `main()` function's elif chain (before the `elif choice == "4"` line):

```python
        elif choice == "3":
            view_tasks()
            num = int(input("Task number to mark done: "))
            mark_done(num)
```

### Try it

1. Stage both files: `git add .`
2. Commit: `git commit -m "Add mark-task-done feature"`
3. Run `git log --oneline` — you should see 4 commits now
4. Now pretend you made a typo. Fix it: `git commit --amend -m "Implement mark-task-done feature"`
5. Run `git log --oneline` again — notice the message changed but you still have 4 commits

---

---

# Part 7: GitHub & Remote Repositories

---

## 7.1 Create a GitHub Repository

1. Go to [github.com](https://github.com) and log in (or sign up)
2. Click the **+** icon in the top-right → **New repository**
3. Settings:
   - **Repository name:** `tasktracker`
   - **Description:** `A simple CLI task manager`
   - **Visibility:** Public (or Private)
   - **Do NOT** initialize with README, .gitignore, or license (we already have a local repo)
4. Click **Create repository**

GitHub will show you commands to connect your local repo. We'll use those next.

---

## 7.2 Connect Local Repo to GitHub

### Concept

`origin` is the **default name** for your remote repository. It's just a shortcut so you don't have to type the full URL every time.

### Commands

```bash
git remote add origin https://github.com/YOUR_USERNAME/tasktracker.git
git branch -M main
git push -u origin main
```

### What happened?

| Command | Purpose |
|---|---|
| `git remote add origin <URL>` | Links your local repo to the GitHub repo |
| `git branch -M main` | Renames your default branch to `main` |
| `git push -u origin main` | Pushes your code to GitHub; `-u` sets `origin main` as the default upstream |

After the `-u` flag, future pushes only need:

```bash
git push
```

---

## 7.3 Verify the Remote

```bash
git remote -v
```

```text
origin  https://github.com/YOUR_USERNAME/tasktracker.git (fetch)
origin  https://github.com/YOUR_USERNAME/tasktracker.git (push)
```

This confirms your local repo is connected to GitHub.

---

## 7.4 Try it

1. Create a new repository on GitHub called `tasktracker`
2. Run the three commands above (with your actual GitHub URL)
3. Refresh your GitHub page — your code should be there!
4. Run `git remote -v` to verify

---

---

# Part 8: Clone, Push, Pull & Fetch

---

## 8.1 Cloning a Repository

### Concept

`git clone` downloads a **complete copy** of a remote repository to your computer, including all files, branches, and history.

### Command

```bash
git clone https://github.com/YOUR_USERNAME/tasktracker.git
```

This creates a new `tasktracker` folder with everything. The remote `origin` is automatically set.

### When to use

- Starting work on a project for the first time
- Getting a copy of someone else's project

---

## 8.2 Push — Upload Changes

### Concept

`git push` sends your local commits to the remote repository.

```bash
git push
```

or explicitly:

```bash
git push origin main
```

---

## 8.3 Pull — Download & Merge Changes

### Concept

`git pull` downloads new commits from the remote **and merges them** into your current branch. It's essentially `git fetch` + `git merge` combined.

```bash
git pull
```

### When to use

When someone else (or you, from another computer) pushed changes to GitHub and you want to update your local copy.

---

## 8.4 Fetch — Download Without Merging

### Concept

`git fetch` downloads new data from the remote but **does not change your files**. It lets you see what's new before deciding to merge.

```bash
git fetch
```

After fetching, you can inspect changes and then merge manually if you want.

---

## 8.5 Comparison

| Command | Downloads? | Merges into your code? | Use when |
|---|---|---|---|
| `git clone` | ✅ Entire repo | N/A (first download) | Starting fresh on a new machine |
| `git push` | ❌ (uploads) | N/A | Sharing your commits with the team |
| `git pull` | ✅ New commits | ✅ Yes, automatically | You want the latest code now |
| `git fetch` | ✅ New commits | ❌ No | You want to check what's new first |

### Two-Computer Scenario

```text
Computer A (work)                    GitHub                    Computer B (home)
      │                                │                            │
      ├── git push ──────────────────→ │                            │
      │                                │ ←──────────── git pull ────┤
      │                                │                            │
      │                                │ ←──────────── git push ────┤
      ├── git pull ←────────────────── │                            │
```

You push from work, pull from home. Push from home, pull from work. The remote (GitHub) keeps everything in sync.

---

## 8.6 Try it

1. On GitHub, click on `main.py` → edit (pencil icon) → add a comment `# Updated from GitHub` at the top → commit on GitHub
2. Back in your terminal, run `git pull`
3. Open `main.py` — you should see the comment from GitHub
4. Make a local change, commit, and `git push`
5. Refresh GitHub — your change should appear

---

---

# Part 9: Branches

---

## 9.1 Why Branches?

Branches let you **work on features independently** without affecting the main codebase. Think of them as parallel timelines for your project.

```text
main:    ●───●───●───●───●
                  \
feature:           ●───●───●
```

The `main` branch stays stable while you experiment on `feature`.

---

## 9.2 Branch Commands

### See All Branches

```bash
git branch
```

```text
* main
```

The `*` indicates your current branch.

### Create and Switch to a New Branch

```bash
git switch -c feature-delete-task
```

This creates `feature-delete-task` and switches to it in one command.

### Switch Between Branches

```bash
git switch main
git switch feature-delete-task
```

### Delete a Branch

```bash
git branch -d feature-delete-task
```

(Only works if the branch has been merged. Use `-D` to force-delete.)

### Rename a Branch

```bash
git branch -m old-name new-name
```

---

## 9.3 `git switch` vs `git checkout`

| Command | Purpose | Note |
|---|---|---|
| `git switch` | Switch branches | Modern command (Git 2.23+) |
| `git switch -c` | Create + switch | Modern command |
| `git checkout` | Switch branches + more | Older command, does many things |
| `git checkout -b` | Create + switch | Older equivalent of `switch -c` |

**Use `git switch`** — it's clearer and focused on one job. `git checkout` still works but it's overloaded (it also restores files, which can be confusing).

---

## 9.4 Practice: Build a Feature

Let's add a "delete task" feature on a branch.

```bash
git switch -c feature-delete-task
```

Add this to `tasks.py`:

```python
def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed['title']}")
    else:
        print("Invalid task number!")
```

Update `main.py` — import the function:

```python
from tasks import add_task, view_tasks, mark_done, delete_task
```

And add to the menu and main loop. In `show_menu()`:

```python
    print("4. Delete Task")
    print("5. Exit")
```

In `main()`, add before the exit option:

```python
        elif choice == "4":
            view_tasks()
            num = int(input("Task number to delete: "))
            delete_task(num)
        elif choice == "5":
            print("Goodbye!")
            break
```

Commit on the feature branch:

```bash
git add .
git commit -m "Add delete task feature"
```

### Try it

1. Run `git log --oneline` — see commits on this branch
2. Switch back: `git switch main`
3. Open `tasks.py` — notice `delete_task` is **gone** (it only exists on the feature branch!)
4. Switch back: `git switch feature-delete-task` — it's back!
