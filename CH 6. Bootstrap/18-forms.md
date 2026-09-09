# Part 19: Forms

---

## 19.1 Basic Form Structure

```html
<form>
    <div class="mb-3">
        <label for="emailInput" class="form-label">Email address</label>
        <input type="email" class="form-control" id="emailInput" placeholder="name@example.com">
    </div>
    <div class="mb-3">
        <label for="passwordInput" class="form-label">Password</label>
        <input type="password" class="form-control" id="passwordInput">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

Key classes:

- `form-label` — styles the `<label>` element
- `form-control` — styles text inputs, textareas, selects
- `mb-3` — adds spacing between form groups

---

## 19.2 Input Types

```html
<!-- Text -->
<input type="text" class="form-control" placeholder="Full name">

<!-- Email -->
<input type="email" class="form-control" placeholder="Email">

<!-- Password -->
<input type="password" class="form-control" placeholder="Password">

<!-- Number -->
<input type="number" class="form-control" placeholder="Quantity">

<!-- Phone -->
<input type="tel" class="form-control" placeholder="Phone number">

<!-- URL -->
<input type="url" class="form-control" placeholder="https://example.com">

<!-- Date -->
<input type="date" class="form-control">

<!-- Color -->
<input type="color" class="form-control form-control-color" value="#0d6efd" title="Choose color">
```

---

## 19.3 Textarea

```html
<div class="mb-3">
    <label for="messageArea" class="form-label">Message</label>
    <textarea class="form-control" id="messageArea" rows="4" placeholder="Write your message..."></textarea>
</div>
```

---

## 19.4 Select

```html
<div class="mb-3">
    <label for="categorySelect" class="form-label">Category</label>
    <select class="form-select" id="categorySelect">
        <option selected disabled>Choose a category...</option>
        <option value="electronics">Electronics</option>
        <option value="accessories">Accessories</option>
        <option value="audio">Audio</option>
    </select>
</div>

<!-- Multiple select -->
<select class="form-select" multiple size="3">
    <option>Option 1</option>
    <option>Option 2</option>
    <option>Option 3</option>
</select>
```

---

## 19.5 Checkboxes & Radio Buttons

```html
<!-- Checkbox -->
<div class="form-check">
    <input class="form-check-input" type="checkbox" id="agreeCheck">
    <label class="form-check-label" for="agreeCheck">
        I agree to the Terms & Conditions
    </label>
</div>

<!-- Inline checkboxes -->
<div class="form-check form-check-inline">
    <input class="form-check-input" type="checkbox" id="electronics" value="electronics">
    <label class="form-check-label" for="electronics">Electronics</label>
</div>
<div class="form-check form-check-inline">
    <input class="form-check-input" type="checkbox" id="audio" value="audio">
    <label class="form-check-label" for="audio">Audio</label>
</div>

<!-- Radio buttons -->
<div class="form-check">
    <input class="form-check-input" type="radio" name="shipping" id="standard" value="standard" checked>
    <label class="form-check-label" for="standard">Standard Shipping (Free)</label>
</div>
<div class="form-check">
    <input class="form-check-input" type="radio" name="shipping" id="express" value="express">
    <label class="form-check-label" for="express">Express Shipping (₹99)</label>
</div>

<!-- Switch -->
<div class="form-check form-switch">
    <input class="form-check-input" type="checkbox" id="notifications" checked>
    <label class="form-check-label" for="notifications">Enable notifications</label>
</div>
```

---

## 19.6 Range

```html
<div class="mb-3">
    <label for="priceRange" class="form-label">Max Price: ₹5,000</label>
    <input type="range" class="form-range" id="priceRange" min="0" max="10000" step="500">
</div>
```

---

## 19.7 File Input

```html
<div class="mb-3">
    <label for="avatarUpload" class="form-label">Profile Picture</label>
    <input class="form-control" type="file" id="avatarUpload" accept="image/*">
</div>
```

---

## 19.8 Input Groups

Combine inputs with text, icons, or buttons:

```html
<!-- Prepend text -->
<div class="input-group mb-3">
    <span class="input-group-text">@</span>
    <input type="text" class="form-control" placeholder="Username">
</div>

<!-- Append text -->
<div class="input-group mb-3">
    <input type="number" class="form-control" placeholder="Amount">
    <span class="input-group-text">.00</span>
</div>

<!-- Prepend icon -->
<div class="input-group mb-3">
    <span class="input-group-text"><i class="bi bi-search"></i></span>
    <input type="text" class="form-control" placeholder="Search products...">
</div>

<!-- With button -->
<div class="input-group mb-3">
    <input type="email" class="form-control" placeholder="Email for newsletter">
    <button class="btn btn-primary" type="button">Subscribe</button>
</div>
```

---

## 19.9 Floating Labels

Labels that float above the input when focused/filled:

```html
<div class="form-floating mb-3">
    <input type="email" class="form-control" id="floatingEmail" placeholder="Email">
    <label for="floatingEmail">Email address</label>
</div>

<div class="form-floating mb-3">
    <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
    <label for="floatingPassword">Password</label>
</div>

<div class="form-floating mb-3">
    <textarea class="form-control" id="floatingMessage" placeholder="Message" style="height: 100px;"></textarea>
    <label for="floatingMessage">Your message</label>
</div>
```

> **Important:** The `<input>` must come **before** the `<label>` for floating labels to work. The `placeholder` is also required (Bootstrap uses it to detect empty state).

---

## 19.10 Form Sizing

```html
<input class="form-control form-control-lg" type="text" placeholder="Large input">
<input class="form-control" type="text" placeholder="Default input">
<input class="form-control form-control-sm" type="text" placeholder="Small input">

<select class="form-select form-select-lg">
    <option>Large select</option>
</select>
```

---

## 19.11 Disabled & Readonly

```html
<!-- Disabled -->
<input class="form-control" type="text" value="Can't edit this" disabled>

<!-- Readonly (can't edit, but can select/copy text) -->
<input class="form-control" type="text" value="Can copy but not edit" readonly>

<!-- Readonly plain text (looks like regular text, not an input) -->
<input class="form-control-plaintext" type="text" value="email@example.com" readonly>
```

---

## 19.12 Form Layout with Grid

```html
<form>
    <div class="row mb-3">
        <div class="col-md-6">
            <label for="firstName" class="form-label">First Name</label>
            <input type="text" class="form-control" id="firstName">
        </div>
        <div class="col-md-6">
            <label for="lastName" class="form-label">Last Name</label>
            <input type="text" class="form-control" id="lastName">
        </div>
    </div>
    <div class="mb-3">
        <label for="fullEmail" class="form-label">Email</label>
        <input type="email" class="form-control" id="fullEmail">
    </div>
</form>
```

---

## 19.13 ShopEase — Registration Form

```html
<section class="py-5 bg-light">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-8 col-lg-6">
                <div class="card shadow-sm border-0">
                    <div class="card-body p-4 p-md-5">
                        <h3 class="fw-bold text-center mb-1">Create Account</h3>
                        <p class="text-muted text-center mb-4">Join ShopEase for exclusive deals</p>

                        <form>
                            <!-- Name fields side by side -->
                            <div class="row mb-3">
                                <div class="col-6">
                                    <div class="form-floating">
                                        <input type="text" class="form-control" id="regFirst" placeholder="First">
                                        <label for="regFirst">First Name</label>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="form-floating">
                                        <input type="text" class="form-control" id="regLast" placeholder="Last">
                                        <label for="regLast">Last Name</label>
                                    </div>
                                </div>
                            </div>

                            <!-- Email -->
                            <div class="form-floating mb-3">
                                <input type="email" class="form-control" id="regEmail" placeholder="Email">
                                <label for="regEmail">Email address</label>
                            </div>

                            <!-- Phone -->
                            <div class="input-group mb-3">
                                <span class="input-group-text">+91</span>
                                <div class="form-floating flex-grow-1">
                                    <input type="tel" class="form-control" id="regPhone" placeholder="Phone">
                                    <label for="regPhone">Phone Number</label>
                                </div>
                            </div>

                            <!-- Password -->
                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" id="regPassword" placeholder="Password">
                                <label for="regPassword">Password</label>
                            </div>

                            <!-- Confirm Password -->
                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" id="regConfirm" placeholder="Confirm">
                                <label for="regConfirm">Confirm Password</label>
                            </div>

                            <!-- Shipping preference -->
                            <div class="mb-3">
                                <label class="form-label fw-semibold">Preferred Shipping</label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="shipping" id="shipStandard" checked>
                                    <label class="form-check-label" for="shipStandard">Standard (Free)</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="shipping" id="shipExpress">
                                    <label class="form-check-label" for="shipExpress">Express (₹99)</label>
                                </div>
                            </div>

                            <!-- Newsletter switch -->
                            <div class="form-check form-switch mb-3">
                                <input class="form-check-input" type="checkbox" id="newsletter" checked>
                                <label class="form-check-label" for="newsletter">Subscribe to newsletter</label>
                            </div>

                            <!-- Terms -->
                            <div class="form-check mb-4">
                                <input class="form-check-input" type="checkbox" id="terms">
                                <label class="form-check-label" for="terms">
                                    I agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>
                                </label>
                            </div>

                            <!-- Submit -->
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg">Create Account</button>
                            </div>

                            <p class="text-center text-muted mt-3 mb-0">
                                Already have an account? <a href="#" class="text-decoration-none">Sign In</a>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
```

### What happened?

- `justify-content-center` + `col-lg-6` centers the form card on the page
- Floating labels create a modern, clean form appearance
- `input-group` with country code prefix for the phone field
- Radio buttons for shipping, switch for newsletter
- `d-grid` makes the submit button full-width
- Grid layout puts first/last name side by side

### Try it

> **Exercise:** Create a "Checkout" form with:
> - Shipping address fields (street, city, state, zip) using grid layout
> - A select dropdown for state
> - Payment method radio buttons (UPI, Card, COD)
> - A file input for "Upload payment proof" (for COD)
