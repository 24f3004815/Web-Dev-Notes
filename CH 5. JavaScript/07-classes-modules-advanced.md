# Part 20: Classes & Object-Oriented JavaScript

---

## 20.1 Class Syntax

```javascript
class Animal {
    constructor(name, sound) {
        this.name = name;
        this.sound = sound;
    }

    speak() {
        return `${this.name} says ${this.sound}`;
    }
}

const cat = new Animal("Whiskers", "Meow");
console.log(cat.speak()); // "Whiskers says Meow"
console.log(cat instanceof Animal); // true
```

### What happened?

- `class` defines a blueprint for creating objects
- `constructor` runs when you create a new instance with `new`
- `this` refers to the new object being created
- Methods are defined directly inside the class body

---

## 20.2 Inheritance with `extends`

```javascript
class Dog extends Animal {
    constructor(name) {
        super(name, "Woof"); // Call parent constructor
    }

    fetch(item) {
        return `${this.name} fetches the ${item}!`;
    }
}

const dog = new Dog("Rex");
console.log(dog.speak());        // "Rex says Woof" (inherited)
console.log(dog.fetch("ball"));  // "Rex fetches the ball!" (own method)
console.log(dog instanceof Dog);    // true
console.log(dog instanceof Animal); // true (also an Animal)
```

---

## 20.3 Getters and Setters

```javascript
class Temperature {
    #celsius; // Private field

    constructor(celsius) {
        this.#celsius = celsius;
    }

    get fahrenheit() {
        return this.#celsius * 9/5 + 32;
    }

    set fahrenheit(f) {
        this.#celsius = (f - 32) * 5/9;
    }

    get celsius() {
        return this.#celsius;
    }

    set celsius(c) {
        if (c < -273.15) throw new Error("Below absolute zero!");
        this.#celsius = c;
    }
}

const temp = new Temperature(100);
console.log(temp.fahrenheit);  // 212 (getter — looks like a property)
temp.fahrenheit = 32;          // setter
console.log(temp.celsius);    // 0
```

---

## 20.4 Static Methods

Static methods belong to the **class itself**, not instances:

```javascript
class MathHelper {
    static add(a, b) {
        return a + b;
    }

    static random(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
}

console.log(MathHelper.add(2, 3));     // 5
console.log(MathHelper.random(1, 10)); // random 1-10

// const helper = new MathHelper();
// helper.add(2, 3); // ❌ TypeError — static methods aren't on instances
```

---

## 20.5 Private Fields (`#`)

```javascript
class BankAccount {
    #balance; // Private — cannot be accessed from outside

    constructor(initialBalance) {
        this.#balance = initialBalance;
    }

    deposit(amount) {
        if (amount <= 0) throw new Error("Amount must be positive");
        this.#balance += amount;
        return this.#balance;
    }

    withdraw(amount) {
        if (amount > this.#balance) throw new Error("Insufficient funds");
        this.#balance -= amount;
        return this.#balance;
    }

    get balance() {
        return this.#balance;
    }
}

const account = new BankAccount(1000);
console.log(account.balance);    // 1000 (via getter)
account.deposit(500);
console.log(account.balance);    // 1500
// console.log(account.#balance); // ❌ SyntaxError — private!
```

---

## 20.6 Prototypal Inheritance (Brief)

JavaScript classes are **syntactic sugar** over prototypes. Under the hood, JavaScript uses prototype-based inheritance:

```javascript
// This class syntax:
class Person {
    constructor(name) { this.name = name; }
    greet() { return `Hi, I'm ${this.name}`; }
}

// Is roughly equivalent to:
function PersonOld(name) { this.name = name; }
PersonOld.prototype.greet = function() { return `Hi, I'm ${this.name}`; };

// Both work the same way
const p1 = new Person("Alice");
const p2 = new PersonOld("Bob");
console.log(p1.greet()); // "Hi, I'm Alice"
console.log(p2.greet()); // "Hi, I'm Bob"
```

> You don't need to write prototype-based code. Just know that classes use prototypes internally — you'll see this in older codebases and documentation.

---

## 20.7 TaskMaster: Class-Based Architecture

Refactor TaskMaster using classes:

```javascript
// task.js — Task class

class Task {
    #id;
    #createdAt;
    #completedAt;

    constructor(id, title, { priority = "medium", tags = [] } = {}) {
        this.#id = id;
        this.title = title.trim();
        this.completed = false;
        this.priority = priority;
        this.tags = [...tags];
        this.#createdAt = new Date().toISOString();
        this.#completedAt = null;
    }

    get id() { return this.#id; }
    get createdAt() { return this.#createdAt; }
    get completedAt() { return this.#completedAt; }

    toggle() {
        this.completed = !this.completed;
        this.#completedAt = this.completed ? new Date().toISOString() : null;
    }

    update(updates) {
        if (updates.title) this.title = updates.title.trim();
        if (updates.priority) this.priority = updates.priority;
        if (updates.tags) this.tags = [...updates.tags];
    }

    // Convert to plain object for storage
    toJSON() {
        return {
            id: this.#id,
            title: this.title,
            completed: this.completed,
            priority: this.priority,
            tags: this.tags,
            createdAt: this.#createdAt,
            completedAt: this.#completedAt
        };
    }

    // Create from plain object (loaded from storage)
    static fromJSON(data) {
        const task = new Task(data.id, data.title, {
            priority: data.priority,
            tags: data.tags
        });
        task.completed = data.completed;
        return task;
    }
}
```

```javascript
// taskManager.js — TaskManager class

class TaskManager {
    #tasks = [];
    #nextId = 1;

    constructor() {
        this.load();
    }

    add(title, options = {}) {
        if (!title || title.trim() === "") {
            throw new Error("Task title is required");
        }
        const task = new Task(this.#nextId++, title, options);
        this.#tasks.push(task);
        this.save();
        return task;
    }

    delete(id) {
        const index = this.#tasks.findIndex(t => t.id === id);
        if (index === -1) return false;
        this.#tasks.splice(index, 1);
        this.save();
        return true;
    }

    toggle(id) {
        const task = this.getById(id);
        if (!task) return false;
        task.toggle();
        this.save();
        return true;
    }

    getById(id) {
        return this.#tasks.find(t => t.id === id) || null;
    }

    getAll(filter = "all") {
        switch (filter) {
            case "pending":   return this.#tasks.filter(t => !t.completed);
            case "completed": return this.#tasks.filter(t => t.completed);
            default:          return [...this.#tasks];
        }
    }

    get stats() {
        const total = this.#tasks.length;
        const completed = this.#tasks.filter(t => t.completed).length;
        return {
            total,
            completed,
            pending: total - completed,
            completionRate: total > 0 ? Math.round((completed / total) * 100) : 0
        };
    }

    clearCompleted() {
        this.#tasks = this.#tasks.filter(t => !t.completed);
        this.save();
    }

    search(keyword) {
        const lower = keyword.toLowerCase();
        return this.#tasks.filter(t =>
            t.title.toLowerCase().includes(lower)
        );
    }

    save() {
        const data = {
            tasks: this.#tasks.map(t => t.toJSON()),
            nextId: this.#nextId
        };
        localStorage.setItem("taskmaster", JSON.stringify(data));
    }

    load() {
        try {
            const saved = localStorage.getItem("taskmaster");
            if (saved) {
                const data = JSON.parse(saved);
                this.#tasks = data.tasks.map(t => Task.fromJSON(t));
                this.#nextId = data.nextId;
            }
        } catch (error) {
            console.error("Failed to load tasks:", error);
            this.#tasks = [];
            this.#nextId = 1;
        }
    }
}
```

```javascript
// Usage
const manager = new TaskManager();
manager.add("Learn JavaScript classes", { priority: "high" });
manager.add("Build TaskMaster with classes", { priority: "high" });
manager.add("Review code", { priority: "low" });

manager.toggle(1);
console.log(manager.stats);
// { total: 3, completed: 1, pending: 2, completionRate: 33 }

console.log(manager.search("learn"));
// [Task { title: "Learn JavaScript classes", ... }]
```

### Try it

1. Add a `sortBy(field)` method to `TaskManager` that sorts by `"title"`, `"priority"`, or `"date"`
2. Add a `getByPriority(priority)` method
3. Why do we use `#tasks` (private) instead of `this.tasks` (public)?
4. What does `static fromJSON` do and why is it useful?

---

---

# Part 21: Modules (Import/Export)

---

## 21.1 Named Exports

```javascript
// utils.js
export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export const PI = 3.14159;
```

```javascript
// app.js
import { add, subtract, PI } from "./utils.js";

console.log(add(2, 3));    // 5
console.log(PI);           // 3.14159
```

---

## 21.2 Default Export

```javascript
// Calculator.js
export default class Calculator {
    add(a, b) { return a + b; }
    subtract(a, b) { return a - b; }
}
```

```javascript
// app.js
import Calculator from "./Calculator.js";  // No curly braces!

const calc = new Calculator();
console.log(calc.add(2, 3)); // 5
```

---

## 21.3 Mixing Named and Default

```javascript
// taskUtils.js
export default class TaskManager { /* ... */ }
export function formatDate(date) { /* ... */ }
export const MAX_TASKS = 100;
```

```javascript
// app.js
import TaskManager, { formatDate, MAX_TASKS } from "./taskUtils.js";
```

---

## 21.4 Using Modules in HTML

```html
<!-- Must use type="module" -->
<script type="module" src="app.js"></script>
```

> Module scripts are **deferred** by default (they wait for HTML to parse), have strict mode enabled, and each module has its own scope (no polluting global scope).

---

## 21.5 When to Use Which

| Export type | When to use | Import syntax |
|---|---|---|
| Named | Multiple exports per file | `import { name } from "./file.js"` |
| Default | One main export per file | `import Name from "./file.js"` |

> **Convention:** Use default export for classes and main components. Use named exports for utility functions and constants.

### Try it

1. Split the TaskMaster code into separate files: `task.js`, `taskManager.js`, `app.js`
2. What happens if you forget `type="module"` in the script tag?
3. Can a file have both a default and named exports? Try it

---

---

# Part 22: Higher-Order Functions & Functional Concepts

---

## 22.1 What is a Higher-Order Function?

A function that **takes a function as an argument** or **returns a function**:

```javascript
// Takes a function as an argument
function repeat(n, action) {
    for (let i = 0; i < n; i++) action(i);
}
repeat(3, console.log); // 0, 1, 2

// Returns a function
function greaterThan(n) {
    return (m) => m > n;
}
const greaterThan10 = greaterThan(10);
console.log(greaterThan10(15)); // true
console.log(greaterThan10(5));  // false
```

You've already used many higher-order functions: `.map()`, `.filter()`, `.reduce()`, `.forEach()`, `addEventListener()`.

---

## 22.2 Sorting with Custom Comparators

```javascript
const users = [
    { name: "Charlie", age: 35 },
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 }
];

// Sort by age (ascending)
const byAge = [...users].sort((a, b) => a.age - b.age);

// Sort by name (alphabetical)
const byName = [...users].sort((a, b) => a.name.localeCompare(b.name));

// Sort by age (descending)
const byAgeDesc = [...users].sort((a, b) => b.age - a.age);

console.log(byAge.map(u => u.name));     // ["Alice", "Bob", "Charlie"]
console.log(byName.map(u => u.name));    // ["Alice", "Bob", "Charlie"]
console.log(byAgeDesc.map(u => u.name)); // ["Charlie", "Bob", "Alice"]
```

> **Remember:** `.sort()` modifies the original array. Use `[...array].sort()` to sort a copy.

---

## 22.3 Function Composition

Combine simple functions to build complex operations:

```javascript
const trim = str => str.trim();
const capitalize = str => str.charAt(0).toUpperCase() + str.slice(1);
const exclaim = str => str + "!";

// Compose manually
const shout = str => exclaim(capitalize(trim(str)));
console.log(shout("  hello  ")); // "Hello!"

// Compose with a helper
function compose(...fns) {
    return (value) => fns.reduceRight((acc, fn) => fn(acc), value);
}

const process = compose(exclaim, capitalize, trim);
console.log(process("  hello  ")); // "Hello!"
```

---

## 22.4 Pure Functions & Immutability

**Pure function** — same inputs always produce same output, no side effects:

```javascript
// ✅ Pure — no side effects
function add(a, b) {
    return a + b;
}

// ❌ Impure — modifies external state
let total = 0;
function addToTotal(n) {
    total += n; // Side effect!
    return total;
}

// ✅ Immutable update — return a new array instead of modifying
function addItem(arr, item) {
    return [...arr, item]; // New array, original unchanged
}

// ❌ Mutating — modifies the original
function addItemBad(arr, item) {
    arr.push(item); // Side effect!
    return arr;
}
```

> **Prefer pure functions and immutable updates** — they're easier to test, debug, and reason about.

---

## 22.5 Chaining in Practice

```javascript
// Real-world example: process task data
const taskReport = tasks
    .filter(task => !task.completed)
    .filter(task => task.priority === "high")
    .map(task => ({
        title: task.title,
        daysOld: Math.floor((Date.now() - new Date(task.createdAt)) / 86400000)
    }))
    .sort((a, b) => b.daysOld - a.daysOld)
    .map(task => `${task.title} (${task.daysOld} days old)`);

console.log("Urgent tasks:", taskReport);
```

### Try it

1. Write a `pipe` function (like `compose` but left-to-right)
2. Use `.reduce()` to group tasks by priority (returning an object like `{ high: [...], medium: [...], low: [...] }`)
3. Create a reusable `sortBy(key)` function that returns a comparator: `users.sort(sortBy("age"))`

---

---

# Part 23: Destructuring, Spread & Rest — Deep Dive

---

## 23.1 Advanced Destructuring

```javascript
// Nested destructuring
const user = {
    name: "Alice",
    address: {
        city: "NYC",
        zip: "10001"
    },
    scores: [95, 87, 92]
};

const { name, address: { city }, scores: [first, ...otherScores] } = user;
console.log(name);        // "Alice"
console.log(city);        // "NYC"
console.log(first);       // 95
console.log(otherScores); // [87, 92]

// Destructuring in function parameters
function printUser({ name, address: { city } = {} }) {
    console.log(`${name} from ${city}`);
}
printUser(user); // "Alice from NYC"
```

---

## 23.2 Rest Parameters (`...`)

Collect remaining arguments into an array:

```javascript
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

console.log(sum(1, 2, 3));       // 6
console.log(sum(1, 2, 3, 4, 5)); // 15

// With other parameters (rest must be last)
function log(level, ...messages) {
    console.log(`[${level}]`, ...messages);
}
log("ERROR", "Something", "went", "wrong");
// [ERROR] Something went wrong
```

---

## 23.3 Spread in Real Patterns

```javascript
// Clone and update (immutable pattern)
const defaults = { theme: "dark", fontSize: 14, lang: "en" };
const userPrefs = { fontSize: 18, lang: "es" };
const settings = { ...defaults, ...userPrefs };
console.log(settings);
// { theme: "dark", fontSize: 18, lang: "es" }

// Remove a property immutably
const { lang, ...settingsWithoutLang } = settings;
console.log(settingsWithoutLang);
// { theme: "dark", fontSize: 18 }

// Pass array elements as function arguments
const coords = [10, 20, 30];
console.log(Math.max(...coords)); // 30
```

### Try it

1. Destructure the first and last item from an array in one line
2. Write a function that accepts an object with `{name, age, ...rest}` and logs the rest
3. Use spread to merge two objects, where the second overrides the first

---

---

# Part 24: Regular Expressions (Brief)

---

## 24.1 Creating Regex

```javascript
// Literal syntax
const pattern1 = /hello/i;  // 'i' flag = case-insensitive

// Constructor syntax
const pattern2 = new RegExp("hello", "i");
```

---

## 24.2 Core Methods

```javascript
const text = "Hello World, hello JavaScript";

// test() — returns true/false
console.log(/hello/i.test(text));         // true

// match() — returns matches
console.log(text.match(/hello/gi));       // ["Hello", "hello"]

// replace() — replace matches
console.log(text.replace(/hello/gi, "Hi")); // "Hi World, Hi JavaScript"

// search() — returns index of first match
console.log(text.search(/world/i));       // 6
```

---

## 24.3 Common Patterns

```javascript
// Digits
/\d+/.test("abc123");        // true

// Email (simplified)
/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test("user@example.com"); // true

// Only letters and spaces
/^[a-zA-Z\s]+$/.test("Hello World"); // true

// URL (simplified)
/^https?:\/\/.+/.test("https://example.com"); // true
```

### Flags

| Flag | Meaning |
|---|---|
| `g` | Global — find all matches |
| `i` | Case-insensitive |
| `m` | Multiline |

> Regex is a **reference topic**. Don't memorize patterns — look them up when needed. Know the basics: `test()`, `match()`, `replace()`.

---

---

# Part 25: Browser APIs

---

## 25.1 Timers

```javascript
// Run once after delay
const timeoutId = setTimeout(() => {
    console.log("Runs after 2 seconds");
}, 2000);
clearTimeout(timeoutId); // Cancel it

// Run repeatedly at interval
const intervalId = setInterval(() => {
    console.log("Runs every second");
}, 1000);
clearInterval(intervalId); // Stop it
```

---

## 25.2 `window`, `document`, and Other Global Objects

```javascript
// window — the global browser object
console.log(window.innerWidth);   // viewport width
console.log(window.innerHeight);  // viewport height

// location — current URL info
console.log(location.href);      // full URL
console.log(location.hostname);  // e.g., "example.com"
// location.href = "/new-page";  // Navigate to a new page

// navigator — browser info
console.log(navigator.userAgent);
console.log(navigator.language); // e.g., "en-US"

// history — browser history
// history.back();    // Go back
// history.forward();  // Go forward
```

---

## 25.3 `requestAnimationFrame` (Brief)

For smooth animations (60fps):

```javascript
function animate() {
    // Update animation state
    element.style.left = position + "px";
    position += 2;

    if (position < 500) {
        requestAnimationFrame(animate); // Schedule next frame
    }
}
requestAnimationFrame(animate);
```

---

## 25.4 `IntersectionObserver` (Brief)

Detect when an element enters/exits the viewport:

```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll(".animate-on-scroll").forEach(el => {
    observer.observe(el);
});
```

> Used for lazy loading images, infinite scroll, scroll animations, and analytics tracking.
