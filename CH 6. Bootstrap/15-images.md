# Part 16: Images

---

## 16.1 Responsive Images

```html
<img src="product.jpg" class="img-fluid" alt="Product">
```

`img-fluid` sets `max-width: 100%` and `height: auto` — the image scales down on small screens but never exceeds its natural size.

---

## 16.2 Image Shapes

```html
<!-- Rounded corners -->
<img src="photo.jpg" class="rounded" alt="Rounded">

<!-- Circle (use on square images) -->
<img src="avatar.jpg" class="rounded-circle" alt="Avatar" width="150" height="150">

<!-- Pill shape (works better on wide images) -->
<img src="banner.jpg" class="rounded-pill" alt="Banner">

<!-- Thumbnail (bordered) -->
<img src="thumb.jpg" class="img-thumbnail" alt="Thumbnail">
```

---

## 16.3 Image Alignment

```html
<!-- Float left or right -->
<img src="photo.jpg" class="rounded float-start me-3" alt="Left aligned">
<img src="photo.jpg" class="rounded float-end ms-3" alt="Right aligned">

<!-- Center a block-level image -->
<img src="photo.jpg" class="rounded mx-auto d-block" alt="Centered">
```

---

## 16.4 Object Fit (Bootstrap 5.3+)

Control how images/videos fill their container:

```html
<img src="photo.jpg" class="object-fit-contain" style="width:200px;height:200px;" alt="Contain">
<img src="photo.jpg" class="object-fit-cover" style="width:200px;height:200px;" alt="Cover">
<img src="photo.jpg" class="object-fit-fill" style="width:200px;height:200px;" alt="Fill">
<img src="photo.jpg" class="object-fit-scale" style="width:200px;height:200px;" alt="Scale">
<img src="photo.jpg" class="object-fit-none" style="width:200px;height:200px;" alt="None">
```

| Class | Behavior |
|---|---|
| `object-fit-contain` | Scales to fit inside container, may have empty space |
| `object-fit-cover` | Fills container, crops overflow — **most common** |
| `object-fit-fill` | Stretches to fill (may distort) |
| `object-fit-scale` | Uses content's natural size, never exceeds container |
| `object-fit-none` | No resizing |

---

## 16.5 Figures

Semantic image + caption:

```html
<figure class="figure">
    <img src="product.jpg" class="figure-img img-fluid rounded" alt="Product">
    <figcaption class="figure-caption text-center">Wireless Headphones — ₹2,499</figcaption>
</figure>
```

---

## 16.6 ShopEase — Product Image Gallery

```html
<section class="py-5 bg-light">
    <div class="container">
        <h2 class="fw-bold mb-4">Product Gallery</h2>

        <div class="row g-3">
            <!-- Large featured image -->
            <div class="col-12 col-md-6">
                <div class="bg-white rounded-3 p-4 text-center h-100 d-flex align-items-center justify-content-center">
                    <span class="display-1">🎧</span>
                </div>
            </div>

            <!-- Thumbnail grid -->
            <div class="col-12 col-md-6">
                <div class="row g-3">
                    <div class="col-6">
                        <div class="bg-white rounded-3 p-3 text-center">
                            <span class="display-4">🎧</span>
                            <p class="small text-muted mt-2 mb-0">Front View</p>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="bg-white rounded-3 p-3 text-center">
                            <span class="display-4">🎧</span>
                            <p class="small text-muted mt-2 mb-0">Side View</p>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="bg-white rounded-3 p-3 text-center">
                            <span class="display-4">📦</span>
                            <p class="small text-muted mt-2 mb-0">Box Contents</p>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="bg-white rounded-3 p-3 text-center">
                            <span class="display-4">🔌</span>
                            <p class="small text-muted mt-2 mb-0">Charging</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
```

### What happened?

- Large image on the left, 4 thumbnails on the right (on desktop)
- On mobile everything stacks: large image on top, thumbnails below
- `h-100` on the large image container makes it match the thumbnail grid height
- Nested `row` inside the right column creates the 2×2 thumbnail grid

### Try it

> **Exercise:** Create a team page with circular avatar images:
> - Use `rounded-circle` with equal `width` and `height`
> - Center each image with `mx-auto d-block`
> - Add names below each avatar with `text-center`
> - Use the grid to show 2 on mobile, 4 on desktop
