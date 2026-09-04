# Part 6: Typography

---

## 6.1 Headings

Bootstrap styles all HTML headings (`<h1>` to `<h6>`) automatically. You can also use heading classes on any element:

```html
<h1>h1 Heading</h1>
<h2>h2 Heading</h2>
<h3>h3 Heading</h3>
<p class="h1">Paragraph styled as h1</p>
```

---

## 6.2 Display Headings

Larger, bolder headings for hero sections and important titles:

```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```

> `display-1` is the largest, `display-6` is the smallest. Use these for page heroes and section headers — not for regular content headings.

---

## 6.3 Lead Text & Paragraphs

```html
<!-- Lead paragraph — larger, lighter text for introductions -->
<p class="lead">This paragraph stands out from regular text.</p>

<!-- Regular paragraph -->
<p>This is normal body text styled by Bootstrap.</p>

<!-- Muted/secondary text -->
<p class="text-muted">Less important secondary information.</p>

<!-- Small text -->
<p><small class="text-body-secondary">Fine print or captions.</small></p>
```

---

## 6.4 Text Alignment

```html
<p class="text-start">Left-aligned (default)</p>
<p class="text-center">Center-aligned</p>
<p class="text-end">Right-aligned</p>

<!-- Responsive alignment -->
<p class="text-center text-md-start">Centered on mobile, left on tablet+</p>
```

---

## 6.5 Text Transformation

```html
<p class="text-lowercase">LOWERCASED TEXT</p>       <!-- lowercased text -->
<p class="text-uppercase">uppercased text</p>       <!-- UPPERCASED TEXT -->
<p class="text-capitalize">capitalize each word</p> <!-- Capitalize Each Word -->
```

---

## 6.6 Font Weight & Style

```html
<p class="fw-bold">Bold text</p>
<p class="fw-semibold">Semibold text</p>
<p class="fw-medium">Medium weight</p>
<p class="fw-normal">Normal weight</p>
<p class="fw-light">Light text</p>
<p class="fst-italic">Italic text</p>
<p class="fst-normal">Normal style (removes italic)</p>
```

---

## 6.7 Text Decoration & Wrapping

```html
<a href="#" class="text-decoration-none">Link without underline</a>
<p class="text-decoration-underline">Underlined text</p>
<p class="text-decoration-line-through">Strikethrough text</p>

<!-- Prevent text from wrapping -->
<p class="text-nowrap">This text will not wrap to the next line.</p>

<!-- Truncate with ellipsis -->
<p class="text-truncate" style="max-width: 200px;">
    This very long text will be truncated with an ellipsis...
</p>
```

---

## 6.8 Line Height

```html
<p class="lh-1">Tight line height</p>
<p class="lh-sm">Small line height</p>
<p class="lh-base">Base line height (default)</p>
<p class="lh-lg">Large line height</p>
```

---

## 6.9 Font Size

```html
<p class="fs-1">Font size 1 (largest)</p>
<p class="fs-2">Font size 2</p>
<p class="fs-3">Font size 3</p>
<p class="fs-4">Font size 4</p>
<p class="fs-5">Font size 5</p>
<p class="fs-6">Font size 6 (smallest)</p>
```

---

## 6.10 Lists

Bootstrap styles lists cleanly by default. You can also remove default styling:

```html
<!-- Unstyled list (removes bullets and margin) -->
<ul class="list-unstyled">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

<!-- Inline list (items side by side) -->
<ul class="list-inline">
    <li class="list-inline-item">Home</li>
    <li class="list-inline-item">About</li>
    <li class="list-inline-item">Contact</li>
</ul>
```

---

## 6.11 Quick Reference Table

| Class | Effect |
|---|---|
| `display-1` to `display-6` | Large display headings |
| `lead` | Larger, lighter paragraph |
| `text-muted` | Gray secondary text |
| `text-start` / `text-center` / `text-end` | Text alignment |
| `text-uppercase` / `text-lowercase` / `text-capitalize` | Text transform |
| `fw-bold` / `fw-semibold` / `fw-light` | Font weight |
| `fst-italic` | Italic |
| `fs-1` to `fs-6` | Font size |
| `lh-1` / `lh-sm` / `lh-base` / `lh-lg` | Line height |
| `text-decoration-none` | Remove underline |
| `text-truncate` | Truncate with ellipsis |
| `list-unstyled` | Remove list bullets |
| `list-inline` | Horizontal list |

---

## 6.12 ShopEase — Apply Typography

Update the hero section and product cards with better typography:

```html
<!-- Announcement Bar -->
<div class="container-fluid bg-dark text-white py-2">
    <div class="container">
        <small class="text-uppercase fw-semibold letter-spacing-1">
            🔥 Free shipping on orders over ₹999!
        </small>
    </div>
</div>

<!-- Hero -->
<div class="container mt-4">
    <div class="row align-items-center g-4 mb-5">
        <div class="col-12 col-lg-6">
            <p class="text-uppercase fw-semibold text-primary mb-2">New Arrivals</p>
            <h1 class="display-4 fw-bold lh-1 mb-3">Shop Smart.<br>Shop Easy.</h1>
            <p class="lead text-muted mb-4">
                Discover quality products at unbeatable prices.
            </p>
            <div class="d-flex flex-column flex-sm-row gap-2">
                <a href="#products" class="btn btn-primary btn-lg">Shop Now</a>
                <a href="#deals" class="btn btn-outline-secondary btn-lg">Today's Deals</a>
            </div>
        </div>
    </div>

    <!-- Product Cards — improved typography -->
    <h2 class="fw-bold mb-1" id="products">Featured Products</h2>
    <p class="text-muted mb-4">Handpicked just for you</p>

    <div class="row g-4">
        <div class="col-12 col-sm-6 col-lg-4">
            <div class="border rounded p-3">
                <p class="text-uppercase fw-semibold text-muted small mb-1">Audio</p>
                <h5 class="fw-bold">Wireless Headphones</h5>
                <p class="text-body-secondary">Premium sound quality with noise cancellation</p>
                <p class="fs-5 fw-bold text-primary mb-0">₹2,499</p>
                <p class="text-decoration-line-through text-muted small">₹3,999</p>
            </div>
        </div>
        <!-- ... more product cards with same typography pattern ... -->
    </div>
</div>
```

### What happened?

- `text-uppercase fw-semibold` on the category label gives a clean tag look
- `display-4 fw-bold lh-1` makes the hero heading large with tight line height
- `lead text-muted` makes the description readable but secondary
- `text-decoration-line-through` creates the original-price strikethrough effect
- `fs-5 fw-bold text-primary` highlights the sale price

### Try it

> **Exercise:** Style a product detail section with:
> - A category label (`text-uppercase`, `small`, `text-muted`)
> - A product name (`h3`, `fw-bold`)
> - A description (`text-body-secondary`)
> - An original price with strikethrough
> - A sale price in bold primary color
