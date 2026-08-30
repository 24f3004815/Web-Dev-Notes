# JavaScript — Cheat Sheet 📋

> One-page reference for the most useful syntax, methods, and patterns.

---

## Variables

```javascript
const name = "Alice";    // Cannot reassign — use by default
let count = 0;           // Can reassign — use when value changes
// var old = "no";       // Never use
```

---

## Data Types

| Type | Example | `typeof` |
|---|---|---|
| String | `"hello"`, `` `hi ${name}` `` | `"string"` |
| Number | `42`, `3.14` | `"number"` |
| Boolean | `true`, `false` | `"boolean"` |
| null | `null` | `"object"` (bug) |
| undefined | `undefined` | `"undefined"` |
| Object | `{}`, `[]` | `"object"` |
| Function | `() => {}` | `"function"` |

**Falsy values:** `false`, `0`, `""`, `null`, `undefined`, `NaN`

---

## Strings

```javascript
str.length                    // Length
str.toUpperCase()             // "HELLO"
str.toLowerCase()             // "hello"
str.trim()                    // Remove whitespace
str.includes("hi")            // true/false
str.indexOf("hi")             // Index or -1
str.slice(0, 5)               // Extract portion
str.split(",")                // String → Array
str.replace("old", "new")    // Replace first match
str.replaceAll("old", "new") // Replace all
`Hello, ${name}!`            // Template literal
```

---

## Numbers & Math

```javascript
parseInt("42")          // 42
parseFloat("3.14")      // 3.14
Number("42")            // 42
Math.round(4.5)         // 5
Math.floor(4.9)         // 4
Math.ceil(4.1)          // 5
Math.random()           // 0 to 0.999...
Math.max(1, 5, 3)       // 5
Math.min(1, 5, 3)       // 1
Math.abs(-10)           // 10
```

---

## Arrays

```javascript
// Create
const arr = [1, 2, 3];

// Add/Remove
arr.push(4)              // Add to end → [1,2,3,4]
arr.pop()                // Remove from end → [1,2,3]
arr.unshift(0)           // Add to start
arr.shift()              // Remove from start
arr.splice(1, 1)         // Remove at index

// Search
arr.includes(2)          // true
arr.indexOf(2)           // 1
arr.find(x => x > 1)    // 2
arr.findIndex(x => x > 1) // 1

// Transform (return new array)
arr.map(x => x * 2)     // [2, 4, 6]
arr.filter(x => x > 1)  // [2, 3]
arr.reduce((sum, x) => sum + x, 0) // 6

// Iterate
arr.forEach(x => console.log(x))

// Other
arr.sort((a, b) => a - b)  // Sort (mutates!)
arr.reverse()               // Reverse (mutates!)
arr.join(", ")              // "1, 2, 3"
arr.slice(1, 3)             // [2, 3] (no mutation)
[...arr1, ...arr2]          // Merge arrays
[...new Set(arr)]           // Remove duplicates
```

---

## Objects

```javascript
const obj = { name: "Alice", age: 25 };

obj.name                     // "Alice"
obj["name"]                  // "Alice"
obj.email = "a@b.com"       // Add property
delete obj.email             // Delete property

Object.keys(obj)             // ["name", "age"]
Object.values(obj)           // ["Alice", 25]
Object.entries(obj)          // [["name","Alice"], ["age",25]]
{ ...obj, age: 26 }         // Clone + update

// Destructuring
const { name, age } = obj;
const { name: n, ...rest } = obj;
```

---

## Functions

```javascript
// Declaration (hoisted)
function add(a, b) { return a + b; }

// Arrow (not hoisted)
const add = (a, b) => a + b;

// Default parameters
function greet(name = "World") { return `Hello, ${name}!`; }

// Rest parameters
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
```

---

## Conditionals

```javascript
if (x > 0) { } else if (x < 0) { } else { }
const result = condition ? "yes" : "no";       // Ternary
const value = input ?? "default";               // Nullish coalescing
const safe = obj?.nested?.prop;                 // Optional chaining
```

---

## Loops

```javascript
for (let i = 0; i < 5; i++) { }       // Classic
for (const item of array) { }          // Arrays/iterables
for (const key in object) { }          // Object keys
while (condition) { }                   // Condition-based
```

---

## DOM

```javascript
// Select
document.querySelector("#id")          // First match
document.querySelectorAll(".class")    // All matches

// Modify
el.textContent = "text"               // Set text
el.innerHTML = "<b>html</b>"          // Set HTML
el.style.color = "red"                // Inline style
el.classList.add("active")            // Add class
el.classList.toggle("active")         // Toggle class
el.setAttribute("data-id", "1")      // Set attribute

// Create/Remove
document.createElement("div")
parent.appendChild(child)
el.remove()

// Events
el.addEventListener("click", (e) => {
    e.preventDefault();
    console.log(e.target);
});
```

---

## Async

```javascript
// Async/Await (preferred)
async function getData() {
    try {
        const res = await fetch(url);
        const data = await res.json();
        return data;
    } catch (err) {
        console.error(err);
    }
}

// Promise
fetch(url)
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));

// Parallel
const [a, b] = await Promise.all([fetch(url1), fetch(url2)]);

// Timer
setTimeout(() => {}, 1000);
setInterval(() => {}, 1000);
```

---

## Classes

```javascript
class Animal {
    #sound;                              // Private field
    constructor(name, sound) {
        this.name = name;
        this.#sound = sound;
    }
    speak() { return `${this.name}: ${this.#sound}`; }
    static create(name) { return new Animal(name, "..."); }
}

class Dog extends Animal {
    constructor(name) { super(name, "Woof"); }
}
```

---

## Modules

```javascript
// Export
export function add(a, b) { return a + b; }
export default class App { }

// Import
import App, { add } from "./module.js";

// HTML
// <script type="module" src="app.js"></script>
```

---

## Error Handling

```javascript
try {
    riskyOperation();
} catch (error) {
    console.error(error.message);
} finally {
    cleanup();
}
throw new Error("Something went wrong");
```

---

## Storage

```javascript
localStorage.setItem("key", JSON.stringify(data));
const data = JSON.parse(localStorage.getItem("key")) || [];
localStorage.removeItem("key");
localStorage.clear();
```

---

## JSON

```javascript
JSON.stringify(obj)            // Object → JSON string
JSON.parse(jsonString)         // JSON string → Object
JSON.stringify(obj, null, 2)   // Pretty print
```

---

## Useful Patterns

```javascript
// Swap variables
[a, b] = [b, a];

// Remove duplicates
[...new Set(array)]

// Clone object/array
const copy = { ...obj };
const copy = [...arr];

// Default value
const val = input ?? "default";

// Short-circuit
isValid && doSomething();
const name = user?.name || "Guest";

// Random integer (min to max inclusive)
Math.floor(Math.random() * (max - min + 1)) + min;

// Sleep/delay
const delay = ms => new Promise(r => setTimeout(r, ms));
await delay(1000);
```

---

*Keep this cheat sheet handy. You'll use it less and less as JavaScript becomes second nature.* 🚀
