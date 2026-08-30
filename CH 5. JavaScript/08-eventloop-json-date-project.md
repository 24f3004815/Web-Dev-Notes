# Part 26: Event Loop & How JavaScript Works

---

## 26.1 JavaScript is Single-Threaded

JavaScript can only execute **one thing at a time**. So how does it handle async operations like `setTimeout`, `fetch`, and DOM events? The **Event Loop**.

```text
 ┌───────────────────┐
 │    Call Stack      │  ← Executes code (one at a time)
 │  ┌─────────────┐  │
 │  │ function()   │  │
 │  └─────────────┘  │
 └────────┬──────────┘
          │
          │  When async operation is encountered,
          │  it's handed off to Web APIs
          ▼
 ┌───────────────────┐
 │    Web APIs        │  ← Browser handles these in the background
 │  setTimeout()      │
 │  fetch()           │
 │  DOM events        │
 └────────┬──────────┘
          │  When done, callback goes to a queue
          ▼
 ┌───────────────────┐
 │  Callback Queue    │  ← setTimeout, setInterval callbacks
 ├───────────────────┤
 │  Microtask Queue   │  ← Promises (.then), queueMicrotask
 └────────┬──────────┘
          │
    Event Loop checks:
    "Is the call stack empty?"
    If yes → move next task from queue to stack
          │
          ▼
    Back to Call Stack
```

---

## 26.2 Order of Execution

```javascript
console.log("1. Synchronous");

setTimeout(() => console.log("2. setTimeout (macrotask)"), 0);

Promise.resolve().then(() => console.log("3. Promise (microtask)"));

console.log("4. Synchronous");

// Output:
// 1. Synchronous
// 4. Synchronous
// 3. Promise (microtask)    ← microtasks run BEFORE macrotasks
// 2. setTimeout (macrotask)
```

### Key Rule

> **Microtasks (Promises) always run before macrotasks (setTimeout)**, even if the setTimeout has a delay of 0.

---

## 26.3 Why This Matters

Understanding the event loop helps you:
- Debug unexpected execution order
- Know why `setTimeout(fn, 0)` doesn't run immediately
- Understand why heavy synchronous code blocks the UI
- Write better async code

> Don't overthink the event loop. Just remember: **sync first → microtasks → macrotasks**.

---

---

# Part 27: JSON

---

## 27.1 What is JSON?

**JSON** (JavaScript Object Notation) is a text format for storing and transmitting data. It looks like JavaScript objects but is a **string**.

```javascript
const obj = { name: "Alice", age: 25, active: true };

// Convert object → JSON string
const json = JSON.stringify(obj);
console.log(json);        // '{"name":"Alice","age":25,"active":true}'
console.log(typeof json); // "string"

// Convert JSON string → object
const parsed = JSON.parse(json);
console.log(parsed.name);  // "Alice"
console.log(typeof parsed); // "object"
```

---

## 27.2 JSON Rules

```javascript
// ✅ Valid JSON
'{"name": "Alice", "age": 25}'

// ❌ Invalid JSON (common mistakes)
"{'name': 'Alice'}"      // Single quotes not allowed
'{name: "Alice"}'        // Keys must be quoted
'{"age": undefined}'     // undefined not allowed
'{"fn": function(){}}'   // Functions not allowed
```

---

## 27.3 Pretty Printing

```javascript
const data = { name: "Alice", scores: [95, 87, 92] };
console.log(JSON.stringify(data, null, 2));
// {
//   "name": "Alice",
//   "scores": [
//     95,
//     87,
//     92
//   ]
// }
```

---

## 27.4 Where JSON is Used

| Use Case | Example |
|---|---|
| APIs | Server sends/receives JSON data |
| localStorage | Store objects as JSON strings |
| Config files | `package.json`, `tsconfig.json` |
| Data exchange | Between frontend and backend |

---

---

# Part 28: Date & Time

---

## 28.1 Creating Dates

```javascript
const now = new Date();                        // Current date/time
const specific = new Date("2025-12-25");       // From string
const fromParts = new Date(2025, 11, 25);      // Year, Month (0-indexed!), Day
const timestamp = new Date(1735084800000);     // From milliseconds
```

> **Months are 0-indexed!** January = 0, December = 11. This is a common gotcha.

---

## 28.2 Getting Date Parts

```javascript
const now = new Date();
console.log(now.getFullYear());    // 2025
console.log(now.getMonth());      // 0-11 (0 = January)
console.log(now.getDate());       // 1-31 (day of month)
console.log(now.getDay());        // 0-6 (0 = Sunday)
console.log(now.getHours());      // 0-23
console.log(now.getMinutes());    // 0-59
console.log(now.getSeconds());    // 0-59
```

---

## 28.3 Formatting & Timestamps

```javascript
const now = new Date();

console.log(now.toLocaleDateString());      // "8/28/2025" (locale-dependent)
console.log(now.toLocaleTimeString());      // "11:30:00 AM"
console.log(now.toISOString());             // "2025-08-28T06:00:00.000Z"
console.log(now.toLocaleString("en-IN"));   // Indian format

// Timestamp (milliseconds since Jan 1, 1970)
console.log(Date.now());                    // e.g., 1756368600000

// Time difference
const start = Date.now();
// ... some operation ...
const elapsed = Date.now() - start;
console.log(`Took ${elapsed}ms`);
```

> For complex date work, use libraries like **`date-fns`** or **`dayjs`** instead of the built-in `Date`.

---

---

# Part 29: Iterators & Generators (Brief)

---

## 29.1 Generators

A generator is a function that can **pause and resume** execution:

```javascript
function* counter() {
    let i = 0;
    while (true) {
        yield i++;
    }
}

const gen = counter();
console.log(gen.next()); // { value: 0, done: false }
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
```

### What happened?

- `function*` defines a generator
- `yield` pauses the function and returns a value
- `.next()` resumes execution until the next `yield`

---

## 29.2 Practical Use

```javascript
// Generate unique IDs
function* idGenerator(prefix = "id") {
    let id = 1;
    while (true) {
        yield `${prefix}_${id++}`;
    }
}

const ids = idGenerator("task");
console.log(ids.next().value); // "task_1"
console.log(ids.next().value); // "task_2"

// Iterate with for...of
function* range(start, end) {
    for (let i = start; i <= end; i++) {
        yield i;
    }
}

for (const num of range(1, 5)) {
    console.log(num); // 1, 2, 3, 4, 5
}
```

> Generators are advanced. Just know they exist — you'll encounter them in libraries and async patterns.

---

---

# Part 30: TaskMaster — Final Project

This is the complete, final version of TaskMaster incorporating **every major concept** from the tutorial. The project files from Part 14 (DOM Manipulation) form the foundation — the code below shows the key enhancements.

---

## 30.1 Features Implemented

| Concept | Where it's used |
|---|---|
| Variables & Types | Task properties, constants |
| Functions | `addTask`, `deleteTask`, `toggleTask`, etc. |
| Arrays | Task storage, `.map()`, `.filter()`, `.reduce()` |
| Objects | Task objects, options, stats |
| DOM Manipulation | Dynamic UI rendering |
| Events | Form submit, click delegation, keyboard shortcuts |
| Classes | `Task` and `TaskManager` classes |
| localStorage | Persistent task storage |
| Fetch API | Load sample tasks from API |
| Error Handling | Input validation, JSON parsing |
| ES6+ Features | Destructuring, spread, template literals, arrow functions |
| Closures | Event handler factories |
| `this` keyword | Class methods |
| Modules | Code organization (when using `type="module"`) |

---

## 30.2 Enhancements to Add (Practice Exercises)

Now that you have a working TaskMaster, challenge yourself:

1. **Edit tasks** — Double-click a task to edit its title inline
2. **Drag and drop** — Reorder tasks by dragging
3. **Due dates** — Add a date picker and highlight overdue tasks
4. **Categories/Tags** — Add tags with colored labels
5. **Search** — Add a search bar that filters tasks in real-time
6. **Dark/Light theme** — Toggle between themes, save preference
7. **Export/Import** — Download tasks as JSON, upload to restore
8. **Keyboard shortcuts** — `Ctrl+Enter` to add, `Delete` to remove
9. **Undo** — Implement undo for delete operations
10. **Animation** — Add smooth transitions when tasks are added/removed

Each of these exercises reinforces concepts from the tutorial.

---

## 30.3 What You've Learned

```text
Variables & Types
      ↓
Operators & Strings
      ↓
Conditionals & Loops
      ↓
Functions (declaration, expression, arrow)
      ↓
Arrays (map, filter, reduce)
      ↓
Objects (destructuring, spread)
      ↓
Scope & Closures
      ↓
DOM Manipulation & Events
      ↓
Error Handling
      ↓
Async/Await & Fetch API
      ↓
Classes & Modules
      ↓
localStorage & Browser APIs
      ↓
Build Real Applications ✅
```

---

## 30.4 Where to Go Next

| Topic | Why |
|---|---|
| **TypeScript** | Adds static typing to JavaScript — used in most professional projects |
| **React / Vue / Svelte** | Frontend frameworks for building complex UIs |
| **Node.js & Express** | Backend JavaScript — build APIs and servers |
| **Testing** | Jest, Vitest — write tests for your code |
| **Bundlers** | Vite, Webpack — build tools for production |
| **Git & GitHub** | Version control (see CH 4 in this course) |

> **You now have a solid JavaScript foundation.** The best way to improve is to **build projects** and read other people's code.
