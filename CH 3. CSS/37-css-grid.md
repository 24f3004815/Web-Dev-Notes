# CSS Grid

Estimated Reading Time: 15 minutes

Prerequisites: [CSS Display](17-css-display.md), [CSS Flexbox](29-css-flexbox.md)

Learning Objectives:
- Master the 2-Dimensional CSS Grid Layout Module.
- Understand Grid Container vs Grid Item relationships.
- Differentiate between Flexbox (1D) and CSS Grid (2D).
- Activate Grid layouts using `display: grid`.

---

## Introduction

**CSS Grid Layout** is a powerful 2-dimensional layout engine built directly into modern web browsers. It allows developers to organize content into structured rows and columns simultaneously.

While Flexbox is designed for 1-dimensional component alignments (either horizontal rows OR vertical columns), CSS Grid is designed for 2-dimensional page layout structures, dashboard grids, magazine editorial layouts, and complex photo galleries.

---

## Real-World Analogy

Imagine a chessboard or spreadsheet table.

- **Flexbox (1D)**: A single queue line of passengers standing in front of a ticket counter.
- **CSS Grid (2D)**: A chessboard grid with lettered columns (A–H) and numbered rows (1–8). You can place any chess piece in a specific grid cell location (e.g. `E4`), span a queen across multiple columns, or define row heights and column widths simultaneously.

CSS Grid manages 2-dimensional row and column layouts.

---

## Core Concepts

### 1. 2D Layout Engine
Grid manages both horizontal columns and vertical rows simultaneously.

### 2. Fractional Unit (`fr`)
The `fr` unit represents a fraction of available free space inside the grid container (`grid-template-columns: 1fr 2fr 1fr;`).

### 3. Grid Lines & Cells
- **Grid Lines**: Numbered horizontal and vertical dividing lines starting at index `1`.
- **Grid Cell**: Single intersection unit box between four grid lines.
- **Grid Area**: Rectangular region spanning multiple cells.

---

## Syntax

```css
/* Activate CSS Grid */
.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 20px;                             /* Gaps between grid cells */
}

/* Spanning Grid Items */
.featured-item {
    grid-column: span 2; /* Spans across 2 columns */
}
```

---

## Property Reference

| Grid Property | Role | Purpose |
| :--- | :--- | :--- |
| `display: grid` | Container | Activates CSS Grid engine |
| `grid-template-columns` | Container | Defines column count and widths |
| `grid-template-rows` | Container | Defines row heights |
| `gap` | Container | Sets row and column gutter spacing |
| `grid-column` | Item | Specifies column start/span |
| `grid-row` | Item | Specifies row start/span |

---

## Visual Explanation

```mermaid
flowchart TD
    subgraph CSS Grid Container (display: grid)
        A["Column 1 (1fr)"] --- B["Column 2 (1fr)"] --- C["Column 3 (1fr)"]
        D["Row 1"] --- E["Row 2"]
    end
```

---

## Example 1

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Basic 3-Column CSS Grid</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 30px; background-color: #f8fafc; }
        
        .grid-wrapper {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }
        
        .grid-box {
            background-color: #2563eb;
            color: white;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="grid-wrapper">
        <div class="grid-box">Box 1</div>
        <div class="grid-box">Box 2</div>
        <div class="grid-box">Box 3</div>
        <div class="grid-box">Box 4</div>
        <div class="grid-box">Box 5</div>
        <div class="grid-box">Box 6</div>
    </div>
</body>
</html>
```

### CSS
```css
.grid-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}
```

### Explanation
`display: grid` combined with `grid-template-columns: repeat(3, 1fr)` builds a 3-column layout grid. Excess items automatically flow onto subsequent rows.

---

## Output Image Prompt

A browser window showing 6 blue boxes arranged neatly in a 3-column by 2-row grid with 20px gutters.

---

## Code Explanation

- `display: grid;`: Activates 2D CSS Grid engine on parent container.
- `grid-template-columns: repeat(3, 1fr);`: Creates 3 equal flexible columns.

---

## Example 2

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Auto-Fit Responsive Grid</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        
        .auto-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }
        
        .card {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 20px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="auto-grid">
        <div class="card">Card A</div>
        <div class="card">Card B</div>
        <div class="card">Card C</div>
    </div>
</body>
</html>
```

### CSS
```css
.auto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}
```

### Explanation
`repeat(auto-fit, minmax(220px, 1fr))` creates a fully responsive media-query-free card grid that adapts across mobile and desktop displays automatically.

---

## Output Image Prompt

A browser window displaying 3 white cards that adjust column counts automatically as screen width resizes.

---

## Code Explanation

- `repeat(auto-fit, minmax(220px, 1fr))`: Dynamic responsive grid pattern automatically wrapping columns at 220px minimum width.

---

## Best Practices

- **Use CSS Grid for 2D Layouts**: Use Grid for overall page layouts and 2D card grids. Use Flexbox for 1D navigation items.
- **Use `repeat(auto-fit, minmax())` for Grids**: Create responsive card grids without writing media queries.

---

## Common Mistakes

### Mistake 1: Using Flexbox for Complex 2D Layouts

```css
/* INCORRECT (Overcomplicating 2D layouts with nested Flex containers) */
.row { display: flex; }
.col { flex: 1; }
```

#### Explanation
CSS Grid handles rows and columns simultaneously in a single clean container.

```css
/* CORRECT */
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```

---

## Browser Compatibility

CSS Grid has 100% universal support across all desktop and mobile web browsers.

---

## Real-World Applications

- **Dashboard Layouts**: Sidebars, main feeds, and top headers.
- **E-Commerce Product Catalogs**: Responsive 4-column product grids.
- **Magazine Editorial Layouts**: Spanning featured articles across multiple cells.

---

## Mini Project

### Project Objective: Responsive Dashboard Grid
Build a dashboard layout with a full-width header, 2-column main area, and a 3-card grid.

---

## Practice Exercises

### Beginner Level
1. Activate CSS Grid using `display: grid;`.
2. Define 3 equal columns using `grid-template-columns: 1fr 1fr 1fr;`.
3. Use the `repeat()` function: `grid-template-columns: repeat(4, 1fr);`.
4. Add 20px grid gaps using `gap: 20px;`.
5. Span an item across 2 columns using `grid-column: span 2;`.

### Intermediate Level
6. Create an auto-responsive grid using `repeat(auto-fit, minmax(200px, 1fr))`.
7. Define explicit row heights using `grid-template-rows: 100px auto 60px;`.
8. Align grid items using `place-items: center`.
9. Define grid areas using `grid-template-areas`.
10. Combine CSS Grid with media queries for mobile layouts.

### Advanced Level
11. Compare `auto-fit` vs `auto-fill` grid column calculation behavior.
12. Audit GPU paint engine costs of complex nested Grid layouts.
13. Build a magazine layout spanning items across irregular rows and columns.
14. Optimize sub-pixel grid line calculation rendering.
15. Solve mobile Safari grid track calculation bugs.

---

## Quick Quiz

**1. What CSS rule activates CSS Grid?**
A) `display: grid`  
B) `display: flex`  

**2. How many dimensions does CSS Grid handle?**
A) 2 Dimensions (rows and columns simultaneously)  
B) 1 Dimension  

**3. What does the `fr` unit represent?**
A) Fraction of available free space  
B) Frame resolution  

**4. What function creates repeated column patterns?**
A) `repeat(count, width)`  
B) `loop()`  

**5. Which pattern creates auto-responsive grids without media queries?**
A) `repeat(auto-fit, minmax(200px, 1fr))`  
B) `width: 100%`  

**6. What property spans a grid item across 2 columns?**
A) `grid-column: span 2`  
B) `column-span: 2`  

**7. Where are column tracks defined?**
A) `grid-template-columns`  
B) `flex-direction`  

**8. What property sets grid gutters?**
A) `gap`  
B) `grid-padding`  

**9. Starting index number for CSS Grid lines?**
A) `1`  
B) `0`  

**10. What shorthand combines `align-items` and `justify-items` in Grid?**
A) `place-items`  
B) `grid-align`  

---

### Answers
1: A | 2: A | 3: A | 4: A | 5: A | 6: A | 7: A | 8: A | 9: A | 10: A

---

## Interview Questions

**1. What is CSS Grid and how does it differ from Flexbox?**  
*Answer:* CSS Grid is a 2-dimensional layout engine designed to manage rows and columns simultaneously. Flexbox is a 1-dimensional layout engine designed for row OR column content alignment.

**2. Explain `auto-fit` vs `auto-fill` in CSS Grid.`**  
*Answer:* Both wrap grid columns when space runs out. `auto-fill` creates empty invisible grid column tracks to fill unused row space. `auto-fit` collapses empty tracks to 0px, allowing active grid items to stretch and fill the row completely.

**3. What is the fractional (`fr`) unit?**  
*Answer:* The `fr` unit represents a flexible fraction of available free space within a grid container after fixed dimensions and gaps are deducted.

---

## Summary

- Use **`display: grid`** for 2D layouts.
- **`grid-template-columns: repeat(3, 1fr)`**: 3 equal columns.
- **`repeat(auto-fit, minmax(200px, 1fr))`**: Auto-responsive grids.

---

## Cheat Sheet

```css
/* 3-COLUMN GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

/* AUTO-RESPONSIVE GRID */
.auto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

---

## Related Topics

- **Previous Topic**: [Order](36-order.md)
- **Next Topic**: [Grid Template Columns](38-grid-template-columns.md)
- **Recommended Learning Order**: Introduction to CSS -> Ways to Add CSS -> CSS Selectors -> CSS Colors -> CSS Fonts -> CSS Borders -> Border Radius -> CSS Shadows -> CSS Margins -> CSS Padding -> CSS Width -> CSS Height -> CSS Box Model -> CSS Float -> CSS Overflow -> CSS Display -> CSS Position -> CSS Background Images -> CSS Background Properties -> CSS Combinators -> CSS Pseudo Classes -> CSS Pseudo Elements -> CSS Pagination -> CSS Dropdown Menu -> CSS Navigation Bar -> Responsive Web Design -> Media Queries -> CSS Flexbox -> Flex Direction -> Justify Content -> Align Items -> Align Self -> Flex Wrap -> Gap -> Order -> CSS Grid -> Grid Template Columns
