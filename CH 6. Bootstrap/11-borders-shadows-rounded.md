# Part 12: Borders, Shadows & Rounded Corners

---

## 12.1 Borders

### Add Borders

```html
<div class="border p-3">Border on all sides</div>
<div class="border-top p-3">Border top only</div>
<div class="border-bottom p-3">Border bottom only</div>
<div class="border-start p-3">Border left</div>
<div class="border-end p-3">Border right</div>
```

### Remove Borders

```html
<div class="border border-0">No border</div>
<div class="border border-top-0">No top border</div>
<div class="border border-bottom-0">No bottom border</div>
```

### Border Colors

```html
<div class="border border-primary p-3">Primary border</div>
<div class="border border-success p-3">Success border</div>
<div class="border border-danger p-3">Danger border</div>
<div class="border border-warning p-3">Warning border</div>
<div class="border border-info p-3">Info border</div>
<div class="border border-dark p-3">Dark border</div>
```

### Border Width

```html
<div class="border border-1 p-3">Thin border</div>
<div class="border border-2 p-3">Medium border</div>
<div class="border border-3 p-3">Thick border</div>
<div class="border border-4 p-3">Thicker border</div>
<div class="border border-5 p-3">Thickest border</div>
```

### Border Opacity

```html
<div class="border border-primary border-opacity-75 p-3">75%</div>
<div class="border border-primary border-opacity-50 p-3">50%</div>
<div class="border border-primary border-opacity-25 p-3">25%</div>
```

---

## 12.2 Rounded Corners

```html
<div class="rounded p-3 bg-light">Rounded (default radius)</div>
<div class="rounded-0 p-3 bg-light">No rounding</div>
<div class="rounded-1 p-3 bg-light">Small radius</div>
<div class="rounded-2 p-3 bg-light">Medium radius</div>
<div class="rounded-3 p-3 bg-light">Large radius</div>
<div class="rounded-4 p-3 bg-light">Extra large radius</div>
<div class="rounded-5 p-3 bg-light">Largest radius</div>
<div class="rounded-pill px-4 py-2 bg-primary text-white">Pill shape</div>
<div class="rounded-circle bg-primary text-white d-inline-flex 
     justify-content-center align-items-center" style="width:60px;height:60px;">
    AB
</div>
```

### Directional Rounding

```html
<div class="rounded-top p-3 bg-light">Top corners rounded</div>
<div class="rounded-bottom p-3 bg-light">Bottom corners rounded</div>
<div class="rounded-start p-3 bg-light">Left corners rounded</div>
<div class="rounded-end p-3 bg-light">Right corners rounded</div>
```

---

## 12.3 Shadows

```html
<div class="shadow-none p-3 mb-3">No shadow</div>
<div class="shadow-sm p-3 mb-3">Small shadow</div>
<div class="shadow p-3 mb-3">Default shadow</div>
<div class="shadow-lg p-3 mb-3">Large shadow</div>
```

> **Tip:** Use `shadow-sm` for subtle depth (cards, buttons). Use `shadow-lg` for modals and elevated elements.

---

## 12.4 ShopEase — Styled Product Cards

Combine borders, shadows, and rounded corners to create professional product cards:

```html
<div class="row g-4">
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="border rounded-3 shadow-sm p-0 h-100">
            <!-- Product image placeholder -->
            <div class="bg-light rounded-top-3 p-5 text-center">
                <span class="display-4">🎧</span>
            </div>
            <!-- Product info -->
            <div class="p-3">
                <p class="text-uppercase fw-semibold text-muted small mb-1">Audio</p>
                <h5 class="fw-bold">Wireless Headphones</h5>
                <p class="text-body-secondary small">Premium sound quality with active noise cancellation</p>
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <span class="fs-5 fw-bold text-primary">₹2,499</span>
                        <span class="text-decoration-line-through text-muted small ms-2">₹3,999</span>
                    </div>
                    <span class="badge rounded-pill text-bg-success">37% off</span>
                </div>
            </div>
            <!-- Card footer with border-top -->
            <div class="border-top p-3">
                <button class="btn btn-primary w-100">
                    <i class="bi bi-cart-plus"></i> Add to Cart
                </button>
            </div>
        </div>
    </div>
    <!-- Repeat for more products -->
</div>
```

### What happened?

- `border rounded-3 shadow-sm` gives the card a subtle, professional look
- `rounded-top-3` rounds only the top of the image area
- `border-top` separates the footer from the card body
- `rounded-pill` on the badge creates a pill-shaped discount indicator
- `h-100` ensures all cards in a row are the same height

### Try it

> **Exercise:** Create a "team member" card with:
> - A `rounded-circle` avatar (use a colored div with initials)
> - A `shadow` on the card
> - A `border-start border-primary border-3` accent stripe
> - Name, role, and a short bio
