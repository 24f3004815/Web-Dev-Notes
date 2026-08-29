# Part 10: Arrays

---

## 10.1 Creating Arrays

```javascript
const fruits = ["apple", "banana", "cherry"];
const mixed = [1, "hello", true, null, { name: "Alice" }];
const empty = [];

console.log(fruits[0]);       // "apple" (0-indexed)
console.log(fruits.length);   // 3
console.log(fruits.at(-1));   // "cherry" (last element)
```

---

## 10.2 Add & Remove Elements

```javascript
const arr = ["a", "b", "c"];

// End
arr.push("d");          // ["a", "b", "c", "d"] — add to end
arr.pop();              // ["a", "b", "c"]       — remove from end (returns "d")

// Beginning
arr.unshift("z");       // ["z", "a", "b", "c"] — add to start
arr.shift();            // ["a", "b", "c"]       — remove from start (returns "z")

// Anywhere — splice(startIndex, deleteCount, ...itemsToAdd)
arr.splice(1, 1);       // ["a", "c"]            — remove 1 element at index 1
arr.splice(1, 0, "b");  // ["a", "b", "c"]       — insert "b" at index 1
arr.splice(1, 1, "B");  // ["a", "B", "c"]       — replace element at index 1
```

---

## 10.3 Searching Arrays

```javascript
const nums = [10, 20, 30, 20, 40];

console.log(nums.indexOf(20));      // 1  — first occurrence
console.log(nums.lastIndexOf(20));  // 3  — last occurrence
console.log(nums.includes(30));     // true

// find() — returns first matching element
const found = nums.find(n => n > 15);
console.log(found); // 20

// findIndex() — returns index of first match
const idx = nums.findIndex(n => n > 25);
console.log(idx); // 2
```

---

## 10.4 The Big Three: `map`, `filter`, `reduce`

These are the **most important array methods**. They don't modify the original array — they return a new one.

### `map()` — Transform every element

```javascript
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// Original unchanged
console.log(numbers); // [1, 2, 3, 4, 5]
```

### `filter()` — Keep elements that pass a test

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evens = numbers.filter(n => n % 2 === 0);
console.log(evens); // [2, 4, 6]
```

### `reduce()` — Reduce array to a single value

```javascript
const numbers = [1, 2, 3, 4, 5];

// Sum all numbers
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum); // 15

// How it works step by step:
// Step 1: acc=0,  cur=1 → 0+1 = 1
// Step 2: acc=1,  cur=2 → 1+2 = 3
// Step 3: acc=3,  cur=3 → 3+3 = 6
// Step 4: acc=6,  cur=4 → 6+4 = 10
// Step 5: acc=10, cur=5 → 10+5 = 15

// Find max value
const max = numbers.reduce((a, b) => a > b ? a : b);
console.log(max); // 5
```

---

## 10.5 Other Useful Methods

```javascript
const arr = [3, 1, 4, 1, 5, 9];

// forEach — iterate (no return value)
arr.forEach(item => console.log(item));

// sort — sorts in place (modifies original!)
const sorted = [...arr].sort((a, b) => a - b);  // copy first!
console.log(sorted); // [1, 1, 3, 4, 5, 9]

// reverse — reverses in place
const reversed = [...arr].reverse();

// join — combine into string
console.log(["Hello", "World"].join(" ")); // "Hello World"

// concat — combine arrays (or use spread)
const merged = [1, 2].concat([3, 4]); // [1, 2, 3, 4]

// slice — extract portion (doesn't modify original)
console.log(arr.slice(1, 3)); // [1, 4]

// flat — flatten nested arrays
console.log([1, [2, [3, 4]]].flat(Infinity)); // [1, 2, 3, 4]

// every & some
console.log([2, 4, 6].every(n => n % 2 === 0)); // true  — all even?
console.log([1, 2, 3].some(n => n > 2));         // true  — any > 2?

// Array.isArray — check if something is an array
console.log(Array.isArray([1, 2])); // true
console.log(Array.isArray("hello")); // false
```

---

## 10.6 Spread Operator & Destructuring

### Spread (`...`) — Expand an Array

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Copy an array (shallow)
const copy = [...arr1];

// Merge arrays
const merged = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Add elements
const withZero = [0, ...arr1]; // [0, 1, 2, 3]
```

### Destructuring — Extract Values

```javascript
const colors = ["red", "green", "blue", "yellow"];

const [first, second, ...rest] = colors;
console.log(first);  // "red"
console.log(second); // "green"
console.log(rest);   // ["blue", "yellow"]

// Skip elements
const [, , third] = colors;
console.log(third);  // "blue"

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b);   // 2, 1
```

---

## 10.7 Method Chaining

Chain array methods together for clean, expressive code:

```javascript
const users = [
    { name: "Alice", age: 25, active: true },
    { name: "Bob", age: 30, active: false },
    { name: "Charlie", age: 35, active: true },
    { name: "Diana", age: 28, active: true }
];

// Get names of active users, sorted alphabetically
const activeNames = users
    .filter(user => user.active)
    .map(user => user.name)
    .sort();

console.log(activeNames); // ["Alice", "Charlie", "Diana"]
```

---

## 10.8 TaskMaster: Array-Powered Task Management

Update `app.js`:

```javascript
// TaskMaster — Array Methods in Action

let tasks = [];
let nextId = 1;

function addTask(title, priority = "medium") {
    tasks.push({
        id: nextId++,
        title: title.trim(),
        completed: false,
        priority,
        createdAt: new Date().toISOString()
    });
}

// Add sample tasks
addTask("Learn JavaScript arrays", "high");
addTask("Master map, filter, reduce", "high");
addTask("Build DOM interface", "medium");
addTask("Review CSS styling", "low");
addTask("Deploy project", "medium");
tasks[0].completed = true; // Mark first as done

// Get incomplete tasks
const incomplete = tasks.filter(t => !t.completed);
console.log("Incomplete:", incomplete.map(t => t.title));
// ["Master map, filter, reduce", "Build DOM interface", "Review CSS styling", "Deploy project"]

// Get high priority task titles
const urgent = tasks
    .filter(t => t.priority === "high" && !t.completed)
    .map(t => `🔴 ${t.title}`);
console.log("Urgent:", urgent);
// ["🔴 Master map, filter, reduce"]

// Count tasks by priority
const countByPriority = tasks.reduce((counts, task) => {
    counts[task.priority] = (counts[task.priority] || 0) + 1;
    return counts;
}, {});
console.log("By priority:", countByPriority);
// { high: 2, medium: 2, low: 1 }

// Get task summary
const summary = {
    total: tasks.length,
    completed: tasks.filter(t => t.completed).length,
    pending: tasks.filter(t => !t.completed).length,
    completionRate: Math.round(
        (tasks.filter(t => t.completed).length / tasks.length) * 100
    ) + "%"
};
console.log("Summary:", summary);
// { total: 5, completed: 1, pending: 4, completionRate: "20%" }
```

### Try it

1. Write a function `searchTasks(keyword)` that filters tasks containing the keyword (case-insensitive)
2. Write a function `sortTasks(by)` that returns tasks sorted by `"priority"`, `"title"`, or `"date"`
3. Use `reduce` to find the task with the longest title
4. Chain `.filter()` and `.map()` to get an array of completed task titles prefixed with "✅ "

---

---

# Part 11: Objects

---

## 11.1 Creating Objects

```javascript
// Object literal — the most common way
const person = {
    name: "Alice",
    age: 25,
    isStudent: true,
    hobbies: ["reading", "coding"],
    address: {
        city: "NYC",
        zip: "10001"
    },
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};
```

---

## 11.2 Accessing Properties

```javascript
// Dot notation — preferred
console.log(person.name);         // "Alice"
console.log(person.address.city); // "NYC"

// Bracket notation — needed for dynamic keys or special characters
console.log(person["name"]);      // "Alice"

let key = "age";
console.log(person[key]);         // 25

// Optional chaining — safe nested access
console.log(person.address?.zip);       // "10001"
console.log(person.phone?.number);     // undefined (no error)
```

---

## 11.3 Modifying Objects

```javascript
const user = { name: "Alice", age: 25 };

// Add properties
user.email = "alice@example.com";

// Modify properties
user.age = 26;

// Delete properties
delete user.email;

console.log(user); // { name: "Alice", age: 26 }
```

> Note: `const` prevents reassigning the variable, but you **can** modify the object's properties.

---

## 11.4 Object Methods

```javascript
const person = { name: "Alice", age: 25, city: "NYC" };

console.log(Object.keys(person));    // ["name", "age", "city"]
console.log(Object.values(person));  // ["Alice", 25, "NYC"]
console.log(Object.entries(person)); // [["name","Alice"], ["age",25], ["city","NYC"]]

// Check if key exists
console.log("name" in person);           // true
console.log(person.hasOwnProperty("age")); // true

// Merge objects
const defaults = { theme: "dark", lang: "en" };
const userPrefs = { lang: "es" };
const settings = Object.assign({}, defaults, userPrefs);
console.log(settings); // { theme: "dark", lang: "es" }

// Freeze — prevent modifications
const frozen = Object.freeze({ x: 1, y: 2 });
frozen.x = 99; // Silently fails (throws in strict mode)
console.log(frozen.x); // 1
```

---

## 11.5 Spread & Destructuring with Objects

### Spread — Copy and Merge

```javascript
const original = { a: 1, b: 2, c: 3 };

// Shallow copy
const copy = { ...original };

// Merge (later values overwrite)
const updated = { ...original, b: 99, d: 4 };
console.log(updated); // { a: 1, b: 99, c: 3, d: 4 }
```

### Destructuring — Extract Properties

```javascript
const person = { name: "Alice", age: 25, city: "NYC", country: "US" };

// Basic destructuring
const { name, age } = person;
console.log(name, age); // "Alice" 25

// Rename variables
const { name: userName, age: userAge } = person;
console.log(userName); // "Alice"

// Default values
const { role = "user" } = person;
console.log(role); // "user" (doesn't exist on person)

// Rest — collect remaining properties
const { city, ...rest } = person;
console.log(city);  // "NYC"
console.log(rest);  // { name: "Alice", age: 25, country: "US" }
```

### Nested Destructuring

```javascript
const user = {
    name: "Alice",
    address: { city: "NYC", zip: "10001" }
};

const { address: { city, zip } } = user;
console.log(city, zip); // "NYC" "10001"
```

---

## 11.6 Enhanced Object Literals (ES6+)

```javascript
const name = "Alice";
const age = 25;

// Shorthand property names (key === variable name)
const person = { name, age };
// Same as: { name: name, age: age }

// Shorthand methods
const calculator = {
    add(a, b) { return a + b; },
    subtract(a, b) { return a - b; }
};
// Same as: { add: function(a, b) { ... } }

// Computed property names
const field = "email";
const obj = { [field]: "alice@example.com" };
console.log(obj.email); // "alice@example.com"
```

---

## 11.7 TaskMaster: Task Object Model

Update `app.js`:

```javascript
// TaskMaster — Object-based task management

let tasks = [];
let nextId = 1;

// Create a task with a structured object
function createTask(title, { priority = "medium", tags = [], dueDate = null } = {}) {
    return {
        id: nextId++,
        title: title.trim(),
        completed: false,
        priority,
        tags: [...tags],
        dueDate,
        createdAt: new Date().toISOString(),
        completedAt: null
    };
}

// Add a task
function addTask(title, options) {
    const task = createTask(title, options);
    tasks.push(task);
    return task;
}

// Get task summary using Object methods
function getTaskSummary(task) {
    const { id, title, completed, priority, tags } = task;
    return {
        display: `[${completed ? "✅" : "⬜"}] #${id}: ${title}`,
        priority,
        tagCount: tags.length
    };
}

// Test
const task1 = addTask("Learn objects in JavaScript", {
    priority: "high",
    tags: ["javascript", "learning"]
});

const task2 = addTask("Build TaskMaster UI", {
    priority: "high",
    tags: ["project", "dom"]
});

const task3 = addTask("Review code", {
    tags: ["review"]
});

// Display summaries
tasks.forEach(task => {
    const summary = getTaskSummary(task);
    console.log(summary.display, `(${summary.priority})`);
});

// Group tasks by priority using reduce
const grouped = tasks.reduce((groups, task) => {
    const key = task.priority;
    groups[key] = groups[key] || [];
    groups[key].push(task.title);
    return groups;
}, {});
console.log("\nGrouped by priority:", grouped);
```

### Try it

1. Add a `updateTask(id, updates)` function that uses spread to merge updates: `{ ...task, ...updates }`
2. Write a function that returns all unique tags across all tasks (hint: `Set`)
3. Destructure the first task from `tasks` and log its `title` and `priority`
4. What happens if you try to `Object.freeze(task1)` and then modify `task1.tags.push("new")`? Why?
