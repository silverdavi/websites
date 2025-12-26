#!/usr/bin/env python3
"""
Generate USPTO-style patent figures for Hybrid Compute Optimization provisional application.
Creates 6 figures as PDF files suitable for patent filing.

USPTO Requirements:
- Black and white (no color)
- Clean lines, clear labels
- Element reference numbers

Run: python generate_figures.py
Output: fig1.pdf through fig6.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, ConnectionPatch
from matplotlib.patches import Rectangle
import numpy as np

# USPTO style: clean, black and white, clear labels
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['figure.facecolor'] = 'white'


def add_box(ax, x, y, w, h, text, fontsize=9, bold=False, ref_num=None, fill='white'):
    """Add a labeled box with optional reference number."""
    box = FancyBboxPatch((x, y), w, h, 
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=fill, edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
            fontsize=fontsize, weight=weight, wrap=True)
    # Reference number
    if ref_num:
        ax.text(x + w - 0.1, y + 0.1, ref_num, ha='right', va='bottom', 
                fontsize=7, weight='bold')


def add_arrow(ax, start, end, connectionstyle="arc3,rad=0", color='black', lw=1.5):
    """Add a properly aligned arrow between two points."""
    arrow = FancyArrowPatch(start, end,
                             connectionstyle=connectionstyle,
                             arrowstyle='-|>',
                             mutation_scale=12,
                             lw=lw,
                             color=color)
    ax.add_patch(arrow)


def add_label(ax, x, y, text, fontsize=8, ha='center', va='center'):
    """Add a text label."""
    ax.text(x, y, text, ha=ha, va=va, fontsize=fontsize)


# ============================================================================
# FIG. 1: System Architecture (100)
# ============================================================================
def fig1_system_architecture():
    fig, ax = plt.subplots(1, 1, figsize=(11, 8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(5.5, 7.7, 'FIG. 1', ha='center', fontsize=14, weight='bold')
    
    # === OUTER LOOP (Left side) ===
    add_box(ax, 0.3, 6, 2.4, 0.9, 'Language Model\nGenerator', fontsize=9, bold=True, ref_num='140')
    add_box(ax, 0.3, 4.8, 2.4, 0.9, 'Search\nController', fontsize=9, ref_num='150')
    
    # === CANDIDATE PATH ===
    add_box(ax, 3.5, 6, 2.2, 0.9, 'Candidate\nArtifact', fontsize=9, ref_num='142')
    
    # === HYBRID COMPUTE SUBSTRATE (Center) ===
    substrate = FancyBboxPatch((3, 2.5), 5, 3, 
                                boxstyle="round,pad=0.03,rounding_size=0.1",
                                facecolor='#f5f5f5', edgecolor='black', linewidth=2)
    ax.add_patch(substrate)
    ax.text(5.5, 5.3, 'Hybrid Compute Substrate (110)', ha='center', fontsize=10, weight='bold')
    
    # Deterministic core (112)
    add_box(ax, 3.3, 3.8, 2, 1.1, 'Deterministic\nDigital Core', fontsize=8, ref_num='112')
    
    # Under-specified element (114)
    add_box(ax, 5.7, 3.8, 2, 1.1, 'Under-Specified\nCompute Element\n(Analog/Neuro)', fontsize=7, ref_num='114')
    
    # Instrumentation (120)
    add_box(ax, 4.2, 2.7, 2.6, 0.8, 'Instrumentation\n(Power, Latency, Accuracy)', fontsize=7, ref_num='120')
    
    # === RIGHT SIDE ===
    add_box(ax, 8.5, 5, 2.2, 0.9, 'On-Device\nEvaluator', fontsize=9, ref_num='130')
    add_box(ax, 8.5, 3.5, 2.2, 0.9, 'Constraint\nEnforcer', fontsize=9, ref_num='145')
    add_box(ax, 8.5, 2, 2.2, 0.9, 'Deployment\nComponent', fontsize=9, ref_num='160')
    
    # === OUTPUT ===
    add_box(ax, 4.2, 0.5, 2.6, 0.9, 'Deployable\nArtifact', fontsize=9, bold=True, ref_num='162')
    
    # === ARROWS (carefully aligned) ===
    # LLM -> Candidate
    add_arrow(ax, (2.7, 6.45), (3.5, 6.45))
    
    # Candidate -> Substrate
    add_arrow(ax, (4.6, 6.0), (4.6, 5.5))
    
    # Substrate -> Instrumentation (internal)
    add_arrow(ax, (5.5, 3.8), (5.5, 3.5))
    
    # Instrumentation -> Evaluator
    add_arrow(ax, (6.8, 3.1), (8.5, 4.5), connectionstyle="arc3,rad=-0.2")
    
    # Evaluator -> Search Controller
    add_arrow(ax, (8.5, 5.45), (2.7, 5.25), connectionstyle="arc3,rad=0.3")
    
    # Search Controller -> LLM
    add_arrow(ax, (1.5, 5.7), (1.5, 6.0))
    
    # Evaluator -> Constraint
    add_arrow(ax, (9.6, 5.0), (9.6, 4.4))
    
    # Constraint -> Deployment
    add_arrow(ax, (9.6, 3.5), (9.6, 2.9))
    
    # Deployment -> Artifact
    add_arrow(ax, (8.5, 2.45), (6.8, 0.95), connectionstyle="arc3,rad=0.2")
    
    # Feedback loop label
    ax.text(5.5, 7.2, 'Closed-Loop Optimization', ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('fig1_system_architecture.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig1_system_architecture.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig1_system_architecture.pdf")


# ============================================================================
# FIG. 2: Search-Space Shaping (200)
# ============================================================================
def fig2_search_space_shaping():
    fig, ax = plt.subplots(1, 1, figsize=(11, 7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    ax.text(5.5, 6.7, 'FIG. 2', ha='center', fontsize=14, weight='bold')
    
    # Initial Search Space (210)
    add_box(ax, 0.5, 5, 2.5, 1.2, 'Initial Search Space\n(IR Operators,\nGrammar Rules)', fontsize=8, ref_num='210')
    
    # LLM generates (220)
    add_box(ax, 3.5, 5, 2.2, 1.2, 'LLM Generates\nCandidates', fontsize=9, ref_num='220')
    
    # Evaluate (230)
    add_box(ax, 6.5, 5, 2.2, 1.2, 'Evaluate on\nHardware', fontsize=9, ref_num='230')
    
    # Analyze patterns
    add_box(ax, 6.5, 3.2, 2.2, 1.0, 'Analyze\nPatterns', fontsize=9, ref_num='232')
    
    # LLM proposes modification (240)
    add_box(ax, 3.5, 3.2, 2.2, 1.0, 'LLM Proposes\nModification', fontsize=9, bold=True, ref_num='240')
    
    # Modification types (row)
    y_mod = 1.5
    add_box(ax, 0.3, y_mod, 1.8, 1.0, 'Add/Remove\nOperators', fontsize=7, ref_num='242')
    add_box(ax, 2.4, y_mod, 1.8, 1.0, 'Modify\nGrammar', fontsize=7, ref_num='244')
    add_box(ax, 4.5, y_mod, 1.8, 1.0, 'Adjust\nConstraints', fontsize=7, ref_num='246')
    add_box(ax, 6.6, y_mod, 1.8, 1.0, 'Shift\nPriors', fontsize=7, ref_num='248')
    
    # Validate (250)
    add_box(ax, 8.7, 3.2, 2, 1.0, 'Validate\nModification', fontsize=9, ref_num='250')
    
    # Updated Search Space (260)
    add_box(ax, 8.7, 1.5, 2, 1.0, 'Updated\nSearch Space', fontsize=9, ref_num='260')
    
    # Arrows
    add_arrow(ax, (3.0, 5.6), (3.5, 5.6))
    add_arrow(ax, (5.7, 5.6), (6.5, 5.6))
    add_arrow(ax, (7.6, 5.0), (7.6, 4.2))
    add_arrow(ax, (6.5, 3.7), (5.7, 3.7))
    add_arrow(ax, (4.6, 3.2), (4.6, 2.5))
    add_arrow(ax, (5.7, 3.5), (8.7, 3.5), connectionstyle="arc3,rad=0.15")
    add_arrow(ax, (9.7, 3.2), (9.7, 2.5))
    
    # Feedback to initial
    add_arrow(ax, (9.7, 1.5), (9.7, 0.7), connectionstyle="arc3,rad=0")
    ax.annotate('', xy=(1.75, 5.0), xytext=(9.7, 0.7),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5,
                               connectionstyle="arc3,rad=-0.15"))
    
    ax.text(5.5, 0.5, 'Iteration: t → t+1', ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('fig2_search_space_shaping.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig2_search_space_shaping.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig2_search_space_shaping.pdf")


# ============================================================================
# FIG. 3: Closed-Loop Optimization Flow (300)
# ============================================================================
def fig3_closed_loop():
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(5, 7.7, 'FIG. 3', ha='center', fontsize=14, weight='bold')
    
    # Flowchart boxes (top to bottom flow)
    add_box(ax, 3.5, 6.5, 3, 0.8, 'Generate Candidates (310)', fontsize=9)
    add_box(ax, 3.5, 5.2, 3, 0.8, 'Compile Artifact (320)', fontsize=9)
    add_box(ax, 3.5, 3.9, 3, 0.8, 'Deploy to Hardware (330)', fontsize=9)
    add_box(ax, 3.5, 2.6, 3, 0.8, 'Execute Workload (340)', fontsize=9)
    add_box(ax, 3.5, 1.3, 3, 0.8, 'Collect Telemetry (350)', fontsize=9)
    
    # Decision diamond for termination
    diamond_x, diamond_y = 8, 2.6
    diamond = plt.Polygon([(diamond_x, diamond_y-0.5), (diamond_x-0.7, diamond_y), 
                            (diamond_x, diamond_y+0.5), (diamond_x+0.7, diamond_y)],
                           facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(diamond)
    ax.text(diamond_x, diamond_y, 'Done?', ha='center', va='center', fontsize=8)
    ax.text(diamond_x + 0.1, diamond_y + 0.6, '380', ha='center', fontsize=7, weight='bold')
    
    # Score and Update (right branch)
    add_box(ax, 7, 4.5, 2.5, 0.8, 'Score (360)', fontsize=9)
    add_box(ax, 7, 5.8, 2.5, 0.8, 'Update Model (370)', fontsize=9)
    
    # Output
    add_box(ax, 3.5, 0, 3, 0.8, 'Output Artifact (390)', fontsize=9, bold=True)
    
    # Arrows (vertical flow)
    add_arrow(ax, (5, 6.5), (5, 6.0))
    add_arrow(ax, (5, 5.2), (5, 4.7))
    add_arrow(ax, (5, 3.9), (5, 3.4))
    add_arrow(ax, (5, 2.6), (5, 2.1))
    
    # To scoring
    add_arrow(ax, (6.5, 1.7), (7.3, 1.7), connectionstyle="arc3,rad=0")
    ax.plot([7.3, 7.3], [1.7, 4.5], 'k-', lw=1.5)
    ax.annotate('', xy=(7.3, 4.5), xytext=(7.3, 4.4),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5))
    
    # Score -> Update
    add_arrow(ax, (8.25, 5.3), (8.25, 5.8))
    
    # Update -> Generate (feedback)
    ax.annotate('', xy=(5, 7.3), xytext=(8.25, 6.6),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5,
                               connectionstyle="arc3,rad=0.3"))
    
    # To decision
    add_arrow(ax, (8.25, 4.5), (8.25, 3.1))
    
    # Decision outputs
    add_arrow(ax, (8.7, 2.6), (9.5, 2.6))
    ax.text(9.2, 2.8, 'No', fontsize=8)
    ax.plot([9.5, 9.5], [2.6, 7.0], 'k-', lw=1.5)
    ax.annotate('', xy=(6.5, 7.0), xytext=(9.5, 7.0),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5))
    
    # Yes to output
    add_arrow(ax, (8, 2.1), (8, 0.4))
    ax.annotate('', xy=(6.5, 0.4), xytext=(8, 0.4),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5))
    ax.text(8.2, 1.5, 'Yes', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('fig3_closed_loop.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig3_closed_loop.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig3_closed_loop.pdf")


# ============================================================================
# FIG. 4: ANN-Node Architecture (400)
# ============================================================================
def fig4_ann_node():
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(5, 7.7, 'FIG. 4', ha='center', fontsize=14, weight='bold')
    
    # Main node enclosure (400)
    node_box = FancyBboxPatch((1, 1.5), 8, 5.5, 
                               boxstyle="round,pad=0.03,rounding_size=0.1",
                               facecolor='#f8f8f8', edgecolor='black', linewidth=2)
    ax.add_patch(node_box)
    ax.text(5, 6.8, 'Artificial Neuron Node (400)', ha='center', fontsize=11, weight='bold')
    
    # Top row: Sensors, Compute, Comm
    add_box(ax, 1.5, 5.5, 2, 1, 'Sensor Array\n(410)', fontsize=9, ref_num='410')
    add_box(ax, 4, 5.2, 2.5, 1.3, 'Local Compute\n(MCU + ADC)\n(440)', fontsize=9, bold=True, ref_num='440')
    add_box(ax, 7, 5.5, 1.8, 1, 'Comm I/F\n(450)', fontsize=9, ref_num='450')
    
    # Optional analog preprocessing
    add_box(ax, 1.5, 4.2, 2, 0.9, 'Analog\nPreprocessing\n(420)', fontsize=8, ref_num='420', fill='#f0f0f0')
    
    # ADC
    add_box(ax, 4, 4.0, 1.2, 0.7, 'ADC\n(430)', fontsize=8, ref_num='430')
    
    # Node artifact storage
    add_box(ax, 5.5, 4.0, 1.5, 0.7, 'Artifact\nStorage', fontsize=8)
    
    # Bottom: Event generation, Message passing
    add_box(ax, 1.5, 2.5, 2.5, 1, 'Event Generation\n(Threshold, Spike)', fontsize=8, ref_num='452')
    add_box(ax, 4.5, 2.5, 2.5, 1, 'Message Passing\n(Sparse, Event-Based)', fontsize=8, ref_num='454')
    
    # Telemetry path
    add_box(ax, 7.2, 2.5, 1.5, 1, 'Telemetry\nPath\n(460)', fontsize=8, ref_num='460')
    
    # Nerve bus connection (external)
    add_box(ax, 7.5, 0.5, 2, 0.7, 'Nerve Bus', fontsize=9, bold=True)
    
    # Arrows
    add_arrow(ax, (2.5, 5.5), (2.5, 5.1))  # Sensor -> Analog
    add_arrow(ax, (3.5, 4.65), (4, 4.65))   # Analog -> ADC
    add_arrow(ax, (5.2, 4.35), (5.5, 4.35)) # ADC -> Storage
    add_arrow(ax, (5.25, 5.2), (5.25, 4.7)) # Compute -> ADC area
    add_arrow(ax, (6.5, 5.85), (7, 5.85))   # Compute -> Comm
    add_arrow(ax, (3.75, 3.5), (3.75, 3.0)) # Event connection
    add_arrow(ax, (5.75, 4.0), (5.75, 3.5)) # Message connection
    add_arrow(ax, (7.95, 2.5), (7.95, 1.2)) # Telemetry -> Bus
    add_arrow(ax, (7.9, 5.5), (7.9, 1.2))   # Comm -> Bus
    
    # External data flow labels
    ax.text(0.8, 6, 'Sensors\nIn', ha='center', fontsize=8)
    ax.annotate('', xy=(1.5, 6), xytext=(1, 6),
                arrowprops=dict(arrowstyle='-|>', color='black', lw=1.5))
    
    ax.text(9.2, 0.85, 'Bus\nOut', ha='center', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('fig4_ann_node.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig4_ann_node.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig4_ann_node.pdf")


# ============================================================================
# FIG. 5: Robotic Deployment (500)
# ============================================================================
def fig5_robotic_deployment():
    fig, ax = plt.subplots(1, 1, figsize=(11, 7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    ax.text(5.5, 6.7, 'FIG. 5', ha='center', fontsize=14, weight='bold')
    
    # Robot structure outline (510) - simplified gripper/hand
    # Palm
    palm = FancyBboxPatch((2, 2), 5, 2.5, 
                           boxstyle="round,pad=0.02,rounding_size=0.15",
                           facecolor='white', edgecolor='black', linewidth=2)
    ax.add_patch(palm)
    ax.text(4.5, 4.3, 'Robotic Structure (510)', ha='center', fontsize=9)
    
    # Fingers (3)
    for x_offset in [2.3, 4.2, 6.1]:
        finger = Rectangle((x_offset, 4.5), 0.6, 1.8, 
                           facecolor='white', edgecolor='black', linewidth=1.5)
        ax.add_patch(finger)
    
    # ANN-nodes distributed (520) - black dots
    node_positions = [
        # Palm nodes
        (2.8, 2.5), (3.8, 2.5), (4.8, 2.5), (5.8, 2.5),
        (3.3, 3.2), (4.3, 3.2), (5.3, 3.2),
        (2.8, 3.9), (4.3, 3.9), (5.8, 3.9),
        # Finger nodes
        (2.6, 4.8), (2.6, 5.5), (2.6, 6.1),
        (4.5, 4.8), (4.5, 5.5), (4.5, 6.1),
        (6.4, 4.8), (6.4, 5.5), (6.4, 6.1),
    ]
    for pos in node_positions:
        circle = plt.Circle(pos, 0.12, facecolor='black', edgecolor='black', linewidth=1)
        ax.add_patch(circle)
    
    ax.text(1.3, 3, 'ANN-Nodes\n(520)', ha='center', fontsize=8)
    
    # Nerve bus (530)
    bus_y = 1.3
    ax.plot([1, 8], [bus_y, bus_y], 'k--', linewidth=2)
    ax.text(4.5, 1.0, 'Nerve Bus (530)', ha='center', fontsize=9, style='italic')
    
    # Vertical connections from palm to bus
    for x in [2.8, 4.3, 5.8]:
        ax.plot([x, x], [2, bus_y], 'k-', linewidth=1, alpha=0.5)
    
    # Hub controller (540)
    add_box(ax, 0.3, 0.3, 1.5, 1.2, 'Hub\nController\n(540)', fontsize=8, bold=True)
    add_arrow(ax, (1.8, 0.9), (2.5, 1.3))
    
    # Optimization system (550) - right side
    opt_box = FancyBboxPatch((8.5, 2), 2.2, 4, 
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#f5f5f5', edgecolor='black', linewidth=1.5)
    ax.add_patch(opt_box)
    ax.text(9.6, 5.8, 'Optimization\nSystem (550)', ha='center', fontsize=8, weight='bold')
    
    add_box(ax, 8.7, 4.8, 1.8, 0.7, 'LLM\nGenerator', fontsize=8)
    add_box(ax, 8.7, 3.8, 1.8, 0.7, 'Evaluator', fontsize=8)
    add_box(ax, 8.7, 2.8, 1.8, 0.7, 'Search\nController', fontsize=8)
    
    # Connections to optimization
    add_arrow(ax, (8, 1.3), (8.7, 2.5), connectionstyle="arc3,rad=0.2")
    add_arrow(ax, (8.7, 4.2), (7.5, 3.5), connectionstyle="arc3,rad=0.2")
    
    ax.text(8.3, 1.8, 'Telemetry', fontsize=7, rotation=45)
    ax.text(7.8, 4.0, 'Config', fontsize=7, rotation=-30)
    
    plt.tight_layout()
    plt.savefig('fig5_robotic_deployment.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig5_robotic_deployment.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig5_robotic_deployment.pdf")


# ============================================================================
# FIG. 6: Deployment Artifact Structure (600)
# ============================================================================
def fig6_deployment_artifact():
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    ax.text(5, 6.7, 'FIG. 6', ha='center', fontsize=14, weight='bold')
    
    # Main artifact container (600)
    artifact_box = FancyBboxPatch((1, 1), 8, 5, 
                                    boxstyle="round,pad=0.03,rounding_size=0.1",
                                    facecolor='#f8f8f8', edgecolor='black', linewidth=2)
    ax.add_patch(artifact_box)
    ax.text(5, 5.8, 'Deployable Artifact (600)', ha='center', fontsize=11, weight='bold')
    
    # Top row: main sections
    add_box(ax, 1.3, 4.2, 2.3, 1.3, 'Bytecode for\nDeterministic\nCore (610)', fontsize=8, ref_num='610')
    add_box(ax, 4, 4.2, 2.3, 1.3, 'Configuration for\nUnder-Specified\nElements (620)', fontsize=8, ref_num='620')
    add_box(ax, 6.7, 4.2, 2, 1.3, 'Calibration\nParameters\n(630)', fontsize=8, ref_num='630')
    
    # Middle row: Safety envelope
    add_box(ax, 1.3, 2.6, 7.4, 1.2, 'Safety Envelope (640)\nBounds: Fmax < 2N, Latency < 10ms | Forbidden States | Rate Limits', fontsize=8, ref_num='640')
    
    # Bottom row: Metadata
    add_box(ax, 1.3, 1.3, 3.5, 1, 'Version Metadata\n(650)', fontsize=8, ref_num='650')
    add_box(ax, 5.2, 1.3, 3.5, 1, 'Rollback Pointer\n(660)', fontsize=8, ref_num='660')
    
    # Verification badges (right side)
    ax.text(9.3, 5.2, '✓ Verified', fontsize=9, ha='left')
    ax.text(9.3, 4.7, '✓ Bounded', fontsize=9, ha='left')
    ax.text(9.3, 4.2, '✓ Deterministic', fontsize=9, ha='left')
    
    plt.tight_layout()
    plt.savefig('fig6_deployment_artifact.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig6_deployment_artifact.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig6_deployment_artifact.pdf")


# ============================================================================
# Generate All Figures
# ============================================================================
if __name__ == '__main__':
    print("=" * 50)
    print("Generating USPTO Patent Figures")
    print("Application: Hybrid Compute Optimization")
    print("=" * 50)
    
    fig1_system_architecture()
    fig2_search_space_shaping()
    fig3_closed_loop()
    fig4_ann_node()
    fig5_robotic_deployment()
    fig6_deployment_artifact()
    
    print("=" * 50)
    print("All figures generated!")
    print("")
    print("Files created:")
    print("  - fig1_system_architecture.pdf/png")
    print("  - fig2_search_space_shaping.pdf/png")
    print("  - fig3_closed_loop.pdf/png")
    print("  - fig4_ann_node.pdf/png")
    print("  - fig5_robotic_deployment.pdf/png")
    print("  - fig6_deployment_artifact.pdf/png")
    print("")
    print("To combine into DRAWINGS.pdf:")
    print("  Option 1: pdftk fig*.pdf cat output DRAWINGS.pdf")
    print("  Option 2: Open in Preview.app → File → Export as PDF")
    print("=" * 50)
