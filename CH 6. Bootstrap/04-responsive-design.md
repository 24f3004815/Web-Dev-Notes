# Part 5: Responsive Design

---

## 5.1 Mobile-First Approach

Bootstrap is **mobile-first**: styles are designed for small screens first, then enhanced for larger ones.

```text
Write for mobile → Add tablet styles → Add desktop styles
     col-12      →     col-md-6       →     col-lg-4
```

This means:

- `col-12` applies to **all** screen sizes (mobile and up)
- `col-md-6` **overrides** at ≥ 768px (tablet and up)
- `col-lg-4` **overrides** at ≥ 992px (desktop and up)

Always start with the mobile layout, then enhance upward.

---

## 5.2 Responsive Breakpoint Summary

```text
xs: 0 - 575px       → Phones (portrait)
sm: 576px - 767px    → Phones (landscape)
md: 768px - 991px    → Tablets
lg: 992px - 1199px   → Laptops
xl: 1200px - 1399px  → Desktops
xxl: 1400px+         → Large desktops
```

> **Tip:** Most responsive work happens between `col-12` (mobile), `col-md-` (tablet), and `col-lg-` (desktop).

---

## 5.3 Responsive Display Utilities

Show or hide elements at different screen sizes:

```html
<!-- Hidden on mobile, visible from md up -->
<div class="d-none d-md-block">Only on tablets and desktop</div>

<!-- Visible on mobile only, hidden from md up -->
<div class="d-block d-md-none">Only on mobile</div>

<!-- Hidden on mobile, flex from lg up -->
<div class="d-none d-lg-flex">Flex layout on desktop only</div>
```

| Class | Effect |
|---|---|
| `d-none` | Hidden on all sizes |
| `d-block` | Visible as block |
| `d-none d-md-block` | Hidden on xs/sm, visible from md up |
| `d-block d-md-none` | Visible on xs/sm, hidden from md up |
| `d-none d-lg-block` | Hidden until lg |

---

## 5.4 Responsive Spacing

Spacing utilities also accept breakpoints:

```html
<!-- No margin on mobile, margin-top 4 on desktop -->
<div class="mt-0 mt-lg-4">Content</div>

<!-- Padding 2 on mobile, padding 5 on desktop -->
<div class="p-2 p-lg-5">Content</div>
```

---

## 5.5 Responsive Text Alignment

```html
<!-- Centered on mobile, left-aligned from md up -->
<p class="text-center text-md-start">Responsive alignment</p>

<!-- Left on mobile, centered on lg -->
<p class="text-start text-lg-center">Changes on desktop</p>
```

---

## 5.6 Responsive Flexbox

```html
<!-- Column on mobile, row on desktop -->
<div class="d-flex flex-column flex-md-row">
    <div>Item 1</div>
    <div>Item 2</div>
</div>
```

---

## 5.7 ShopEase — Responsive Layout

Let's make the ShopEase layout truly responsive. Update the main content area:

```html
<div class="container mt-4">
    <!-- Hero Section -->
    <div class="row align-items-center g-4 mb-5">
        <div class="col-12 col-lg-6">
            <h1 class="display-5 fw-bold">Shop Smart.<br>Shop Easy.</h1>
            <p class="lead text-muted">Discover quality products at unbeatable prices. Free shipping on orders over ₹999.</p>
            <div class="d-flex flex-column flex-sm-row gap-2">
                <a href="#products" class="btn btn-primary btn-lg">Shop Now</a>
                <a href="#deals" class="btn btn-outline-secondary btn-lg">Today's Deals</a>
            </div>
        </div>
        <div class="col-12 col-lg-6 d-none d-lg-block">
            <!-- Hero image placeholder (visible only on desktop) -->
            <div class="bg-light rounded-3 p-5 text-center text-muted">
                <p class="display-1">🛒</p>
                <p>Hero Image</p>
            </div>
        </div>
    </div>

    <!-- Products Section -->
    <h2 class="mb-4" id="products">Featured Products</h2>
    <!-- ... product grid from previous chapter ... -->
</div>
```

### What happened?

- **Hero section:** Two-column on desktop (`col-lg-6`), single column stacked on mobile (`col-12`)
- **Buttons:** Stack vertically on mobile (`flex-column`), side by side from sm up (`flex-sm-row`)
- **Hero image:** Hidden on mobile (`d-none`), visible on desktop (`d-lg-block`)
- **Text:** Large display heading (`display-5`), lead text for emphasis

### Try it

1. Resize from desktop to mobile
2. Watch the hero switch from 2-column to single-column
3. Watch buttons stack on small screens
4. Notice the hero image disappears on mobile (saves space)

> **Exercise:** Build a 3-section layout:
>
> - **Mobile:** All 3 sections stacked (full width)
> - **Tablet:** Section 1 full width, Sections 2 & 3 side by side
> - **Desktop:** All 3 sections in one row
>
> Hint: Use `col-12`, `col-md-6`, `col-lg-4`
