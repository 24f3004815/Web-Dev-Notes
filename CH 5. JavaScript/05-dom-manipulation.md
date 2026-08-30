# Part 14: DOM Manipulation

This is where JavaScript becomes **visual**. The DOM (Document Object Model) is the browser's representation of your HTML as a tree of objects that JavaScript can manipulate.

---

## 14.1 Selecting Elements

```javascript
// By ID — returns ONE element
const header = document.getElementById("main-header");

// By CSS selector — returns FIRST match
const firstButton = document.querySelector(".btn");
const nav = document.querySelector("nav > ul");

// By CSS selector — returns ALL matches (NodeList)
const allButtons = document.querySelectorAll(".btn");
const allItems = document.querySelectorAll("li");

// Loop over NodeList
allButtons.forEach(btn => console.log(btn.textContent));
```

> **Prefer `querySelector` and `querySelectorAll`** — they use CSS selectors, which you already know.

---

## 14.2 Modifying Elements

```javascript
const el = document.querySelector("#title");

// Text content (safe — no HTML parsing)
el.textContent = "New Title";

// HTML content (parses HTML — use carefully)
el.innerHTML = "<strong>Bold Title</strong>";

// Styles
el.style.color = "red";
el.style.fontSize = "24px";
el.style.backgroundColor = "#1a1a2e";

// CSS Classes (preferred over inline styles)
el.classList.add("active");
el.classList.remove("hidden");
el.classList.toggle("dark-mode");   // add if absent, remove if present
el.classList.contains("active");    // true

// Attributes
el.setAttribute("data-id", "42");
el.getAttribute("data-id");        // "42"
el.removeAttribute("data-id");
```

---

## 14.3 Creating & Removing Elements

```javascript
// Create a new element
const newItem = document.createElement("li");
newItem.textContent = "New task";
newItem.classList.add("task-item");

// Add to the page
const list = document.querySelector("#task-list");
list.appendChild(newItem);                    // Add at end
list.prepend(newItem);                        // Add at beginning
list.insertBefore(newItem, referenceElement); // Insert before a specific element

// Remove from the page
newItem.remove();             // Modern way
// list.removeChild(newItem); // Older way

// Replace an element
const replacement = document.createElement("li");
replacement.textContent = "Replaced task";
list.replaceChild(replacement, oldElement);
```

---

## 14.4 Event Handling

Events are things that happen on the page — clicks, typing, scrolling, etc.

```javascript
const button = document.querySelector("#add-btn");

// Add an event listener
button.addEventListener("click", function(event) {
    console.log("Button clicked!");
    console.log("Event type:", event.type);        // "click"
    console.log("Target:", event.target);           // the <button> element
    console.log("Current target:", event.currentTarget); // same here
});

// Arrow function version
button.addEventListener("click", (e) => {
    console.log("Clicked!", e.target.textContent);
});

// Remove an event listener (must use named function)
function handleClick(e) {
    console.log("Clicked!");
}
button.addEventListener("click", handleClick);
button.removeEventListener("click", handleClick);
```

---

## 14.5 Common Events

| Event | Fires when |
|---|---|
| `click` | Element is clicked |
| `dblclick` | Element is double-clicked |
| `submit` | Form is submitted |
| `input` | Input value changes (real-time) |
| `change` | Input value changes (on blur) |
| `keydown` | Key is pressed down |
| `keyup` | Key is released |
| `mouseover` | Mouse enters element |
| `mouseout` | Mouse leaves element |
| `focus` | Element gains focus |
| `blur` | Element loses focus |
| `load` | Page finishes loading |
| `DOMContentLoaded` | HTML is parsed (before images load) |
| `scroll` | Page is scrolled |

---

## 14.6 `event.preventDefault()`

Stops the default browser behavior:

```javascript
// Prevent form from refreshing the page
const form = document.querySelector("#task-form");
form.addEventListener("submit", (e) => {
    e.preventDefault();  // Stop page refresh
    const input = document.querySelector("#task-input");
    console.log("Submitted:", input.value);
});

// Prevent link from navigating
const link = document.querySelector("a");
link.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("Link click intercepted");
});
```

---

## 14.7 Event Delegation

Instead of adding listeners to many child elements, add one listener to the parent and check which child was clicked:

```javascript
// ❌ Inefficient — listener on every button
document.querySelectorAll(".delete-btn").forEach(btn => {
    btn.addEventListener("click", () => { /* ... */ });
});

// ✅ Efficient — one listener on the parent
document.querySelector("#task-list").addEventListener("click", (e) => {
    if (e.target.classList.contains("delete-btn")) {
        const taskId = e.target.dataset.id;
        console.log("Delete task:", taskId);
    }
});
```

> Event delegation works because events **bubble up** — a click on a child also fires on every parent element.

---

## 14.8 TaskMaster: Build the UI

Now let's make TaskMaster visual! Update your files:

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TaskMaster</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="app">
        <header>
            <h1>📋 TaskMaster</h1>
            <p class="subtitle">Your personal task manager</p>
        </header>

        <form id="task-form">
            <input
                type="text"
                id="task-input"
                placeholder="What needs to be done?"
                required
                autofocus
            >
            <select id="priority-select">
                <option value="low">🟢 Low</option>
                <option value="medium" selected>🟡 Medium</option>
                <option value="high">🔴 High</option>
            </select>
            <button type="submit">Add Task</button>
        </form>

        <div class="filters">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="pending">Pending</button>
            <button class="filter-btn" data-filter="completed">Completed</button>
        </div>

        <ul id="task-list"></ul>

        <footer id="task-stats">
            <span id="task-count">0 tasks</span>
            <button id="clear-completed">Clear Completed</button>
        </footer>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

### `style.css`

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: #0f0f23;
    color: #e0e0e0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 40px 20px;
}

.app {
    width: 100%;
    max-width: 560px;
}

header {
    text-align: center;
    margin-bottom: 30px;
}

h1 {
    font-size: 2rem;
    background: linear-gradient(135deg, #e94560, #0f3460);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.subtitle {
    color: #888;
    margin-top: 5px;
}

/* Form */
#task-form {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
}

#task-input {
    flex: 1;
    padding: 12px 16px;
    border: 2px solid #2a2a4a;
    border-radius: 8px;
    background: #1a1a3e;
    color: #fff;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.2s;
}

#task-input:focus {
    border-color: #e94560;
}

#priority-select {
    padding: 12px;
    border: 2px solid #2a2a4a;
    border-radius: 8px;
    background: #1a1a3e;
    color: #fff;
    font-size: 0.9rem;
    cursor: pointer;
    outline: none;
}

#task-form button {
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    background: #e94560;
    color: #fff;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s, transform 0.1s;
}

#task-form button:hover {
    background: #c73e54;
}

#task-form button:active {
    transform: scale(0.96);
}

/* Filters */
.filters {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
}

.filter-btn {
    padding: 8px 16px;
    border: 1px solid #2a2a4a;
    border-radius: 20px;
    background: transparent;
    color: #888;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.2s;
}

.filter-btn:hover {
    color: #e0e0e0;
    border-color: #555;
}

.filter-btn.active {
    background: #e94560;
    color: #fff;
    border-color: #e94560;
}

/* Task List */
#task-list {
    list-style: none;
}

.task-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 16px;
    background: #1a1a3e;
    border-radius: 8px;
    margin-bottom: 8px;
    transition: background 0.2s, transform 0.2s;
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.task-item:hover {
    background: #22224a;
}

.task-item.completed .task-title {
    text-decoration: line-through;
    color: #666;
}

.task-checkbox {
    width: 20px;
    height: 20px;
    border: 2px solid #555;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: all 0.2s;
    background: transparent;
    color: transparent;
    font-size: 12px;
}

.task-checkbox:hover {
    border-color: #e94560;
}

.task-item.completed .task-checkbox {
    background: #e94560;
    border-color: #e94560;
    color: #fff;
}

.task-title {
    flex: 1;
    font-size: 0.95rem;
}

.task-priority {
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 12px;
    font-weight: 600;
}

.priority-high {
    background: rgba(233, 69, 96, 0.2);
    color: #e94560;
}

.priority-medium {
    background: rgba(255, 193, 7, 0.2);
    color: #ffc107;
}

.priority-low {
    background: rgba(76, 175, 80, 0.2);
    color: #4caf50;
}

.task-delete {
    background: none;
    border: none;
    color: #555;
    font-size: 1.2rem;
    cursor: pointer;
    padding: 4px;
    border-radius: 4px;
    transition: color 0.2s;
    line-height: 1;
}

.task-delete:hover {
    color: #e94560;
}

/* Footer */
footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 0;
    border-top: 1px solid #2a2a4a;
    margin-top: 8px;
}

#task-count {
    color: #888;
    font-size: 0.85rem;
}

#clear-completed {
    padding: 6px 14px;
    border: 1px solid #2a2a4a;
    border-radius: 6px;
    background: transparent;
    color: #888;
    cursor: pointer;
    font-size: 0.8rem;
    transition: all 0.2s;
}

#clear-completed:hover {
    color: #e94560;
    border-color: #e94560;
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: 40px;
    color: #555;
}
```

### `app.js`

```javascript
// TaskMaster — DOM-powered Task Manager

// ============ STATE ============
let tasks = [];
let nextId = 1;
let currentFilter = "all";

// ============ DOM ELEMENTS ============
const form = document.getElementById("task-form");
const input = document.getElementById("task-input");
const prioritySelect = document.getElementById("priority-select");
const taskList = document.getElementById("task-list");
const taskCount = document.getElementById("task-count");
const clearCompletedBtn = document.getElementById("clear-completed");
const filterButtons = document.querySelectorAll(".filter-btn");

// ============ TASK FUNCTIONS ============
function addTask(title, priority = "medium") {
    const task = {
        id: nextId++,
        title: title.trim(),
        completed: false,
        priority,
        createdAt: new Date().toISOString()
    };
    tasks.push(task);
    return task;
}

function deleteTask(id) {
    tasks = tasks.filter(t => t.id !== id);
}

function toggleTask(id) {
    const task = tasks.find(t => t.id === id);
    if (task) task.completed = !task.completed;
}

function clearCompleted() {
    tasks = tasks.filter(t => !t.completed);
}

function getFilteredTasks() {
    switch (currentFilter) {
        case "pending":   return tasks.filter(t => !t.completed);
        case "completed": return tasks.filter(t => t.completed);
        default:          return tasks;
    }
}

// ============ RENDER ============
function renderTasks() {
    const filtered = getFilteredTasks();

    if (filtered.length === 0) {
        taskList.innerHTML = `<div class="empty-state">No tasks yet. Add one above!</div>`;
    } else {
        taskList.innerHTML = filtered.map(task => `
            <li class="task-item ${task.completed ? "completed" : ""}" data-id="${task.id}">
                <span class="task-checkbox" data-action="toggle">${task.completed ? "✓" : ""}</span>
                <span class="task-title">${task.title}</span>
                <span class="task-priority priority-${task.priority}">${task.priority}</span>
                <button class="task-delete" data-action="delete" title="Delete task">&times;</button>
            </li>
        `).join("");
    }

    // Update counter
    const pending = tasks.filter(t => !t.completed).length;
    const total = tasks.length;
    taskCount.textContent = `${pending} pending / ${total} total`;
}

// ============ EVENT HANDLERS ============

// Form submit — add new task
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = input.value.trim();
    if (!title) return;

    addTask(title, prioritySelect.value);
    input.value = "";
    input.focus();
    renderTasks();
});

// Task list — event delegation for toggle and delete
taskList.addEventListener("click", (e) => {
    const action = e.target.dataset.action;
    if (!action) return;

    const taskItem = e.target.closest(".task-item");
    const id = Number(taskItem.dataset.id);

    if (action === "toggle") {
        toggleTask(id);
    } else if (action === "delete") {
        deleteTask(id);
    }

    renderTasks();
});

// Filter buttons
filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        filterButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentFilter = btn.dataset.filter;
        renderTasks();
    });
});

// Clear completed
clearCompletedBtn.addEventListener("click", () => {
    clearCompleted();
    renderTasks();
});

// Keyboard shortcut — Enter to add task (already handled by form submit)
input.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        input.value = "";
        input.blur();
    }
});

// ============ INITIAL RENDER ============
renderTasks();
console.log("TaskMaster is running! 🚀");
```

### What happened?

We built a **complete interactive task manager** using only vanilla JavaScript:

- **`document.querySelector()`** to find elements
- **`element.innerHTML`** to render dynamic content
- **`addEventListener()`** to handle user interactions
- **Event delegation** on the task list (one listener handles all toggle/delete clicks)
- **`e.preventDefault()`** to stop form from refreshing the page
- **Template literals** to build HTML strings
- **`data-*` attributes** to store task IDs and actions

### Try it

1. Open the files in your browser — you should have a working task manager!
2. Add several tasks with different priorities
3. Try toggling, deleting, and filtering tasks
4. Open the console — you should see "TaskMaster is running! 🚀"
5. **Challenge:** Add an "Edit" button to each task that lets you rename it
