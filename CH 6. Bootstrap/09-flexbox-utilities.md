# Part 10: Flexbox Utilities

---

## 10.1 Enable Flexbox

Bootstrap provides utility classes for CSS Flexbox — no custom CSS needed.

```html
<div class="d-flex">Flex container (horizontal by default)</div>
<div class="d-inline-flex">Inline flex container</div>
```

---

## 10.2 Direction

```html
<div class="d-flex flex-row">Items left to right (default)</div>
<div class="d-flex flex-row-reverse">Items right to left</div>
<div class="d-flex flex-column">Items top to bottom</div>
<div class="d-flex flex-column-reverse">Items bottom to top</div>
```

Responsive: `flex-md-row`, `flex-lg-column`, etc.

---

## 10.3 Main-Axis Alignment (justify-content)

Controls horizontal alignment (in a row) or vertical alignment (in a column):

```html
<div class="d-flex justify-content-start">Left (default)</div>
<div class="d-flex justify-content-center">Center</div>
<div class="d-flex justify-content-end">Right</div>
<div class="d-flex justify-content-between">Space between</div>
<div class="d-flex justify-content-around">Space around</div>
<div class="d-flex justify-content-evenly">Space evenly</div>
```

```text
justify-content-start:    |■ ■ ■          |
justify-content-center:   |    ■ ■ ■      |
justify-content-end:       |         ■ ■ ■ |
justify-content-between:  |■     ■      ■ |
justify-content-around:   | ■    ■     ■  |
justify-content-evenly:   |  ■    ■    ■  |
```

---

## 10.4 Cross-Axis Alignment (align-items)

Controls vertical alignment (in a row):

```html
<div class="d-flex align-items-start" style="height: 100px;">Top</div>
<div class="d-flex align-items-center" style="height: 100px;">Center</div>
<div class="d-flex align-items-end" style="height: 100px;">Bottom</div>
<div class="d-flex align-items-stretch" style="height: 100px;">Stretch (default)</div>
<div class="d-flex align-items-baseline" style="height: 100px;">Baseline</div>
```

### Align Individual Items

```html
<div class="d-flex" style="height: 100px;">
    <div class="align-self-start">Top</div>
    <div class="align-self-center">Middle</div>
    <div class="align-self-end">Bottom</div>
</div>
```

---

## 10.5 Wrapping

```html
<div class="d-flex flex-wrap">Items wrap to next line</div>
<div class="d-flex flex-nowrap">Items stay on one line (default)</div>
<div class="d-flex flex-wrap-reverse">Wrap in reverse order</div>
```

---

## 10.6 Gap

```html
<div class="d-flex gap-2">Small gap between items</div>
<div class="d-flex gap-3">Medium gap</div>
<div class="d-flex gap-4">Large gap</div>
```

---

## 10.7 Grow & Shrink

```html
<div class="d-flex">
    <div class="flex-grow-1">Grows to fill remaining space</div>
    <div>Fixed</div>
</div>

<div class="d-flex">
    <div class="flex-shrink-0">Won't shrink</div>
    <div class="flex-shrink-1">Will shrink if needed</div>
</div>
```

---

## 10.8 Order

```html
<div class="d-flex">
    <div class="order-3">Shows third</div>
    <div class="order-1">Shows first</div>
    <div class="order-2">Shows second</div>
</div>
```

Values: `order-0` through `order-5`, plus `order-first` and `order-last`.

---

## 10.9 Common Flexbox Patterns

### Centering Everything

```html
<div class="d-flex justify-content-center align-items-center" style="height: 200px;">
    <p>Perfectly centered</p>
</div>
```

### Space Between with Vertical Centering (Header Pattern)

```html
<div class="d-flex justify-content-between align-items-center p-3 bg-light">
    <h5 class="mb-0">Logo</h5>
    <nav class="d-flex gap-3">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
</div>
```

### Sticky Footer Layout

```html
<div class="d-flex flex-column min-vh-100">
    <header class="p-3 bg-dark text-white">Header</header>
    <main class="flex-grow-1 p-3">Content grows to fill space</main>
    <footer class="p-3 bg-dark text-white">Footer stays at bottom</footer>
</div>
```

---

## 10.10 Responsive Flexbox

Every flex utility accepts breakpoints:

```html
<!-- Column on mobile, row on tablet+ -->
<div class="d-flex flex-column flex-md-row gap-3">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>

<!-- Centered on mobile, space-between on desktop -->
<div class="d-flex justify-content-center justify-content-lg-between">
    <span>Left</span>
    <span>Right</span>
</div>
```

---

## 10.11 ShopEase — Header with Flexbox

Build a simple header bar for ShopEase using flexbox utilities:

```html
<!-- Top utility bar -->
<div class="bg-dark text-white py-2">
    <div class="container d-flex justify-content-between align-items-center">
        <small>🔥 Free shipping on orders over ₹999!</small>
        <div class="d-none d-md-flex gap-3">
            <small><i class="bi bi-telephone"></i> +91 98765-43210</small>
            <small><i class="bi bi-envelope"></i> help@shopease.com</small>
        </div>
    </div>
</div>
```

### What happened?

- `d-flex justify-content-between` pushes the promo text left and contact info right
- `align-items-center` vertically centers everything
- Contact info is hidden on mobile (`d-none`) and shown from md up (`d-md-flex`)
- `gap-3` creates spacing between the contact items

### Try it

> **Exercise:** Build a product card footer using flexbox:
> - Price on the left
> - "Add to Cart" button on the right
> - Vertically centered
> - Use `d-flex justify-content-between align-items-center`
