"""
Flowchart — Simple flow diagrams
Using Matplotlib for static visualizations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import List, Tuple, Optional, Dict


# =============================================================================
# FLOWCHART ELEMENTS
# =============================================================================

def _draw_box(ax, x, y, text, box_type="process", width=2, height=0.8):
    """Draw a flowchart box"""
    colors = {
        "start": ("#90EE90", "green"),       # Light green
        "end": ("#FFB6C1", "red"),           # Light pink
        "process": ("#ADD8E6", "blue"),       # Light blue
        "decision": ("#FFFACD", "orange"),    # Lemon
        "io": ("#E6E6FA", "purple"),          # Lavender
    }

    fill_color, edge_color = colors.get(box_type, colors["process"])

    if box_type == "decision":
        # Diamond shape
        diamond = patches.FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.05",
            facecolor=fill_color,
            edgecolor=edge_color,
            linewidth=2,
            transform=ax.transData
        )
        # Actually draw a diamond using polygon
        diamond_pts = [
            (x, y + height/2),      # top
            (x + width/2, y),       # right
            (x, y - height/2),      # bottom
            (x - width/2, y),       # left
        ]
        diamond = patches.Polygon(diamond_pts, closed=True,
                                  facecolor=fill_color, edgecolor=edge_color, linewidth=2)
        ax.add_patch(diamond)
    elif box_type in ["start", "end"]:
        # Rounded rectangle (stadium)
        box = patches.FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.1,rounding_size=0.4",
            facecolor=fill_color,
            edgecolor=edge_color,
            linewidth=2
        )
        ax.add_patch(box)
    elif box_type == "io":
        # Parallelogram
        skew = 0.3
        pts = [
            (x - width/2 + skew, y + height/2),
            (x + width/2 + skew, y + height/2),
            (x + width/2 - skew, y - height/2),
            (x - width/2 - skew, y - height/2),
        ]
        para = patches.Polygon(pts, closed=True,
                              facecolor=fill_color, edgecolor=edge_color, linewidth=2)
        ax.add_patch(para)
    else:
        # Rectangle
        box = patches.FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.05",
            facecolor=fill_color,
            edgecolor=edge_color,
            linewidth=2
        )
        ax.add_patch(box)

    # Text
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')

    return (x, y)


def _draw_arrow(ax, start, end, label="", curved=False):
    """Draw arrow between two points"""
    if curved:
        style = "arc3,rad=0.3"
    else:
        style = "-"

    ax.annotate(
        '', xy=end, xytext=start,
        arrowprops=dict(
            arrowstyle='->',
            color='black',
            lw=1.5,
            connectionstyle=style
        )
    )

    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x + 0.2, mid_y, label, fontsize=9, color='gray')


# =============================================================================
# SIMPLE FLOWCHART
# =============================================================================

def draw_simple_flowchart(
    steps: List[Tuple[str, str]],  # (text, type) - types: start, end, process, decision, io
    title: str = "Flowchart",
    figsize: Tuple[int, int] = (8, 12),
    filename: Optional[str] = None
):
    """
    Draw a simple vertical flowchart

    Example:
        draw_simple_flowchart([
            ("Start", "start"),
            ("Input x", "io"),
            ("x > 0?", "decision"),
            ("Print positive", "process"),
            ("End", "end"),
        ])
    """
    fig, ax = plt.subplots(figsize=figsize)

    n = len(steps)
    spacing = 1.5
    start_y = (n - 1) * spacing / 2

    positions = []
    for i, (text, box_type) in enumerate(steps):
        y = start_y - i * spacing
        pos = _draw_box(ax, 0, y, text, box_type)
        positions.append(pos)

    # Draw arrows
    for i in range(len(positions) - 1):
        start = (positions[i][0], positions[i][1] - 0.4)
        end = (positions[i+1][0], positions[i+1][1] + 0.4)
        _draw_arrow(ax, start, end)

    # Set limits
    ax.set_xlim(-3, 3)
    ax.set_ylim(-start_y - 2, start_y + 2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def draw_decision_flowchart(
    before_decision: List[Tuple[str, str]],
    decision_text: str,
    yes_branch: List[Tuple[str, str]],
    no_branch: List[Tuple[str, str]],
    after_merge: List[Tuple[str, str]] = [],
    title: str = "Decision Flowchart",
    figsize: Tuple[int, int] = (12, 10),
    filename: Optional[str] = None
):
    """
    Draw flowchart with decision branching

    Example:
        draw_decision_flowchart(
            before_decision=[("Start", "start"), ("Input x", "io")],
            decision_text="x > 0?",
            yes_branch=[("Positive", "process")],
            no_branch=[("Negative", "process")],
            after_merge=[("End", "end")]
        )
    """
    fig, ax = plt.subplots(figsize=figsize)

    spacing_y = 1.5
    spacing_x = 3
    current_y = 4

    positions = {}

    # Before decision
    for i, (text, box_type) in enumerate(before_decision):
        pos = _draw_box(ax, 0, current_y, text, box_type)
        positions[f"before_{i}"] = pos
        if i > 0:
            prev = positions[f"before_{i-1}"]
            _draw_arrow(ax, (prev[0], prev[1] - 0.4), (pos[0], pos[1] + 0.4))
        current_y -= spacing_y

    # Decision
    decision_pos = _draw_box(ax, 0, current_y, decision_text, "decision", height=1)
    positions["decision"] = decision_pos
    if before_decision:
        prev = positions[f"before_{len(before_decision)-1}"]
        _draw_arrow(ax, (prev[0], prev[1] - 0.4), (decision_pos[0], decision_pos[1] + 0.5))

    current_y -= spacing_y

    # Yes branch (right)
    yes_y = current_y
    for i, (text, box_type) in enumerate(yes_branch):
        pos = _draw_box(ax, spacing_x, yes_y, text, box_type)
        positions[f"yes_{i}"] = pos
        if i == 0:
            _draw_arrow(ax, (decision_pos[0] + 1, decision_pos[1]), (pos[0] - 1, pos[1]), label="Yes")
        else:
            prev = positions[f"yes_{i-1}"]
            _draw_arrow(ax, (prev[0], prev[1] - 0.4), (pos[0], pos[1] + 0.4))
        yes_y -= spacing_y

    # No branch (left)
    no_y = current_y
    for i, (text, box_type) in enumerate(no_branch):
        pos = _draw_box(ax, -spacing_x, no_y, text, box_type)
        positions[f"no_{i}"] = pos
        if i == 0:
            _draw_arrow(ax, (decision_pos[0] - 1, decision_pos[1]), (pos[0] + 1, pos[1]), label="No")
        else:
            prev = positions[f"no_{i-1}"]
            _draw_arrow(ax, (prev[0], prev[1] - 0.4), (pos[0], pos[1] + 0.4))
        no_y -= spacing_y

    # After merge
    merge_y = min(yes_y, no_y) - spacing_y / 2
    for i, (text, box_type) in enumerate(after_merge):
        pos = _draw_box(ax, 0, merge_y, text, box_type)
        positions[f"after_{i}"] = pos

        if i == 0:
            # Connect from both branches
            if yes_branch:
                last_yes = positions[f"yes_{len(yes_branch)-1}"]
                ax.plot([last_yes[0], last_yes[0], pos[0]],
                       [last_yes[1] - 0.4, merge_y + 0.8, merge_y + 0.8], 'k-', lw=1.5)
            if no_branch:
                last_no = positions[f"no_{len(no_branch)-1}"]
                ax.plot([last_no[0], last_no[0], pos[0]],
                       [last_no[1] - 0.4, merge_y + 0.8, merge_y + 0.8], 'k-', lw=1.5)
            ax.annotate('', xy=(pos[0], pos[1] + 0.4), xytext=(pos[0], merge_y + 0.8),
                       arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        else:
            prev = positions[f"after_{i-1}"]
            _draw_arrow(ax, (prev[0], prev[1] - 0.4), (pos[0], pos[1] + 0.4))

        merge_y -= spacing_y

    # Set limits
    ax.set_xlim(-6, 6)
    ax.set_ylim(merge_y - 1, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold')

    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
        print(f"✅ Saved: {filename}")

    plt.close()
    return fig


def draw_process_flow(
    processes: List[str],
    title: str = "Process Flow",
    horizontal: bool = True,
    figsize: Tuple[int, int] = None,
    filename: Optional[str] = None
):
    """
    Draw a simple linear process flow

    Example:
        draw_process_flow(["Step 1", "Step 2", "Step 3", "Step 4"])
    """
    n = len(processes)

    if figsize is None:
        if horizontal:
            figsize = (3 * n, 3)
        else:
            figsize = (4, 2 * n)

    fig, ax = plt.subplots(figsize=figsize)

    if horizontal:
        for i, text in enumerate(processes):
            x = i * 3
            _draw_box(ax, x, 0, text, "process")
            if i > 0:
                _draw_arrow(ax, ((i-1) * 3 + 1, 0), (i * 3 - 1, 0))
        ax.set_xlim(-2, (n-1) * 3 + 2)
        ax.set_ylim(-2, 2)
    else:
        for i, text in enumerate(processes):
            y = -i * 2
            _draw_box(ax, 0, y, text, "process")
            if i > 0:
                _draw_arrow(ax, (0, -(i-1) * 2 - 0.4), (0, -i * 2 + 0.4))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-(n-1) * 2 - 2, 2)

    ax.set_aspect('equal')
    ax.axis('off')
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
    print("🎯 Flowchart Demo")
    print("=" * 50)

    # 1. Simple flowchart
    print("\n1. Simple flowchart...")
    draw_simple_flowchart(
        [
            ("Start", "start"),
            ("Input x", "io"),
            ("Calculate x²", "process"),
            ("Output result", "io"),
            ("End", "end"),
        ],
        title="Simple Calculation",
        filename=f"{output_dir}/flowchart_simple.png"
    )

    # 2. Decision flowchart
    print("\n2. Decision flowchart...")
    draw_decision_flowchart(
        before_decision=[
            ("Start", "start"),
            ("Input number", "io"),
        ],
        decision_text="number > 0?",
        yes_branch=[
            ("Print 'Positive'", "process"),
        ],
        no_branch=[
            ("Print 'Non-positive'", "process"),
        ],
        after_merge=[
            ("End", "end"),
        ],
        title="Number Check",
        filename=f"{output_dir}/flowchart_decision.png"
    )

    # 3. Process flow
    print("\n3. Process flow...")
    draw_process_flow(
        ["Collect Data", "Clean Data", "Analyze", "Visualize", "Report"],
        title="Data Pipeline",
        horizontal=True,
        filename=f"{output_dir}/flowchart_process.png"
    )

    print("\n" + "=" * 50)
    print(f"✅ Done! Check {output_dir}/ for PNG files")
    print("=" * 50)
