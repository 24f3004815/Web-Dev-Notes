# Part 2: Bootstrap Installation & Setup

---

## 2.1 Method 1: CDN (Recommended for Learning)

A **CDN** (Content Delivery Network) lets you use Bootstrap by linking to it directly — no downloads needed.

Add these two lines to your HTML:

**In `<head>` — Bootstrap CSS:**

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
```

**Before `</body>` — Bootstrap JavaScript Bundle:**

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
```

> The **bundle** includes Popper.js (required for dropdowns, tooltips, popovers). Always use the bundle.

---

## 2.2 Method 2: Download Bootstrap

Download from [getbootstrap.com](https://getbootstrap.com/). You'll get:

```text
bootstrap/
├── css/
│   ├── bootstrap.min.css       ← Use this
│   └── bootstrap.css           ← Unminified (for reading)
└── js/
    ├── bootstrap.bundle.min.js ← Use this
    └── bootstrap.bundle.js     ← Unminified
```

Link the local files:

```html
<link rel="stylesheet" href="css/bootstrap.min.css">
<script src="js/bootstrap.bundle.min.js"></script>
```

---

## 2.3 Method 3: npm (For Build Tools)

If you're using a build tool (Vite, Webpack, etc.):

```bash
npm install bootstrap@5.3.8
```

Then import in your JavaScript:

```javascript
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
```

> For this tutorial, we'll use the **CDN method** — simplest for learning.

---

## 2.4 CSS vs JavaScript — What Needs What?

Bootstrap has two parts:

| Part | What it does | Examples |
|---|---|---|
| **CSS** (`bootstrap.min.css`) | All visual styling — grid, buttons, cards, colors, spacing | Grid, typography, buttons, cards, badges, tables |
| **JS** (`bootstrap.bundle.min.js`) | Interactive behavior — toggling, animations, dynamic UI | Modals, dropdowns, carousels, tooltips, collapse, offcanvas |

**Rule of thumb:** If a component opens, closes, slides, or toggles — it needs JavaScript.

---

## 2.5 Start the ShopEase Project

Create a folder called `shopease` with this file:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShopEase — Your One-Stop Shop</title>
    <meta name="description" content="ShopEase - Quality products at amazing prices">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">

    <!-- Custom CSS (loaded AFTER Bootstrap so our styles can override) -->
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Welcome to ShopEase</h1>
    <p>We'll build this into a full responsive website using Bootstrap.</p>

    <!-- Bootstrap JS Bundle (includes Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**`style.css`** (empty for now — we'll add custom styles later):

```css
/* ShopEase — Custom Styles
   Loaded after Bootstrap to allow overrides */
```

### What happened?

- `bootstrap.min.css` loads all Bootstrap styles
- `bootstrap-icons` loads the icon font library
- `style.css` is linked **after** Bootstrap so your custom CSS can override Bootstrap's defaults
- `bootstrap.bundle.min.js` loads at the bottom for interactive components
- The `viewport` meta tag is **critical** — without it, Bootstrap's responsive design won't work on mobile

### Try it

1. Create the `shopease` folder with `index.html` and `style.css`
2. Open `index.html` in your browser
3. Notice the font has changed — Bootstrap's CSS is active
4. Open DevTools (`F12`) → Console — no errors means Bootstrap loaded successfully
5. Try removing the `viewport` meta tag, resize the browser, then add it back — see the difference
