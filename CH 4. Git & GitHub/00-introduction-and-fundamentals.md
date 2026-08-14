# Git & GitHub — Complete Practical Tutorial

> **Philosophy: Cover everything important. Explain briefly. Demonstrate practically.**

Throughout this tutorial, you'll build a single Python project called **TaskTracker** — a simple command-line task manager. Every Git concept will be practiced on this real project.

---

# Part 1: Git & Version Control Fundamentals

---

## 1.1 What is Version Control?

Version control is a system that **records changes to files over time** so you can recall specific versions later. Think of it as an unlimited "undo" system for your entire project that also lets multiple people work on the same codebase simultaneously.

### Why do you need it?

| Without Version Control | With Version Control |
|---|---|
| `project_final.py` | One clean project folder |
| `project_final_v2.py` | Complete history of every change |
| `project_FINAL_REAL.py` | Ability to undo any mistake |
| No idea who changed what | Clear record of who changed what and why |
| Overwriting each other's work | Multiple people work in parallel safely |

---

## 1.2 What is Git?

**Git** is a free, open-source **distributed version control system**. It runs **locally on your computer** and tracks every change you make to your project.

Key points:
- Created by Linus Torvalds (creator of Linux) in 2005
- It's **distributed** — every developer has the full project history on their machine
- It works **offline** — you don't need internet to track changes

---

## 1.3 What is GitHub?

**GitHub** is a **cloud platform** that hosts Git repositories online. It adds collaboration features like pull requests, issues, and project management on top of Git.

### Git vs GitHub

| Git | GitHub |
|---|---|
| A tool (software) | A platform (website/service) |
| Runs locally on your computer | Runs in the cloud |
| Tracks changes | Hosts repositories online |
| Works offline | Requires internet |
| Command-line tool | Web interface + API |
| Created by Linus Torvalds | Created by Tom Preston-Werner & others |

> **Git is the engine. GitHub is the garage where you park and share your car.**

---

## 1.4 Core Terminology

Learn these terms now. You'll use every one of them.

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git. Contains all files + their complete history. |
| **Local repository** | The Git repo on **your computer**. |
| **Remote repository** | The Git repo hosted **online** (e.g., on GitHub). |
| **Working directory** | The folder where you edit files. What you see in your file explorer. |
| **Staging area** | A preparation zone where you select which changes to include in the next commit. |
| **Commit** | A snapshot of your project at a specific point in time. Like a save point. |
| **Branch** | An independent line of development. Lets you work on features without affecting the main code. |
| **HEAD** | A pointer to the **current commit** you're working on. Usually points to the latest commit on your current branch. |
| **Remote** | A reference to a remote repository (like `origin` pointing to your GitHub repo). |
| **Pull Request (PR)** | A request to merge your branch's changes into another branch. Used for code review. |

---

## 1.5 The Basic Git Workflow

This is the flow you'll use hundreds of times:

```text
Working Directory     ← You edit files here
       ↓
   git add            ← Select changes to include
       ↓
Staging Area          ← Changes ready to be saved
       ↓
  git commit          ← Save a snapshot locally
       ↓
Local Repository      ← Full history on your machine
       ↓
   git push           ← Upload to the cloud
       ↓
GitHub (Remote)       ← Shared with the world
```

**Memorize this flow.** Everything else builds on it.

---

---

# Part 2: Git Installation & Configuration

---

## 2.1 Installing Git

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install git
```

**Linux (Fedora):**
```bash
sudo dnf install git
```

**macOS:**
```bash
brew install git
```

**Windows:**
Download from [git-scm.com](https://git-scm.com/downloads) and run the installer.

### Verify Installation

```bash
git --version
```

**Expected output:**
```text
git version 2.45.2
```

(Your version number may differ — that's fine.)

---

## 2.2 Configuring Git

Before using Git, tell it who you are. This information is attached to every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Verify Your Configuration

```bash
git config --list
```

**Expected output (relevant lines):**
```text
user.name=Your Name
user.email=you@example.com
```

### Global vs Local Configuration

| Scope | Command | Applies to |
|---|---|---|
| **Global** | `git config --global` | All repos on your machine |
| **Local** | `git config --local` | Only the current repo |

Local config overrides global. Useful when you use a different email for work vs personal projects.

---

## 2.3 HTTPS vs SSH

When connecting to GitHub, you have two options:

| Method | URL format | Authentication |
|---|---|---|
| **HTTPS** | `https://github.com/user/repo.git` | Username + Personal Access Token |
| **SSH** | `git@github.com:user/repo.git` | SSH key pair |

**For beginners:** Start with HTTPS. It's simpler to set up.

**For daily use:** SSH is more convenient — no password prompts after initial setup.

---

## 2.4 Setup Exercise

### Try it

1. Install Git (if not already installed)
2. Run `git --version` to confirm
3. Set your name and email using `git config --global`
4. Run `git config --list` and verify your name and email appear

---

---

# Part 3: Creating Your First Repository

---

## 3.1 Create the Project Folder

We'll build **TaskTracker** — a simple Python CLI task manager.

```bash
mkdir tasktracker
cd tasktracker
```

Create the first file:

```bash
touch main.py
```

Add this code to `main.py`:

```python
# TaskTracker - A simple command-line task manager

def show_menu():
    print("=== TaskTracker ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

if __name__ == "__main__":
    show_menu()
```

---

## 3.2 Initialize a Git Repository

### Command

```bash
git init
```

### What happened?

```text
Initialized empty Git repository in /path/to/tasktracker/.git/
```

Git created a hidden `.git` folder inside your project. This folder contains **everything Git needs** — the complete history, configuration, and internal data.

> **Never manually edit or delete the `.git` folder.** If you delete it, you lose all version history.

---

## 3.3 Check the Status

### Command

```bash
git status
```

### What happened?

```text
On branch main
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py

nothing added to commit but untracked files present
```

Git sees `main.py` but isn't tracking it yet. The file is **untracked** — Git knows it exists but isn't recording its changes.

> **Use `git status` constantly.** It's your best friend. Run it before and after every operation.

---

## 3.4 Try it

1. Create a new folder called `tasktracker`
2. Create `main.py` with the code above
3. Run `git init`
4. Run `git status`
5. Look at the `.git` folder: `ls -la` (you should see it listed)

---

---

# Part 4: Git's Three Main Areas

---

## 4.1 The Three Areas

Every file in a Git project exists in one of three states:

```text
┌─────────────────────┐
│  Working Directory   │  ← You edit files here
│  (Modified)          │
└────────┬────────────┘
         │ git add
         ▼
┌─────────────────────┐
│   Staging Area       │  ← Changes selected for next commit
│   (Staged)           │
└────────┬────────────┘
         │ git commit
         ▼
┌─────────────────────┐
│   Repository         │  ← Permanent snapshot saved
│   (Committed)        │
└─────────────────────┘
```

| State | Meaning |
|---|---|
| **Modified** | You changed the file, but haven't staged it |
| **Staged** | You marked the file to be included in the next commit |
| **Committed** | The file's snapshot is safely stored in the repository |

---

## 4.2 Stage Your File

### Command

```bash
git add main.py
```

### What happened?

The file moved from **Working Directory** → **Staging Area**. Verify:

```bash
git status
```

```text
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   main.py
```

The file is now **staged** — ready to be committed.

### Stage All Files at Once

```bash
git add .
```

The `.` means "everything in the current directory." Useful when you've changed multiple files.

---

## 4.3 Commit Your Changes

### Command

```bash
git commit -m "Initial commit: add main menu"
```

### What happened?

```text
[main (root-commit) a1b2c3d] Initial commit: add main menu
 1 file changed, 10 insertions(+)
 create mode 100644 main.py
```

Git saved a **permanent snapshot** of your project. The `a1b2c3d` is a unique ID (hash) for this commit.

---

## 4.4 Practice: Add More Code and Commit

Add a new file `tasks.py`:

```python
# Task management functions

tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Task added: {title}")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['title']}")
```

Now stage and commit:

```bash
git add tasks.py
git commit -m "Add task management functions"
```

### Try it

1. Create `tasks.py` with the code above
2. Run `git status` (see it as untracked)
3. Run `git add tasks.py`
4. Run `git status` again (see it as staged)
5. Run `git commit -m "Add task management functions"`
6. Run `git status` one more time (should be clean)
