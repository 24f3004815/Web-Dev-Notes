# Part 3: Containers

---

## 3.1 What is a Container?

A **container** is Bootstrap's most basic layout element. It wraps your content and provides:

- Horizontal padding
- Centering on the page
- Responsive width adjustments

**Every Bootstrap layout should start with a container.**

---

## 3.2 Container Types

### `.container` — Fixed-Width, Responsive

Centers content with a `max-width` that changes at each breakpoint:

```html
<div class="container">
    <h1>Centered Content</h1>
    <p>This has a max-width that adjusts per breakpoint.</p>
</div>
```

| Breakpoint | Screen Width | Container max-width |
|---|---|---|
| xs | < 576px | 100% |
| sm | ≥ 576px | 540px |
| md | ≥ 768px | 720px |
| lg | ≥ 992px | 960px |
| xl | ≥ 1200px | 1140px |
| xxl | ≥ 1400px | 1320px |

### `.container-fluid` — Full Width, Always

Spans the entire viewport width at all sizes:

```html
<div class="container-fluid">
    <h1>Full Width</h1>
    <p>This stretches edge to edge.</p>
</div>
```

### `.container-{breakpoint}` — Fluid Until Breakpoint

100% wide until the specified breakpoint, then fixed:

```html
<div class="container-md">
    <!-- Full width on xs and sm, fixed from md upward -->
</div>
```

| Class | Full-width until | Fixed from |
|---|---|---|
| `container-sm` | < 576px | ≥ 576px |
| `container-md` | < 768px | ≥ 768px |
| `container-lg` | < 992px | ≥ 992px |
| `container-xl` | < 1200px | ≥ 1200px |
| `container-xxl` | < 1400px | ≥ 1400px |

---

## 3.3 ShopEase — Add Containers

Update your `index.html` `<body>`:

```html
<body>

    <!-- Full-width header area -->
    <div class="container-fluid bg-dark text-white py-2">
        <div class="container">
            <small>Free shipping on orders over ₹999!</small>
        </div>
    </div>

    <!-- Main content in a centered container -->
    <div class="container mt-4">
        <h1>Welcome to ShopEase</h1>
        <p>Your one-stop shop for quality products at amazing prices.</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
```

### What happened?

- `container-fluid` on the announcement bar makes it span the full width with a dark background
- Inside it, a `container` keeps the text aligned with the main content
- The main content uses `container` for centered, responsive width
- `bg-dark`, `text-white`, `py-2`, `mt-4` are **utility classes** (we'll cover these in detail soon)

### Try it

Resize your browser window from wide to narrow. Notice:

- The announcement bar always stretches full width
- The main content area has margins that change at different breakpoints
- On very small screens, the container becomes full width

> **Exercise:** Add a footer section using `container-fluid` with a light background (`bg-light`) and a centered `container` inside it with copyright text.
