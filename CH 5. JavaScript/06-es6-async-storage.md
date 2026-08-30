# Part 15: ES6+ Features

---

## 15.1 Features Already Covered

These ES6+ features were covered in previous sections:

- `let` and `const` (Part 3)
- Template literals (Part 5)
- Arrow functions (Part 9)
- Destructuring — arrays & objects (Parts 10, 11)
- Spread/rest operator (Parts 10, 11)
- Default parameters (Part 9)
- Enhanced object literals (Part 11)
- `for...of` loop (Part 8)
- Optional chaining `?.` (Part 4)
- Nullish coalescing `??` (Part 4)

This section covers the remaining ES6+ features.

---

## 15.2 `Map` — Key-Value Collection

A `Map` is like an object, but with important differences:

```javascript
const map = new Map();

// Set and get values
map.set("name", "Alice");
map.set(42, "a number key");     // Keys can be ANY type
map.set(true, "boolean key");

console.log(map.get("name"));    // "Alice"
console.log(map.get(42));        // "a number key"
console.log(map.size);           // 3
console.log(map.has("name"));    // true

// Delete
map.delete(42);

// Iterate
map.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// Also works with for...of
for (const [key, value] of map) {
    console.log(`${key}: ${value}`);
}
```

### Map vs Object

| Feature | `Map` | `Object` |
|---|---|---|
| Key types | Any (objects, numbers, etc.) | Strings and Symbols only |
| Size | `map.size` | `Object.keys(obj).length` |
| Iteration order | Guaranteed (insertion order) | Mostly insertion order |
| Performance | Better for frequent add/remove | Better for simple data |
| JSON support | ❌ (needs conversion) | ✅ |

---

## 15.3 `Set` — Unique Values

A `Set` stores unique values — no duplicates allowed:

```javascript
const set = new Set([1, 2, 3, 3, 3]);
console.log(set); // Set {1, 2, 3}

set.add(4);
set.add(1);        // Already exists — ignored
console.log(set.size); // 4
console.log(set.has(2)); // true

set.delete(2);

// Iterate
set.forEach(value => console.log(value));

// Common use: remove duplicates from an array
const numbers = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(numbers)];
console.log(unique); // [1, 2, 3, 4]

// Unique strings
const tags = ["js", "css", "js", "html", "css"];
const uniqueTags = [...new Set(tags)];
console.log(uniqueTags); // ["js", "css", "html"]
```

---

## 15.4 `Symbol` (Brief)

Symbols are **unique identifiers**. Each `Symbol()` call creates a completely unique value:

```javascript
const id1 = Symbol("id");
const id2 = Symbol("id");
console.log(id1 === id2); // false — always unique

// Used as unique object keys
const user = {
    [id1]: 123,
    name: "Alice"
};
console.log(user[id1]); // 123
```

> Symbols are mainly used in libraries and frameworks. As a beginner, just know they exist.

---

---

# Part 16: Error Handling

---

## 16.1 `try / catch / finally`

```javascript
try {
    // Code that might throw an error
    const data = JSON.parse("invalid json");
} catch (error) {
    // Handle the error
    console.error("Error:", error.message);
    // Output: Error: Unexpected token i in JSON at position 0
} finally {
    // Always runs — whether error occurred or not
    console.log("Cleanup done.");
}
```

---

## 16.2 `throw` — Create Custom Errors

```javascript
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero!");
    }
    return a / b;
}

try {
    console.log(divide(10, 0));
} catch (error) {
    console.error(error.message); // "Cannot divide by zero!"
}
```

---

## 16.3 Error Types

| Error Type | When it occurs |
|---|---|
| `Error` | Generic error |
| `TypeError` | Wrong type used (e.g., calling a non-function) |
| `ReferenceError` | Using a variable that doesn't exist |
| `SyntaxError` | Invalid syntax |
| `RangeError` | Value out of allowed range |

```javascript
// TypeError
// null.toString();   // TypeError: Cannot read properties of null

// ReferenceError
// console.log(xyz);  // ReferenceError: xyz is not defined

// RangeError
// [].length = -1;    // RangeError: Invalid array length
```

---

## 16.4 Custom Error Classes

```javascript
class ValidationError extends Error {
    constructor(field, message) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

function validateTask(title) {
    if (!title || title.trim() === "") {
        throw new ValidationError("title", "Task title cannot be empty");
    }
    if (title.length > 200) {
        throw new ValidationError("title", "Task title too long (max 200 chars)");
    }
    return true;
}

try {
    validateTask("");
} catch (error) {
    if (error instanceof ValidationError) {
        console.error(`Validation failed on '${error.field}': ${error.message}`);
    } else {
        console.error("Unexpected error:", error);
    }
}
// Output: Validation failed on 'title': Task title cannot be empty
```

---

## 16.5 TaskMaster: Error Handling

Add error handling to TaskMaster's `app.js`:

```javascript
// Enhanced addTask with validation
function addTask(title, priority = "medium") {
    try {
        // Validate
        if (!title || typeof title !== "string" || title.trim() === "") {
            throw new Error("Task title is required");
        }
        if (title.trim().length > 200) {
            throw new Error("Task title must be under 200 characters");
        }
        if (!["low", "medium", "high"].includes(priority)) {
            throw new Error(`Invalid priority: "${priority}"`);
        }

        // Create task
        const task = {
            id: nextId++,
            title: title.trim(),
            completed: false,
            priority,
            createdAt: new Date().toISOString()
        };
        tasks.push(task);
        return { success: true, task };
    } catch (error) {
        console.error("Failed to add task:", error.message);
        return { success: false, error: error.message };
    }
}

// Test
console.log(addTask("Valid task"));           // { success: true, task: {...} }
console.log(addTask(""));                     // { success: false, error: "..." }
console.log(addTask("Test", "urgent"));       // { success: false, error: "..." }
```

### Try it

1. What happens if you don't `catch` an error? Try removing the `catch` block
2. Write a `safeParse(jsonString)` function that uses `try/catch` to safely parse JSON and returns `null` on failure
3. When should you use `finally`? Give an example

---

---

# Part 17: Asynchronous JavaScript

This is one of the **most critical topics** in JavaScript. Understanding async is essential for real-world development.

---

## 17.1 Synchronous vs Asynchronous

```text
Synchronous:   Task 1 → wait → Task 2 → wait → Task 3 (blocking)
Asynchronous:  Task 1 → start Task 2 → Task 1 finishes → Task 2 finishes (non-blocking)
```

JavaScript is **single-threaded** — it can only do one thing at a time. Async operations (network requests, timers, file reads) are handled by the browser/Node.js and notify JavaScript when they're done.

---

## 17.2 Callbacks

A callback is a function passed to another function, to be called later:

```javascript
console.log("1. Start");

setTimeout(() => {
    console.log("2. This runs after 1 second");
}, 1000);

console.log("3. End");

// Output:
// 1. Start
// 3. End
// 2. This runs after 1 second  (after 1000ms)
```

### Callback Hell — The Problem

```javascript
// When callbacks are nested — hard to read and maintain
getData(function(a) {
    getMoreData(a, function(b) {
        getEvenMoreData(b, function(c) {
            processData(c, function(d) {
                // 😵 "Pyramid of Doom"
            });
        });
    });
});
```

> Promises were invented to solve this problem.

---

## 17.3 Promises

A Promise represents a **future value** — something that will be available later.

```javascript
// A promise is in one of three states:
// PENDING   → not yet resolved
// FULFILLED → completed successfully (resolved)
// REJECTED  → failed (rejected)

const promise = new Promise((resolve, reject) => {
    const success = true;
    setTimeout(() => {
        if (success) {
            resolve("Data loaded!");    // Fulfilled
        } else {
            reject("Something failed"); // Rejected
        }
    }, 1000);
});

// Consume the promise
promise
    .then(data => console.log(data))      // "Data loaded!"
    .catch(error => console.error(error))
    .finally(() => console.log("Done"));  // Always runs
```

### Promise Chaining

```javascript
fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response => response.json())    // Parse JSON
    .then(post => {
        console.log(post.title);
        return fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
    })
    .then(response => response.json())    // Parse user JSON
    .then(user => console.log(user.name))
    .catch(error => console.error("Error:", error));
```

### Promise Utility Methods

```javascript
const p1 = fetch("https://jsonplaceholder.typicode.com/posts/1");
const p2 = fetch("https://jsonplaceholder.typicode.com/posts/2");
const p3 = fetch("https://jsonplaceholder.typicode.com/posts/3");

// Promise.all — wait for ALL to complete (fails if ANY fails)
Promise.all([p1, p2, p3])
    .then(responses => Promise.all(responses.map(r => r.json())))
    .then(posts => console.log("All posts:", posts.length));

// Promise.race — resolves/rejects with the FIRST to complete
Promise.race([p1, p2, p3])
    .then(response => console.log("First response!"));

// Promise.allSettled — wait for ALL, even if some fail
Promise.allSettled([p1, p2, Promise.reject("Error")])
    .then(results => {
        results.forEach(r => {
            console.log(r.status); // "fulfilled" or "rejected"
        });
    });
```

---

## 17.4 Async/Await — The Modern Way

`async/await` makes async code **look and behave like synchronous code**:

```javascript
async function getPost() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
        const post = await response.json();
        console.log(post.title);
        return post;
    } catch (error) {
        console.error("Failed to fetch:", error);
    }
}

getPost();
```

### What happened?

- `async` marks a function as asynchronous (it always returns a Promise)
- `await` **pauses** execution until the Promise resolves
- The code reads top-to-bottom like synchronous code
- Error handling uses familiar `try/catch`

### Multiple Awaits

```javascript
async function getDashboardData() {
    try {
        // Sequential — one after another (slower)
        const posts = await fetch("/api/posts").then(r => r.json());
        const users = await fetch("/api/users").then(r => r.json());

        // Parallel — both at once (faster!)
        const [postsData, usersData] = await Promise.all([
            fetch("/api/posts").then(r => r.json()),
            fetch("/api/users").then(r => r.json())
        ]);

        return { posts: postsData, users: usersData };
    } catch (error) {
        console.error("Dashboard error:", error);
    }
}
```

> **Async/await is the modern, preferred way to handle async code.** Use it instead of `.then()` chains.

### Try it

1. What's the order of output for `console.log("A"); setTimeout(() => console.log("B"), 0); console.log("C");`?
2. Create a function `delay(ms)` that returns a Promise which resolves after `ms` milliseconds
3. Use `async/await` to fetch data from `https://jsonplaceholder.typicode.com/todos/1` and log the title

---

---

# Part 18: Fetch API & Working with APIs

---

## 18.1 What is an API?

An **API** (Application Programming Interface) is a way for programs to communicate. Web APIs let your JavaScript code request data from a server.

```text
Your App  →  HTTP Request  →  Server
Your App  ←  JSON Response ←  Server
```

---

## 18.2 GET Request — Fetch Data

```javascript
async function getPosts() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");

        // Check if request was successful
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const posts = await response.json();
        console.log(`Loaded ${posts.length} posts`);
        return posts;
    } catch (error) {
        console.error("Fetch failed:", error);
    }
}
```

---

## 18.3 POST Request — Send Data

```javascript
async function createPost(title, body) {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title,
                body,
                userId: 1
            })
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const newPost = await response.json();
        console.log("Created:", newPost);
        return newPost;
    } catch (error) {
        console.error("Create failed:", error);
    }
}

createPost("My Title", "My content here");
```

---

## 18.4 Other HTTP Methods

```javascript
// PUT — Replace entire resource
await fetch("https://jsonplaceholder.typicode.com/posts/1", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: 1, title: "Updated", body: "New body", userId: 1 })
});

// PATCH — Update partial resource
await fetch("https://jsonplaceholder.typicode.com/posts/1", {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: "Updated Title Only" })
});

// DELETE — Remove resource
await fetch("https://jsonplaceholder.typicode.com/posts/1", {
    method: "DELETE"
});
```

---

## 18.5 Response Status Codes

| Code | Meaning |
|---|---|
| `200` | OK — Request succeeded |
| `201` | Created — Resource created |
| `400` | Bad Request — Invalid data sent |
| `401` | Unauthorized — Not logged in |
| `403` | Forbidden — No permission |
| `404` | Not Found — Resource doesn't exist |
| `500` | Internal Server Error — Server problem |

---

## 18.6 TaskMaster: API Integration

Add API functionality to TaskMaster:

```javascript
// Fetch tasks from a public API and display them
async function loadSampleTasks() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos?_limit=5");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const apiTasks = await response.json();

        // Transform API data to our format
        apiTasks.forEach(apiTask => {
            const task = {
                id: nextId++,
                title: apiTask.title,
                completed: apiTask.completed,
                priority: apiTask.completed ? "low" : "medium",
                createdAt: new Date().toISOString()
            };
            tasks.push(task);
        });

        renderTasks();
        console.log(`Loaded ${apiTasks.length} tasks from API`);
    } catch (error) {
        console.error("Failed to load tasks:", error);
        // Show error in UI
        taskList.innerHTML = `<div class="empty-state">⚠️ Failed to load tasks. Try again later.</div>`;
    }
}

// Call on startup (optional — uncomment to auto-load)
// loadSampleTasks();
```

### Try it

1. Fetch a user from `https://jsonplaceholder.typicode.com/users/1` and display their name and email
2. What happens if you fetch a URL that doesn't exist? Does `fetch` throw an error or do you need to check `response.ok`?
3. Create a function that fetches posts and filters them to only show posts with a title longer than 50 characters

---

---

# Part 19: Local Storage & Session Storage

---

## 19.1 `localStorage` — Persistent Browser Storage

Data stays even after the browser is closed:

```javascript
// Store data
localStorage.setItem("username", "Alice");
localStorage.setItem("theme", "dark");

// Retrieve data
const name = localStorage.getItem("username");
console.log(name); // "Alice"

// Remove one item
localStorage.removeItem("theme");

// Clear all data
localStorage.clear();
```

---

## 19.2 Storing Objects and Arrays

`localStorage` only stores **strings**. Use `JSON.stringify()` and `JSON.parse()`:

```javascript
// Save
const user = { name: "Alice", age: 25 };
localStorage.setItem("user", JSON.stringify(user));

// Load
const saved = JSON.parse(localStorage.getItem("user"));
console.log(saved.name); // "Alice"

// Save array
const tasks = [{ id: 1, title: "Learn JS" }, { id: 2, title: "Build project" }];
localStorage.setItem("tasks", JSON.stringify(tasks));

// Load array
const loadedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
console.log(loadedTasks.length); // 2
```

> Always provide a fallback (`|| []`, `|| {}`) in case `localStorage` returns `null`.

---

## 19.3 `localStorage` vs `sessionStorage`

| Feature | `localStorage` | `sessionStorage` |
|---|---|---|
| Persists | Until cleared manually | Until tab/window closes |
| Scope | All tabs (same origin) | Current tab only |
| Size | ~5–10 MB | ~5–10 MB |
| Use case | User preferences, saved data | Temporary form data, session state |

---

## 19.4 TaskMaster: Persistent Tasks

Add persistence to TaskMaster's `app.js`:

```javascript
// ============ STORAGE ============
const STORAGE_KEY = "taskmaster_tasks";
const STORAGE_ID_KEY = "taskmaster_nextId";

function saveTasks() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
    localStorage.setItem(STORAGE_ID_KEY, String(nextId));
}

function loadTasks() {
    try {
        const saved = localStorage.getItem(STORAGE_KEY);
        tasks = saved ? JSON.parse(saved) : [];
        nextId = Number(localStorage.getItem(STORAGE_ID_KEY)) || 1;
    } catch (error) {
        console.error("Failed to load tasks:", error);
        tasks = [];
        nextId = 1;
    }
}

// Call saveTasks() after every modification:
// In addTask:  tasks.push(task); saveTasks();
// In deleteTask: tasks = tasks.filter(...); saveTasks();
// In toggleTask: task.completed = !task.completed; saveTasks();
// In clearCompleted: tasks = tasks.filter(...); saveTasks();

// Load tasks on startup instead of starting empty
loadTasks();
renderTasks();
```

### What happened?

Now tasks persist across page refreshes! When you add, toggle, or delete a task, `saveTasks()` writes the entire `tasks` array to `localStorage` as a JSON string. When the page loads, `loadTasks()` reads and parses it back.

### Try it

1. Add some tasks, refresh the page — they should still be there
2. Open DevTools → Application → Local Storage to see the stored data
3. What happens if someone manually edits the localStorage data to invalid JSON? Does your `loadTasks` handle it?
