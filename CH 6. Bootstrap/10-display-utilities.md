# Part 11: Display Utilities

---

## 11.1 Display Classes

Control how elements are displayed:

```html
<div class="d-block">Block element (full width, new line)</div>
<span class="d-inline">Inline element (stays in line)</span>
<span class="d-inline-block">Inline block (inline but can have width/height)</span>
<div class="d-flex">Flexbox container</div>
<div class="d-grid">Grid container</div>
<div class="d-none">Hidden (not rendered)</div>
<div class="d-table">Behaves like a table</div>
```

---

## 11.2 Responsive Display — Show/Hide Elements

This is one of the most commonly used utility patterns:

```html
<!-- Hidden everywhere, visible from md up -->
<div class="d-none d-md-block">Desktop only</div>

<!-- Visible on mobile, hidden from md up -->
<div class="d-block d-md-none">Mobile only</div>

<!-- Hidden everywhere, flex from lg up -->
<div class="d-none d-lg-flex">Desktop flex</div>

<!-- Visible from sm, hidden from lg up -->
<div class="d-none d-sm-block d-lg-none">Tablet only</div>
```

### Common Patterns

| What you want | Classes |
|---|---|
| Show only on mobile | `d-block d-md-none` |
| Show only on desktop | `d-none d-lg-block` |
| Show only on tablet | `d-none d-md-block d-lg-none` |
| Hide on mobile, show rest | `d-none d-md-block` |
| Show everywhere except lg | `d-block d-lg-none` |

---

## 11.3 Print Display

Control visibility when printing:

```html
<div class="d-print-none">Hidden when printing</div>
<div class="d-none d-print-block">Visible only when printing</div>
```

---

## 11.4 Grid Display

Bootstrap 5.3 supports CSS Grid via `d-grid`:

```html
<div class="d-grid gap-2">
    <button class="btn btn-primary">Full-width button</button>
    <button class="btn btn-secondary">Full-width button</button>
</div>
```

> `d-grid` makes all children full-width by default. Great for stacking buttons.

### Responsive Grid Columns

```html
<div class="d-grid gap-2 d-md-flex">
    <button class="btn btn-primary">Button 1</button>
    <button class="btn btn-secondary">Button 2</button>
</div>
```

Stacked on mobile (`d-grid`), inline from md up (`d-md-flex`).

---

## 11.5 ShopEase — Responsive Content Sections

```html
<!-- Desktop sidebar + main, mobile stacked -->
<div class="container my-4">
    <div class="row">
        <!-- Sidebar: hidden on mobile, visible on lg+ -->
        <div class="col-lg-3 d-none d-lg-block">
            <div class="bg-light rounded p-3">
                <h6 class="fw-bold mb-3">Categories</h6>
                <ul class="list-unstyled">
                    <li class="mb-2"><a href="#" class="text-decoration-none">Electronics</a></li>
                    <li class="mb-2"><a href="#" class="text-decoration-none">Accessories</a></li>
                    <li class="mb-2"><a href="#" class="text-decoration-none">Peripherals</a></li>
                    <li class="mb-2"><a href="#" class="text-decoration-none">Audio</a></li>
                </ul>
            </div>
        </div>

        <!-- Main content: full width on mobile, 9 cols on desktop -->
        <div class="col-12 col-lg-9">
            <!-- Mobile-only filter button (visible only on small screens) -->
            <button class="btn btn-outline-secondary mb-3 d-lg-none w-100">
                <i class="bi bi-funnel"></i> Show Filters
            </button>

            <h4>All Products</h4>
            <p class="text-muted">Showing 6 products</p>
            <!-- Product grid goes here -->
        </div>
    </div>
</div>
```

### What happened?

- Sidebar is hidden on mobile (`d-none`) and appears on large screens (`d-lg-block`)
- A "Show Filters" button appears only on mobile (`d-lg-none`) as a replacement
- Main content takes full width on mobile (`col-12`) and 9 columns on desktop (`col-lg-9`)

### Try it

> **Exercise:** Create an element that:
> 1. Shows as a grid (`d-grid`) on mobile
> 2. Shows as flexbox (`d-md-flex`) on tablet
> 3. Contains 3 buttons that stack on mobile and sit inline on tablet+
