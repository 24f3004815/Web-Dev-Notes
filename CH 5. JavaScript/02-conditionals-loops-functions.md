# Part 7: Booleans & Conditional Statements

---

## 7.1 Booleans

A boolean is either `true` or `false`. But JavaScript also treats other values as "truthy" or "falsy" in conditions.

### Falsy Values — the Complete List

```javascript
// ALL falsy values in JavaScript (memorize these):
false
0
-0
0n        // BigInt zero
""        // empty string
null
undefined
NaN
```

> **Everything else is truthy** — including `"0"`, `"false"`, `[]`, `{}`.

```javascript
// Surprising truthy values
console.log(Boolean("0"));      // true  — non-empty string
console.log(Boolean("false"));  // true  — non-empty string
console.log(Boolean([]));       // true  — empty array is truthy!
console.log(Boolean({}));       // true  — empty object is truthy!
```

---

## 7.2 `if / else if / else`

```javascript
let score = 85;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}
// Output: Grade: B
```

---

## 7.3 `switch` Statement

Use `switch` when comparing one value against many options:

```javascript
let day = "Monday";

switch (day) {
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        console.log("Weekday");
        break;
    case "Saturday":
    case "Sunday":
        console.log("Weekend");
        break;
    default:
        console.log("Invalid day");
}
// Output: Weekday
```

> Don't forget `break`! Without it, execution "falls through" to the next case.

---

## 7.4 Ternary Operator

```javascript
let age = 20;
let access = age >= 18 ? "Allowed" : "Denied";
console.log(access); // "Allowed"

// Nested ternary (use sparingly — can be hard to read)
let grade = score >= 90 ? "A" : score >= 80 ? "B" : "C";
```

---

## 7.5 Short-Circuit Evaluation

Logical operators don't just return `true`/`false` — they return the actual value:

```javascript
// && returns the first falsy value, or the last value if all truthy
console.log("hello" && 42);      // 42
console.log(0 && "hello");       // 0
console.log(null && "hello");    // null

// || returns the first truthy value, or the last value if all falsy
console.log("" || "default");    // "default"
console.log("hello" || "default"); // "hello"
console.log(0 || null || "last");  // "last"
```

**Practical use:**

```javascript
// Setting default values
let username = inputName || "Guest";

// Conditional execution
isLoggedIn && showDashboard();
```

---

## 7.6 TaskMaster: Task Priority Logic

Add to `app.js`:

```javascript
// Determine task urgency based on priority and due date
function getUrgencyLabel(priority, daysUntilDue) {
    if (daysUntilDue < 0) {
        return "⚠️ OVERDUE";
    } else if (daysUntilDue === 0) {
        return "🔴 Due Today";
    } else if (priority === "high" && daysUntilDue <= 3) {
        return "🟠 Urgent";
    } else if (priority === "high") {
        return "🟡 High Priority";
    } else {
        return "🟢 Normal";
    }
}

// Test
console.log(getUrgencyLabel("high", -1));   // ⚠️ OVERDUE
console.log(getUrgencyLabel("high", 0));    // 🔴 Due Today
console.log(getUrgencyLabel("high", 2));    // 🟠 Urgent
console.log(getUrgencyLabel("high", 10));   // 🟡 High Priority
console.log(getUrgencyLabel("low", 5));     // 🟢 Normal
```

### Try it

1. What does `Boolean([])` return? What about `Boolean("")`?
2. Rewrite `getUrgencyLabel` using a ternary operator (is it more readable?)
3. What does `"hello" && 0 && "world"` return? Why?
4. Write a function that takes a temperature and returns "cold" (<15), "warm" (15-25), or "hot" (>25)

---

---

# Part 8: Loops

---

## 8.1 `for` Loop

Use when you know how many times to iterate:

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
// Output: 0, 1, 2, 3, 4
```

Anatomy: `for (initialization; condition; update)`

---

## 8.2 `while` Loop

Use when you don't know how many iterations:

```javascript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
// Output: 0, 1, 2, 3, 4
```

---

## 8.3 `do...while` Loop

Runs **at least once**, then checks the condition:

```javascript
let input;
do {
    input = prompt("Enter 'yes' to continue:");
} while (input !== "yes");
```

---

## 8.4 `for...of` — Iterate Over Values

Best for arrays and strings:

```javascript
const colors = ["red", "green", "blue"];

for (const color of colors) {
    console.log(color);
}
// Output: red, green, blue

// Also works on strings
for (const char of "Hello") {
    console.log(char);
}
// Output: H, e, l, l, o
```

---

## 8.5 `for...in` — Iterate Over Object Keys

Best for objects:

```javascript
const person = { name: "Alice", age: 25, city: "NYC" };

for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}
// Output:
// name: Alice
// age: 25
// city: NYC
```

> **Don't use `for...in` on arrays.** It iterates over indices (as strings) and can include inherited properties. Use `for...of` instead.

---

## 8.6 `break` and `continue`

```javascript
// break — exit the loop entirely
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i);
}
// Output: 0, 1, 2, 3, 4

// continue — skip current iteration, go to next
for (let i = 0; i < 5; i++) {
    if (i === 2) continue;
    console.log(i);
}
// Output: 0, 1, 3, 4
```

---

## 8.7 Loop Comparison

| Loop | Best for |
|---|---|
| `for` | Known number of iterations |
| `while` | Unknown iterations, condition-based |
| `do...while` | Must run at least once |
| `for...of` | Iterating over arrays, strings, iterables |
| `for...in` | Iterating over object properties |

---

## 8.8 TaskMaster: Display Tasks

Add to `app.js`:

```javascript
// Sample tasks array
const sampleTasks = [
    { id: 1, title: "Learn JavaScript basics", completed: true, priority: "high" },
    { id: 2, title: "Practice DOM manipulation", completed: false, priority: "high" },
    { id: 3, title: "Build a project", completed: false, priority: "medium" },
    { id: 4, title: "Learn async/await", completed: false, priority: "low" },
    { id: 5, title: "Review array methods", completed: true, priority: "medium" }
];

// Display all tasks
function displayTasks(taskList) {
    if (taskList.length === 0) {
        console.log("No tasks found.");
        return;
    }

    console.log("\n=== TaskMaster ===");
    for (const task of taskList) {
        const status = task.completed ? "✅" : "⬜";
        const priority = task.priority === "high" ? "🔴" :
                         task.priority === "medium" ? "🟡" : "🟢";
        console.log(`${status} ${priority} ${task.title}`);
    }
    console.log(`\nTotal: ${taskList.length} tasks`);
}

// Count completed tasks
function countCompleted(taskList) {
    let count = 0;
    for (const task of taskList) {
        if (task.completed) count++;
    }
    return count;
}

// Test
displayTasks(sampleTasks);
console.log(`Completed: ${countCompleted(sampleTasks)}/${sampleTasks.length}`);
```

### Try it

1. Write a loop that prints numbers from 10 down to 1
2. Write a loop that finds the first incomplete task in the `sampleTasks` array
3. Write a `while` loop that calculates the sum of all numbers from 1 to 100
4. Modify `displayTasks` to only show incomplete tasks

---

---

# Part 9: Functions

---

## 9.1 Function Declaration

```javascript
function greet(name) {
    return `Hello, ${name}!`;
}
console.log(greet("Alice")); // "Hello, Alice!"
```

### What happened?

`greet` is a function that takes `name` as a **parameter** and returns a greeting string. When we call `greet("Alice")`, `"Alice"` is the **argument**.

---

## 9.2 Function Expression

```javascript
const greet = function(name) {
    return `Hello, ${name}!`;
};
console.log(greet("Bob")); // "Hello, Bob!"
```

---

## 9.3 Arrow Function

```javascript
// Full syntax
const greet = (name) => {
    return `Hello, ${name}!`;
};

// Shorthand — single expression, implicit return
const greet = (name) => `Hello, ${name}!`;

// Single parameter — parentheses optional
const greet = name => `Hello, ${name}!`;

// No parameters — parentheses required
const sayHi = () => "Hi!";
```

---

## 9.4 Comparison

| Feature | Declaration | Expression | Arrow |
|---|---|---|---|
| Hoisted | ✅ | ❌ | ❌ |
| Has own `this` | ✅ | ✅ | ❌ (inherits) |
| Can be named | ✅ | Optional | ❌ |
| Shortest syntax | ❌ | ❌ | ✅ |

```javascript
// Hoisting example
sayHello();  // ✅ Works — declarations are hoisted
// sayBye();  // ❌ ReferenceError — expressions are NOT hoisted

function sayHello() {
    console.log("Hello!");
}
const sayBye = () => console.log("Bye!");
```

---

## 9.5 Default Parameters

```javascript
function createTask(title, priority = "medium", completed = false) {
    return { title, priority, completed };
}

console.log(createTask("Learn JS"));
// { title: "Learn JS", priority: "medium", completed: false }

console.log(createTask("Learn JS", "high"));
// { title: "Learn JS", priority: "high", completed: false }
```

---

## 9.6 Return Values

A function without `return` returns `undefined`:

```javascript
function noReturn() {
    console.log("I log, but return nothing.");
}
let result = noReturn();
console.log(result); // undefined
```

---

## 9.7 Callback Functions

A **callback** is a function passed as an argument to another function:

```javascript
function processTask(task, callback) {
    console.log(`Processing: ${task}`);
    callback();
}

processTask("Learn JS", function() {
    console.log("Done processing!");
});
// Output:
// Processing: Learn JS
// Done processing!

// With arrow function
processTask("Build project", () => console.log("Complete!"));
```

Callbacks are everywhere in JavaScript — event handlers, array methods, async operations.

---

## 9.8 IIFE (Immediately Invoked Function Expression)

A function that runs immediately after it's defined:

```javascript
(function() {
    let secret = "hidden";
    console.log("IIFE ran!", secret);
})();
// Output: IIFE ran! hidden
// 'secret' is not accessible outside
```

Used to create a private scope. Less common with modern `let`/`const` and modules.

---

## 9.9 TaskMaster: Core Task Functions

Update `app.js` with proper task management functions:

```javascript
// TaskMaster — Core Functions

const APP_NAME = "TaskMaster";
let tasks = [];
let nextId = 1;

// Create a new task
function addTask(title, priority = "medium") {
    const task = {
        id: nextId++,
        title: formatTaskTitle(title),
        completed: false,
        priority,
        createdAt: new Date().toISOString()
    };
    tasks.push(task);
    console.log(`✅ Added: "${task.title}"`);
    return task;
}

// Format title (reusing our earlier function)
function formatTaskTitle(title) {
    if (!title || typeof title !== "string") return "Untitled";
    let cleaned = title.trim();
    return cleaned.charAt(0).toUpperCase() + cleaned.slice(1);
}

// Delete a task by ID
function deleteTask(id) {
    const index = tasks.findIndex(t => t.id === id);
    if (index === -1) {
        console.log(`❌ Task #${id} not found.`);
        return false;
    }
    const removed = tasks.splice(index, 1)[0];
    console.log(`🗑️ Deleted: "${removed.title}"`);
    return true;
}

// Toggle task completion
const toggleTask = (id) => {
    const task = tasks.find(t => t.id === id);
    if (!task) {
        console.log(`❌ Task #${id} not found.`);
        return false;
    }
    task.completed = !task.completed;
    const status = task.completed ? "completed ✅" : "uncompleted ⬜";
    console.log(`${task.title} marked as ${status}`);
    return true;
};

// Test the functions
addTask("Learn JavaScript basics", "high");
addTask("practice DOM manipulation", "high");
addTask("Build a real project", "medium");

toggleTask(1);  // Mark first task as completed
deleteTask(99); // Try deleting non-existent task

console.log("\nAll tasks:", tasks);
```

### Try it

1. Add a function `getTaskById(id)` that returns a task or `null`
2. Add a function `updateTask(id, newTitle)` that changes a task's title
3. What happens if you call `addTask()` with no arguments? Fix it so it returns an error message
