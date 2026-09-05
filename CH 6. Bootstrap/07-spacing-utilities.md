# Part 8: Spacing Utilities

---

## 8.1 The Spacing System

Bootstrap uses a shorthand system for margin and padding:

```text
{property}{side}-{size}
```

### Property

| Letter | Property |
|---|---|
| `m` | Margin |
| `p` | Padding |

### Side

| Letter | Side |
|---|---|
| `t` | Top |
| `b` | Bottom |
| `s` | Start (left in LTR) |
| `e` | End (right in LTR) |
| `x` | Horizontal (left + right) |
| `y` | Vertical (top + bottom) |
| _(none)_ | All four sides |

### Size Scale

| Value | Size |
|---|---|
| `0` | 0 |
| `1` | 0.25rem (4px) |
| `2` | 0.5rem (8px) |
| `3` | 1rem (16px) |
| `4` | 1.5rem (24px) |
| `5` | 3rem (48px) |
| `auto` | Auto (margin only) |

---

## 8.2 Examples

```html
<!-- Margin -->
<div class="mt-3">Margin-top: 1rem</div>
<div class="mb-4">Margin-bottom: 1.5rem</div>
<div class="ms-2">Margin-start (left): 0.5rem</div>
<div class="me-5">Margin-end (right): 3rem</div>
<div class="mx-auto" style="width: 200px;">Horizontally centered</div>
<div class="my-3">Vertical margin: 1rem top & bottom</div>
<div class="m-0">Zero margin on all sides</div>

<!-- Padding -->
<div class="p-3">Padding: 1rem on all sides</div>
<div class="pt-2">Padding-top: 0.5rem</div>
<div class="px-4">Horizontal padding: 1.5rem</div>
<div class="py-5">Vertical padding: 3rem</div>
```

### Centering with `mx-auto`

```html
<!-- Center a fixed-width block -->
<div class="mx-auto" style="width: 300px;">
    This block is centered horizontally
</div>
```

`mx-auto` sets `margin-left: auto` and `margin-right: auto` — the classic CSS centering technique.

---

## 8.3 Responsive Spacing

Add breakpoints to any spacing utility:

```html
<!-- No padding on mobile, padding-4 on desktop -->
<div class="p-0 p-lg-4">Responsive padding</div>

<!-- Margin-2 on mobile, margin-5 on tablet+ -->
<div class="mt-2 mt-md-5">Responsive margin</div>
```

Pattern: `{property}{side}-{breakpoint}-{size}`

```text
mt-3       → margin-top 1rem on all screens
mt-md-5    → margin-top 3rem from md (768px) up
p-2 p-lg-4 → padding 0.5rem on mobile, 1.5rem on desktop
```

---

## 8.4 Gap Utility (for Flexbox & Grid)

When using `d-flex` or `d-grid`, use `gap-` instead of margins between items:

```html
<div class="d-flex gap-3">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>

<!-- Row and column gaps -->
<div class="d-flex flex-wrap row-gap-2 column-gap-3">
    <div>A</div>
    <div>B</div>
    <div>C</div>
</div>
```

Gap values follow the same `0`–`5` scale.

---

## 8.5 ShopEase — Spacing in Practice

The spacing is already woven throughout our ShopEase project. Here's a focused look at the patterns:

```html
<!-- Section with vertical spacing -->
<section class="py-5">
    <div class="container">
        <!-- Section header with bottom margin -->
        <h2 class="fw-bold mb-1">Why Shop With Us?</h2>
        <p class="text-muted mb-4">Three reasons to choose ShopEase</p>

        <div class="row g-4">
            <div class="col-12 col-md-4">
                <!-- Card with internal padding -->
                <div class="bg-light rounded-3 p-4">
                    <h5 class="mb-2">🚚 Fast Delivery</h5>
                    <p class="mb-0">Get your products within 2-3 business days.</p>
                </div>
            </div>
            <div class="col-12 col-md-4">
                <div class="bg-light rounded-3 p-4">
                    <h5 class="mb-2">💰 Best Prices</h5>
                    <p class="mb-0">We match any competitor's price, guaranteed.</p>
                </div>
            </div>
            <div class="col-12 col-md-4">
                <div class="bg-light rounded-3 p-4">
                    <h5 class="mb-2">⭐ 5-Star Support</h5>
                    <p class="mb-0">24/7 customer support via chat and email.</p>
                </div>
            </div>
        </div>
    </div>
</section>
```

### What happened?

- `py-5` gives the section generous vertical padding (48px top and bottom)
- `mb-1` keeps the heading close to its subtitle; `mb-4` creates separation before the grid
- `g-4` on the row controls spacing between columns
- `p-4` inside each card creates internal breathing room
- `mb-2` on headings, `mb-0` on last paragraphs keeps spacing tight and intentional

### Try it

> **Exercise:** Take the product cards from Part 4 and adjust spacing:
> 1. Add `py-5` to the product section wrapper
> 2. Use `mb-2` between the product name and description
> 3. Use `mb-0` on the price (last element — no extra bottom margin)
> 4. Compare how the layout looks with `g-3` vs `g-4` vs `g-5` on the row
