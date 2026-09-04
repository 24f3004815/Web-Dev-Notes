# Part 4: The Grid System

This is Bootstrap's most important feature. Master this and you can build any layout.

---

## 4.1 How the Grid Works

```text
Container
   ↓
Row  (horizontal group)
   ↓
Columns  (content blocks — up to 12 per row)
```

Bootstrap divides every row into **12 equal columns**. You decide how many columns each element should span.

```text
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 |
|______________________________________________________________|
```

---

## 4.2 Basic Grid

### Equal-Width Columns

```html
<div class="container">
    <div class="row">
        <div class="col">Column 1</div>
        <div class="col">Column 2</div>
        <div class="col">Column 3</div>
    </div>
</div>
```

Three `.col` divs = three equal columns (4 columns each out of 12).

### Specific Column Widths

```html
<div class="container">
    <div class="row">
        <div class="col-8">Main Content (8/12)</div>
        <div class="col-4">Sidebar (4/12)</div>
    </div>
</div>
```

Common column patterns:

```text
col-12              → Full width (1 column)
col-6 + col-6       → Two equal halves
col-4 + col-4 + col-4 → Three equal thirds
col-3 × 4           → Four equal quarters
col-8 + col-4       → Main + sidebar
col-9 + col-3       → Wide main + narrow sidebar
```

### Rules

1. Columns must be inside a `.row`
2. Rows must be inside a `.container` (or `.container-fluid`)
3. Column numbers in a row should add up to 12 (or less)
4. If they exceed 12, extra columns wrap to the next line

---

## 4.3 Responsive Columns — Breakpoints

This is where Bootstrap's grid becomes powerful. You can set **different column widths at different screen sizes**.

### Breakpoint Classes

| Breakpoint | Class prefix | Screen width | Typical device |
|---|---|---|---|
| Extra small | `col-` | < 576px | Phones (portrait) |
| Small | `col-sm-` | ≥ 576px | Phones (landscape) |
| Medium | `col-md-` | ≥ 768px | Tablets |
| Large | `col-lg-` | ≥ 992px | Laptops |
| Extra large | `col-xl-` | ≥ 1200px | Desktops |
| Extra extra large | `col-xxl-` | ≥ 1400px | Large desktops |

### How to Read Responsive Classes

```html
<div class="col-12 col-md-6 col-lg-4">Product Card</div>
```

Translation:

```text
Mobile (< 768px):   col-12  → Full width (1 card per row)
Tablet (≥ 768px):   col-md-6 → Half width (2 cards per row)
Desktop (≥ 992px):  col-lg-4 → One-third width (3 cards per row)
```

**Mobile-first:** Start from the smallest class. Larger breakpoints override smaller ones going up.

---

## 4.4 Grid Gutters (Spacing Between Columns)

By default, columns have horizontal padding (gutters). Control them with `g-` classes on the `.row`:

```html
<!-- No gutters -->
<div class="row g-0">

<!-- Small gutters -->
<div class="row g-2">

<!-- Default gutters -->
<div class="row g-3">

<!-- Large gutters -->
<div class="row g-4">

<!-- Horizontal only -->
<div class="row gx-3">

<!-- Vertical only -->
<div class="row gy-3">
```

Gutter scale: `0`, `1`, `2`, `3`, `4`, `5`

---

## 4.5 Offset & Alignment

### Offset — Push Columns Right

```html
<div class="row">
    <div class="col-md-6 offset-md-3">Centered column</div>
</div>
```

This creates a 6-column-wide element, pushed 3 columns from the left = centered.

### Vertical Alignment

```html
<div class="row align-items-center" style="height: 200px;">
    <div class="col">Vertically centered</div>
</div>
```

### Horizontal Alignment

```html
<div class="row justify-content-center">
    <div class="col-6">Horizontally centered</div>
</div>
```

---

## 4.6 Nesting Rows

You can nest rows inside columns:

```html
<div class="container">
    <div class="row">
        <div class="col-md-8">
            <!-- Nested row inside a column -->
            <div class="row">
                <div class="col-6">Nested Left</div>
                <div class="col-6">Nested Right</div>
            </div>
        </div>
        <div class="col-md-4">Sidebar</div>
    </div>
</div>
```

> Nested rows get their own 12-column grid within the parent column.

---

## 4.7 ShopEase — Product Grid

Add this to your `index.html` inside the main `container`, below the welcome text:

```html
<!-- Product Grid -->
<h2 class="mb-4">Featured Products</h2>
<div class="row g-4">
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>Wireless Headphones</h5>
            <p class="text-muted">Premium sound quality</p>
            <p class="fw-bold">₹2,499</p>
        </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>Smart Watch</h5>
            <p class="text-muted">Track your fitness</p>
            <p class="fw-bold">₹4,999</p>
        </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>Laptop Stand</h5>
            <p class="text-muted">Ergonomic design</p>
            <p class="fw-bold">₹1,299</p>
        </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>USB-C Hub</h5>
            <p class="text-muted">7-in-1 connectivity</p>
            <p class="fw-bold">₹1,799</p>
        </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>Mechanical Keyboard</h5>
            <p class="text-muted">RGB backlit</p>
            <p class="fw-bold">₹3,499</p>
        </div>
    </div>
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded p-3">
            <h5>Webcam HD</h5>
            <p class="text-muted">1080p streaming</p>
            <p class="fw-bold">₹2,199</p>
        </div>
    </div>
</div>
```

### What happened?

- `row g-4` creates a row with comfortable gutters
- Each product: full-width on mobile (`col-12`), 2-per-row on small+ (`col-sm-6`), 3-per-row on large+ (`col-lg-4`)
- `border rounded p-3` gives each card a visible border with rounded corners and padding
- `text-muted` and `fw-bold` are Bootstrap utility classes

### Try it

1. Open in browser and resize from wide to narrow
2. Watch the products rearrange: 3 → 2 → 1 per row
3. **Exercise:** Add two more products. What happens to the layout?
4. **Exercise:** Change `col-lg-4` to `col-lg-3` — now you get 4 per row on desktop. Try it!
