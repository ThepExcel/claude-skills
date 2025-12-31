# Manim Guide — 3Blue1Brown Style Animations

## Installation

```bash
pip install manim

# Dependencies (Ubuntu/WSL)
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
```

## Basic Structure

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # สร้าง objects
        circle = Circle(color=BLUE)

        # Animate
        self.play(Create(circle))
        self.wait(1)
```

## Render Commands

```bash
# Preview (low quality, fast)
manim -pql script.py MyScene

# Preview (high quality)
manim -pqh script.py MyScene

# Save without preview
manim -ql script.py MyScene

# GIF output
manim -ql --format=gif script.py MyScene
```

**Flags:**
- `-p` = preview (เปิดดูทันที)
- `-q` = quality (l=low, m=medium, h=high, k=4K)
- `-a` = render all scenes

---

## Common Objects

### Shapes

```python
circle = Circle(radius=1, color=BLUE)
square = Square(side_length=2, color=RED)
triangle = Triangle(color=GREEN)
line = Line(start=LEFT, end=RIGHT)
arrow = Arrow(start=LEFT, end=RIGHT)
dot = Dot(point=ORIGIN)
```

### Text & Math

```python
text = Text("Hello", font_size=48)
math = MathTex(r"E = mc^2")
tex = Tex(r"This is \textbf{bold}")
```

### Positioning

```python
# Constants
LEFT, RIGHT, UP, DOWN, ORIGIN
UL, UR, DL, DR  # corners

# Methods
obj.move_to(ORIGIN)
obj.next_to(other, RIGHT)
obj.shift(UP * 2)
obj.align_to(other, LEFT)
```

---

## Animations

### Create & Remove

```python
self.play(Create(obj))       # วาดขึ้นมา
self.play(FadeIn(obj))       # จางเข้า
self.play(FadeOut(obj))      # จางออก
self.play(Uncreate(obj))     # ลบแบบ reverse
```

### Transform

```python
self.play(Transform(a, b))           # a กลายเป็น b
self.play(ReplacementTransform(a, b)) # a หายไป b มาแทน
self.play(TransformMatchingShapes(a, b))  # จับคู่ shape
```

### Movement

```python
self.play(obj.animate.shift(RIGHT * 2))
self.play(obj.animate.move_to(UP))
self.play(obj.animate.scale(2))
self.play(obj.animate.rotate(PI/2))
```

### Multiple Animations

```python
# พร้อมกัน
self.play(Create(a), Create(b))

# ทีละอัน
self.play(Create(a))
self.play(Create(b))

# Lag ratio (เหลื่อมกัน)
self.play(LaggedStart(Create(a), Create(b), lag_ratio=0.5))
```

---

## Colors

```python
# Built-in
RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK
WHITE, BLACK, GRAY

# Hex
color="#FF5733"

# RGB
color=rgb_to_color([1, 0.5, 0])
```

---

## Useful Patterns

### Equation Transformation

```python
eq1 = MathTex(r"a^2 + b^2")
eq2 = MathTex(r"c^2")

self.play(Write(eq1))
self.wait()
self.play(Transform(eq1, eq2))
```

### Number Line

```python
number_line = NumberLine(x_range=[-5, 5, 1])
self.play(Create(number_line))

dot = Dot(number_line.n2p(3), color=RED)
self.play(Create(dot))
```

### Axes & Graph

```python
axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
graph = axes.plot(lambda x: np.sin(x), color=BLUE)

self.play(Create(axes))
self.play(Create(graph))
```

### Vector

```python
vector = Arrow(ORIGIN, [2, 1, 0], buff=0, color=YELLOW)
label = MathTex(r"\vec{v}").next_to(vector, UP)

self.play(Create(vector), Write(label))
```

---

## Physics Examples

### Vector Addition

```python
class VectorAddition(Scene):
    def construct(self):
        # Vectors
        v1 = Arrow(ORIGIN, [2, 0, 0], buff=0, color=RED)
        v2 = Arrow([2, 0, 0], [2, 2, 0], buff=0, color=BLUE)
        v_sum = Arrow(ORIGIN, [2, 2, 0], buff=0, color=GREEN)

        # Labels
        l1 = MathTex(r"\vec{a}").next_to(v1, DOWN)
        l2 = MathTex(r"\vec{b}").next_to(v2, RIGHT)
        l_sum = MathTex(r"\vec{a}+\vec{b}").next_to(v_sum, LEFT)

        # Animate
        self.play(Create(v1), Write(l1))
        self.play(Create(v2), Write(l2))
        self.play(Create(v_sum), Write(l_sum))
```

### F = ma

```python
class NewtonSecondLaw(Scene):
    def construct(self):
        # Equation
        eq = MathTex(r"F", r"=", r"m", r"a")
        eq[0].set_color(RED)
        eq[2].set_color(BLUE)
        eq[3].set_color(GREEN)

        self.play(Write(eq))
        self.wait()

        # Box
        box = Square(side_length=1, color=BLUE).shift(DOWN * 2)
        force = Arrow(box.get_left(), box.get_left() + LEFT * 2, color=RED)

        self.play(Create(box))
        self.play(Create(force))
        self.play(box.animate.shift(RIGHT * 3), run_time=2)
```

---

## Tips

1. **Start simple** — ทำ scene เล็กๆ ก่อน แล้วค่อยรวม
2. **Use wait()** — ให้เวลาคนดูดีคิด `self.wait(1)`
3. **Preview low quality** — ใช้ `-ql` ตอน develop ให้เร็ว
4. **Group related objects** — `VGroup(a, b, c)` เพื่อ animate พร้อมกัน
5. **Copy 3b1b** — ดู source code ของ 3Blue1Brown ได้ที่ GitHub

---

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [3Blue1Brown GitHub](https://github.com/3b1b/manim)
- [Manim Community](https://www.manim.community/)
