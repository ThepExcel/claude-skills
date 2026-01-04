"""
Math Plots — Graphs, Functions, Geometry
Using Matplotlib for static visualizations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import Callable, List, Tuple, Optional


# =============================================================================
# FUNCTION PLOTS
# =============================================================================

def plot_function(
    func: Callable[[np.ndarray], np.ndarray],
    x_range: Tuple[float, float] = (-10, 10),
    title: str = "",
    xlabel: str = "x",
    ylabel: str = "y",
    color: str = "blue",
    show_grid: bool = True,
    show_axes: bool = True,
    figsize: Tuple[int, int] = (10, 6),
    filename: Optional[str] = None
):
    """
    Plot a mathematical function

    Example:
        plot_function(lambda x: np.sin(x), x_range=(-2*np.pi, 2*np.pi), title="sin(x)")
        plot_function(lambda x: x**2, x_range=(-5, 5), title="x²")
    """
    fig, ax = plt.subplots(figsize=figsize)

    x = np.linspace(x_range[0], x_range[1], 500)
    y = func(x)

    ax.plot(x, y, color=color, linewidth=2, label=title if title else "f(x)")

    if show_axes:
        ax.axhline(y=0, color='black', linewidth=0.5)
        ax.axvline(x=0, color='black', linewidth=0.5)

    if show_grid:
        ax.grid(True, alpha=0.3)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def plot_multiple_functions(
    functions: List[Tuple[Callable, str, str]],  # (func, label, color)
    x_range: Tuple[float, float] = (-10, 10),
    title: str = "",
    figsize: Tuple[int, int] = (10, 6),
    filename: Optional[str] = None
):
    """
    Plot multiple functions on same axes

    Example:
        plot_multiple_functions([
            (lambda x: np.sin(x), "sin(x)", "blue"),
            (lambda x: np.cos(x), "cos(x)", "red"),
        ], x_range=(-2*np.pi, 2*np.pi))
    """
    fig, ax = plt.subplots(figsize=figsize)

    x = np.linspace(x_range[0], x_range[1], 500)

    for func, label, color in functions:
        y = func(x)
        ax.plot(x, y, color=color, linewidth=2, label=label)

    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend()

    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def plot_derivative(
    func: Callable,
    x_range: Tuple[float, float] = (-5, 5),
    title: str = "Function and Derivative",
    filename: Optional[str] = None
):
    """
    Plot function and its numerical derivative
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(x_range[0], x_range[1], 500)
    y = func(x)

    # Numerical derivative
    dx = x[1] - x[0]
    dy = np.gradient(y, dx)

    ax.plot(x, y, 'b-', linewidth=2, label="f(x)")
    ax.plot(x, dy, 'r--', linewidth=2, label="f'(x)")

    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


# =============================================================================
# GEOMETRY
# =============================================================================

def draw_triangle(
    vertices: List[Tuple[float, float]],
    labels: List[str] = ["A", "B", "C"],
    show_angles: bool = False,
    show_sides: bool = False,
    title: str = "Triangle",
    filename: Optional[str] = None
):
    """
    Draw a triangle with optional labels

    Example:
        draw_triangle([(0, 0), (4, 0), (2, 3)], labels=["A", "B", "C"])
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Close the triangle
    vertices_closed = vertices + [vertices[0]]
    xs, ys = zip(*vertices_closed)

    # Draw triangle
    ax.plot(xs, ys, 'b-', linewidth=2)
    ax.fill(xs, ys, alpha=0.2, color='blue')

    # Labels
    for i, (x, y) in enumerate(vertices):
        offset = 0.2
        ax.plot(x, y, 'ko', markersize=8)
        ax.annotate(labels[i], (x, y), fontsize=14, fontweight='bold',
                   xytext=(offset, offset), textcoords='offset points')

    if show_sides:
        # Calculate and show side lengths
        for i in range(3):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % 3]
            length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.annotate(f"{length:.1f}", (mx, my), fontsize=10, color='red')

    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def draw_circle_with_parts(
    radius: float = 2,
    show_radius: bool = True,
    show_diameter: bool = False,
    show_chord: bool = False,
    show_arc: bool = False,
    angle_deg: float = 60,
    title: str = "Circle",
    filename: Optional[str] = None
):
    """
    Draw circle with various parts labeled
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Circle
    circle = plt.Circle((0, 0), radius, fill=False, color='blue', linewidth=2)
    ax.add_patch(circle)

    # Center
    ax.plot(0, 0, 'ko', markersize=6)
    ax.annotate('O', (0, 0), xytext=(-0.3, -0.3), fontsize=12)

    if show_radius:
        angle_rad = np.radians(angle_deg)
        x_end = radius * np.cos(angle_rad)
        y_end = radius * np.sin(angle_rad)
        ax.plot([0, x_end], [0, y_end], 'r-', linewidth=2)
        ax.annotate(f'r = {radius}', (x_end/2, y_end/2), fontsize=10, color='red')

    if show_diameter:
        ax.plot([-radius, radius], [0, 0], 'g-', linewidth=2)
        ax.annotate(f'd = {2*radius}', (0, -0.3), fontsize=10, color='green', ha='center')

    if show_arc:
        arc = patches.Arc((0, 0), 2*radius, 2*radius, angle=0,
                         theta1=0, theta2=angle_deg, color='orange', linewidth=3)
        ax.add_patch(arc)

    ax.set_xlim(-radius * 1.5, radius * 1.5)
    ax.set_ylim(-radius * 1.5, radius * 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def draw_unit_circle(
    angles_deg: List[float] = [0, 30, 45, 60, 90],
    show_coordinates: bool = True,
    filename: Optional[str] = None
):
    """
    Draw unit circle with common angles
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    # Unit circle
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=2)

    # Axes
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)

    # Points and labels
    for angle_deg in angles_deg:
        angle_rad = np.radians(angle_deg)
        x = np.cos(angle_rad)
        y = np.sin(angle_rad)

        # Point
        ax.plot(x, y, 'ro', markersize=8)

        # Line from origin
        ax.plot([0, x], [0, y], 'r-', linewidth=1, alpha=0.5)

        # Label
        if show_coordinates:
            label = f"{angle_deg}°\n({x:.2f}, {y:.2f})"
        else:
            label = f"{angle_deg}°"

        # Position label outside circle
        offset = 1.15
        ax.annotate(label, (x * offset, y * offset), fontsize=9, ha='center', va='center')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Unit Circle', fontsize=14, fontweight='bold')
    ax.set_xlabel('cos(θ)')
    ax.set_ylabel('sin(θ)')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


# =============================================================================
# COORDINATE SYSTEMS
# =============================================================================

def draw_coordinate_plane(
    points: List[Tuple[float, float, str]] = [],  # (x, y, label)
    vectors: List[Tuple[Tuple[float, float], Tuple[float, float], str, str]] = [],  # (start, end, label, color)
    x_range: Tuple[int, int] = (-5, 5),
    y_range: Tuple[int, int] = (-5, 5),
    title: str = "Coordinate Plane",
    filename: Optional[str] = None
):
    """
    Draw coordinate plane with points and vectors

    Example:
        draw_coordinate_plane(
            points=[(2, 3, "A"), (-1, 2, "B")],
            vectors=[((0, 0), (3, 2), "v", "red")]
        )
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    # Grid
    ax.set_xlim(x_range[0] - 0.5, x_range[1] + 0.5)
    ax.set_ylim(y_range[0] - 0.5, y_range[1] + 0.5)
    ax.set_xticks(range(x_range[0], x_range[1] + 1))
    ax.set_yticks(range(y_range[0], y_range[1] + 1))
    ax.grid(True, alpha=0.3)

    # Axes
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Points
    for x, y, label in points:
        ax.plot(x, y, 'bo', markersize=10)
        ax.annotate(f"{label} ({x}, {y})", (x, y), fontsize=10,
                   xytext=(5, 5), textcoords='offset points')

    # Vectors
    for start, end, label, color in vectors:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        ax.annotate(label, mid, fontsize=12, color=color, fontweight='bold')

    ax.set_aspect('equal')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


# =============================================================================
# MAIN — DEMO
# =============================================================================

if __name__ == "__main__":
    output_dir = "learning-notes"
    import os
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 50)
    print("🎯 Math Plots Demo")
    print("=" * 50)

    # 1. Function plot
    print("\n1. Plotting sin(x)...")
    plot_function(
        lambda x: np.sin(x),
        x_range=(-2 * np.pi, 2 * np.pi),
        title="y = sin(x)",
        filename=f"{output_dir}/sin_function.png"
    )

    # 2. Multiple functions
    print("\n2. Plotting sin(x) and cos(x)...")
    plot_multiple_functions(
        [
            (lambda x: np.sin(x), "sin(x)", "blue"),
            (lambda x: np.cos(x), "cos(x)", "red"),
        ],
        x_range=(-2 * np.pi, 2 * np.pi),
        title="Trigonometric Functions",
        filename=f"{output_dir}/trig_functions.png"
    )

    # 3. Derivative
    print("\n3. Plotting x² and its derivative...")
    plot_derivative(
        lambda x: x**2,
        x_range=(-3, 3),
        title="f(x) = x² and f'(x) = 2x",
        filename=f"{output_dir}/derivative.png"
    )

    # 4. Triangle
    print("\n4. Drawing triangle...")
    draw_triangle(
        [(0, 0), (4, 0), (2, 3)],
        show_sides=True,
        title="Triangle ABC",
        filename=f"{output_dir}/triangle.png"
    )

    # 5. Unit circle
    print("\n5. Drawing unit circle...")
    draw_unit_circle(
        angles_deg=[0, 30, 45, 60, 90, 120, 135, 150, 180],
        filename=f"{output_dir}/unit_circle.png"
    )

    # 6. Coordinate plane with vectors
    print("\n6. Drawing coordinate plane with vectors...")
    draw_coordinate_plane(
        points=[(2, 3, "A"), (-1, 2, "B")],
        vectors=[
            ((0, 0), (2, 3), "a", "red"),
            ((0, 0), (-1, 2), "b", "blue"),
            ((0, 0), (1, 5), "a+b", "green"),
        ],
        title="Vector Addition",
        filename=f"{output_dir}/vectors.png"
    )

    print("\n" + "=" * 50)
    print(f"✅ Done! Check {output_dir}/ for PNG files")
    print("=" * 50)
