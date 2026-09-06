# Part 13: Buttons

---

## 13.1 Basic Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-light">Light</button>
<button class="btn btn-dark">Dark</button>
<button class="btn btn-link">Link</button>
```

> Always include the base `btn` class first, then the variant.

---

## 13.2 Outline Buttons

Transparent background with a colored border — lighter visual weight:

```html
<button class="btn btn-outline-primary">Primary</button>
<button class="btn btn-outline-secondary">Secondary</button>
<button class="btn btn-outline-success">Success</button>
<button class="btn btn-outline-danger">Danger</button>
<button class="btn btn-outline-warning">Warning</button>
<button class="btn btn-outline-info">Info</button>
<button class="btn btn-outline-dark">Dark</button>
```

---

## 13.3 Button Sizes

```html
<button class="btn btn-primary btn-lg">Large Button</button>
<button class="btn btn-primary">Default Button</button>
<button class="btn btn-primary btn-sm">Small Button</button>
```

---

## 13.4 Disabled Buttons

```html
<button class="btn btn-primary" disabled>Disabled</button>

<!-- For <a> tags, use the class instead -->
<a href="#" class="btn btn-primary disabled" aria-disabled="true">Disabled Link</a>
```

> For accessibility, always add `aria-disabled="true"` on disabled link-buttons.

---

## 13.5 Block Buttons (Full Width)

```html
<!-- Using d-grid for full-width stacked buttons -->
<div class="d-grid gap-2">
    <button class="btn btn-primary">Full Width</button>
    <button class="btn btn-secondary">Full Width</button>
</div>

<!-- Full width on mobile, inline from md up -->
<div class="d-grid gap-2 d-md-flex">
    <button class="btn btn-primary">Button 1</button>
    <button class="btn btn-secondary">Button 2</button>
</div>
```

---

## 13.6 Button on Any Element

The `btn` classes work on `<button>`, `<a>`, and `<input>`:

```html
<a href="#" class="btn btn-primary">Link Button</a>
<button class="btn btn-success">Button</button>
<input type="submit" class="btn btn-info" value="Submit">
```

---

## 13.7 Button Groups

Group related buttons together:

```html
<div class="btn-group" role="group" aria-label="Product actions">
    <button class="btn btn-primary">Buy</button>
    <button class="btn btn-outline-primary">Wishlist</button>
    <button class="btn btn-outline-primary">Compare</button>
</div>
```

### Vertical Button Group

```html
<div class="btn-group-vertical" role="group">
    <button class="btn btn-outline-secondary">Top</button>
    <button class="btn btn-outline-secondary">Middle</button>
    <button class="btn btn-outline-secondary">Bottom</button>
</div>
```

### Button Toolbar

```html
<div class="btn-toolbar gap-2" role="toolbar" aria-label="Toolbar">
    <div class="btn-group" role="group">
        <button class="btn btn-primary">1</button>
        <button class="btn btn-primary">2</button>
        <button class="btn btn-primary">3</button>
    </div>
    <div class="btn-group" role="group">
        <button class="btn btn-outline-secondary">A</button>
        <button class="btn btn-outline-secondary">B</button>
    </div>
</div>
```

---

## 13.8 Buttons with Icons

```html
<button class="btn btn-primary">
    <i class="bi bi-cart-plus me-1"></i> Add to Cart
</button>
<button class="btn btn-outline-danger">
    <i class="bi bi-heart me-1"></i> Wishlist
</button>
<button class="btn btn-success">
    <i class="bi bi-check-lg me-1"></i> Confirm
</button>

<!-- Icon-only button -->
<button class="btn btn-outline-secondary" aria-label="Search">
    <i class="bi bi-search"></i>
</button>
```

> Always add `aria-label` on icon-only buttons for screen readers.

---

## 13.9 ShopEase — Product Action Buttons

```html
<div class="row g-4">
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="card h-100 shadow-sm">
            <div class="card-body">
                <h5 class="card-title fw-bold">Wireless Headphones</h5>
                <p class="card-text text-muted">Premium noise-cancelling headphones</p>
                <p class="fs-5 fw-bold text-primary mb-3">₹2,499</p>

                <!-- Primary action: full width -->
                <div class="d-grid mb-2">
                    <button class="btn btn-primary">
                        <i class="bi bi-cart-plus me-1"></i> Add to Cart
                    </button>
                </div>

                <!-- Secondary actions: inline group -->
                <div class="d-flex gap-2">
                    <button class="btn btn-outline-secondary flex-grow-1 btn-sm">
                        <i class="bi bi-heart"></i> Wishlist
                    </button>
                    <button class="btn btn-outline-secondary flex-grow-1 btn-sm">
                        <i class="bi bi-arrow-repeat"></i> Compare
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
```

### What happened?

- `d-grid` makes "Add to Cart" span full width
- `d-flex gap-2` puts Wishlist and Compare side by side
- `flex-grow-1` makes both secondary buttons equal width
- `btn-sm` keeps secondary buttons smaller than the primary
- Icons from Bootstrap Icons add visual clarity

### Try it

> **Exercise:** Create a button toolbar for a product admin panel:
> - Group 1: `Edit`, `Duplicate`, `Archive` (primary outline buttons)
> - Group 2: `Delete` (danger button)
> - Wrap in a `btn-toolbar`
