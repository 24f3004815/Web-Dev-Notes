# Git & GitHub — Cheat Sheet 📋

> One-page reference for every command you need.

---

## Setup & Configuration

| Command | Purpose |
|---|---|
| `git --version` | Check Git version |
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "email"` | Set your email |
| `git config --list` | View all configuration |

---

## Creating Repositories

| Command | Purpose |
|---|---|
| `git init` | Initialize a new Git repo in current folder |
| `git clone <url>` | Download a remote repo to your machine |

---

## Basic Workflow

| Command | Purpose |
|---|---|
| `git status` | See what's changed, staged, untracked |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save a snapshot with a message |
| `git commit --amend` | Modify the last commit |

---

## Inspecting Changes & History

| Command | Purpose |
|---|---|
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git log` | View commit history |
| `git log --oneline` | Compact history view |
| `git log --oneline --graph --all` | Visual branch history |
| `git show <commit>` | Details of a specific commit |
| `git blame <file>` | Who changed each line |

---

## Branches

| Command | Purpose |
|---|---|
| `git branch` | List local branches |
| `git branch -a` | List all branches (including remote) |
| `git switch -c <branch>` | Create and switch to a new branch |
| `git switch <branch>` | Switch to an existing branch |
| `git branch -d <branch>` | Delete a merged branch |
| `git branch -D <branch>` | Force-delete a branch |
| `git branch -m <old> <new>` | Rename a branch |

---

## Merging & Rebasing

| Command | Purpose |
|---|---|
| `git merge <branch>` | Merge a branch into current branch |
| `git rebase <branch>` | Rebase current branch onto another |
| `git rebase -i HEAD~n` | Interactive rebase (squash, reword, etc.) |
| `git cherry-pick <commit>` | Copy a specific commit to current branch |

---

## Remote Repositories

| Command | Purpose |
|---|---|
| `git remote -v` | View remote connections |
| `git remote add origin <url>` | Connect to a remote repo |
| `git push` | Upload commits to remote |
| `git push -u origin <branch>` | Push and set upstream tracking |
| `git push origin --tags` | Push all tags |
| `git pull` | Download and merge remote changes |
| `git fetch` | Download remote changes (no merge) |

---

## Undoing Changes

| Command | Purpose |
|---|---|
| `git restore <file>` | Discard unstaged file changes |
| `git restore --staged <file>` | Unstage a file (keep changes) |
| `git revert <commit>` | Create a new commit that undoes a commit |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git reset --mixed HEAD~1` | Undo last commit, keep changes unstaged |
| `git reset --hard HEAD~1` | ⚠️ Undo last commit, DELETE changes |

---

## Stashing

| Command | Purpose |
|---|---|
| `git stash` | Save uncommitted changes temporarily |
| `git stash list` | View all stashes |
| `git stash pop` | Restore most recent stash and remove it |
| `git stash apply` | Restore most recent stash but keep it |
| `git stash drop stash@{n}` | Delete a specific stash |

---

## Tags & Releases

| Command | Purpose |
|---|---|
| `git tag` | List all tags |
| `git tag v1.0.0` | Create a lightweight tag |
| `git tag -a v1.0.0 -m "msg"` | Create an annotated tag |
| `git push origin v1.0.0` | Push a specific tag |
| `git push origin --tags` | Push all tags |

---

## .gitignore Essentials (Python)

```text
__pycache__/
*.pyc
.venv/
.env
.idea/
.vscode/
.DS_Store
```

---

## The Complete Workflow

```text
git init / git clone         ← Start
git switch -c feature        ← Branch
  ... edit files ...         ← Code
git add .                    ← Stage
git commit -m "message"      ← Commit
git push -u origin feature   ← Push
  → Create Pull Request      ← Review
  → Merge PR                 ← Merge
git switch main              ← Switch back
git pull                     ← Update
git tag -a v1.0.0 -m "msg"  ← Release
git push origin v1.0.0       ← Publish
```

---

## Danger Zone ⚠️

| Command | Risk |
|---|---|
| `git reset --hard` | Permanently deletes uncommitted work |
| `git push --force` | Overwrites remote history (breaks teammates) |
| `git rebase` on shared branches | Rewrites history others depend on |
| Committing `.env` files | Exposes secrets permanently |

> **Golden Rule:** Never rewrite history that has been pushed to a shared branch.

---

*Keep this cheat sheet handy. You'll use it less and less as the commands become muscle memory.* 🚀
