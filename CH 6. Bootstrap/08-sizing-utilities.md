# Part 9: Sizing Utilities

---

## 9.1 Width Utilities

Set an element's width as a percentage of its parent:

```html
<div class="w-25 bg-primary-subtle p-2">25% wide</div>
<div class="w-50 bg-primary-subtle p-2">50% wide</div>
<div class="w-75 bg-primary-subtle p-2">75% wide</div>
<div class="w-100 bg-primary-subtle p-2">100% wide</div>
<div class="w-auto bg-primary-subtle p-2">Auto width</div>
```

---

## 9.2 Height Utilities

Set height as a percentage of the parent (parent must have a defined height):

```html
<div style="height: 200px;" class="bg-light">
    <div class="h-25 bg-info-subtle p-2">25% height</div>
    <div class="h-50 bg-info-subtle p-2">50% height</div>
</div>
```

Available: `h-25`, `h-50`, `h-75`, `h-100`, `h-auto`

---

## 9.3 Max-Width & Max-Height

```html
<div class="mw-100">Max-width: 100%</div>
<div class="mh-100">Max-height: 100%</div>
```

> `mw-100` is commonly used on images to prevent them from overflowing their container.

---

## 9.4 Viewport Sizing

Size relative to the **viewport** (browser window), not the parent:

```html
<div class="vw-100">100% of viewport width</div>
<div class="vh-100">100% of viewport height</div>
<div class="min-vw-100">Min 100% viewport width</div>
<div class="min-vh-100">Min 100% viewport height</div>
```

> `min-vh-100` is useful for making a section take up at least the full screen height.

---

## 9.5 Practical Example

```html
<!-- Full-height hero section -->
<section class="min-vh-100 d-flex align-items-center bg-dark text-white">
    <div class="container">
        <div class="w-75 mx-auto text-center">
            <h1 class="display-3 fw-bold">Welcome</h1>
            <p class="lead">This section fills the entire viewport height.</p>
        </div>
    </div>
</section>
```

### What happened?

- `min-vh-100` makes the section at least as tall as the viewport
- `d-flex align-items-center` vertically centers the content
- `w-75 mx-auto` constrains the text to 75% width and centers it

### Try it

> **Exercise:** Create a two-section page:
> 1. First section: `min-vh-100`, dark background, centered welcome text
> 2. Second section: `min-vh-50`, light background, product showcase
> - Use `w-50 mx-auto` to center a call-to-action box
