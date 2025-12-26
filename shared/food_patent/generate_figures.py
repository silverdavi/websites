#!/usr/bin/env python3
"""
Generate USPTO-style patent figures for HTAS (Hydro-Thermal Agitation System).
BLACK AND WHITE LINE DRAWINGS ONLY - Letter size (8.5 x 11 inches).

Run: python generate_figures.py
Output: fig1.pdf through fig5.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc, Wedge, Rectangle
import numpy as np

# USPTO style: black and white only, Letter size
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.5

# Letter size in inches
LETTER_WIDTH = 8.5
LETTER_HEIGHT = 11


def add_box(ax, x, y, w, h, text, fontsize=9, bold=False, hatch=None):
    """Add a labeled box (white fill, black outline)."""
    box = FancyBboxPatch((x, y), w, h, 
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='white', edgecolor='black', linewidth=1.5,
                          hatch=hatch)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
            fontsize=fontsize, weight=weight, wrap=True)


def add_arrow(ax, start, end, style='->', lw=1.5, linestyle='-'):
    """Add a black arrow between two points."""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color='black', lw=lw, linestyle=linestyle))


def add_label(ax, x, y, text, fontsize=8, ha='center'):
    """Add a text label."""
    ax.text(x, y, text, ha=ha, va='center', fontsize=fontsize)


def add_ref_num(ax, x, y, num, fontsize=8):
    """Add a reference number with circle."""
    circle = plt.Circle((x, y), 0.15, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(circle)
    ax.text(x, y, str(num), ha='center', va='center', fontsize=fontsize, weight='bold')


def create_figure():
    """Create a Letter-sized figure (8.5 x 11 inches exactly)."""
    fig, ax = plt.subplots(1, 1, figsize=(LETTER_WIDTH, LETTER_HEIGHT))
    # Set margins for proper Letter page
    fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05)
    return fig, ax


def save_figure(name):
    """Save figure as exact Letter size PDF (8.5 x 11 inches)."""
    # Save PDF with exact figure size (no cropping)
    plt.savefig(f'{name}.pdf', format='pdf', dpi=300, pad_inches=0)
    # Save PNG for preview
    plt.savefig(f'{name}.png', dpi=150, pad_inches=0)
    plt.close()
    print(f"Created: {name}.pdf")


# ============================================================================
# FIG. 1: System Cross-Section (Apparatus Overview)
# ============================================================================
def fig1_system_cross_section():
    fig, ax = create_figure()
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(4.25, 10.5, 'FIG. 1', ha='center', fontsize=14, weight='bold')
    
    # Outer housing (resonant cavity) - dashed outline
    housing = FancyBboxPatch((1, 1.5), 6.5, 7.5, 
                              boxstyle="round,pad=0.02,rounding_size=0.2",
                              facecolor='white', edgecolor='black', 
                              linewidth=2, linestyle='--')
    ax.add_patch(housing)
    ax.text(4.25, 8.7, 'Resonant Cavity (100)', fontsize=9, ha='center')
    
    # Magnetron (microwave source) - top left
    add_box(ax, 1.3, 7.8, 1.5, 0.7, 'Magnetron\n(10)', fontsize=8)
    
    # Waveguide
    waveguide = Rectangle((2.8, 7.95), 1.0, 0.4, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(waveguide)
    ax.text(3.3, 8.15, '12', fontsize=7, ha='center', weight='bold')
    
    # Cooking vessel (cylindrical cross-section)
    vessel_left = Rectangle((2.5, 2.2), 0.12, 4.5, facecolor='white', edgecolor='black', lw=1.5)
    vessel_right = Rectangle((5.88, 2.2), 0.12, 4.5, facecolor='white', edgecolor='black', lw=1.5)
    # Conical bottom
    vessel_bottom = plt.Polygon([[2.5, 2.2], [2.62, 1.8], [5.88, 1.8], [6.0, 2.2]], 
                                 facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(vessel_left)
    ax.add_patch(vessel_right)
    ax.add_patch(vessel_bottom)
    add_ref_num(ax, 2.0, 4.5, 20)
    
    # Food mass (granules) - stippled pattern
    food = Rectangle((2.75, 2.0), 3.0, 2.5, facecolor='white', edgecolor='black', 
                      lw=1, linestyle=':')
    ax.add_patch(food)
    # Add granule dots
    np.random.seed(42)
    for _ in range(30):
        gx = np.random.uniform(2.85, 5.65)
        gy = np.random.uniform(2.1, 4.3)
        ax.plot(gx, gy, 'ko', markersize=1.5)
    ax.text(4.25, 3.2, 'Food Mass', fontsize=7, ha='center')
    
    # Circumferential manifold (ring at top of vessel)
    manifold_left = plt.Circle((2.7, 6.5), 0.18, facecolor='white', edgecolor='black', lw=1.5)
    manifold_right = plt.Circle((5.8, 6.5), 0.18, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(manifold_left)
    ax.add_patch(manifold_right)
    add_ref_num(ax, 1.9, 6.5, 30)
    
    # Water droplets / falling film (dashed lines)
    for y_pos in [6.2, 5.8, 5.4, 5.0, 4.6]:
        ax.plot(2.65, y_pos, 'k.', markersize=3)
        ax.plot(5.85, y_pos, 'k.', markersize=3)
    ax.plot([2.65, 2.65], [6.3, 4.5], 'k--', lw=0.8)
    ax.plot([5.85, 5.85], [6.3, 4.5], 'k--', lw=0.8)
    
    # Agitator drive (outside cavity, top)
    drive_housing = FancyBboxPatch((3.5, 9.0), 1.5, 0.7, 
                                    boxstyle="round,pad=0.01,rounding_size=0.1",
                                    facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(drive_housing)
    ax.text(4.25, 9.35, 'Drive (40)', fontsize=7, ha='center', weight='bold')
    
    # Drive shaft
    shaft = Rectangle((4.15, 4.5), 0.2, 4.5, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(shaft)
    add_ref_num(ax, 4.8, 6.0, 42)
    
    # Fork/tine tool head
    tine_base = Rectangle((3.5, 4.3), 1.5, 0.2, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(tine_base)
    for tx in [3.6, 3.9, 4.2, 4.5, 4.8]:
        tine = Rectangle((tx, 2.6), 0.08, 1.7, facecolor='white', edgecolor='black', lw=1)
        ax.add_patch(tine)
    add_ref_num(ax, 5.5, 3.5, 44)
    
    # Motion arrows (vertical reciprocation)
    ax.annotate('', xy=(5.2, 5.5), xytext=(5.2, 4.8),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(5.6, 5.15, 'Z', fontsize=8)
    add_ref_num(ax, 6.0, 5.15, 50)
    
    # Rotation arrow
    arc = Arc((4.25, 4.5), 0.8, 0.4, angle=0, theta1=30, theta2=330, color='black', lw=1.5)
    ax.add_patch(arc)
    ax.text(4.25, 4.85, 'θ', fontsize=8, ha='center')
    add_ref_num(ax, 4.9, 4.85, 52)
    
    # IR sensor array (top) - small rectangles
    for sx in [3.2, 3.8, 4.4, 5.0]:
        sensor = Rectangle((sx, 7.3), 0.2, 0.12, facecolor='white', edgecolor='black', lw=1)
        ax.add_patch(sensor)
    add_ref_num(ax, 6.0, 7.36, 60)
    
    # Peltier / cooling element (bottom)
    peltier = Rectangle((2.8, 1.4), 2.9, 0.25, facecolor='white', edgecolor='black', lw=1.5, hatch='///')
    ax.add_patch(peltier)
    add_ref_num(ax, 6.2, 1.52, 70)
    
    # Reference legend
    ax.text(7.0, 8.5, 'Ref:', fontsize=8, weight='bold', ha='left')
    legend_items = [
        ('10', 'Magnetron'),
        ('12', 'Waveguide'),
        ('20', 'Vessel'),
        ('30', 'Manifold'),
        ('40', 'Drive Unit'),
        ('42', 'Shaft'),
        ('44', 'Tool Head'),
        ('50', 'Z-Axis'),
        ('52', 'θ-Axis'),
        ('60', 'IR Sensors'),
        ('70', 'Peltier'),
    ]
    for i, (num, desc) in enumerate(legend_items):
        ax.text(7.0, 8.1 - i*0.35, f'{num}: {desc}', fontsize=6, ha='left')
    
    save_figure('fig1_cross_section')


# ============================================================================
# FIG. 2: Circumferential Manifold Detail
# ============================================================================
def fig2_manifold_detail():
    fig, ax = create_figure()
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    ax.text(4.25, 10.5, 'FIG. 2', ha='center', fontsize=14, weight='bold')
    
    # Top-down view (plan view) - left side
    ax.text(2.5, 9.5, 'A. Plan View', fontsize=10, ha='center', weight='bold')
    
    # Vessel outline (circle)
    vessel_circle = plt.Circle((2.5, 6.5), 2.0, facecolor='white', edgecolor='black', lw=2)
    ax.add_patch(vessel_circle)
    
    # Manifold ring (outer circle)
    manifold_outer = plt.Circle((2.5, 6.5), 2.2, facecolor='none', edgecolor='black', lw=2)
    ax.add_patch(manifold_outer)
    
    # Nozzles (8 positions around the ring)
    for angle in range(0, 360, 45):
        rad = np.radians(angle)
        nx = 2.5 + 2.2 * np.cos(rad)
        ny = 6.5 + 2.2 * np.sin(rad)
        nozzle = plt.Circle((nx, ny), 0.1, facecolor='black', edgecolor='black', lw=1)
        ax.add_patch(nozzle)
        # Spray direction arrows (inward, angled)
        inner_rad = np.radians(angle + 15)
        tx = 2.5 + 1.6 * np.cos(inner_rad)
        ty = 6.5 + 1.6 * np.sin(inner_rad)
        ax.annotate('', xy=(tx, ty), xytext=(nx, ny),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1))
    
    ax.text(2.5, 6.5, 'Food\nBed', fontsize=8, ha='center')
    add_ref_num(ax, 2.5, 4.0, 30)
    
    # Cross-section detail - right side
    ax.text(6.5, 9.5, 'B. Nozzle Detail', fontsize=10, ha='center', weight='bold')
    
    # Vessel wall (vertical)
    wall = Rectangle((5.2, 4.5), 0.25, 4.0, facecolor='white', edgecolor='black', lw=1.5, hatch='|||')
    ax.add_patch(wall)
    ax.text(4.8, 6.5, 'Wall', fontsize=7, ha='center', rotation=90)
    
    # Manifold tube (cross-section)
    manifold_tube = plt.Circle((6.0, 8.2), 0.25, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(manifold_tube)
    ax.text(6.6, 8.2, 'Tube', fontsize=7, ha='left')
    
    # Nozzle with angle
    nozzle_start = (5.85, 8.0)
    nozzle_end = (5.5, 7.4)
    ax.plot([nozzle_start[0], nozzle_end[0]], [nozzle_start[1], nozzle_end[1]], 'k-', lw=2)
    ax.plot(nozzle_end[0], nozzle_end[1], 'ko', markersize=4)
    
    # Angle annotation
    arc = Arc((5.85, 8.0), 0.6, 0.6, angle=0, theta1=220, theta2=270, color='black', lw=1.5)
    ax.add_patch(arc)
    ax.text(5.4, 7.8, 'θ=20°', fontsize=7)
    
    # Falling film (water flow) - dashed line with dots
    for y in [7.1, 6.6, 6.1, 5.6, 5.1]:
        ax.plot(5.35, y, 'ko', markersize=4)
    ax.plot([5.35, 5.35], [7.2, 4.8], 'k--', lw=1)
    ax.text(5.6, 5.8, 'Falling\nFilm', fontsize=7, ha='left')
    
    # Food bed (right side) - dotted outline
    food_bed = plt.Polygon([[5.6, 4.5], [5.6, 6.0], [7.8, 6.0], [7.8, 4.5]], 
                           facecolor='white', edgecolor='black', lw=1, linestyle=':')
    ax.add_patch(food_bed)
    ax.text(6.7, 5.25, 'Granule\nBed', fontsize=7, ha='center')
    
    # Hydration arrow (radial inward)
    ax.annotate('', xy=(7.5, 5.25), xytext=(5.8, 5.25),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax.text(6.6, 4.8, 'Centripetal\nHydration', fontsize=7, ha='center')
    
    save_figure('fig2_manifold')


# ============================================================================
# FIG. 3: Agitation Assembly and Motion Modes
# ============================================================================
def fig3_agitator():
    fig, ax = create_figure()
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    ax.text(4.25, 10.5, 'FIG. 3', ha='center', fontsize=14, weight='bold')
    
    # Left: Physical assembly
    ax.text(2.5, 9.8, 'A. Assembly', fontsize=10, ha='center', weight='bold')
    
    # Drive housing
    drive = FancyBboxPatch((1.5, 8.5), 2, 0.8, 
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(drive)
    ax.text(2.5, 8.9, 'Drive Unit', fontsize=8, ha='center')
    
    # Linear actuator symbol
    actuator = Rectangle((2.2, 7.4), 0.6, 1.0, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(actuator)
    ax.text(2.5, 7.9, 'LA', fontsize=7, ha='center', weight='bold')
    
    # Rotary motor symbol
    motor_circle = plt.Circle((2.5, 8.2), 0.15, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(motor_circle)
    
    # Shaft
    shaft = Rectangle((2.4, 4.0), 0.2, 3.4, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(shaft)
    add_ref_num(ax, 3.2, 5.5, 42)
    
    # Tool head base
    head_base = Rectangle((1.6, 3.8), 1.8, 0.2, facecolor='white', edgecolor='black', lw=1)
    ax.add_patch(head_base)
    
    # Tines
    for tx in [1.7, 2.1, 2.5, 2.9, 3.3]:
        tine = Rectangle((tx, 2.5), 0.1, 1.3, facecolor='white', edgecolor='black', lw=1)
        ax.add_patch(tine)
    add_ref_num(ax, 4.0, 3.2, 44)
    
    # Motion arrows
    ax.annotate('', xy=(3.8, 6.0), xytext=(3.8, 5.0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(4.2, 5.5, 'Z (0-5 Hz)', fontsize=7)
    
    # Rotation
    arc = Arc((2.5, 4.0), 1.2, 0.6, angle=0, theta1=30, theta2=330, color='black', lw=1.5)
    ax.add_patch(arc)
    ax.text(2.5, 4.4, 'θ (0-30 RPM)', fontsize=7, ha='center')
    
    # Right: Operating modes
    ax.text(6.5, 9.8, 'B. Operating Modes', fontsize=10, ha='center', weight='bold')
    
    modes = [
        ('Mode A:\nTumble/Coat', 'Slow θ\nMinimal Z'),
        ('Mode B:\nDe-agglomerate', 'High-freq Z\n(3-5 Hz)'),
        ('Mode C:\nLift/Fluff', 'Dip-Twist-Lift\nCycle'),
    ]
    
    for i, (mode_name, desc) in enumerate(modes):
        y_pos = 8.0 - i * 1.8
        add_box(ax, 5.0, y_pos, 1.5, 1.2, mode_name, fontsize=7, bold=True)
        add_box(ax, 6.7, y_pos, 1.5, 1.2, desc, fontsize=6)
        add_arrow(ax, (6.5, y_pos + 0.6), (6.7, y_pos + 0.6))
    
    # Mode C detail (small diagram)
    ax.text(6.0, 3.5, 'Mode C Cycle:', fontsize=7, weight='bold')
    cycle_steps = ['Dip', 'Twist', 'Lift']
    for j, step in enumerate(cycle_steps):
        ax.text(5.0 + j*1.2, 3.0, step, fontsize=8, ha='center')
        if j < 2:
            ax.annotate('', xy=(5.5 + j*1.2, 3.0), xytext=(5.2 + j*1.2, 3.0),
                        arrowprops=dict(arrowstyle='->', color='black', lw=1))
    
    save_figure('fig3_agitator')


# ============================================================================
# FIG. 4: Control Algorithm Flowchart
# ============================================================================
def fig4_algorithm():
    fig, ax = create_figure()
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    ax.text(4.25, 10.5, 'FIG. 4', ha='center', fontsize=14, weight='bold')
    
    # Define box dimensions
    phase_w, phase_h = 1.8, 0.9
    detail_w, detail_h = 1.6, 0.9
    
    # Start circle
    start = plt.Circle((2.4, 9.5), 0.25, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(start)
    ax.text(2.4, 9.5, 'Start', ha='center', va='center', fontsize=8)
    
    # Phase 1
    p1_x, p1_y = 1.5, 8.0
    add_box(ax, p1_x, p1_y, phase_w, phase_h, 'PHASE 1\nLipid Intercalation', fontsize=7, bold=True)
    add_box(ax, p1_x + phase_w + 0.2, p1_y, detail_w, detail_h, 'Oil coating\nMode A\nMW 10%', fontsize=6)
    
    # Phase 2
    p2_x, p2_y = 1.5, 6.6
    add_box(ax, p2_x, p2_y, phase_w, phase_h, 'PHASE 2\nGradient Hydration', fontsize=7, bold=True)
    add_box(ax, p2_x + phase_w + 0.2, p2_y, detail_w, detail_h, 'Perimeter inject\nMode B (2 Hz)\nMW 50%', fontsize=6)
    
    # Phase 3
    p3_x, p3_y = 1.5, 5.2
    add_box(ax, p3_x, p3_y, phase_w, phase_h, 'PHASE 3\nGelatinization', fontsize=7, bold=True)
    add_box(ax, p3_x + phase_w + 0.2, p3_y, detail_w, detail_h, 'Hold 98°C\nMode C (Fluff)\nIR monitor', fontsize=6)
    
    # Phase 4
    p4_x, p4_y = 1.5, 3.8
    add_box(ax, p4_x, p4_y, phase_w, phase_h, 'PHASE 4\nRetrogradation', fontsize=7, bold=True)
    add_box(ax, p4_x + phase_w + 0.2, p4_y, detail_w, detail_h, 'MW OFF, Cool\nMax Z (5 Hz)\nCool to 45°C', fontsize=6)
    
    # Arrows between phases (center of boxes)
    phase_center_x = p1_x + phase_w / 2
    add_arrow(ax, (2.4, 9.25), (phase_center_x, p1_y + phase_h))  # Start -> Phase 1
    add_arrow(ax, (phase_center_x, p1_y), (phase_center_x, p2_y + phase_h))
    add_arrow(ax, (phase_center_x, p2_y), (phase_center_x, p3_y + phase_h))
    add_arrow(ax, (phase_center_x, p3_y), (phase_center_x, p4_y + phase_h))
    
    # End circle below Phase 4
    end = plt.Circle((phase_center_x, 3.0), 0.25, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(end)
    ax.text(phase_center_x, 3.0, 'Done', ha='center', va='center', fontsize=8)
    add_arrow(ax, (phase_center_x, p4_y), (phase_center_x, 3.25))
    
    # === Sensor Feedback Loop (right side) ===
    ax.text(6.8, 9.5, 'Closed-Loop Control', fontsize=9, weight='bold', ha='center')
    
    # Sensor boxes
    sensor_y = 8.3
    add_box(ax, 5.6, sensor_y, 1.1, 0.6, 'IR Temp\nMatrix', fontsize=6)
    add_box(ax, 6.9, sensor_y, 1.1, 0.6, 'Torque\nSensor', fontsize=6)
    
    # Controller box
    ctrl_x, ctrl_y, ctrl_w, ctrl_h = 6.0, 7.0, 1.5, 0.7
    add_box(ax, ctrl_x, ctrl_y, ctrl_w, ctrl_h, 'Control Unit', fontsize=7, bold=True)
    
    # Arrows from sensors to controller
    add_arrow(ax, (6.15, sensor_y), (6.5, ctrl_y + ctrl_h))
    add_arrow(ax, (7.45, sensor_y), (7.2, ctrl_y + ctrl_h))
    
    # Decision diamond
    diamond_cx, diamond_cy = 6.75, 5.8
    diamond_size = 0.45
    diamond_points = [
        [diamond_cx, diamond_cy + diamond_size],
        [diamond_cx + diamond_size, diamond_cy],
        [diamond_cx, diamond_cy - diamond_size],
        [diamond_cx - diamond_size, diamond_cy],
    ]
    diamond = plt.Polygon(diamond_points, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(diamond)
    ax.text(diamond_cx, diamond_cy, 'Clump?', fontsize=6, ha='center', va='center')
    
    # Arrow from controller to diamond
    add_arrow(ax, (ctrl_x + ctrl_w/2, ctrl_y), (diamond_cx, diamond_cy + diamond_size))
    
    # Yes path -> action box
    action_x, action_y = 7.0, 4.8
    add_box(ax, action_x, action_y, 1.0, 0.5, 'Increase\nAgitation', fontsize=6)
    add_arrow(ax, (diamond_cx + diamond_size, diamond_cy), (action_x, action_y + 0.25))
    ax.text(diamond_cx + diamond_size + 0.1, diamond_cy + 0.15, 'Yes', fontsize=6)
    
    # Loop back from action to controller
    ax.annotate('', xy=(ctrl_x + ctrl_w, ctrl_y + ctrl_h/2), xytext=(action_x + 0.5, action_y + 0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1,
                               connectionstyle='arc3,rad=0.3'))
    
    # No path -> back to phases (dashed line)
    ax.text(diamond_cx - diamond_size - 0.1, diamond_cy + 0.15, 'No', fontsize=6, ha='right')
    ax.annotate('', xy=(p3_x + phase_w + 0.2 + detail_w + 0.15, p3_y + detail_h/2), 
                xytext=(diamond_cx - diamond_size, diamond_cy),
                arrowprops=dict(arrowstyle='->', color='black', lw=1, linestyle='--'))
    
    save_figure('fig4_algorithm')


# ============================================================================
# FIG. 5: Closed-Loop Sensor Control System
# ============================================================================
def fig5_sensor_control():
    fig, ax = create_figure()
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    ax.text(4.25, 10.5, 'FIG. 5', ha='center', fontsize=14, weight='bold')
    
    # Main control loop diagram
    # Setpoint
    add_box(ax, 0.5, 6.5, 1.0, 0.7, 'Setpoint\n(Recipe)', fontsize=6)
    
    # Summing junction
    sum_circle = plt.Circle((2.0, 6.85), 0.2, facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(sum_circle)
    ax.text(2.0, 6.85, 'Σ', fontsize=10, ha='center', va='center')
    
    # Controller
    add_box(ax, 2.5, 6.5, 1.1, 0.7, 'PID\nController', fontsize=6, bold=True)
    
    # Actuators
    add_box(ax, 4.0, 7.5, 1.0, 0.6, 'Magnetron', fontsize=6)
    add_box(ax, 4.0, 6.5, 1.0, 0.6, 'Manifold', fontsize=6)
    add_box(ax, 4.0, 5.5, 1.0, 0.6, 'Agitator', fontsize=6)
    
    # Process (plant)
    add_box(ax, 5.5, 6.0, 1.5, 1.5, 'PROCESS\n(Food Mass)', fontsize=7, bold=True)
    
    # Sensors
    add_box(ax, 7.3, 7.5, 1.0, 0.6, 'IR Matrix\n(Temp)', fontsize=5)
    add_box(ax, 7.3, 6.5, 1.0, 0.6, 'Torque\n(Viscosity)', fontsize=5)
    add_box(ax, 7.3, 5.5, 1.0, 0.6, 'Humidity\n(Steam)', fontsize=5)
    
    # Arrows - forward path
    add_arrow(ax, (1.5, 6.85), (1.8, 6.85))
    add_arrow(ax, (2.2, 6.85), (2.5, 6.85))
    add_arrow(ax, (3.6, 6.85), (4.0, 7.8))
    add_arrow(ax, (3.6, 6.85), (4.0, 6.8))
    add_arrow(ax, (3.6, 6.85), (4.0, 5.8))
    add_arrow(ax, (5.0, 7.8), (5.5, 7.2))
    add_arrow(ax, (5.0, 6.8), (5.5, 6.75))
    add_arrow(ax, (5.0, 5.8), (5.5, 6.3))
    
    # Arrows - to sensors
    add_arrow(ax, (7.0, 7.2), (7.3, 7.8))
    add_arrow(ax, (7.0, 6.75), (7.3, 6.8))
    add_arrow(ax, (7.0, 6.3), (7.3, 5.8))
    
    # Feedback path
    ax.plot([7.8, 7.8], [5.5, 5.0], 'k-', lw=1.5)
    ax.plot([7.8, 2.0], [5.0, 5.0], 'k-', lw=1.5)
    ax.plot([2.0, 2.0], [5.0, 6.65], 'k-', lw=1.5)
    ax.annotate('', xy=(2.0, 6.65), xytext=(2.0, 5.0),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.text(4.9, 4.7, 'Feedback Signal', fontsize=7, ha='center')
    
    # Labels
    ax.text(1.85, 7.15, '-', fontsize=12)
    ax.text(2.15, 6.6, '+', fontsize=10)
    
    # Torque curve inset (bottom)
    ax.text(2.0, 3.5, 'Torque Profile During Cooking:', fontsize=8, weight='bold')
    
    # Axes
    ax.plot([1.0, 7.0], [1.5, 1.5], 'k-', lw=1)  # X-axis
    ax.plot([1.0, 1.0], [1.5, 3.2], 'k-', lw=1)  # Y-axis
    ax.text(4.0, 1.1, 'Time →', fontsize=7, ha='center')
    ax.text(0.7, 2.35, 'Torque', fontsize=7, ha='center', rotation=90)
    
    # Torque curve
    t = np.linspace(0, 6, 100)
    # Phase 1: low, Phase 2: rising, Phase 3: peak then stable, Phase 4: dropping
    torque = np.piecewise(t, 
        [t < 1.5, (t >= 1.5) & (t < 3), (t >= 3) & (t < 4.5), t >= 4.5],
        [lambda x: 0.3, 
         lambda x: 0.3 + 0.8*(x-1.5)/1.5, 
         lambda x: 1.1 - 0.3*(x-3)/1.5,
         lambda x: 0.8 - 0.3*(x-4.5)/1.5])
    ax.plot(1.0 + t, 1.5 + torque, 'k-', lw=1.5)
    
    # Phase labels
    ax.text(1.75, 2.0, 'Ph.1', fontsize=6, ha='center')
    ax.text(3.25, 2.6, 'Ph.2', fontsize=6, ha='center')
    ax.text(4.75, 2.4, 'Ph.3', fontsize=6, ha='center')
    ax.text(6.25, 2.1, 'Ph.4', fontsize=6, ha='center')
    
    # Phase boundaries (dashed vertical lines)
    for x_pos in [2.5, 4.0, 5.5]:
        ax.plot([x_pos, x_pos], [1.5, 3.0], 'k--', lw=0.5)
    
    save_figure('fig5_sensor_control')


# ============================================================================
# Generate All Figures
# ============================================================================
if __name__ == '__main__':
    print("Generating USPTO patent figures (B&W, Letter size)...")
    print("-" * 50)
    
    fig1_system_cross_section()
    fig2_manifold_detail()
    fig3_agitator()
    fig4_algorithm()
    fig5_sensor_control()
    
    print("-" * 50)
    print("Done! Files created:")
    print("  - fig1_cross_section.pdf  (System Overview)")
    print("  - fig2_manifold.pdf       (Fluid Distribution)")
    print("  - fig3_agitator.pdf       (Agitation Assembly)")
    print("  - fig4_algorithm.pdf      (Process Control)")
    print("  - fig5_sensor_control.pdf (Closed-Loop Control)")
    print("\nAll figures: BLACK & WHITE, Letter size (8.5 x 11 in)")
    print("\nCombine into single PDF with:")
    print("  pdftk fig*.pdf cat output DRAWINGS.pdf")
