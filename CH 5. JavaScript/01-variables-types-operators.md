# Part 3: Variables & Data Types

---

## 3.1 Declaring Variables

JavaScript has three ways to declare variables:

```javascript
let name = "Alice";       // Can be reassigned
const PI = 3.14159;       // Cannot be reassigned
var old = "avoid this";   // Legacy — don't use
```

### `let` vs `const` vs `var`

| Feature | `let` | `const` | `var` |
|---|---|---|---|
| Reassignable | ✅ | ❌ | ✅ |
| Block scoped | ✅ | ✅ | ❌ (function scoped) |
| Hoisted | ✅ (TDZ) | ✅ (TDZ) | ✅ (initialized as `undefined`) |
| Use when | Value changes | Value stays the same | Never (legacy) |

> **TDZ** = Temporal Dead Zone. `let` and `const` exist before their declaration line, but you can't access them — you get a `ReferenceError`.

```javascript
// ❌ var is function scoped — leaks out of blocks
if (true) {
    var leaked = "I'm everywhere!";
}
console.log(leaked); // "I'm everywhere!" — BAD

// ✅ let is block scoped — stays inside
if (true) {
    let contained = "I stay here.";
}
// console.log(contained); // ReferenceError — GOOD
```

> **Rule of thumb:** Use `const` by default. Use `let` only when you need to reassign. Never use `var`.

---

## 3.2 Data Types

JavaScript has **7 primitive types** and **1 reference type**:

### Primitive Types

```javascript
// String — text
let name = "Alice";
let greeting = 'Hello';
let template = `Hi, ${name}!`;    // template literal

// Number — integers and decimals (both are 'number')
let age = 25;
let price = 9.99;

// Boolean — true or false
let isActive = true;
let isDeleted = false;

// null — intentional absence of value
let result = null;

// undefined — variable declared but not assigned
let score;
console.log(score); // undefined

// Symbol — unique identifier (rarely used by beginners)
let id = Symbol("id");

// BigInt — very large integers
let huge = 9007199254740991n;
```

### Reference Type

```javascript
// Object — collections of data (arrays, functions are also objects)
let person = { name: "Alice", age: 25 };
let colors = ["red", "green", "blue"];
```

---

## 3.3 `typeof` Operator

Check the type of any value:

```javascript
console.log(typeof "Hello");     // "string"
console.log(typeof 42);          // "number"
console.log(typeof true);        // "boolean"
console.log(typeof undefined);   // "undefined"
console.log(typeof null);        // "object"  ← JS bug! Should be "null"
console.log(typeof {});          // "object"
console.log(typeof []);          // "object"  ← Arrays are objects
console.log(typeof function(){}); // "function"
```

> The `typeof null === "object"` bug has been in JavaScript since day one. It's never been fixed for backward compatibility.

---

## 3.4 Type Coercion & Dynamic Typing

JavaScript is **dynamically typed** — variables can change types:

```javascript
let value = "Hello";   // string
value = 42;            // now it's a number — no error!
```

**Type coercion** — JavaScript automatically converts types in certain situations:

```javascript
// String + Number = String (concatenation)
console.log("5" + 3);     // "53" (number becomes string)

// Other operators convert to number
console.log("5" - 3);     // 2
console.log("5" * 2);     // 10
console.log("5" / 2);     // 2.5

// Boolean to number
console.log(true + 1);    // 2 (true = 1)
console.log(false + 1);   // 1 (false = 0)
```

> Type coercion is a common source of bugs. This is why `===` (strict equality) is important — it doesn't coerce types.

---

## 3.5 TaskMaster: Add Task Variables

Update `app.js`:

```javascript
// TaskMaster — A browser-based task management app

// Task data using different variable types
const APP_NAME = "TaskMaster";           // string, never changes
const MAX_TASKS = 100;                   // number, limit
let taskCount = 0;                       // number, will change
let tasks = [];                          // array (object), will grow

// A single task as an object
let sampleTask = {
    id: 1,
    title: "Learn JavaScript",
    completed: false,
    priority: "high",
    createdAt: new Date().toISOString()
};

console.log(`${APP_NAME} loaded!`);
console.log("Sample task:", sampleTask);
console.log("Task title type:", typeof sampleTask.title);    // "string"
console.log("Task completed type:", typeof sampleTask.completed); // "boolean"
console.log("Tasks array type:", typeof tasks);               // "object"
```

### Try it

1. Update your `app.js` with the code above
2. Open the browser console and check the output
3. Try changing the `sampleTask` values and see how `typeof` responds
4. What happens if you try `const APP_NAME = "New Name"` after the declaration?

---

---

# Part 4: Operators

---

## 4.1 Arithmetic Operators

```javascript
console.log(10 + 3);   // 13  — Addition
console.log(10 - 3);   // 7   — Subtraction
console.log(10 * 3);   // 30  — Multiplication
console.log(10 / 3);   // 3.333...  — Division
console.log(10 % 3);   // 1   — Remainder (modulo)
console.log(10 ** 3);  // 1000 — Exponentiation

// Increment and decrement
let count = 5;
count++;       // 6
count--;       // 5
```

---

## 4.2 Assignment Operators

```javascript
let x = 10;
x += 5;    // x = x + 5  → 15
x -= 3;    // x = x - 3  → 12
x *= 2;    // x = x * 2  → 24
x /= 4;    // x = x / 4  → 6
x %= 4;    // x = x % 4  → 2
```

---

## 4.3 Comparison Operators

```javascript
console.log(5 > 3);    // true
console.log(5 < 3);    // false
console.log(5 >= 5);   // true
console.log(5 <= 4);   // false
```

### `==` vs `===` — This is Critical

```javascript
// == (loose equality) — converts types before comparing
console.log(0 == "");       // true  — both become 0
console.log(0 == false);    // true  — both become 0
console.log("" == false);   // true  — both become 0
console.log(null == undefined); // true
console.log("5" == 5);     // true  — string becomes number

// === (strict equality) — no type conversion
console.log(0 === "");      // false — different types
console.log(0 === false);   // false
console.log("5" === 5);    // false
console.log(5 === 5);      // true  — same type, same value
```

> **Always use `===` and `!==`.** Using `==` leads to subtle bugs because of unexpected type conversions.

---

## 4.4 Logical Operators

```javascript
// && (AND) — true only if BOTH are true
console.log(true && true);    // true
console.log(true && false);   // false

// || (OR) — true if EITHER is true
console.log(true || false);   // true
console.log(false || false);  // false

// ! (NOT) — flips the value
console.log(!true);           // false
console.log(!false);          // true
```

---

## 4.5 Ternary Operator

A shorthand `if/else` that returns a value:

```javascript
let age = 20;
let status = age >= 18 ? "adult" : "minor";
console.log(status); // "adult"
```

---

## 4.6 Nullish Coalescing (`??`) & Optional Chaining (`?.`)

```javascript
// ?? — returns right side ONLY if left is null or undefined
let username = null;
console.log(username ?? "Guest");     // "Guest"
console.log(0 ?? "Guest");           // 0 (0 is not null/undefined)
console.log("" ?? "Guest");          // "" (empty string is not null/undefined)

// Compare with || which treats 0, "", false as falsy
console.log(0 || "Guest");           // "Guest" — probably not what you want!

// ?. — safely access nested properties without crashing
let user = { name: "Alice", address: null };
console.log(user.address?.city);     // undefined (no error)
// console.log(user.address.city);   // TypeError: Cannot read properties of null
```

> Use `??` when you want to provide a default only for `null`/`undefined`. Use `||` when you want to provide a default for any falsy value.

---

## 4.7 TaskMaster: Task Validation

Add this to `app.js`:

```javascript
// Task validation using operators
function isValidTask(title, priority) {
    // Check title is not empty and not too long
    const hasTitle = title && title.trim().length > 0;
    const validLength = title?.length <= 200;

    // Check priority is valid
    const validPriorities = ["low", "medium", "high"];
    const hasValidPriority = validPriorities.includes(priority ?? "medium");

    return hasTitle && validLength && hasValidPriority;
}

// Test it
console.log(isValidTask("Learn JS", "high"));     // true
console.log(isValidTask("", "high"));              // false
console.log(isValidTask("Learn JS", null));        // true (defaults to "medium")
console.log(isValidTask(null, "high"));            // false
```

### Try it

1. What does `10 % 3` return? What about `10 % 5`?
2. What's the difference between `null ?? "default"` and `null || "default"`?
3. What does `"" ?? "default"` return? What about `"" || "default"`?
4. Write an expression that checks if a number is even using `%`

---

---

# Part 5: Strings

---

## 5.1 Creating Strings

```javascript
let single = 'Hello';            // single quotes
let double = "Hello";            // double quotes
let backtick = `Hello`;          // template literal (backticks)
```

All three create strings, but **backticks** have superpowers:

```javascript
let name = "Alice";
let age = 25;

// Template literal — embed expressions with ${...}
let intro = `My name is ${name} and I'm ${age} years old.`;
console.log(intro);
// Output: My name is Alice and I'm 25 years old.

// Multi-line strings
let multiLine = `
  Line 1
  Line 2
  Line 3
`;
```

> **Prefer template literals** (backticks) whenever you need to include variables or multi-line text.

---

## 5.2 String Properties & Methods

Strings are **immutable** — methods return a new string, they don't change the original.

```javascript
let text = "  Hello, World!  ";

// Length
console.log(text.length);               // 17 (includes spaces)

// Case
console.log(text.toUpperCase());        // "  HELLO, WORLD!  "
console.log(text.toLowerCase());        // "  hello, world!  "

// Trimming whitespace
console.log(text.trim());              // "Hello, World!"
console.log(text.trimStart());         // "Hello, World!  "
console.log(text.trimEnd());           // "  Hello, World!"

// Searching
console.log(text.includes("World"));    // true
console.log(text.indexOf("World"));     // 9
console.log(text.startsWith("  He"));   // true
console.log(text.endsWith("!  "));      // true

// Extracting
console.log(text.slice(2, 7));          // "Hello"
console.log(text.slice(-8));            // "World!  "

// Replacing
console.log(text.replace("World", "JS")); // "  Hello, JS!  "

// Splitting into an array
console.log("a,b,c".split(","));        // ["a", "b", "c"]
console.log("hello".split(""));         // ["h", "e", "l", "l", "o"]
```

### What happened?

Every method returns a **new** string. The original `text` variable is unchanged — strings are immutable in JavaScript.

---

## 5.3 Practical String Usage

```javascript
// Checking user input
let email = "  User@Example.COM  ";
let cleaned = email.trim().toLowerCase();
console.log(cleaned); // "user@example.com"

// Building messages
let items = 3;
let message = `You have ${items} item${items !== 1 ? "s" : ""} in your cart.`;
console.log(message); // "You have 3 items in your cart."

// Extracting file extension
let filename = "report.final.pdf";
let ext = filename.slice(filename.lastIndexOf("."));
console.log(ext); // ".pdf"
```

---

## 5.4 TaskMaster: Task Title Formatting

Add to `app.js`:

```javascript
// Format and validate task titles
function formatTaskTitle(title) {
    if (!title || typeof title !== "string") return null;

    // Clean up the title
    let cleaned = title.trim();

    // Capitalize first letter
    cleaned = cleaned.charAt(0).toUpperCase() + cleaned.slice(1);

    // Truncate if too long
    if (cleaned.length > 50) {
        cleaned = cleaned.slice(0, 47) + "...";
    }

    return cleaned;
}

// Test it
console.log(formatTaskTitle("  learn javascript  "));
// Output: "Learn javascript"

console.log(formatTaskTitle("This is a very long task title that exceeds the maximum allowed character limit for display"));
// Output: "This is a very long task title that exceeds t..."

console.log(formatTaskTitle(""));
// Output: null
```

### Try it

1. Write a function that counts the number of words in a string (hint: `.split()` and `.length`)
2. Write a function that reverses a string (hint: `.split("")`, `.reverse()`, `.join("")`)
3. What does `"hello".includes("")` return? Why?

---

---

# Part 6: Numbers & Math

---

## 6.1 Numbers in JavaScript

JavaScript has **one number type** for both integers and decimals:

```javascript
let integer = 42;
let decimal = 3.14;
let negative = -10;

console.log(typeof integer);   // "number"
console.log(typeof decimal);   // "number"
```

### Special Number Values

```javascript
console.log(1 / 0);            // Infinity
console.log(-1 / 0);           // -Infinity
console.log("hello" * 2);      // NaN (Not a Number)
console.log(NaN === NaN);      // false (NaN is not equal to anything, even itself)
console.log(Number.isNaN(NaN)); // true (correct way to check)
```

---

## 6.2 Converting to Numbers

```javascript
console.log(Number("42"));      // 42
console.log(Number("3.14"));    // 3.14
console.log(Number(""));        // 0
console.log(Number("hello"));   // NaN
console.log(Number(true));      // 1
console.log(Number(false));     // 0

console.log(parseInt("42px"));     // 42  — stops at first non-digit
console.log(parseFloat("3.14em")); // 3.14
console.log(parseInt("abc"));     // NaN
```

---

## 6.3 Math Object

```javascript
console.log(Math.round(4.5));   // 5   — round to nearest integer
console.log(Math.floor(4.9));   // 4   — round down
console.log(Math.ceil(4.1));    // 5   — round up
console.log(Math.abs(-10));     // 10  — absolute value
console.log(Math.max(1, 5, 3)); // 5   — largest value
console.log(Math.min(1, 5, 3)); // 1   — smallest value
console.log(Math.sqrt(16));     // 4   — square root
console.log(Math.pow(2, 3));    // 8   — 2³

// Random number between 0 (inclusive) and 1 (exclusive)
console.log(Math.random());     // e.g., 0.7342...

// Random integer between min and max (inclusive)
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
console.log(randomInt(1, 10));  // e.g., 7
```

---

## 6.4 The Floating-Point Trap

```javascript
console.log(0.1 + 0.2);         // 0.30000000000000004 (NOT 0.3!)
console.log(0.1 + 0.2 === 0.3); // false

// Fix: round or use tolerance
console.log((0.1 + 0.2).toFixed(1));  // "0.3" (returns a string)
console.log(Math.abs(0.1 + 0.2 - 0.3) < 0.0001); // true
```

> This is a limitation of how all computers store decimals (IEEE 754), not a JavaScript bug. It happens in Python, Java, etc. too.

---

## 6.5 TaskMaster: Task Statistics

Add to `app.js`:

```javascript
// Generate a unique task ID
function generateTaskId() {
    return Date.now() + Math.floor(Math.random() * 1000);
}

// Calculate task completion percentage
function getCompletionPercentage(completed, total) {
    if (total === 0) return 0;
    return Math.round((completed / total) * 100);
}

// Test
console.log("Task ID:", generateTaskId());
console.log("Completion:", getCompletionPercentage(3, 10) + "%"); // "30%"
console.log("Completion:", getCompletionPercentage(0, 0) + "%");  // "0%"
```

### Try it

1. Generate a random number between 1 and 100
2. What does `parseInt("10.9")` return? What about `parseFloat("10.9")`?
3. Write a function that converts Celsius to Fahrenheit: `F = C × 9/5 + 32`
