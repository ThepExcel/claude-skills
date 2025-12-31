"""
Manim Physics Animations — 3Blue1Brown Style
"""

from manim import *


class VectorAddition(Scene):
    """แสดงการบวก Vector แบบหางต่อหัว"""

    def construct(self):
        # Title
        title = Text("Vector Addition", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create axes (optional, for reference)
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=6,
            y_length=4,
            tips=False,
        ).shift(DOWN * 0.5)

        self.play(Create(axes), run_time=0.5)

        # Vector A (red)
        vec_a = Arrow(
            axes.c2p(0, 0), axes.c2p(3, 0),
            buff=0, color=RED, stroke_width=6
        )
        label_a = MathTex(r"\vec{a}", color=RED).next_to(vec_a, DOWN)

        # Vector B (blue)
        vec_b = Arrow(
            axes.c2p(0, 0), axes.c2p(1, 2),
            buff=0, color=BLUE, stroke_width=6
        )
        label_b = MathTex(r"\vec{b}", color=BLUE).next_to(vec_b, LEFT)

        # Show vectors from origin first
        self.play(GrowArrow(vec_a), Write(label_a))
        self.wait(0.5)
        self.play(GrowArrow(vec_b), Write(label_b))
        self.wait(0.5)

        # Move B to tip of A (head-to-tail method)
        vec_b_moved = Arrow(
            axes.c2p(3, 0), axes.c2p(4, 2),
            buff=0, color=BLUE, stroke_width=6
        )
        label_b_moved = MathTex(r"\vec{b}", color=BLUE).next_to(vec_b_moved, RIGHT)

        self.play(
            Transform(vec_b, vec_b_moved),
            Transform(label_b, label_b_moved),
            run_time=1.5
        )
        self.wait(0.5)

        # Resultant vector (green)
        vec_sum = Arrow(
            axes.c2p(0, 0), axes.c2p(4, 2),
            buff=0, color=GREEN, stroke_width=6
        )
        label_sum = MathTex(r"\vec{a} + \vec{b}", color=GREEN).next_to(vec_sum, UP)

        self.play(GrowArrow(vec_sum), Write(label_sum))
        self.wait(1)

        # Show equation
        equation = MathTex(
            r"\vec{a} + \vec{b} = \vec{c}",
            font_size=36
        ).to_edge(DOWN)
        equation[0][0:2].set_color(RED)
        equation[0][3:5].set_color(BLUE)
        equation[0][6:8].set_color(GREEN)

        self.play(Write(equation))
        self.wait(2)


class ForcesOnBox(Scene):
    """แสดงแรงที่กระทำต่อกล่อง (FBD style)"""

    def construct(self):
        # Title
        title = Text("Forces on a Box", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Box
        box = Square(side_length=1.5, color=WHITE, fill_opacity=0.3)
        box.set_fill(BLUE, opacity=0.3)
        label_m = MathTex("m").move_to(box)

        self.play(Create(box), Write(label_m))
        self.wait(0.5)

        # Weight (down)
        weight = Arrow(
            box.get_center(),
            box.get_center() + DOWN * 2,
            buff=0, color=RED, stroke_width=5
        )
        label_w = MathTex(r"mg", color=RED).next_to(weight, RIGHT)

        self.play(GrowArrow(weight), Write(label_w))
        self.wait(0.5)

        # Normal force (up)
        normal = Arrow(
            box.get_bottom(),
            box.get_bottom() + UP * 2,
            buff=0, color=GREEN, stroke_width=5
        )
        label_n = MathTex(r"N", color=GREEN).next_to(normal, LEFT)

        # Ground
        ground = Line(LEFT * 3, RIGHT * 3, color=GRAY).next_to(box, DOWN, buff=0)

        self.play(Create(ground))
        self.play(GrowArrow(normal), Write(label_n))
        self.wait(0.5)

        # Applied force (right)
        applied = Arrow(
            box.get_left(),
            box.get_left() + LEFT * 2,
            buff=0, color=YELLOW, stroke_width=5
        )
        # Flip direction - force pushing right
        applied = Arrow(
            box.get_left() + LEFT * 2,
            box.get_left(),
            buff=0, color=YELLOW, stroke_width=5
        )
        label_f = MathTex(r"F", color=YELLOW).next_to(applied, UP)

        self.play(GrowArrow(applied), Write(label_f))
        self.wait(0.5)

        # Equation
        eq = MathTex(r"F = ma", font_size=48).to_edge(DOWN)
        eq[0][0].set_color(YELLOW)

        self.play(Write(eq))
        self.wait(1)

        # Animate box moving
        self.play(
            box.animate.shift(RIGHT * 3),
            label_m.animate.shift(RIGHT * 3),
            run_time=2,
            rate_func=rate_functions.ease_in_quad
        )
        self.wait(1)


class NewtonThirdLaw(Scene):
    """แสดงกฎข้อ 3 ของนิวตัน: Action-Reaction"""

    def construct(self):
        # Title
        title = Text("Newton's Third Law", font_size=48).to_edge(UP)
        subtitle = Text("Action = Reaction", font_size=32, color=GRAY).next_to(title, DOWN)

        self.play(Write(title), Write(subtitle))
        self.wait(0.5)

        # Two boxes
        box_a = Square(side_length=1.2, color=RED, fill_opacity=0.3)
        box_a.set_fill(RED, opacity=0.3)
        box_a.shift(LEFT * 2)
        label_a = Text("A", font_size=24).move_to(box_a)

        box_b = Square(side_length=1.2, color=BLUE, fill_opacity=0.3)
        box_b.set_fill(BLUE, opacity=0.3)
        box_b.shift(RIGHT * 0.5)
        label_b = Text("B", font_size=24).move_to(box_b)

        self.play(
            Create(box_a), Write(label_a),
            Create(box_b), Write(label_b)
        )
        self.wait(0.5)

        # A pushes B (action)
        force_ab = Arrow(
            box_a.get_right(),
            box_b.get_left(),
            buff=0.1, color=YELLOW, stroke_width=5
        )
        label_ab = MathTex(r"F_{A \to B}", color=YELLOW, font_size=28).next_to(force_ab, UP)

        self.play(GrowArrow(force_ab), Write(label_ab))
        self.wait(0.5)

        # B pushes A back (reaction)
        force_ba = Arrow(
            box_b.get_left() + DOWN * 0.5,
            box_a.get_right() + DOWN * 0.5,
            buff=0.1, color=ORANGE, stroke_width=5
        )
        label_ba = MathTex(r"F_{B \to A}", color=ORANGE, font_size=28).next_to(force_ba, DOWN)

        self.play(GrowArrow(force_ba), Write(label_ba))
        self.wait(0.5)

        # Equation
        eq = MathTex(
            r"F_{A \to B} = -F_{B \to A}",
            font_size=40
        ).to_edge(DOWN)
        eq[0][0:5].set_color(YELLOW)
        eq[0][7:12].set_color(ORANGE)

        self.play(Write(eq))
        self.wait(2)


class InclinedPlane(Scene):
    """แสดงแรงบนพื้นเอียง"""

    def construct(self):
        # Title
        title = Text("Forces on Inclined Plane", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Draw inclined plane
        angle = 30 * DEGREES
        plane_length = 5
        plane_start = LEFT * 2.5 + DOWN * 1.5
        plane_end = plane_start + plane_length * np.array([np.cos(angle), np.sin(angle), 0])

        plane = Line(plane_start, plane_end, color=WHITE, stroke_width=4)
        ground = Line(plane_start, plane_start + RIGHT * plane_length * np.cos(angle), color=GRAY, stroke_width=2)

        # Angle arc
        arc = Arc(radius=0.8, start_angle=0, angle=angle, arc_center=plane_start, color=YELLOW)
        angle_label = MathTex(r"30°", font_size=28, color=YELLOW).next_to(arc, RIGHT, buff=0.1)

        self.play(Create(plane), Create(ground), Create(arc), Write(angle_label))

        # Box on plane
        box_pos = plane_start + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
        box = Square(side_length=0.6, color=BLUE, fill_opacity=0.5)
        box.move_to(box_pos)
        box.rotate(angle)
        label_m = MathTex("m", font_size=24).move_to(box)

        self.play(Create(box), Write(label_m))
        self.wait(0.5)

        # Forces
        # mg (straight down)
        mg = Arrow(box_pos, box_pos + DOWN * 1.5, buff=0, color=RED, stroke_width=4)
        mg_label = MathTex("mg", color=RED, font_size=28).next_to(mg, RIGHT)
        self.play(GrowArrow(mg), Write(mg_label))
        self.wait(0.3)

        # N (perpendicular to plane)
        normal_dir = np.array([-np.sin(angle), np.cos(angle), 0])
        N = Arrow(box_pos, box_pos + normal_dir * 1.2, buff=0, color=GREEN, stroke_width=4)
        N_label = MathTex("N", color=GREEN, font_size=28).next_to(N, UP + LEFT, buff=0.1)
        self.play(GrowArrow(N), Write(N_label))
        self.wait(0.3)

        # mg sin θ (parallel to plane, down)
        parallel_dir = np.array([np.cos(angle), np.sin(angle), 0])
        mg_sin = Arrow(box_pos, box_pos - parallel_dir * 1.0, buff=0, color=ORANGE, stroke_width=4)
        mg_sin_label = MathTex(r"mg\sin\theta", color=ORANGE, font_size=24).next_to(mg_sin, DOWN + LEFT, buff=0.1)
        self.play(GrowArrow(mg_sin), Write(mg_sin_label))
        self.wait(0.3)

        # mg cos θ (perpendicular to plane, into surface)
        mg_cos = Arrow(box_pos, box_pos - normal_dir * 1.0, buff=0, color=PURPLE, stroke_width=4)
        mg_cos_label = MathTex(r"mg\cos\theta", color=PURPLE, font_size=24).next_to(mg_cos, DOWN + RIGHT, buff=0.1)
        self.play(GrowArrow(mg_cos), Write(mg_cos_label))
        self.wait(0.5)

        # Equations
        eq1 = MathTex(r"N = mg\cos\theta", font_size=32).to_edge(DOWN).shift(LEFT * 2.5)
        eq2 = MathTex(r"a = g\sin\theta", font_size=32).to_edge(DOWN).shift(RIGHT * 2.5)

        self.play(Write(eq1), Write(eq2))
        self.wait(2)


class ProjectileMotion(Scene):
    """แสดงการเคลื่อนที่แบบ Projectile"""

    def construct(self):
        # Title
        title = Text("Projectile Motion", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        ).shift(DOWN * 0.5 + LEFT * 0.5)

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Projectile path (parabola)
        v0 = 5
        angle = 45 * DEGREES
        g = 10

        def trajectory(t):
            x = v0 * np.cos(angle) * t
            y = v0 * np.sin(angle) * t - 0.5 * g * t * t
            return axes.c2p(x, max(y, 0))

        # Draw path
        t_flight = 2 * v0 * np.sin(angle) / g
        path = ParametricFunction(
            lambda t: trajectory(t),
            t_range=[0, t_flight],
            color=YELLOW
        )

        self.play(Create(path), run_time=2)

        # Ball following path
        ball = Dot(color=RED, radius=0.15)
        ball.move_to(axes.c2p(0, 0))

        # Velocity vectors at different points
        t_points = [0, t_flight/4, t_flight/2, 3*t_flight/4]

        for t in t_points:
            pos = trajectory(t)
            vx = v0 * np.cos(angle)
            vy = v0 * np.sin(angle) - g * t

            # Scale for visualization
            scale = 0.3
            v_arrow = Arrow(
                pos, pos + np.array([vx * scale, vy * scale, 0]),
                buff=0, color=BLUE, stroke_width=3
            )

            if t == 0:
                self.play(ball.animate.move_to(pos), GrowArrow(v_arrow))
            else:
                self.play(
                    ball.animate.move_to(pos),
                    GrowArrow(v_arrow),
                    run_time=0.5
                )
            self.wait(0.3)

        # Equations
        eq = MathTex(
            r"x = v_0 \cos\theta \cdot t",
            r"\quad",
            r"y = v_0 \sin\theta \cdot t - \frac{1}{2}gt^2",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(eq))
        self.wait(2)


class MomentumConservation(Scene):
    """แสดงการอนุรักษ์โมเมนตัม (การชน)"""

    def construct(self):
        # Title
        title = Text("Conservation of Momentum", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Before collision
        before_text = Text("Before:", font_size=24, color=GRAY).shift(UP * 2 + LEFT * 4)
        self.play(Write(before_text))

        # Ball A (moving right)
        ball_a = Circle(radius=0.4, color=RED, fill_opacity=0.7)
        ball_a.shift(LEFT * 4 + UP * 0.5)
        label_a = MathTex("m_1", font_size=24).move_to(ball_a)
        v_a = Arrow(ball_a.get_right(), ball_a.get_right() + RIGHT * 1.5, buff=0, color=RED, stroke_width=4)
        v_a_label = MathTex(r"v_1", font_size=24, color=RED).next_to(v_a, UP)

        # Ball B (stationary)
        ball_b = Circle(radius=0.5, color=BLUE, fill_opacity=0.7)
        ball_b.shift(LEFT * 1 + UP * 0.5)
        label_b = MathTex("m_2", font_size=24).move_to(ball_b)
        v_b = MathTex(r"v_2 = 0", font_size=20, color=BLUE).next_to(ball_b, UP)

        self.play(
            Create(ball_a), Write(label_a), GrowArrow(v_a), Write(v_a_label),
            Create(ball_b), Write(label_b), Write(v_b)
        )
        self.wait(1)

        # Collision animation
        self.play(
            ball_a.animate.shift(RIGHT * 2.5),
            label_a.animate.shift(RIGHT * 2.5),
            v_a.animate.shift(RIGHT * 2.5),
            v_a_label.animate.shift(RIGHT * 2.5),
            run_time=1
        )

        # Flash at collision
        flash = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(ball_a.get_right())
        self.play(flash.animate.scale(5).set_opacity(0), run_time=0.3)
        self.remove(flash)

        # After collision - move to bottom
        after_text = Text("After:", font_size=24, color=GRAY).shift(DOWN * 1 + LEFT * 4)
        self.play(
            Write(after_text),
            FadeOut(v_a), FadeOut(v_a_label), FadeOut(v_b)
        )

        # Ball A after (slower or stopped)
        ball_a_after = ball_a.copy().shift(DOWN * 2 + LEFT * 1)
        label_a_after = MathTex("m_1", font_size=24).move_to(ball_a_after)
        v_a_after = Arrow(ball_a_after.get_right(), ball_a_after.get_right() + RIGHT * 0.5, buff=0, color=RED, stroke_width=4)
        v_a_after_label = MathTex(r"v_1'", font_size=24, color=RED).next_to(v_a_after, UP)

        # Ball B after (moving)
        ball_b_after = ball_b.copy().shift(DOWN * 2 + RIGHT * 1)
        label_b_after = MathTex("m_2", font_size=24).move_to(ball_b_after)
        v_b_after = Arrow(ball_b_after.get_right(), ball_b_after.get_right() + RIGHT * 1.2, buff=0, color=BLUE, stroke_width=4)
        v_b_after_label = MathTex(r"v_2'", font_size=24, color=BLUE).next_to(v_b_after, UP)

        self.play(
            Create(ball_a_after), Write(label_a_after), GrowArrow(v_a_after), Write(v_a_after_label),
            Create(ball_b_after), Write(label_b_after), GrowArrow(v_b_after), Write(v_b_after_label)
        )

        # Conservation equation
        eq = MathTex(
            r"m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'",
            font_size=32
        ).to_edge(DOWN)

        self.play(Write(eq))
        self.wait(2)


class CircularMotion(Scene):
    """แสดงการเคลื่อนที่เป็นวงกลม"""

    def construct(self):
        # Title
        title = Text("Circular Motion", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Circle path
        radius = 2
        circle_path = Circle(radius=radius, color=WHITE, stroke_width=2)
        center = Dot(ORIGIN, color=WHITE)
        center_label = MathTex("O", font_size=24).next_to(center, DOWN + LEFT, buff=0.1)

        self.play(Create(circle_path), Create(center), Write(center_label))

        # Ball
        ball = Dot(color=RED, radius=0.15)
        ball.move_to(RIGHT * radius)

        # Radius line
        radius_line = Line(ORIGIN, ball.get_center(), color=GRAY)
        r_label = MathTex("r", font_size=24, color=GRAY).move_to(radius_line.get_center() + UP * 0.2)

        self.play(Create(ball), Create(radius_line), Write(r_label))

        # Velocity vector (tangent)
        v_arrow = Arrow(ball.get_center(), ball.get_center() + UP * 1.5, buff=0, color=BLUE, stroke_width=4)
        v_label = MathTex(r"\vec{v}", color=BLUE, font_size=28).next_to(v_arrow, RIGHT)

        # Centripetal acceleration (toward center)
        a_arrow = Arrow(ball.get_center(), ball.get_center() + LEFT * 1.2, buff=0, color=GREEN, stroke_width=4)
        a_label = MathTex(r"\vec{a}_c", color=GREEN, font_size=28).next_to(a_arrow, UP)

        self.play(GrowArrow(v_arrow), Write(v_label))
        self.play(GrowArrow(a_arrow), Write(a_label))
        self.wait(0.5)

        # Animate rotation
        angle_tracker = ValueTracker(0)

        def update_ball(mob):
            angle = angle_tracker.get_value()
            mob.move_to(radius * np.array([np.cos(angle), np.sin(angle), 0]))

        def update_radius(mob):
            mob.put_start_and_end_on(ORIGIN, ball.get_center())

        def update_v(mob):
            angle = angle_tracker.get_value()
            pos = ball.get_center()
            # Tangent direction (perpendicular to radius)
            tangent = np.array([-np.sin(angle), np.cos(angle), 0])
            mob.put_start_and_end_on(pos, pos + tangent * 1.5)

        def update_a(mob):
            pos = ball.get_center()
            # Toward center
            to_center = -pos / np.linalg.norm(pos)
            mob.put_start_and_end_on(pos, pos + to_center * 1.2)

        ball.add_updater(update_ball)
        radius_line.add_updater(update_radius)
        v_arrow.add_updater(update_v)
        a_arrow.add_updater(update_a)

        self.play(angle_tracker.animate.set_value(2 * PI), run_time=4, rate_func=linear)

        ball.remove_updater(update_ball)
        radius_line.remove_updater(update_radius)
        v_arrow.remove_updater(update_v)
        a_arrow.remove_updater(update_a)

        # Equations
        eq = MathTex(
            r"a_c = \frac{v^2}{r} = \omega^2 r",
            font_size=32
        ).to_edge(DOWN)

        self.play(Write(eq))
        self.wait(2)


class WorkEnergy(Scene):
    """แสดงงานและพลังงาน"""

    def construct(self):
        # Title
        title = Text("Work and Energy", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Ground
        ground = Line(LEFT * 5, RIGHT * 5, color=GRAY).shift(DOWN * 2)
        self.play(Create(ground))

        # Box
        box = Square(side_length=0.8, color=BLUE, fill_opacity=0.5)
        box.move_to(LEFT * 3 + DOWN * 1.6)
        label_m = MathTex("m", font_size=24).move_to(box)

        self.play(Create(box), Write(label_m))

        # Force arrow
        F = Arrow(box.get_left() + LEFT * 1.5, box.get_left(), buff=0, color=YELLOW, stroke_width=5)
        F_label = MathTex("F", color=YELLOW, font_size=28).next_to(F, UP)

        self.play(GrowArrow(F), Write(F_label))
        self.wait(0.5)

        # Displacement arrow (below)
        d_start = box.get_center() + DOWN * 1
        d_end = d_start + RIGHT * 4
        d_arrow = Arrow(d_start, d_end, buff=0, color=GREEN, stroke_width=3)
        d_label = MathTex("d", color=GREEN, font_size=28).next_to(d_arrow, DOWN)

        self.play(GrowArrow(d_arrow), Write(d_label))

        # Move box
        self.play(
            box.animate.shift(RIGHT * 4),
            label_m.animate.shift(RIGHT * 4),
            F.animate.shift(RIGHT * 4),
            F_label.animate.shift(RIGHT * 4),
            run_time=2
        )

        # Work equation
        work_eq = MathTex(r"W = F \cdot d", font_size=36).shift(UP * 0.5)
        self.play(Write(work_eq))
        self.wait(0.5)

        # Energy equation
        energy_eq = MathTex(r"W = \Delta KE = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2", font_size=32).to_edge(DOWN)
        self.play(Write(energy_eq))
        self.wait(2)


class AtwoodIncline(Scene):
    """
    Customizable: Two masses connected by rope over pulley
    - m1 on inclined plane
    - m2 hanging vertically

    Usage: Modify m1, m2, theta to match your problem
    manim -pql manim_physics.py AtwoodIncline
    """

    def construct(self):
        # === CUSTOMIZE THESE VALUES ===
        m1 = 4  # kg (on incline)
        m2 = 3  # kg (hanging)
        theta = 30  # degrees
        mu = 0  # friction coefficient (0 = frictionless)
        # ==============================

        title = Text("Atwood Machine on Incline", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Draw inclined plane
        angle_rad = theta * PI / 180
        plane_length = 4
        plane_start = LEFT * 2 + DOWN * 1.5
        plane_end = plane_start + plane_length * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])

        incline = Line(plane_start, plane_end, color=WHITE, stroke_width=4)
        ground = Line(plane_start, plane_start + RIGHT * 3, color=WHITE, stroke_width=4)

        # Pulley at top
        pulley_pos = plane_end + UP * 0.3 + RIGHT * 0.2
        pulley = Circle(radius=0.3, color=BLUE).move_to(pulley_pos)
        pulley_center = Dot(pulley_pos, color=WHITE)

        self.play(Create(incline), Create(ground), Create(pulley), Create(pulley_center))

        # Box 1 on incline (positioned on the slope)
        box1_pos = plane_start + 0.4 * plane_length * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        box1 = Square(side_length=0.6, color=RED, fill_opacity=0.7).move_to(box1_pos)
        box1.rotate(angle_rad)
        label1 = MathTex(f"m_1={m1}", font_size=28).next_to(box1, UP + LEFT, buff=0.1)

        # Box 2 hanging
        rope_over_pulley = pulley_pos + RIGHT * 0.3
        box2_pos = rope_over_pulley + DOWN * 2
        box2 = Square(side_length=0.6, color=GREEN, fill_opacity=0.7).move_to(box2_pos)
        label2 = MathTex(f"m_2={m2}", font_size=28).next_to(box2, RIGHT, buff=0.1)

        # Rope
        rope_to_pulley = Line(box1.get_center(), pulley_pos + LEFT * 0.2, color=YELLOW)
        rope_down = Line(rope_over_pulley, box2.get_top(), color=YELLOW)

        self.play(
            Create(box1), Write(label1),
            Create(box2), Write(label2),
            Create(rope_to_pulley), Create(rope_down)
        )
        self.wait(0.5)

        # === Forces on m1 (on incline) ===
        # Weight
        g = 10
        w1 = Arrow(box1.get_center(), box1.get_center() + DOWN * 1.2, color=YELLOW, buff=0)
        w1_label = MathTex("m_1 g", font_size=24, color=YELLOW).next_to(w1, DOWN, buff=0.1)

        # Normal force (perpendicular to incline)
        normal_dir = np.array([-np.sin(angle_rad), np.cos(angle_rad), 0])
        n1 = Arrow(box1.get_center(), box1.get_center() + normal_dir * 0.9, color=GREEN, buff=0)
        n1_label = MathTex("N", font_size=24, color=GREEN).next_to(n1.get_end(), UP, buff=0.1)

        # Tension (up the incline)
        tension_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        t1 = Arrow(box1.get_center(), box1.get_center() + tension_dir * 0.8, color=BLUE, buff=0)
        t1_label = MathTex("T", font_size=24, color=BLUE).next_to(t1.get_end(), UP, buff=0.1)

        self.play(
            GrowArrow(w1), Write(w1_label),
            GrowArrow(n1), Write(n1_label),
            GrowArrow(t1), Write(t1_label),
        )

        # === Forces on m2 (hanging) ===
        w2 = Arrow(box2.get_center(), box2.get_center() + DOWN * 1.0, color=YELLOW, buff=0)
        w2_label = MathTex("m_2 g", font_size=24, color=YELLOW).next_to(w2, LEFT, buff=0.1)

        t2 = Arrow(box2.get_center(), box2.get_center() + UP * 0.8, color=BLUE, buff=0)
        t2_label = MathTex("T", font_size=24, color=BLUE).next_to(t2.get_end(), RIGHT, buff=0.1)

        self.play(
            GrowArrow(w2), Write(w2_label),
            GrowArrow(t2), Write(t2_label),
        )
        self.wait(0.5)

        # === Equations ===
        # m2*g - T = m2*a  (for hanging mass, assuming it goes down)
        # T - m1*g*sin(theta) = m1*a  (for mass on incline)
        # Solving: a = (m2*g - m1*g*sin(theta)) / (m1 + m2)

        sin_theta = np.sin(angle_rad)
        a_val = (m2 * g - m1 * g * sin_theta) / (m1 + m2)
        T_val = m2 * (g - a_val)

        equations = VGroup(
            MathTex(r"m_2 g - T = m_2 a", font_size=28),
            MathTex(r"T - m_1 g \sin\theta = m_1 a", font_size=28),
            MathTex(r"a = \frac{m_2 g - m_1 g \sin\theta}{m_1 + m_2}", font_size=28),
            MathTex(f"a = {a_val:.2f}" + r"\text{ m/s}^2", font_size=28, color=YELLOW),
            MathTex(f"T = {T_val:.1f}" + r"\text{ N}", font_size=28, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        equations.to_edge(RIGHT).shift(DOWN * 0.5)

        for eq in equations:
            self.play(Write(eq), run_time=0.5)

        self.wait(2)


# Quick test scene
class QuickTest(Scene):
    """ทดสอบว่า Manim ทำงานได้"""

    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
