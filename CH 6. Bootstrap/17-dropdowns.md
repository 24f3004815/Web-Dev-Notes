# Part 18: Dropdowns

---

## 18.1 Basic Dropdown

```html
<div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button"
            data-bs-toggle="dropdown" aria-expanded="false">
        Sort By
    </button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Price: Low to High</a></li>
        <li><a class="dropdown-item" href="#">Price: High to Low</a></li>
        <li><a class="dropdown-item" href="#">Newest First</a></li>
        <li><a class="dropdown-item" href="#">Best Selling</a></li>
    </ul>
</div>
```

> **Requires:** Bootstrap JavaScript bundle for toggle behavior.

---

## 18.2 Dropdown Elements

```html
<ul class="dropdown-menu">
    <!-- Header -->
    <li><h6 class="dropdown-header">Categories</h6></li>

    <!-- Items -->
    <li><a class="dropdown-item" href="#">Electronics</a></li>
    <li><a class="dropdown-item active" href="#">Audio</a></li>
    <li><a class="dropdown-item disabled" href="#">Coming Soon</a></li>

    <!-- Divider -->
    <li><hr class="dropdown-divider"></li>

    <!-- More items -->
    <li><a class="dropdown-item" href="#">View All</a></li>
</ul>
```

---

## 18.3 Dropdown Directions

```html
<!-- Drop down (default) -->
<div class="dropdown">

<!-- Drop up -->
<div class="dropup">

<!-- Drop start (left) -->
<div class="dropstart">

<!-- Drop end (right) -->
<div class="dropend">
```

---

## 18.4 Dropdown Alignment

```html
<!-- Right-aligned dropdown menu -->
<ul class="dropdown-menu dropdown-menu-end">

<!-- Left-aligned (default) -->
<ul class="dropdown-menu dropdown-menu-start">
```

---

## 18.5 Dropdown with Forms

```html
<div class="dropdown">
    <button class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown">
        <i class="bi bi-funnel"></i> Filter
    </button>
    <div class="dropdown-menu p-3" style="min-width: 250px;">
        <h6 class="dropdown-header px-0">Filter Products</h6>
        <div class="mb-2">
            <label class="form-label small">Price Range</label>
            <select class="form-select form-select-sm">
                <option>All Prices</option>
                <option>Under ₹1,000</option>
                <option>₹1,000 - ₹3,000</option>
                <option>₹3,000+</option>
            </select>
        </div>
        <div class="mb-2">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="inStock">
                <label class="form-check-label small" for="inStock">In Stock Only</label>
            </div>
        </div>
        <button class="btn btn-primary btn-sm w-100">Apply Filters</button>
    </div>
</div>
```

> Use `<div>` instead of `<ul>` for dropdowns with non-link content.

---

## 18.6 Auto Close Behavior

```html
<!-- Default: closes on click inside or outside -->
<div class="dropdown" data-bs-auto-close="true">

<!-- Don't close when clicking inside -->
<div class="dropdown" data-bs-auto-close="outside">

<!-- Don't close when clicking outside -->
<div class="dropdown" data-bs-auto-close="inside">

<!-- Only close with toggle button -->
<div class="dropdown" data-bs-auto-close="false">
```

---

## 18.7 ShopEase — Product Sort Dropdown

Add a sort dropdown above the product grid:

```html
<div class="d-flex justify-content-between align-items-center mb-4">
    <div>
        <h2 class="fw-bold mb-0">All Products</h2>
        <p class="text-muted mb-0">Showing 6 products</p>
    </div>
    <div class="dropdown">
        <button class="btn btn-outline-secondary dropdown-toggle" type="button"
                data-bs-toggle="dropdown" aria-expanded="false">
            <i class="bi bi-sort-down me-1"></i> Sort By
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
            <li><h6 class="dropdown-header">Sort Products</h6></li>
            <li><a class="dropdown-item active" href="#"><i class="bi bi-star me-2"></i>Featured</a></li>
            <li><a class="dropdown-item" href="#"><i class="bi bi-sort-numeric-down me-2"></i>Price: Low to High</a></li>
            <li><a class="dropdown-item" href="#"><i class="bi bi-sort-numeric-up me-2"></i>Price: High to Low</a></li>
            <li><a class="dropdown-item" href="#"><i class="bi bi-calendar me-2"></i>Newest First</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#"><i class="bi bi-fire me-2"></i>Best Selling</a></li>
        </ul>
    </div>
</div>
```

### What happened?

- `dropdown-menu-end` aligns the menu to the right edge of the button
- `active` highlights the currently selected sort option
- Icons from Bootstrap Icons make menu items more scannable
- `d-flex justify-content-between` pushes the title left and sort button right

### Try it

> **Exercise:** Create a "Categories" dropdown button that includes:
> - A header: "Shop by Category"
> - 4-5 category items with icons
> - A divider
> - An "All Categories" link at the bottom
