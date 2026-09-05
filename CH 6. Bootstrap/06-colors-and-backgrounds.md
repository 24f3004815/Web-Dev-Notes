# Part 7: Colors & Backgrounds

---

## 7.1 Bootstrap's Color System

Bootstrap uses **contextual color names** — each color communicates meaning:

| Color Name | Meaning | Typical Use |
|---|---|---|
| `primary` | Main brand color (blue) | Primary actions, links |
| `secondary` | Neutral (gray) | Secondary actions |
| `success` | Positive (green) | Confirmations, completed |
| `danger` | Negative (red) | Errors, destructive actions |
| `warning` | Caution (yellow) | Warnings, attention |
| `info` | Information (cyan) | Tips, extra info |
| `light` | Light background | Light sections |
| `dark` | Dark background | Dark sections, text |

---

## 7.2 Text Colors

```html
<p class="text-primary">Primary text (blue)</p>
<p class="text-secondary">Secondary text (gray)</p>
<p class="text-success">Success text (green)</p>
<p class="text-danger">Danger text (red)</p>
<p class="text-warning">Warning text (yellow)</p>
<p class="text-info">Info text (cyan)</p>
<p class="text-dark">Dark text</p>
<p class="text-light bg-dark">Light text (on dark bg)</p>
<p class="text-white bg-dark">White text (on dark bg)</p>
<p class="text-muted">Muted/gray text</p>
<p class="text-body">Default body text color</p>
<p class="text-body-secondary">Secondary body text</p>
```

---

## 7.3 Background Colors

```html
<div class="bg-primary text-white p-3">Primary background</div>
<div class="bg-secondary text-white p-3">Secondary background</div>
<div class="bg-success text-white p-3">Success background</div>
<div class="bg-danger text-white p-3">Danger background</div>
<div class="bg-warning text-dark p-3">Warning background</div>
<div class="bg-info text-dark p-3">Info background</div>
<div class="bg-light text-dark p-3">Light background</div>
<div class="bg-dark text-white p-3">Dark background</div>
<div class="bg-body-secondary p-3">Body secondary bg</div>
```

> **Important:** Always ensure text has enough contrast against the background. `bg-warning` and `bg-info` need `text-dark`, not `text-white`.

---

## 7.4 Subtle Backgrounds (Bootstrap 5.3+)

Softer, lighter versions of contextual backgrounds:

```html
<div class="bg-primary-subtle text-primary-emphasis p-3">Subtle primary</div>
<div class="bg-success-subtle text-success-emphasis p-3">Subtle success</div>
<div class="bg-danger-subtle text-danger-emphasis p-3">Subtle danger</div>
<div class="bg-warning-subtle text-warning-emphasis p-3">Subtle warning</div>
```

> These are great for alerts, badges, and notification areas — softer than full-color backgrounds.

---

## 7.5 Background Opacity

```html
<div class="bg-primary bg-opacity-75 text-white p-3">75% opacity</div>
<div class="bg-primary bg-opacity-50 text-white p-3">50% opacity</div>
<div class="bg-primary bg-opacity-25 p-3">25% opacity</div>
<div class="bg-primary bg-opacity-10 p-3">10% opacity</div>
```

Opacity values: `10`, `25`, `50`, `75` (plus default 100%).

---

## 7.6 Background Gradient

```html
<div class="bg-primary bg-gradient text-white p-3">Primary with gradient</div>
<div class="bg-danger bg-gradient text-white p-3">Danger with gradient</div>
```

> Adds a subtle `linear-gradient` overlay to any background color.

---

## 7.7 ShopEase — Color Showcase

Add a promotional banner section to ShopEase:

```html
<!-- Promo Banners -->
<div class="row g-3 my-5">
    <div class="col-12 col-md-4">
        <div class="bg-primary-subtle text-primary-emphasis rounded-3 p-4 text-center">
            <h5 class="fw-bold">🚚 Free Shipping</h5>
            <p class="mb-0 small">On orders above ₹999</p>
        </div>
    </div>
    <div class="col-12 col-md-4">
        <div class="bg-success-subtle text-success-emphasis rounded-3 p-4 text-center">
            <h5 class="fw-bold">🔄 Easy Returns</h5>
            <p class="mb-0 small">30-day return policy</p>
        </div>
    </div>
    <div class="col-12 col-md-4">
        <div class="bg-warning-subtle text-warning-emphasis rounded-3 p-4 text-center">
            <h5 class="fw-bold">🔒 Secure Payment</h5>
            <p class="mb-0 small">100% secure checkout</p>
        </div>
    </div>
</div>
```

### What happened?

- `bg-primary-subtle` + `text-primary-emphasis` creates a soft blue banner with readable dark-blue text
- Each banner uses a different contextual color to communicate its purpose visually
- `rounded-3` and `p-4` give comfortable styling

### Try it

> **Exercise:** Create a sale announcement banner using:
> - `bg-danger` with `text-white` for an urgent "Flash Sale!" banner
> - Below it, add a softer `bg-danger-subtle` section with sale details
> - Compare how full-color vs subtle backgrounds feel
