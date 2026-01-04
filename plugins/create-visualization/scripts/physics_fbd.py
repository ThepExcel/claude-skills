"""
Free Body Diagram (FBD) Visualizer
For learning Physics with Claude
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_inclined_plane_fbd(
    mass=4,           # kg
    angle=30,         # degrees
    g=10,             # m/s²
    show_components=True,  # Show mg decomposition
    figsize=(12, 5)
):
    """
    Draw Free Body Diagram for object on inclined plane
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    theta = np.radians(angle)
    mg = mass * g
    mg_parallel = mg * np.sin(theta)      # Component parallel to incline
    mg_perpendicular = mg * np.cos(theta)  # Component perpendicular to incline

    # === LEFT: Physical situation ===
    ax1 = axes[0]
    ax1.set_xlim(-0.5, 5)
    ax1.set_ylim(-0.5, 4)
    ax1.set_aspect('equal')
    ax1.set_title(f'Situation: {mass} kg box on {angle}° incline', fontsize=12, fontweight='bold')
    ax1.axis('off')

    # Draw inclined plane
    incline_length = 4.5
    incline_x = [0, incline_length * np.cos(theta)]
    incline_y = [0, incline_length * np.sin(theta)]
    ax1.fill([0, incline_x[1], incline_x[1], 0], [0, incline_y[1], 0, 0],
             color='tan', alpha=0.5, edgecolor='black', linewidth=2)
    ax1.plot(incline_x, incline_y, 'k-', linewidth=3)
    ax1.plot([0, incline_length * np.cos(theta)], [0, 0], 'k-', linewidth=2)

    # Draw angle arc
    arc = patches.Arc((0, 0), 1.2, 1.2, angle=0, theta1=0, theta2=angle, color='blue', linewidth=2)
    ax1.add_patch(arc)
    ax1.text(0.8, 0.15, f'{angle}°', fontsize=11, color='blue', fontweight='bold')

    # Draw box on incline
    box_dist = 2.2  # distance along incline
    box_center_x = box_dist * np.cos(theta)
    box_center_y = box_dist * np.sin(theta) + 0.25
    box_size = 0.5

    # Create rotated rectangle
    rect = patches.Rectangle(
        (box_center_x - box_size/2, box_center_y - box_size/2),
        box_size, box_size,
        angle=angle,
        facecolor='lightblue',
        edgecolor='black',
        linewidth=2
    )
    ax1.add_patch(rect)
    ax1.text(box_center_x + 0.1, box_center_y + 0.4, f'{mass} kg', fontsize=10, fontweight='bold')

    # Draw gravity arrow
    ax1.annotate('', xy=(box_center_x, box_center_y - 0.8), xytext=(box_center_x, box_center_y),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax1.text(box_center_x + 0.15, box_center_y - 0.5, 'mg', fontsize=10, color='red', fontweight='bold')

    # Draw motion direction
    ax1.annotate('', xy=(3.8, 0.15), xytext=(3.2, 0.15),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    ax1.text(3.5, 0.35, 'slides down', fontsize=9, color='purple')

    # === RIGHT: Free Body Diagram ===
    ax2 = axes[1]
    ax2.set_xlim(-3.5, 3.5)
    ax2.set_ylim(-3.5, 3.5)
    ax2.set_aspect('equal')
    ax2.set_title('Free Body Diagram (rotated axes)', fontsize=12, fontweight='bold')
    ax2.axis('off')

    # Draw box at center
    box_fbd = patches.FancyBboxPatch(
        (-0.4, -0.4), 0.8, 0.8,
        boxstyle="round,pad=0.02",
        facecolor='lightblue',
        edgecolor='black',
        linewidth=2
    )
    ax2.add_patch(box_fbd)
    ax2.text(0, 0, f'{mass}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw rotated axes (dashed)
    ax2.plot([-3, 3], [0, 0], 'k--', alpha=0.4, linewidth=1)
    ax2.plot([0, 0], [-3, 3], 'k--', alpha=0.4, linewidth=1)
    ax2.text(3.1, 0, 'x (parallel)', fontsize=9, color='gray', va='center')
    ax2.text(0.1, 3.1, 'y (perp)', fontsize=9, color='gray')

    # Scale for arrows
    scale = 0.06

    # Normal force N (perpendicular, pointing up from surface)
    N = mg_perpendicular
    ax2.annotate('', xy=(0, 0.5 + N * scale), xytext=(0, 0.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=3))
    ax2.text(0.2, 0.5 + N * scale + 0.2, f'N = {N:.0f} N', fontsize=11, color='green', fontweight='bold')

    if show_components:
        # mg sin θ (parallel to incline, pointing down-slope = negative x)
        ax2.annotate('', xy=(-0.5 - mg_parallel * scale, 0), xytext=(-0.5, 0),
                    arrowprops=dict(arrowstyle='->', color='red', lw=3))
        ax2.text(-0.5 - mg_parallel * scale - 0.2, 0.3,
                f'mg sin{angle}°', fontsize=10, color='red', ha='right', fontweight='bold')
        ax2.text(-0.5 - mg_parallel * scale - 0.2, -0.1,
                f'= {mg_parallel:.0f} N', fontsize=10, color='red', ha='right')

        # mg cos θ (perpendicular to incline, pointing into surface = negative y)
        ax2.annotate('', xy=(0, -0.5 - mg_perpendicular * scale), xytext=(0, -0.5),
                    arrowprops=dict(arrowstyle='->', color='orange', lw=3))
        ax2.text(0.2, -0.5 - mg_perpendicular * scale - 0.1,
                f'mg cos{angle}°', fontsize=10, color='orange', fontweight='bold')
        ax2.text(0.2, -0.5 - mg_perpendicular * scale - 0.5,
                f'= {mg_perpendicular:.0f} N', fontsize=10, color='orange')

        # Summary box
        a = mg_parallel / mass
        summary = f"""SUMMARY:

y-axis: N = mg cos{angle}° = {N:.0f} N
        (cancel each other, no motion)

x-axis: F_net = mg sin{angle}° = {mg_parallel:.0f} N
        (net force down the slope)

a = F/m = {mg_parallel:.0f}/{mass} = {a:.1f} m/s²"""

        ax2.text(-3.3, -3.3, summary, fontsize=9, verticalalignment='top',
                family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='gray'))
    else:
        # Show mg straight down (before decomposition)
        ax2.annotate('', xy=(0.8, -0.5 - mg * scale * 0.5), xytext=(0.8, -0.5),
                    arrowprops=dict(arrowstyle='->', color='red', lw=3))
        ax2.text(1.0, -0.5 - mg * scale * 0.3, f'mg = {mg:.0f} N', fontsize=11, color='red', fontweight='bold')

    plt.tight_layout()

    # Save
    filename = f'learning-notes/fbd_incline_{angle}deg.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {filename}")
    print(f"   Mass: {mass} kg, Angle: {angle}°")
    print(f"   mg = {mg} N")
    print(f"   mg sin{angle}° = {mg_parallel:.1f} N (down slope)")
    print(f"   mg cos{angle}° = {mg_perpendicular:.1f} N (into surface)")
    print(f"   N = {mg_perpendicular:.1f} N")
    print(f"   a = {mg_parallel/mass:.2f} m/s²")

    plt.close()  # Close instead of show (for CLI)
    return filename


def draw_two_blocks_rope(
    mass_A=2,         # kg (front block, being pulled)
    mass_B=3,         # kg (back block)
    F_pull=10,        # N (pulling force on A)
    figsize=(12, 8)
):
    """
    Draw FBD for two blocks connected by rope on frictionless surface
    """
    fig, axes = plt.subplots(2, 2, figsize=figsize)

    total_mass = mass_A + mass_B
    a = F_pull / total_mass  # acceleration
    T = mass_B * a           # tension (from analyzing block B)

    # === Top Left: Physical situation ===
    ax1 = axes[0, 0]
    ax1.set_xlim(-1, 8)
    ax1.set_ylim(-1, 3)
    ax1.set_aspect('equal')
    ax1.set_title('Situation: Two blocks connected by rope', fontsize=11, fontweight='bold')
    ax1.axis('off')

    # Ground
    ax1.plot([-0.5, 7.5], [0, 0], 'k-', linewidth=2)
    ax1.fill([-0.5, 7.5, 7.5, -0.5], [0, 0, -0.3, -0.3], color='tan', alpha=0.3)

    # Block B (left)
    ax1.add_patch(patches.FancyBboxPatch((1, 0.1), 1.2, 1, boxstyle="round,pad=0.02",
                  facecolor='lightcoral', edgecolor='black', linewidth=2))
    ax1.text(1.6, 0.6, f'B\n{mass_B}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # Rope
    ax1.plot([2.2, 3.3], [0.6, 0.6], 'k-', linewidth=2)
    ax1.text(2.75, 0.85, 'T', fontsize=10, fontweight='bold')

    # Block A (right)
    ax1.add_patch(patches.FancyBboxPatch((3.3, 0.1), 1.2, 1, boxstyle="round,pad=0.02",
                  facecolor='lightblue', edgecolor='black', linewidth=2))
    ax1.text(3.9, 0.6, f'A\n{mass_A}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # Pull force
    ax1.annotate('', xy=(5.5, 0.6), xytext=(4.5, 0.6),
                arrowprops=dict(arrowstyle='->', color='blue', lw=3))
    ax1.text(5.6, 0.6, f'F = {F_pull} N', fontsize=11, color='blue', fontweight='bold', va='center')

    # Motion direction
    ax1.annotate('', xy=(7, 2), xytext=(5.5, 2),
                arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax1.text(6.25, 2.3, 'motion', fontsize=10, color='purple', ha='center')

    # === Top Right: Combined system ===
    ax2 = axes[0, 1]
    ax2.set_xlim(-2, 4)
    ax2.set_ylim(-2, 2)
    ax2.set_aspect('equal')
    ax2.set_title(f'System: A+B combined (find a)', fontsize=11, fontweight='bold')
    ax2.axis('off')

    # Combined box
    ax2.add_patch(patches.FancyBboxPatch((-1, -0.5), 2, 1, boxstyle="round,pad=0.02",
                  facecolor='lightgreen', edgecolor='black', linewidth=2))
    ax2.text(0, 0, f'A+B\n{total_mass}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # F pull
    ax2.annotate('', xy=(2.2, 0), xytext=(1.1, 0),
                arrowprops=dict(arrowstyle='->', color='blue', lw=3))
    ax2.text(2.3, 0, f'F={F_pull}N', fontsize=10, color='blue', fontweight='bold', va='center')

    # Result
    ax2.text(0, -1.5, f'F = ma\n{F_pull} = {total_mass} × a\na = {a:.1f} m/s²',
            fontsize=11, ha='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # === Bottom Left: Block B alone ===
    ax3 = axes[1, 0]
    ax3.set_xlim(-2, 4)
    ax3.set_ylim(-2, 2)
    ax3.set_aspect('equal')
    ax3.set_title(f'System: B alone (find T)', fontsize=11, fontweight='bold')
    ax3.axis('off')

    # Block B
    ax3.add_patch(patches.FancyBboxPatch((-0.5, -0.4), 1, 0.8, boxstyle="round,pad=0.02",
                  facecolor='lightcoral', edgecolor='black', linewidth=2))
    ax3.text(0, 0, f'B\n{mass_B}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # Tension T (only force in x)
    ax3.annotate('', xy=(1.5, 0), xytext=(0.6, 0),
                arrowprops=dict(arrowstyle='->', color='orange', lw=3))
    ax3.text(1.6, 0, f'T=?', fontsize=11, color='orange', fontweight='bold', va='center')

    # Result
    ax3.text(0, -1.5, f'T = ma\nT = {mass_B} × {a:.1f}\nT = {T:.1f} N',
            fontsize=11, ha='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # === Bottom Right: Block A alone (verification) ===
    ax4 = axes[1, 1]
    ax4.set_xlim(-3, 4)
    ax4.set_ylim(-2, 2)
    ax4.set_aspect('equal')
    ax4.set_title(f'System: A alone (verify)', fontsize=11, fontweight='bold')
    ax4.axis('off')

    # Block A
    ax4.add_patch(patches.FancyBboxPatch((-0.5, -0.4), 1, 0.8, boxstyle="round,pad=0.02",
                  facecolor='lightblue', edgecolor='black', linewidth=2))
    ax4.text(0, 0, f'A\n{mass_A}kg', ha='center', va='center', fontsize=10, fontweight='bold')

    # Tension T (pulling back)
    ax4.annotate('', xy=(-1.5, 0), xytext=(-0.6, 0),
                arrowprops=dict(arrowstyle='->', color='orange', lw=3))
    ax4.text(-2.2, 0, f'T={T:.0f}N', fontsize=10, color='orange', fontweight='bold', va='center')

    # F pull
    ax4.annotate('', xy=(1.8, 0), xytext=(0.6, 0),
                arrowprops=dict(arrowstyle='->', color='blue', lw=3))
    ax4.text(1.9, 0, f'F={F_pull}N', fontsize=10, color='blue', fontweight='bold', va='center')

    # Result
    net_force = F_pull - T
    ax4.text(0, -1.5, f'F - T = ma\n{F_pull} - {T:.0f} = {mass_A} × a\n{net_force:.0f} = {mass_A} × {a:.1f} ✓',
            fontsize=11, ha='center', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9))

    plt.tight_layout()

    filename = 'learning-notes/fbd_two_blocks.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {filename}")
    print(f"   Mass A: {mass_A} kg, Mass B: {mass_B} kg")
    print(f"   Pull force F: {F_pull} N")
    print(f"   Acceleration a: {a:.2f} m/s²")
    print(f"   Tension T: {T:.2f} N")

    plt.close()
    return filename


# === MAIN ===
if __name__ == "__main__":
    print("=" * 50)
    print("🎯 Physics FBD Visualizer")
    print("=" * 50)

    print("\n1. Inclined Plane (30°)")
    draw_inclined_plane_fbd(mass=4, angle=30, show_components=True)

    print("\n2. Two Blocks with Rope")
    draw_two_blocks_rope(mass_A=2, mass_B=3, F_pull=10)

    print("\n" + "=" * 50)
    print("Done! Check learning-notes/ folder for PNG files")
    print("=" * 50)
