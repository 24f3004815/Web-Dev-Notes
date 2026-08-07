# CSS Flexbox

Estimated Reading Time: 15 minutes

Prerequisites: [CSS Display](17-css-display.md), [Responsive Web Design](27-responsive-web-design.md)

Learning Objectives:
- Master the Flexible Box Layout Model (Flexbox).
- Understand Flex Container vs Flex Item relationships.
- Understand the Main Axis vs Cross Axis concept.
- Activate Flexbox layouts using `display: flex`.

---

## Introduction

The **Flexible Box Layout Module (Flexbox)** is a 1-dimensional CSS layout model designed to distribute space dynamically and align items along a row or column axis—even when element dimensions are unknown or dynamic.

Before Flexbox, aligning elements side-by-side or centering a box vertically required floats, table hacks, or relative positioning tricks. Flexbox provides built-in alignment, distribution, and re-ordering capabilities.

---

## Real-World Analogy

Imagine an elastic clothesline.

- **Flex Container (`display: flex`)**: The physical elastic clothesline cable stretched between two posts.
- **Flex Items**: Clothespins clipped onto the cable.
- **Main Axis**: The horizontal direction of the clothesline cable (Left to Right).
- **Cross Axis**: The vertical direction perpendicular to the cable (Top to Bottom).
- **Dynamic Resizing**: Pushing pins apart smoothly so clothes hangers adjust spacing automatically when the line stretches or shrinks.

Flexbox controls 1-dimensional element alignment.

---

## Core Concepts

### 1. The Two Axes
Flexbox operates on two perpendicular axes:
- **Main Axis**: Primary axis along which flex items are laid out (horizontal by default).
- **Cross Axis**: Perpendicular axis to the main axis (vertical by default).

### 2. Flex Container vs Flex Items
- **Flex Container**: The parent element declared with `display: flex;` or `display: inline-flex;`.
- **Flex Items**: The **direct children** of the flex container.

### 3. Container vs Item Properties
- **Container Properties**: `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap`.
- **Item Properties**: `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`, `order`.

---

## Syntax

```css
/* Activate Flexbox on Parent Container */
.flex-container {
    display: flex; /* Activates Flexbox */
    justify-content: space-between; /* Main axis alignment */
    align-items: center;            /* Cross axis alignment */
    gap: 20px;                      /* Spacing between items */
}

/* Direct Children automatically become Flex Items */
.flex-item {
    flex: 1; /* Grow equally */
}
```

---

## Property Reference

| Role | Property | Purpose | Values |
| :--- | :--- | :--- | :--- |
| Container | `display` | Activates Flexbox | `flex`, `inline-flex` |
| Container | `flex-direction` | Sets Main Axis direction | `row`, `column`, `row-reverse` |
| Container | `justify-content` | Aligns along Main Axis | `flex-start`, `center`, `space-between` |
| Container | `align-items` | Aligns along Cross Axis | `stretch`, `center`, `flex-start` |
| Container | `gap` | Sets gap spacing between items | Lengths (`20px`, `1rem`) |

---

## Visual Explanation

```mermaid
flowchart LR
    subgraph Flex Container (display: flex)
        A["Main Axis (Horizontal L -> R)"] --> Item1["Flex Item 1"]
        Item1 --> Item2["Flex Item 2"]
        Item2 --> Item3["Flex Item 3"]
    end
    
    CrossAxis["Cross Axis (Vertical Top -> Bottom)"] --> A
```

---

## Example 1

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Basic Flexbox Container</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 30px; background-color: #f8fafc; }
        
        .card-row {
            display: flex;
            gap: 20px;
            background-color: #ffffff;
            padding: 20px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
        }
        
        .card-box {
            flex: 1;
            background-color: #2563eb;
            color: #ffffff;
            padding: 20px;
            border-radius: 6px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="card-row">
        <div class="card-box">Flex Box 1</div>
        <div class="card-box">Flex Box 2</div>
        <div class="card-box">Flex Box 3</div>
    </div>
</body>
</html>
```

### CSS
```css
.card-row {
    display: flex;
    gap: 20px;
}
.card-box {
    flex: 1;
}
```

### Explanation
`display: flex` on `.card-row` turns it into a flex container. `flex: 1` on `.card-box` forces all 3 cards to expand equally across available horizontal space.

---

## Output Image Prompt

A browser window showing 3 blue card boxes arranged side-by-side in a horizontal row with equal widths and 20px spacing gaps.

---

## Code Explanation

- `display: flex;`: Converts parent container into a Flexbox layout box.
- `flex: 1;`: Instructs flex items to expand equally across available space.

---

## Example 2

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Perfect Vertical & Horizontal Centering</title>
    <style>
        body { margin: 0; font-family: Arial, sans-serif; }
        
        .center-wrapper {
            display: flex;
            justify-content: center; /* Main axis centering */
            align-items: center;     /* Cross axis centering */
            min-height: 100vh;
            background-color: #0f172a;
        }
        
        .centered-card {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 12px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="center-wrapper">
        <div class="centered-card">
            <h2 style="margin-top:0;">Perfect Centering</h2>
            <p style="margin:0; color:#64748b;">Centered vertically and horizontally using Flexbox.</p>
        </div>
    </div>
</body>
</html>
```

### CSS
```css
.center-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
```

### Explanation
Combining `justify-content: center` and `align-items: center` centers child content perfectly in 2 lines of CSS.

---

## Output Image Prompt

A browser window showing a white card centered in the screen viewport against a dark navy canvas (`#0f172a`).

---

## Code Explanation

- `justify-content: center`: Centers item horizontally along main axis.
- `align-items: center`: Centers item vertically along cross axis.

---

## Best Practices

- **Use Flexbox for 1D Layouts**: Use Flexbox for 1-dimensional rows or columns (navbars, card rows). Use CSS Grid for 2D layouts.
- **Use `gap` Property for Spacing**: Use `gap: 20px` on flex containers instead of margin hacks on children.

---

## Common Mistakes

### Mistake 1: Setting Flex Item Properties on Parent Container

```css
/* INCORRECT */
.flex-container {
    display: flex;
    flex: 1; /* Item property applied to container! Has no effect */
}
```

#### Explanation
`flex`, `flex-grow`, `flex-shrink`, and `align-self` belong on **flex items**, not containers.

```css
/* CORRECT */
.flex-container { display: flex; }
.flex-item { flex: 1; }
```

---

## Browser Compatibility

CSS Flexbox has 100% universal support across all desktop and mobile web browsers.

---

## Real-World Applications

- **Header Navbars**: Aligned logo and links.
- **Card Grid Rows**: Equal height product cards.
- **Modal Centering**: Vertical popup centering.

---

## Mini Project

### Project Objective: Equal Height Feature Cards
Build a 3-card feature section where all cards match equal height and width using Flexbox.

---

## Practice Exercises

### Beginner Level
1. Activate Flexbox on a `<div>` using `display: flex;`.
2. Center items horizontally using `justify-content: center;`.
3. Center items vertically using `align-items: center;`.
4. Add 15px space between flex items using `gap: 15px;`.
5. Make flex items expand equally using `flex: 1;`.

### Intermediate Level
6. Change flex direction to vertical column (`flex-direction: column`).
7. Push navbar logo left and links right using `justify-content: space-between`.
8. Create a full-screen perfectly centered login card wrapper (`min-height: 100vh`).
9. Wrap flex items onto multi-line rows using `flex-wrap: wrap`.
10. Override cross-axis alignment for a single item using `align-self: flex-end`.

### Advanced Level
11. Compare `flex-basis: 0` vs `flex-basis: auto` calculation algorithms.
12. Audit GPU paint engine costs of complex nested flex containers.
13. Implement auto-margin alignment tricks (`margin-left: auto`) inside flex rows.
14. Solve sub-pixel flex item width rounding bugs.
15. Build a dynamic responsive dashboard header with auto-collapsing flex items.

---

## Quick Quiz

**1. What CSS rule activates Flexbox on a parent container?**
A) `display: flex`  
B) `layout: flexbox`  

**2. How many dimensions does Flexbox handle primarily?**
A) 1 Dimension (row or column)  
B) 2 Dimensions  

**3. What is the default main axis direction in Flexbox?**
A) Horizontal row (`row`)  
B) Vertical column  

**4. What property centers items along the Main Axis?**
A) `align-items`  
B) `justify-content`  

**5. What property centers items along the Cross Axis?**
A) `align-items`  
B) `justify-content`  

**6. What property sets spacing gaps between flex items on the container?**
A) `gap`  
B) `flex-space`  

**7. Which element receives `display: flex`?**
A) The parent container  
B) Each individual child item  

**8. What property allows a single flex item to override container `align-items`?**
A) `align-self`  
B) `justify-self`  

**9. What does `flex: 1` do on flex items?**
A) Forces items to grow and distribute available space equally  
B) Rotates items 1 degree  

**10. How do you push a single flex item to the far right inside a flex row?**
A) `margin-left: auto`  
B) `float: right`  

---

### Answers
1: A | 2: A | 3: A | 4: B | 5: A | 6: A | 7: A | 8: A | 9: A | 10: A

---

## Interview Questions

**1. What is CSS Flexbox and how does it differ from CSS Grid?**  
*Answer:* Flexbox is a 1-dimensional layout model optimized for aligning content in a single row or column. CSS Grid is a 2-dimensional layout model designed to control rows and columns simultaneously.

**2. Explain Main Axis vs Cross Axis in Flexbox.**  
*Answer:* Main Axis is the primary direction along which flex items are placed (horizontal when `flex-direction: row`, vertical when `flex-direction: column`). Cross Axis is the axis perpendicular to Main Axis (`justify-content` controls Main Axis alignment; `align-items` controls Cross Axis alignment).

**3. How does `margin-left: auto` work inside a Flexbox row?**  
*Answer:* In a flex row, setting `margin-left: auto` on a single flex item consumes all remaining unused horizontal space to its left, pushing that item (and subsequent items) to the far right end of the container.

---

## Summary

- Set parent to **`display: flex`**.
- Use **`justify-content`** for Main Axis alignment.
- Use **`align-items`** for Cross Axis alignment.
- Use **`gap`** for item spacing.

---

## Cheat Sheet

```css
/* FLEX CONTAINER */
.flex-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

/* EQUAL FLEX ITEMS */
.flex-item {
    flex: 1;
}

/* PERFECT CENTERING */
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
```

---

## Related Topics

- **Previous Topic**: [Media Queries](28-media-queries.md)
- **Next Topic**: [Flex Direction](30-flex-direction.md)
- **Recommended Learning Order**: Introduction to CSS -> Ways to Add CSS -> CSS Selectors -> CSS Colors -> CSS Fonts -> CSS Borders -> Border Radius -> CSS Shadows -> CSS Margins -> CSS Padding -> CSS Width -> CSS Height -> CSS Box Model -> CSS Float -> CSS Overflow -> CSS Display -> CSS Position -> CSS Background Images -> CSS Background Properties -> CSS Combinators -> CSS Pseudo Classes -> CSS Pseudo Elements -> CSS Pagination -> CSS Dropdown Menu -> CSS Navigation Bar -> Responsive Web Design -> Media Queries -> CSS Flexbox -> Flex Direction
