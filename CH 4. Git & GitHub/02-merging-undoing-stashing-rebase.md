# Part 10: Merging

---

## 10.1 What is Merging?

Merging takes the changes from one branch and **combines them into another**. It's how feature work gets incorporated into the main codebase.

```text
Before merge:

main:    ●───●───●
                  \
feature:           ●───●

After merge:

main:    ●───●───●───────●  (merge commit)
                  \      /
feature:           ●───●
```

---

## 10.2 Merge a Branch

First, switch to the branch you want to merge **into** (usually `main`):

```bash
git switch main
```

Then merge the feature branch:

```bash
git merge feature-delete-task
```

### What happened?

Git combined all the commits from `feature-delete-task` into `main`. Your main branch now has the delete task feature.

---

## 10.3 Types of Merges

| Type | When it happens | Result |
|---|---|---|
| **Fast-forward** | No new commits on `main` since the branch was created | Git just moves `main` pointer forward. No merge commit. |
| **Merge commit** | Both branches have new commits | Git creates a new commit that combines both. |

```text
Fast-forward:
main:    ●───●───●───●───●
              (branch was here)

Merge commit:
main:    ●───●───●───M
                  \  /
feature:           ●
```

---

## 10.4 Clean Up

After merging, delete the feature branch (it's no longer needed):

```bash
git branch -d feature-delete-task
```

---

## 10.5 Try it

1. Make sure you're on `main`: `git switch main`
2. Merge: `git merge feature-delete-task`
3. Run `git log --oneline` — see the commits from the feature branch in main's history
4. Delete the branch: `git branch -d feature-delete-task`
5. Run `git branch` — only `main` should remain
6. Push to GitHub: `git push`

---

---

# Part 11: Merge Conflicts

---

## 11.1 Why Conflicts Happen

A merge conflict occurs when **two branches modify the same lines** in the same file. Git can't decide which version to keep, so it asks you.

---

## 11.2 Create a Conflict (Intentionally)

Let's create one to learn how to resolve it.

### Step 1: Create a Branch and Make a Change

```bash
git switch -c feature-search
```

Edit `tasks.py` — add this function at the end:

```python
def search_tasks(keyword):
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]
    if results:
        for t in results:
            print(f"  - {t['title']}")
    else:
        print("No matching tasks found.")
```

Commit:

```bash
git add tasks.py
git commit -m "Add search tasks feature"
```

### Step 2: Go Back to Main and Make a DIFFERENT Change to the SAME Area

```bash
git switch main
```

Edit `tasks.py` — add a **different** function at the end (same location):

```python
def count_tasks():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    print(f"Total: {total} | Done: {done} | Pending: {total - done}")
```

Commit:

```bash
git add tasks.py
git commit -m "Add task counter feature"
```

### Step 3: Merge and See the Conflict

```bash
git merge feature-search
```

```text
Auto-merging tasks.py
CONFLICT (content): Merge conflict in tasks.py
Automatic merge failed; fix conflicts and then commit the result.
```

---

## 11.3 Understanding Conflict Markers

Open `tasks.py`. You'll see something like:

```text
<<<<<<< HEAD
def count_tasks():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    print(f"Total: {total} | Done: {done} | Pending: {total - done}")
=======
def search_tasks(keyword):
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]
    if results:
        for t in results:
            print(f"  - {t['title']}")
    else:
        print("No matching tasks found.")
>>>>>>> feature-search
```

| Marker | Meaning |
|---|---|
| `<<<<<<< HEAD` | Start of **your current branch's** version |
| `=======` | Divider between the two versions |
| `>>>>>>> feature-search` | End of **the incoming branch's** version |

---

## 11.4 Resolve the Conflict

In this case, we want **both** functions. Remove the conflict markers and keep both:

```python
def count_tasks():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    print(f"Total: {total} | Done: {done} | Pending: {total - done}")

def search_tasks(keyword):
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]
    if results:
        for t in results:
            print(f"  - {t['title']}")
    else:
        print("No matching tasks found.")
```

### Stage and Complete the Merge

```bash
git add tasks.py
git commit -m "Merge feature-search: add search and keep counter"
```

### Clean Up

```bash
git branch -d feature-search
```

---

## 11.5 Try it

1. Follow the steps above to create and resolve a conflict
2. Run `git log --oneline --graph` — see the branching and merging history visualized
3. Push: `git push`

---

---

# Part 12: Undoing Changes

---

## 12.1 Overview

Git gives you multiple ways to undo work. Choosing the right one depends on **where** the change is.

| Situation | Command |
|---|---|
| Changed a file, want to discard changes | `git restore file.py` |
| Staged a file, want to unstage it | `git restore --staged file.py` |
| Committed something, want to safely undo | `git revert <commit>` |
| Want to move/remove commits locally | `git reset` |

---

## 12.2 Discard Unstaged Changes — `git restore`

### Concept

You modified a file but want to throw away the changes and go back to the last committed version.

### Setup

Edit `main.py` — add a bad line:

```python
print("THIS IS A MISTAKE")
```

### Command

```bash
git restore main.py
```

### What happened?

The file is restored to its last committed version. The bad line is gone.

> ⚠️ **Warning:** This **permanently discards** your changes. There's no undo for this.

---

## 12.3 Unstage a File — `git restore --staged`

### Concept

You staged a file by accident and want to remove it from the staging area (without losing your changes).

### Setup

```bash
git add main.py
```

### Command

```bash
git restore --staged main.py
```

### What happened?

The file is removed from the staging area but your changes in the working directory are **preserved**.

---

## 12.4 Undo a Commit Safely — `git revert`

### Concept

`git revert` creates a **new commit** that undoes the changes from a specific commit. It's safe because it doesn't erase history.

### Command

```bash
git revert HEAD
```

(This reverts the most recent commit. You can also use a specific commit hash.)

Git opens an editor for the commit message. Save and close to complete.

### When to use

When you've already pushed a commit and need to undo it. Since revert adds a new commit (rather than removing the old one), it's safe for shared branches.

---

## 12.5 Move/Remove Commits — `git reset`

### Concept

`git reset` moves the branch pointer backward, effectively removing commits from the branch history.

| Mode | Effect |
|---|---|
| `git reset --soft HEAD~1` | Undo last commit, keep changes **staged** |
| `git reset --mixed HEAD~1` | Undo last commit, keep changes **unstaged** (default) |
| `git reset --hard HEAD~1` | Undo last commit, **delete all changes** |

> ⚠️ **Danger:** `git reset --hard` permanently destroys changes. Never use `reset` on commits that have been pushed to a shared remote unless you fully understand the consequences.

### When to use

Only on **local, unpushed** commits. For pushed commits, use `git revert` instead.

---

## 12.6 Quick Comparison

```text
┌──────────────────────┐
│  Discard file changes │  →  git restore file.py
├──────────────────────┤
│  Unstage a file       │  →  git restore --staged file.py
├──────────────────────┤
│  Undo a pushed commit │  →  git revert <commit>    (safe)
├──────────────────────┤
│  Remove local commits │  →  git reset              (dangerous if pushed)
└──────────────────────┘
```

---

## 12.7 Try it

1. Edit `main.py`, add a random line, then discard: `git restore main.py`
2. Edit again, stage it: `git add main.py`, then unstage: `git restore --staged main.py`
3. Make a commit with a small change, then revert it: `git revert HEAD`
4. Check `git log --oneline` — you should see the revert commit

---

---

# Part 13: Stashing

---

## 13.1 The Problem

> You're halfway through building a feature, but your teammate reports a critical bug on `main`. You need to switch branches, but you're not ready to commit your half-done work.

**Stashing** saves your uncommitted changes temporarily so you can switch branches with a clean working directory.

---

## 13.2 Commands

### Save Changes to Stash

```bash
git stash
```

Your working directory is now clean. Changes are saved in a hidden stash.

### See All Stashes

```bash
git stash list
```

```text
stash@{0}: WIP on feature-delete-task: a1b2c3d Add delete task feature
```

### Restore Stashed Changes

```bash
git stash pop
```

This applies the most recent stash **and removes it** from the stash list.

### Apply Without Removing

```bash
git stash apply
```

Applies the stash but keeps it in the list (useful if you want to apply to multiple branches).

### Drop a Specific Stash

```bash
git stash drop stash@{0}
```

---

## 13.3 Practice

### Setup

```bash
git switch -c feature-export
```

Create a new file `export.py`:

```python
# Export tasks to a text file

def export_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            status = "DONE" if task["done"] else "TODO"
            f.write(f"[{status}] {task['title']}\n")
    print(f"Tasks exported to {filename}")
```

Now imagine an urgent bug report comes in. You're not ready to commit this.

```bash
git stash
```

Check:

```bash
git status
```

Clean! Now you can safely switch branches:

```bash
git switch main
# ... fix the bug, commit, push ...
git switch feature-export
```

Restore your work:

```bash
git stash pop
```

Your `export.py` changes are back.

### Try it

1. Follow the steps above
2. After popping the stash, finish the feature: `git add . && git commit -m "Add task export feature"`
3. Merge into main: `git switch main && git merge feature-export`
4. Clean up: `git branch -d feature-export`
5. Push: `git push`

---

---

# Part 14: Git Rebase

---

## 14.1 What is Rebase?

Rebase takes the commits from your branch and **replays them on top of** another branch. It creates a **linear, clean history** instead of a merge commit.

```text
Before rebase:

main:    ●───●───●───●
                  \
feature:           ●───●

After rebase:

main:    ●───●───●───●
                      \
feature:               ●───●
```

The feature branch now looks like it was started from the latest `main` commit.

---

## 14.2 Rebase vs Merge

| Merge | Rebase |
|---|---|
| Creates a merge commit | No merge commit, linear history |
| Preserves exact branch history | Rewrites commit history |
| Safe for shared branches | ⚠️ Dangerous for shared branches |
| History shows when branches merged | History looks like one straight line |

```text
Merge result:       ●───●───●───M
                         \  /
                          ●

Rebase result:      ●───●───●───●───●
                    (clean, linear)
```

---

## 14.3 Basic Rebase

```bash
git switch feature-branch
git rebase main
```

This replays your feature branch's commits on top of `main`'s latest commit.

After rebasing, you can do a fast-forward merge:

```bash
git switch main
git merge feature-branch
```

---

## 14.4 Interactive Rebase (Brief Introduction)

```bash
git rebase -i HEAD~3
```

This opens an editor showing your last 3 commits. You can:
- **pick** — keep the commit as-is
- **squash** — combine with the previous commit
- **reword** — change the commit message
- **drop** — remove the commit

Interactive rebase is powerful for cleaning up messy commit history before merging. You'll use it more as you gain experience.

---

## 14.5 The Golden Rule of Rebase

> ⚠️ **NEVER rebase commits that have been pushed to a shared remote branch.**

Rebasing rewrites commit history. If other people have those commits, their history will diverge from yours, causing chaos.

**Safe to rebase:** Your own local branches that no one else is using.

**Not safe to rebase:** `main`, or any branch others have pulled from.

---

## 14.6 Try it

1. Create a branch: `git switch -c feature-test-rebase`
2. Make a small commit (e.g., add a comment to any file)
3. Switch to main, make a different small commit
4. Switch back to your branch: `git switch feature-test-rebase`
5. Rebase: `git rebase main`
6. Run `git log --oneline --graph` — notice the linear history
7. Merge into main: `git switch main && git merge feature-test-rebase`
8. Clean up: `git branch -d feature-test-rebase`

---

---

# Part 15: Cherry-Pick

---

## 15.1 What is Cherry-Pick?

Cherry-pick lets you **copy a specific commit** from one branch to another without merging the entire branch.

### When is it useful?

- A bug fix was made on a feature branch but `main` needs it **now**
- You accidentally committed to the wrong branch
- You only want one specific change from a branch with many commits

---

## 15.2 Command

```bash
git cherry-pick <commit-hash>
```

### Example

```bash
git log --oneline feature-branch
# abc1234 Fix critical calculation bug    ← you want this one
# def5678 Add new UI layout
# ghi9012 Refactor database connection

git switch main
git cherry-pick abc1234
```

Now `main` has the bug fix without the other changes.

---

## 15.3 Try it

1. Create a branch, make 2 commits on it
2. Switch to main
3. Cherry-pick only the first commit: `git cherry-pick <hash>`
4. Run `git log --oneline` on main — you should see the cherry-picked commit
