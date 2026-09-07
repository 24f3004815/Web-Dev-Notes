# Part 14: Alerts

---

## 14.1 Basic Alerts

```html
<div class="alert alert-primary" role="alert">This is a primary alert.</div>
<div class="alert alert-secondary" role="alert">This is a secondary alert.</div>
<div class="alert alert-success" role="alert">Order placed successfully!</div>
<div class="alert alert-danger" role="alert">Error: Payment failed.</div>
<div class="alert alert-warning" role="alert">Warning: Stock is low.</div>
<div class="alert alert-info" role="alert">Info: New products added.</div>
<div class="alert alert-light" role="alert">Light alert.</div>
<div class="alert alert-dark" role="alert">Dark alert.</div>
```

> Always include `role="alert"` for screen readers.

---

## 14.2 Alerts with Links

```html
<div class="alert alert-warning" role="alert">
    Your cart will expire soon.
    <a href="#" class="alert-link">View cart</a> to complete checkout.
</div>
```

`alert-link` automatically styles the link to match the alert color.

---

## 14.3 Alerts with Additional Content

```html
<div class="alert alert-success" role="alert">
    <h4 class="alert-heading">Order Confirmed! 🎉</h4>
    <p>Your order #12345 has been placed successfully. You will receive a confirmation email shortly.</p>
    <hr>
    <p class="mb-0">Expected delivery: 3-5 business days.</p>
</div>
```

---

## 14.4 Dismissible Alerts

Alerts that the user can close (requires Bootstrap JavaScript):

```html
<div class="alert alert-warning alert-dismissible fade show" role="alert">
    <strong>Heads up!</strong> This product will be discontinued soon.
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
```

Key classes:

- `alert-dismissible` — adds padding for the close button
- `fade show` — smooth fade-out animation when dismissed
- `btn-close` — Bootstrap's built-in close button
- `data-bs-dismiss="alert"` — triggers the dismiss behavior (needs JS bundle)

---

## 14.5 Alerts with Icons

```html
<div class="alert alert-success d-flex align-items-center" role="alert">
    <i class="bi bi-check-circle-fill me-2 fs-5"></i>
    <div>Product added to your cart!</div>
</div>

<div class="alert alert-danger d-flex align-items-center" role="alert">
    <i class="bi bi-exclamation-triangle-fill me-2 fs-5"></i>
    <div>Payment declined. Please try another card.</div>
</div>
```

---

## 14.6 ShopEase — Notification Alerts

Add these alerts at the top of the main content area:

```html
<div class="container mt-4">
    <!-- Flash sale alert -->
    <div class="alert alert-danger alert-dismissible fade show d-flex align-items-center" role="alert">
        <i class="bi bi-lightning-fill me-2 fs-5"></i>
        <div>
            <strong>Flash Sale!</strong> Up to 50% off on electronics.
            <a href="#products" class="alert-link">Shop now →</a>
        </div>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    <!-- Info alert -->
    <div class="alert alert-info alert-dismissible fade show" role="alert">
        <i class="bi bi-info-circle me-2"></i>
        Free shipping on all orders above ₹999 — limited time only!
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>

    <!-- Rest of page content... -->
</div>
```

### What happened?

- Two dismissible alerts show promotional info at the top of the page
- `fade show` provides smooth closing animation
- `d-flex align-items-center` keeps the icon and text vertically aligned
- Users can close alerts they've read — the JavaScript bundle handles this

### Try it

> **Exercise:** Create a success alert that appears when a product is "added to cart":
> - Use `alert-success` with a checkmark icon
> - Make it dismissible
> - Include a link to "View Cart" using `alert-link`
