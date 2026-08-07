# CSS 3D Transforms

Estimated Reading Time: 12 minutes

Prerequisites: [CSS 2D Transforms](42-css-2d-transforms.md)

Learning Objectives:
- Master the `transform` property for 3D depth manipulations (`rotateX`, `rotateY`, `translateZ`).
- Understand perspective context using `perspective` and `perspective-origin`.
- Control backface visibility using `backface-visibility`.
- Build 3D card flip animation components.

---

## Introduction

**CSS 3D Transforms** extend spatial manipulations into 3-dimensional space by adding a Z-axis for depth (towards or away from the user's screen).

Using 3D transform functions—`rotateX()`, `rotateY()`, `translateZ()`, and `perspective`—developers can build interactive 3D card flip effects, rotating 3D cubes, page-turn book animations, and immersive parallax depth effects directly in web browsers.

---

## Real-World Analogy

Imagine holding a playing card in your hands.

- **`perspective: 1000px`**: Standing 1 meter away from a 3D stage window to view physical depth perspective.
- **`rotateY(180deg)`**: Flipping the playing card around its vertical axis from front to back.
- **`rotateX(45deg)`**: Tilting the card backward like a solar panel facing up toward the sun.
- **`backface-visibility: hidden`**: Printing the card front so that when flipped around 180 degrees, the back face becomes invisible.

3D transforms manipulate depth geometry.

---

## Core Concepts

### 1. The Z-Axis & Perspective
- **Z-Axis**: Spatial axis pointing directly out of the screen toward the viewer (`translateZ(100px)` moves object closer).
- **`perspective`**: Mandatory parent container property defining 3D depth perception distance (`perspective: 1000px`).

### 2. 3D Functions
- `rotateX(angle)`: Rotates element around horizontal X-axis (tilting forward/backward).
- `rotateY(angle)`: Rotates element around vertical Y-axis (flipping left/right).
- `translateZ(px)`: Moves element along depth Z-axis.

### 3. Key 3D Properties
- `transform-style: preserve-3d`: Instructs child elements to maintain 3D spatial positioning.
- `backface-visibility: hidden`: Hides the back side of elements when rotated facing away from viewer.

---

## Syntax

```css
/* 1. Parent 3D Perspective Container */
.card-scene {
    perspective: 1000px; /* Activates 3D depth viewport */
}

/* 2. 3D Card Object */
.card-object {
    width: 300px;
    height: 200px;
    transform-style: preserve-3d;
    transition: transform 0.8s ease;
}

/* 3. Flip Card on Hover */
.card-scene:hover .card-object {
    transform: rotateY(180deg);
}

/* 4. Hide Backface */
.card-front, .card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
}

.card-back {
    transform: rotateY(180deg);
}
```

---

## Property Reference

| Property / Function | Role | Purpose |
| :--- | :--- | :--- |
| `perspective` | Parent Container | Sets 3D viewing distance (e.g. `1000px`) |
| `transform-style` | Parent/Card | Set `preserve-3d` to keep children in 3D space |
| `rotateY(180deg)` | Card Object | Flips element around vertical Y-axis |
| `rotateX(45deg)` | Card Object | Tilts element around horizontal X-axis |
| `translateZ(50px)` | Card Object | Pulls element closer to user along Z-axis |
| `backface-visibility` | Card Faces | Set `hidden` to hide reverse side |

---

## Visual Explanation

```mermaid
flowchart TD
    A["Perspective Container (perspective: 1000px)"] --> B["3D Card (transform-style: preserve-3d)"]
    B -->|rotateY(180deg)| C["Front Face (backface-visibility: hidden)"]
    B -->|Rotates 180 deg| D["Back Face (rotateY(180deg))"]
```

---

## Example 1

### HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>3D Card Flip Effect</title>
    <style>
        body { display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: Arial, sans-serif; background-color: #f8fafc; }
        
        /* 3D Scene Viewport */
        .scene {
            width: 260px;
            height: 160px;
            perspective: 1000px;
        }
        
        /* 3D Card Object */
        .card {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.8s ease;
        }
        
        .scene:hover .card {
            transform: rotateY(180deg);
        }
        
        /* Card Faces */
        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 20px;
            font-weight: bold;
            backface-visibility: hidden;
        }
        
        .card-front { background-color: #2563eb; }
        .card-back { background-color: #16a34a; transform: rotateY(180deg); }
    </style>
</head>
<body>
    <div class="scene">
        <div class="card">
            <div class="card-face card-front">Front Face</div>
            <div class="card-face card-back">Back Face</div>
        </div>
    </div>
</body>
</html>
```

### CSS
```css
.scene { perspective: 1000px; }
.card { transform-style: preserve-3d; transition: transform 0.8s; }
.scene:hover .card { transform: rotateY(180deg); }
.card-face { backface-visibility: hidden; }
.card-back { transform: rotateY(180deg); }
```

### Explanation
Hovering over `.scene` rotates `.card` 180 degrees around the Y-axis. `backface-visibility: hidden` hides the blue front face and displays the green back face seamlessly.

---

## Output Image Prompt

A browser window showing a 3D card midway through a smooth horizontal 180-degree flip animation transition from blue to green.

---

## Code Explanation

- `perspective: 1000px;`: Sets 3D depth perception container.
- `transform-style: preserve-3d;`: Preserves 3D spatial positions for children.
- `backface-visibility: hidden;`: Hides faces when flipped backward away from view.

---

## Best Practices

- **Set `perspective` on Parent Container**: Declare `perspective` on the parent container (e.g. `.scene`), not on the card element itself.
- **Use `backface-visibility: hidden`**: Always add `backface-visibility: hidden` to front and back face elements for 3D card flips.

---

## Common Mistakes

### Mistake 1: Omitting `transform-style: preserve-3d`

```css
/* INCORRECT */
.card {
    /* Missing transform-style: preserve-3d! Children flatten into 2D plane */
    transition: transform 0.8s;
}
```

#### Explanation
Without `preserve-3d`, 3D child transformations flatten onto a flat 2D plane.

```css
/* CORRECT */
.card {
    transform-style: preserve-3d;
}
```

---

## Browser Compatibility

CSS 3D Transforms have 100% universal support across all desktop and mobile web browsers.

---

## Real-World Applications

- **Interactive 3D Card Flips**: Flashcards, product details reverse side.
- **3D Hero Carousel Cubes**: Rotating 3D image banners.
- **Product Preview Rotations**: Interactive 3D product viewports.

---

## Mini Project

### Project Objective: 3D Credit Card Flip Component
Build a credit card component that flips 180 degrees on hover to display card security code details on the back.

---

## Practice Exercises

### Beginner Level
1. Add `perspective: 1000px;` to a container.
2. Rotate an element 180 degrees around Y-axis (`transform: rotateY(180deg);`).
3. Rotate an element 45 degrees around X-axis (`transform: rotateX(45deg);`).
4. Hide backface using `backface-visibility: hidden;`.
5. Pull an element closer using `translateZ(50px);`.

### Intermediate Level
6. Preserve 3D space using `transform-style: preserve-3d;`.
7. Build a 3D card flip hover component.
8. Combine `rotateX()` and `rotateY()` in a 3D rotation rule.
9. Adjust perspective viewpoint using `perspective-origin: top left`.
10. Transition a 3D card flip smoothly over 0.8 seconds.

### Advanced Level
11. Build a 4-sided rotating 3D cube carousel using CSS 3D transforms.
12. Audit GPU memory usage of heavy 3D perspective scenes.
13. Combine 3D transforms with CSS parallax scrolling effects.
14. Optimize sub-pixel rendering artifact anti-aliasing on flipped card edges.
15. Solve mobile Safari z-index clipping bugs on 3D preserved layers.

---

## Quick Quiz

**1. Which axis represents depth (towards or away from the user)?**
A) Z-Axis  
B) X-Axis  

**2. Where should the `perspective` property be declared?**
A) Parent container of the 3D scene  
B) Individual text spans  

**3. What property preserves 3D positioning for child elements?**
A) `transform-style: preserve-3d`  
B) `3d-style: active`  

**4. What property hides the back side of a 3D card when rotated facing away from view?**
A) `backface-visibility: hidden`  
B) `display: none`  

**5. Which function flips a card horizontally left to right?**
A) `rotateY(180deg)`  
B) `rotateX(180deg)`  

**6. Which function tilts a card forward or backward?**
A) `rotateX(45deg)`  
B) `rotateZ(45deg)`  

**7. What does smaller `perspective` value (e.g. `200px`) produce compared to `2000px`?**
A) Intense, dramatic 3D distortion perspective  
B) Subtle, flat perspective  

**8. What function moves an element closer to the viewer along the Z-axis?**
A) `translateZ(100px)`  
B) `translateX(100px)`  

**9. Can 3D transforms run smoothly on mobile devices?**
A) Yes (hardware-accelerated by GPU)  
B) No  

**10. What property changes 3D perspective viewing origin angles?**
A) `perspective-origin`  
B) `3d-origin`  

---

### Answers
1: A | 2: A | 3: A | 4: A | 5: A | 6: A | 7: A | 8: A | 9: A | 10: A

---

## Interview Questions

**1. What are CSS 3D Transforms?**  
*Answer:* CSS 3D Transforms extend spatial geometry into 3D space by introducing a depth Z-axis, using functions (`rotateX`, `rotateY`, `translateZ`) and container properties (`perspective`, `transform-style: preserve-3d`) to construct 3D depth scenes.

**2. Explain the purpose of `perspective` and `transform-style: preserve-3d`.**  
*Answer:* `perspective` declared on a parent container sets the viewer's 3D depth perspective distance. `transform-style: preserve-3d` declared on an object instructs the browser renderer to maintain 3D spatial depth coordinates for child elements rather than flattening them onto a 2D plane.

**3. How do you create a 3D card flip effect in CSS?**  
*Answer:* Set `perspective: 1000px` on a parent scene. Place a card box inside with `transform-style: preserve-3d`. Create front and back face children with `position: absolute` and `backface-visibility: hidden`. Pre-rotate `.card-back` using `rotateY(180deg)`. On hover, apply `transform: rotateY(180deg)` to the card box.

---

## Summary

- Set **`perspective: 1000px`** on parent scene.
- Use **`transform-style: preserve-3d`**.
- Use **`backface-visibility: hidden`**.
- **`rotateY(180deg)`**: Horizontal card flip.

---

## Cheat Sheet

```css
/* 3D CARD FLIP PATTERN */
.scene {
    perspective: 1000px;
}

.card {
    transform-style: preserve-3d;
    transition: transform 0.8s;
}

.scene:hover .card {
    transform: rotateY(180deg);
}

.face {
    backface-visibility: hidden;
}

.face-back {
    transform: rotateY(180deg);
}
```

---

## Related Topics

- **Previous Topic**: [CSS 2D Transforms](42-css-2d-transforms.md)
- **Next Topic**: [CSS Variables](44-css-variables.md)
- **Recommended Learning Order**: Introduction to CSS -> Ways to Add CSS -> CSS Selectors -> CSS Colors -> CSS Fonts -> CSS Borders -> Border Radius -> CSS Shadows -> CSS Margins -> CSS Padding -> CSS Width -> CSS Height -> CSS Box Model -> CSS Float -> CSS Overflow -> CSS Display -> CSS Position -> CSS Background Images -> CSS Background Properties -> CSS Combinators -> CSS Pseudo Classes -> CSS Pseudo Elements -> CSS Pagination -> CSS Dropdown Menu -> CSS Navigation Bar -> Responsive Web Design -> Media Queries -> CSS Flexbox -> Flex Direction -> Justify Content -> Align Items -> Align Self -> Flex Wrap -> Gap -> Order -> CSS Grid -> Grid Template Columns -> Grid Template Rows -> CSS Transitions -> CSS Animations -> CSS 2D Transforms -> CSS 3D Transforms -> CSS Variables
