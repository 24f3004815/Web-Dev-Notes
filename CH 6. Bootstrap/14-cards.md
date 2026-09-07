# Part 15: Cards

---

## 15.1 Basic Card Structure

```html
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Card Title</h5>
        <h6 class="card-subtitle mb-2 text-muted">Subtitle</h6>
        <p class="card-text">Some quick example text.</p>
        <a href="#" class="card-link">Learn more</a>
    </div>
</div>
```

---

## 15.2 Card with Image

```html
<div class="card" style="width: 18rem;">
    <img src="product.jpg" class="card-img-top" alt="Product Name">
    <div class="card-body">
        <h5 class="card-title">Product Name</h5>
        <p class="card-text">Short description of the product.</p>
        <a href="#" class="btn btn-primary">Buy Now</a>
    </div>
</div>
```

- `card-img-top` — image at the top of the card
- `card-img-bottom` — image at the bottom

---

## 15.3 Card Header & Footer

```html
<div class="card">
    <div class="card-header">
        Featured Product
    </div>
    <div class="card-body">
        <h5 class="card-title">Wireless Earbuds</h5>
        <p class="card-text">Crystal clear sound with 24-hour battery life.</p>
        <button class="btn btn-primary">Add to Cart</button>
    </div>
    <div class="card-footer text-body-secondary">
        Last updated 3 days ago
    </div>
</div>
```

---

## 15.4 List Groups Inside Cards

```html
<div class="card">
    <div class="card-header fw-bold">Order Summary</div>
    <ul class="list-group list-group-flush">
        <li class="list-group-item d-flex justify-content-between">
            <span>Headphones ×1</span>
            <span>₹2,499</span>
        </li>
        <li class="list-group-item d-flex justify-content-between">
            <span>USB Hub ×1</span>
            <span>₹1,799</span>
        </li>
        <li class="list-group-item d-flex justify-content-between fw-bold">
            <span>Total</span>
            <span>₹4,298</span>
        </li>
    </ul>
</div>
```

`list-group-flush` removes outer borders so the list fits seamlessly inside the card.

---

## 15.5 Card Image Overlays

```html
<div class="card text-bg-dark">
    <img src="hero.jpg" class="card-img" alt="Hero" style="opacity: 0.4;">
    <div class="card-img-overlay d-flex flex-column justify-content-end">
        <h5 class="card-title">New Collection</h5>
        <p class="card-text">Explore our latest arrivals.</p>
    </div>
</div>
```

---

## 15.6 Horizontal Card

```html
<div class="card mb-3" style="max-width: 540px;">
    <div class="row g-0">
        <div class="col-4">
            <img src="product.jpg" class="img-fluid rounded-start h-100 object-fit-cover" alt="Product">
        </div>
        <div class="col-8">
            <div class="card-body">
                <h5 class="card-title">Product Name</h5>
                <p class="card-text">Description goes here.</p>
                <p class="card-text"><small class="text-body-secondary">₹1,499</small></p>
            </div>
        </div>
    </div>
</div>
```

---

## 15.7 Card Groups & Grid Layouts

### Card Group (equal-height, joined cards)

```html
<div class="card-group">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Plan A</h5>
            <p class="card-text">Basic plan features.</p>
        </div>
    </div>
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Plan B</h5>
            <p class="card-text">Pro plan features.</p>
        </div>
    </div>
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Plan C</h5>
            <p class="card-text">Enterprise features.</p>
        </div>
    </div>
</div>
```

### Card Grid (using Bootstrap grid)

```html
<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
    <div class="col">
        <div class="card h-100">
            <div class="card-body">Card 1</div>
        </div>
    </div>
    <div class="col">
        <div class="card h-100">
            <div class="card-body">Card 2</div>
        </div>
    </div>
    <div class="col">
        <div class="card h-100">
            <div class="card-body">Card 3</div>
        </div>
    </div>
</div>
```

- `row-cols-1` → 1 card per row on mobile
- `row-cols-md-2` → 2 cards per row on tablet
- `row-cols-lg-3` → 3 cards per row on desktop
- `h-100` ensures equal card heights

---

## 15.8 ShopEase — Complete Product Cards

```html
<!-- Product Grid -->
<section class="py-5">
    <div class="container">
        <h2 class="fw-bold mb-1">Featured Products</h2>
        <p class="text-muted mb-4">Handpicked just for you</p>

        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 g-4">
            <!-- Product 1 -->
            <div class="col">
                <div class="card h-100 shadow-sm border-0">
                    <div class="bg-light text-center p-4 rounded-top">
                        <span class="display-3">🎧</span>
                    </div>
                    <div class="card-body">
                        <span class="badge text-bg-success mb-2">Best Seller</span>
                        <h5 class="card-title fw-bold">Wireless Headphones</h5>
                        <p class="card-text text-muted small">Premium noise-cancelling over-ear headphones with 30-hour battery.</p>
                        <div class="d-flex align-items-center gap-2 mb-3">
                            <span class="fs-5 fw-bold text-primary">₹2,499</span>
                            <span class="text-decoration-line-through text-muted small">₹3,999</span>
                            <span class="badge rounded-pill text-bg-danger">37% off</span>
                        </div>
                    </div>
                    <div class="card-footer bg-transparent border-0 pb-3 px-3">
                        <div class="d-grid">
                            <button class="btn btn-primary">
                                <i class="bi bi-cart-plus me-1"></i> Add to Cart
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="col">
                <div class="card h-100 shadow-sm border-0">
                    <div class="bg-light text-center p-4 rounded-top">
                        <span class="display-3">⌚</span>
                    </div>
                    <div class="card-body">
                        <span class="badge text-bg-info mb-2">New Arrival</span>
                        <h5 class="card-title fw-bold">Smart Watch</h5>
                        <p class="card-text text-muted small">Fitness tracker with heart rate monitor and GPS.</p>
                        <div class="d-flex align-items-center gap-2 mb-3">
                            <span class="fs-5 fw-bold text-primary">₹4,999</span>
                            <span class="text-decoration-line-through text-muted small">₹6,999</span>
                            <span class="badge rounded-pill text-bg-danger">28% off</span>
                        </div>
                    </div>
                    <div class="card-footer bg-transparent border-0 pb-3 px-3">
                        <div class="d-grid">
                            <button class="btn btn-primary">
                                <i class="bi bi-cart-plus me-1"></i> Add to Cart
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="col">
                <div class="card h-100 shadow-sm border-0">
                    <div class="bg-light text-center p-4 rounded-top">
                        <span class="display-3">💻</span>
                    </div>
                    <div class="card-body">
                        <span class="badge text-bg-warning text-dark mb-2">Limited Stock</span>
                        <h5 class="card-title fw-bold">Laptop Stand</h5>
                        <p class="card-text text-muted small">Adjustable aluminum stand for ergonomic working.</p>
                        <div class="d-flex align-items-center gap-2 mb-3">
                            <span class="fs-5 fw-bold text-primary">₹1,299</span>
                            <span class="text-decoration-line-through text-muted small">₹1,999</span>
                            <span class="badge rounded-pill text-bg-danger">35% off</span>
                        </div>
                    </div>
                    <div class="card-footer bg-transparent border-0 pb-3 px-3">
                        <div class="d-grid">
                            <button class="btn btn-primary">
                                <i class="bi bi-cart-plus me-1"></i> Add to Cart
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
```

### What happened?

- `row-cols-*` provides responsive columns without specifying `col-*` on each item
- `card h-100` makes cards equal height within a row
- `shadow-sm border-0` gives a floating card look
- `card-footer bg-transparent border-0` removes the default footer border
- Badges show product status (Best Seller, New Arrival, Limited Stock)
- Price + discount layout uses `d-flex align-items-center gap-2`

### Try it

> **Exercise:** Add 3 more products to the grid. Use different badge colors and product types. Try adding a horizontal card for a "Featured Deal" section above the grid.
