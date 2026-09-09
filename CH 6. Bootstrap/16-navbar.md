# Part 17: Navigation & Navbar

---

## 17.1 Basic Navbar Structure

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
        <!-- Brand -->
        <a class="navbar-brand" href="#">SiteName</a>

        <!-- Mobile toggle button -->
        <button class="navbar-toggler" type="button"
                data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false"
                aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Collapsible nav links -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### Key Parts

| Element | Purpose |
|---|---|
| `navbar` | Base navbar class |
| `navbar-expand-lg` | Collapsed (hamburger) below lg, expanded above lg |
| `navbar-brand` | Logo/site name |
| `navbar-toggler` | Hamburger button (mobile) |
| `collapse navbar-collapse` | Content that shows/hides on mobile |
| `navbar-nav` | Container for nav links |
| `nav-link active` | Current page link |

---

## 17.2 Navbar Color Schemes

```html
<!-- Light navbar -->
<nav class="navbar navbar-expand-lg bg-body-tertiary">

<!-- Dark navbar -->
<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">

<!-- Primary colored navbar -->
<nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">

<!-- Custom background -->
<nav class="navbar navbar-expand-lg" style="background-color: #1a1a2e;">
```

> Use `data-bs-theme="dark"` on dark backgrounds so text and toggler icons turn white.

---

## 17.3 Nav Items — Dropdowns

```html
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button"
       data-bs-toggle="dropdown" aria-expanded="false">
        Products
    </a>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Electronics</a></li>
        <li><a class="dropdown-item" href="#">Accessories</a></li>
        <li><a class="dropdown-item" href="#">Audio</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">All Products</a></li>
    </ul>
</li>
```

---

## 17.4 Navbar with Search & Buttons

```html
<div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav me-auto">
        <!-- Nav links here -->
    </ul>

    <!-- Search form -->
    <form class="d-flex gap-2" role="search">
        <input class="form-control" type="search" placeholder="Search products..." aria-label="Search">
        <button class="btn btn-outline-light" type="submit">
            <i class="bi bi-search"></i>
        </button>
    </form>

    <!-- Right-side items -->
    <div class="d-flex align-items-center ms-3 gap-3">
        <a href="#" class="text-white text-decoration-none">
            <i class="bi bi-heart"></i>
        </a>
        <a href="#" class="text-white text-decoration-none position-relative">
            <i class="bi bi-cart3 fs-5"></i>
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                3
            </span>
        </a>
        <a href="#" class="btn btn-outline-light btn-sm">Login</a>
    </div>
</div>
```

> `me-auto` pushes everything after the nav links to the right.

---

## 17.5 Fixed & Sticky Navbar

```html
<!-- Stays at top when scrolling -->
<nav class="navbar navbar-expand-lg bg-dark sticky-top" data-bs-theme="dark">

<!-- Always fixed at top (overlaps content — add padding to body) -->
<nav class="navbar navbar-expand-lg bg-dark fixed-top" data-bs-theme="dark">

<!-- Fixed at bottom -->
<nav class="navbar navbar-expand-lg bg-dark fixed-bottom" data-bs-theme="dark">
```

> If using `fixed-top`, add `padding-top` to `<body>` so content isn't hidden behind the navbar.

---

## 17.6 ShopEase — Complete Responsive Navbar

Replace the announcement bar and add this navbar to ShopEase:

```html
<!-- Announcement Bar -->
<div class="bg-dark text-white py-2 text-center small d-none d-md-block">
    🔥 Flash Sale! Up to 50% off on electronics — <a href="#" class="text-warning text-decoration-none fw-semibold">Shop now</a>
</div>

<!-- Main Navbar -->
<nav class="navbar navbar-expand-lg bg-white shadow-sm sticky-top">
    <div class="container">
        <!-- Brand -->
        <a class="navbar-brand fw-bold fs-4" href="#">
            <i class="bi bi-bag-heart text-primary me-1"></i>ShopEase
        </a>

        <!-- Mobile: cart + toggler -->
        <div class="d-flex align-items-center gap-3 d-lg-none">
            <a href="#" class="text-dark position-relative">
                <i class="bi bi-cart3 fs-5"></i>
                <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">3</span>
            </a>
            <button class="navbar-toggler border-0" type="button"
                    data-bs-toggle="collapse" data-bs-target="#shopNavbar"
                    aria-controls="shopNavbar" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>

        <!-- Collapsible content -->
        <div class="collapse navbar-collapse" id="shopNavbar">
            <!-- Main nav links -->
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active fw-semibold" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button"
                       data-bs-toggle="dropdown" aria-expanded="false">Products</a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Electronics</a></li>
                        <li><a class="dropdown-item" href="#">Accessories</a></li>
                        <li><a class="dropdown-item" href="#">Audio</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">All Products</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Deals</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>
            </ul>

            <!-- Search (visible on lg+) -->
            <form class="d-flex gap-2 me-3 d-none d-lg-flex" role="search">
                <input class="form-control" type="search" placeholder="Search products..." aria-label="Search">
                <button class="btn btn-outline-primary" type="submit">
                    <i class="bi bi-search"></i>
                </button>
            </form>

            <!-- Desktop right items -->
            <div class="d-none d-lg-flex align-items-center gap-3">
                <a href="#" class="text-dark text-decoration-none" aria-label="Wishlist">
                    <i class="bi bi-heart fs-5"></i>
                </a>
                <a href="#" class="text-dark text-decoration-none position-relative" aria-label="Cart">
                    <i class="bi bi-cart3 fs-5"></i>
                    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">3</span>
                </a>
                <a href="#" class="btn btn-primary btn-sm">
                    <i class="bi bi-person me-1"></i> Login
                </a>
            </div>

            <!-- Mobile search (shown inside hamburger) -->
            <form class="d-lg-none mt-3" role="search">
                <input class="form-control" type="search" placeholder="Search products..." aria-label="Search">
            </form>
        </div>
    </div>
</nav>
```

### What happened?

- `sticky-top` keeps the navbar fixed when scrolling
- `navbar-expand-lg` collapses to hamburger below `lg`
- Desktop shows: Brand, nav links, search, wishlist, cart, login
- Mobile shows: Brand, cart icon + hamburger; nav links + search inside collapse
- Dropdown on "Products" reveals categories
- Cart has a badge showing item count (positioned with `position-absolute translate-middle`)
- Announcement bar is hidden on mobile (`d-none d-md-block`)

### Try it

1. Resize the browser — watch the navbar transform
2. Click the hamburger on mobile to see the collapse
3. Click the Products dropdown

> **Exercise:** Change the navbar to use a dark theme:
> - Replace `bg-white` with `bg-dark`
> - Add `data-bs-theme="dark"`
> - Change text color classes from `text-dark` to `text-white`
