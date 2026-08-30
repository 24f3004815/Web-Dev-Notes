# Part 12: Scope & Closures

---

## 12.1 Types of Scope

**Scope** determines where variables are accessible in your code.

```javascript
// 1. Global Scope — accessible everywhere
const globalVar = "I'm global";

function example() {
    // 2. Function Scope — accessible inside this function only
    const funcVar = "I'm function-scoped";

    if (true) {
        // 3. Block Scope — accessible inside this {} only
        const blockVar = "I'm block-scoped";
        let alsoBlock = "Me too";
        var notBlock = "I escape blocks!"; // var is NOT block-scoped
        console.log(blockVar);  // ✅ works
    }

    // console.log(blockVar);  // ❌ ReferenceError
    console.log(notBlock);     // ✅ "I escape blocks!" — var leaks out!
    console.log(funcVar);      // ✅ works
}

// console.log(funcVar);  // ❌ ReferenceError
console.log(globalVar);   // ✅ works
```

### Scope Summary

| Scope | Created by | `let`/`const` | `var` |
|---|---|---|---|
| Global | Top-level code | ✅ | ✅ |
| Function | `function() {}` | ✅ | ✅ |
| Block | `if {}`, `for {}`, `{}` | ✅ | ❌ (leaks out) |

---

## 12.2 Lexical Scope

Inner functions can access variables from outer functions. This is called **lexical** (or static) scoping — scope is determined by where code is **written**, not where it's **called**.

```javascript
function outer() {
    const message = "Hello from outer";

    function inner() {
        console.log(message); // ✅ Can access outer's variable
    }

    inner();
}
outer(); // "Hello from outer"
```

---

## 12.3 Closures

A **closure** is a function that **remembers** the variables from its outer scope, even after the outer function has returned.

```javascript
function counter() {
    let count = 0; // This variable is "closed over"

    return function() {
        count++;
        return count;
    };
}

const increment = counter();
console.log(increment()); // 1
console.log(increment()); // 2
console.log(increment()); // 3

// Each call to counter() creates a NEW closure
const anotherCounter = counter();
console.log(anotherCounter()); // 1 — starts fresh
```

### What happened?

When `counter()` finishes executing, normally `count` would be garbage collected. But because the returned function **references** `count`, JavaScript keeps it alive. The inner function "closes over" the variable — hence **closure**.

---

## 12.4 Practical Closure Examples

### Example 1: Private Variables

```javascript
function createWallet(initialBalance) {
    let balance = initialBalance; // private — can't be accessed directly

    return {
        deposit(amount) {
            balance += amount;
            return `Deposited $${amount}. Balance: $${balance}`;
        },
        withdraw(amount) {
            if (amount > balance) return "Insufficient funds";
            balance -= amount;
            return `Withdrew $${amount}. Balance: $${balance}`;
        },
        getBalance() {
            return balance;
        }
    };
}

const wallet = createWallet(100);
console.log(wallet.deposit(50));    // "Deposited $50. Balance: $150"
console.log(wallet.withdraw(30));   // "Withdrew $30. Balance: $120"
console.log(wallet.getBalance());   // 120
// console.log(wallet.balance);     // undefined — truly private!
```

### Example 2: Function Factory

```javascript
function createMultiplier(factor) {
    return (number) => number * factor;
}

const double = createMultiplier(2);
const triple = createMultiplier(3);
const tenX = createMultiplier(10);

console.log(double(5));  // 10
console.log(triple(5));  // 15
console.log(tenX(5));    // 50
```

### Example 3: The Classic Loop Gotcha

```javascript
// ❌ Common bug with var
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3 — NOT 0, 1, 2!
// Because var is function-scoped, there's only ONE 'i'

// ✅ Fixed with let (block-scoped — each iteration gets its own 'i')
for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2 ✅
```

> This is one of the most important reasons to use `let` instead of `var`.

---

---

# Part 13: The `this` Keyword

---

## 13.1 What is `this`?

`this` refers to the **object that is executing the current function**. Its value changes depending on **how** the function is called.

---

## 13.2 `this` in Different Contexts

```javascript
// 1. Global context — this = window (browser) or global (Node.js)
console.log(this); // Window {...} in browser

// 2. Object method — this = the object
const person = {
    name: "Alice",
    greet() {
        console.log(this.name); // "Alice"
    }
};
person.greet();

// 3. Regular function — this = window (non-strict) or undefined (strict)
function showThis() {
    console.log(this);
}
showThis(); // Window (non-strict) or undefined (strict mode)

// 4. Arrow function — this = enclosing scope's this (lexical)
const obj = {
    name: "Bob",
    greet: () => {
        console.log(this.name); // undefined! Arrow uses OUTER this
    },
    greetCorrect() {
        const inner = () => {
            console.log(this.name); // "Bob" — arrow inherits from greetCorrect
        };
        inner();
    }
};
obj.greet();         // undefined
obj.greetCorrect();  // "Bob"

// 5. Event handler — this = the element that fired the event
// button.addEventListener("click", function() {
//     console.log(this); // <button> element
// });
```

---

## 13.3 Quick Reference

| Context | `this` refers to |
|---|---|
| Global (non-strict) | `window` / `global` |
| Regular function (non-strict) | `window` / `global` |
| Regular function (strict) | `undefined` |
| Object method | The object |
| Arrow function | Enclosing scope's `this` |
| Event handler (function) | The element that fired the event |
| Event handler (arrow) | Enclosing scope's `this` |
| `new Constructor()` | The new object being created |
| `.bind(obj)` / `.call(obj)` / `.apply(obj)` | `obj` (explicitly set) |

---

## 13.4 `bind`, `call`, `apply`

These methods let you **explicitly set** what `this` should be:

```javascript
function greet(greeting) {
    return `${greeting}, I'm ${this.name}`;
}

const alice = { name: "Alice" };
const bob = { name: "Bob" };

// call — invokes immediately, args passed individually
console.log(greet.call(alice, "Hi"));     // "Hi, I'm Alice"
console.log(greet.call(bob, "Hello"));    // "Hello, I'm Bob"

// apply — same as call, but args passed as array
console.log(greet.apply(alice, ["Hey"])); // "Hey, I'm Alice"

// bind — returns a NEW function with this permanently set
const aliceGreet = greet.bind(alice);
console.log(aliceGreet("Yo"));           // "Yo, I'm Alice"
console.log(aliceGreet("Sup"));          // "Sup, I'm Alice"
```

> **Practical tip:** Use arrow functions in callbacks where you want to keep the outer `this`. Use `bind` when you need to pass a method as a callback but preserve its `this`.

### Try it

1. Create an object with a `name` and a `getName()` method. Call it — what does `this` refer to?
2. Store `getName` in a separate variable and call it. What happens to `this`? Fix it with `.bind()`
3. Why does an arrow function inside `setTimeout` inside an object method correctly access `this.name`?
