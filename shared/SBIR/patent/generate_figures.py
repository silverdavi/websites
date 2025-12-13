#!/usr/bin/env python3
"""
Generate USPTO-style patent figures for Embino provisional application.
Creates 5 figures as PDF files suitable for patent filing.

Run: python generate_figures.py
Output: fig1.pdf through fig5.pdf
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# USPTO style: clean, black and white, clear labels
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.5

def add_box(ax, x, y, w, h, text, fontsize=9, bold=False):
    """Add a labeled box to the figure."""
    box = FancyBboxPatch((x, y), w, h, 
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='white', edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
            fontsize=fontsize, weight=weight, wrap=True)

def add_arrow(ax, start, end, style='->', color='black'):
    """Add an arrow between two points."""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=1.5))

def add_label(ax, x, y, text, fontsize=8):
    """Add a text label."""
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize)


# ============================================================================
# FIG. 1: System-Level Block Diagram
# ============================================================================
def fig1_system_overview():
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(5, 6.7, 'FIG. 1 — System Architecture', ha='center', fontsize=12, weight='bold')
    
    # Natural Language Input
    add_box(ax, 0.5, 5, 2, 0.8, 'Natural Language\nInput', fontsize=9)
    
    # GC-SLM
    add_box(ax, 3.5, 5, 2.5, 0.8, 'Grammar-Constrained\nSmall Language Model\n(GC-SLM)', fontsize=8, bold=True)
    
    # Grammar-Guided Decoder
    add_box(ax, 3.5, 3.5, 2.5, 0.8, 'Grammar-Guided\nDecoding Module', fontsize=9)
    
    # DSL Grammar (side)
    add_box(ax, 7, 3.5, 1.8, 0.8, 'DSL\nGrammar', fontsize=9)
    
    # DSL Program Output
    add_box(ax, 3.5, 2, 2.5, 0.8, 'DSL Program\n(Syntactically Valid)', fontsize=9)
    
    # Compiler
    add_box(ax, 3.5, 0.5, 2.5, 0.8, 'Bytecode\nCompiler', fontsize=9, bold=True)
    
    # Bytecode
    add_box(ax, 7, 0.5, 1.8, 0.8, 'Bytecode', fontsize=9)
    
    # MCU / Interpreter (bottom right)
    add_box(ax, 7, -1.2, 2.5, 1.2, 'Embedded MCU\n+ Micro-Interpreter', fontsize=9, bold=True)
    
    # Sensors/Actuators
    add_box(ax, 0.5, -1.2, 2, 1.2, 'Sensors\nActuators\nPeripherals', fontsize=9)
    
    # Arrows
    add_arrow(ax, (2.5, 5.4), (3.5, 5.4))  # NL -> GC-SLM
    add_arrow(ax, (4.75, 5), (4.75, 4.3))  # GC-SLM -> Decoder
    add_arrow(ax, (6, 3.9), (7, 3.9))      # Decoder <-> Grammar
    add_arrow(ax, (7, 3.9), (6, 3.9), style='<-')
    add_arrow(ax, (4.75, 3.5), (4.75, 2.8))  # Decoder -> DSL
    add_arrow(ax, (4.75, 2), (4.75, 1.3))  # DSL -> Compiler
    add_arrow(ax, (6, 0.9), (7, 0.9))      # Compiler -> Bytecode
    add_arrow(ax, (7.9, 0.5), (7.9, -0.1)) # Bytecode -> MCU
    add_arrow(ax, (7, -0.6), (2.5, -0.6))  # MCU <-> Sensors
    add_arrow(ax, (2.5, -0.6), (7, -0.6), style='<-')
    
    # Labels on arrows
    add_label(ax, 3, 5.6, '"Blink LED\nwhen button\npressed"', fontsize=7)
    
    ax.set_ylim(-2, 7.2)
    
    plt.tight_layout()
    plt.savefig('fig1_system_overview.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig1_system_overview.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig1_system_overview.pdf")


# ============================================================================
# FIG. 2: Grammar-Guided Decoding Flow
# ============================================================================
def fig2_grammar_decoding():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.text(5, 5.7, 'FIG. 2 — Grammar-Guided Decoding Flow', ha='center', fontsize=12, weight='bold')
    
    # Loop structure
    # Start
    ax.add_patch(plt.Circle((1, 4.5), 0.3, facecolor='white', edgecolor='black', lw=1.5))
    ax.text(1, 4.5, 'Start', ha='center', va='center', fontsize=8)
    
    # Compute logits
    add_box(ax, 2, 4, 2, 0.8, 'Compute Logits\nP(token | context)', fontsize=8)
    
    # Query parser state
    add_box(ax, 5, 4, 2.2, 0.8, 'Query Parser\nState', fontsize=8)
    
    # Valid tokens
    add_box(ax, 5, 2.5, 2.2, 0.8, 'Get Valid\nTokens', fontsize=8)
    
    # Mask logits
    add_box(ax, 2, 2.5, 2, 0.8, 'Mask Invalid\nLogits → 0', fontsize=8)
    
    # Sample token
    add_box(ax, 2, 1, 2, 0.8, 'Sample Token\nfrom Masked\nDistribution', fontsize=8)
    
    # Update parser
    add_box(ax, 5, 1, 2.2, 0.8, 'Update Parser\nState', fontsize=8)
    
    # Decision diamond
    diamond = plt.Polygon([[8.5, 2.5], [9.3, 1.9], [8.5, 1.3], [7.7, 1.9]], 
                          facecolor='white', edgecolor='black', lw=1.5)
    ax.add_patch(diamond)
    ax.text(8.5, 1.9, 'Complete?', ha='center', va='center', fontsize=7)
    
    # End
    ax.add_patch(plt.Circle((8.5, 0.3), 0.3, facecolor='white', edgecolor='black', lw=1.5))
    ax.text(8.5, 0.3, 'End', ha='center', va='center', fontsize=8)
    
    # Grammar box (side)
    add_box(ax, 8, 4, 1.5, 0.8, 'DSL\nGrammar\n(CFG)', fontsize=8)
    
    # Arrows
    add_arrow(ax, (1.3, 4.5), (2, 4.5))
    add_arrow(ax, (4, 4.4), (5, 4.4))
    add_arrow(ax, (6.1, 4), (6.1, 3.3))
    add_arrow(ax, (5, 2.9), (4, 2.9))
    add_arrow(ax, (3, 2.5), (3, 1.8))
    add_arrow(ax, (4, 1.4), (5, 1.4))
    add_arrow(ax, (7.2, 1.4), (7.7, 1.9))
    add_arrow(ax, (8.5, 1.3), (8.5, 0.6))
    
    # Loop back arrow (No)
    ax.annotate('', xy=(3, 4.8), xytext=(8.5, 2.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5,
                               connectionstyle='arc3,rad=0.3'))
    
    # Grammar connection
    add_arrow(ax, (8, 4.4), (7.2, 4.4), style='<->')
    
    # Labels
    ax.text(8.8, 0.9, 'Yes', fontsize=7)
    ax.text(6, 2.7, 'No', fontsize=7)
    
    plt.tight_layout()
    plt.savefig('fig2_grammar_decoding.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig2_grammar_decoding.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig2_grammar_decoding.pdf")


# ============================================================================
# FIG. 3: S-LoRA Structure
# ============================================================================
def fig3_slora():
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    ax.text(5, 4.7, 'FIG. 3 — Sparse Low-Rank Adaptation (S-LoRA)', ha='center', fontsize=12, weight='bold')
    
    # Pre-trained weights W
    add_box(ax, 0.5, 1.5, 1.5, 2, 'W\n(Frozen\nPre-trained\nWeights)\nd × d', fontsize=8, bold=True)
    
    # Plus sign
    ax.text(2.5, 2.5, '+', fontsize=20, ha='center', va='center')
    
    # Low-rank A
    add_box(ax, 3.2, 2.5, 0.8, 1.5, 'A\nd × r', fontsize=8)
    
    # Multiply sign
    ax.text(4.3, 2.5, '×', fontsize=14, ha='center', va='center')
    
    # Low-rank B
    add_box(ax, 4.7, 2.5, 0.8, 1.5, 'B\nr × d', fontsize=8)
    
    # Sparsity mask
    ax.text(5.9, 2.5, '⊙', fontsize=16, ha='center', va='center')
    add_box(ax, 6.3, 2.5, 1, 1.5, 'M\n(Sparse\nMask)', fontsize=8)
    
    # Equals
    ax.text(7.8, 2.5, '=', fontsize=16, ha='center', va='center')
    
    # Result
    add_box(ax, 8.2, 1.5, 1.5, 2, "W'\n(Adapted\nWeights)", fontsize=8, bold=True)
    
    # Annotations
    ax.text(3.6, 1.5, 'r << d', fontsize=8, ha='center', style='italic')
    ax.text(6.8, 1.5, 'Block\nSparsity', fontsize=7, ha='center')
    
    # Block sparsity illustration
    # Small grid showing sparse blocks
    for i in range(4):
        for j in range(4):
            color = 'black' if (i+j) % 3 == 0 else 'white'
            rect = plt.Rectangle((6.4 + j*0.2, 0.3 + i*0.2), 0.18, 0.18, 
                                 facecolor=color, edgecolor='black', lw=0.5)
            ax.add_patch(rect)
    ax.text(7.2, 0.2, 'Active Blocks', fontsize=7, ha='center')
    
    plt.tight_layout()
    plt.savefig('fig3_slora.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig3_slora.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig3_slora.pdf")


# ============================================================================
# FIG. 4: Bytecode Interpreter Architecture
# ============================================================================
def fig4_interpreter():
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')
    
    ax.text(5, 6.7, 'FIG. 4 — Micro-Interpreter Architecture', ha='center', fontsize=12, weight='bold')
    
    # Main interpreter box (dashed outline)
    main_box = FancyBboxPatch((0.5, 0.5), 9, 5.8, 
                               boxstyle="round,pad=0.02,rounding_size=0.1",
                               facecolor='none', edgecolor='black', 
                               linewidth=2, linestyle='--')
    ax.add_patch(main_box)
    ax.text(5, 6.1, 'Micro-Interpreter (<16KB)', ha='center', fontsize=10, weight='bold')
    
    # Program Counter
    add_box(ax, 1, 5, 1.5, 0.7, 'Program\nCounter', fontsize=8)
    
    # Instruction Decoder
    add_box(ax, 3, 5, 2, 0.7, 'Instruction\nDecoder', fontsize=8, bold=True)
    
    # Bytecode Memory
    add_box(ax, 6, 5, 2, 0.7, 'Bytecode\nMemory', fontsize=8)
    
    # Evaluation Stack
    add_box(ax, 1, 3.2, 1.8, 1.2, 'Evaluation\nStack\n(Fixed Depth)', fontsize=8)
    
    # Variable Storage
    add_box(ax, 3.5, 3.2, 1.8, 1.2, 'Variable\nStorage\n(Fixed Size)', fontsize=8)
    
    # Execution Loop
    add_box(ax, 6, 3.2, 2.5, 1.2, 'Execution Loop\n(Bounded Cycles\nper Instruction)', fontsize=8, bold=True)
    
    # Hardware Abstraction
    add_box(ax, 1, 1, 3, 1, 'Hardware Abstraction Layer', fontsize=9)
    
    # Pin interfaces
    add_box(ax, 4.5, 1, 1.3, 0.5, 'GPIO', fontsize=8)
    add_box(ax, 6, 1, 1.3, 0.5, 'ADC', fontsize=8)
    add_box(ax, 7.5, 1, 1.3, 0.5, 'PWM', fontsize=8)
    
    # Arrows
    add_arrow(ax, (2.5, 5.3), (3, 5.3))
    add_arrow(ax, (5, 5.3), (6, 5.3))
    add_arrow(ax, (4, 5), (4, 4.4))
    add_arrow(ax, (1.9, 4.4), (1.9, 3.2), style='<->')
    add_arrow(ax, (4.4, 4.4), (4.4, 3.2), style='<->')
    add_arrow(ax, (6.5, 3.2), (6.5, 2.5))
    add_arrow(ax, (2.5, 2), (2.5, 1))
    
    plt.tight_layout()
    plt.savefig('fig4_interpreter.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig4_interpreter.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig4_interpreter.pdf")


# ============================================================================
# FIG. 5: MCU Deployment Environment
# ============================================================================
def fig5_deployment():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.text(5, 5.7, 'FIG. 5 — MCU Deployment Environment', ha='center', fontsize=12, weight='bold')
    
    # External: Host/Cloud
    add_box(ax, 0.5, 4, 2.5, 1.2, 'Host Device\nor Cloud\n(Generation)', fontsize=8)
    
    # Communication channel
    add_box(ax, 3.5, 4.3, 1.5, 0.6, 'WiFi/BLE/\nSerial', fontsize=7)
    
    # MCU (main box)
    mcu_box = FancyBboxPatch((5.5, 1), 4, 4.2, 
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#f0f0f0', edgecolor='black', linewidth=2)
    ax.add_patch(mcu_box)
    ax.text(7.5, 5, 'Embedded MCU', ha='center', fontsize=10, weight='bold')
    
    # Inside MCU
    add_box(ax, 5.8, 4, 1.5, 0.7, 'Flash\n(Bytecode)', fontsize=8)
    add_box(ax, 7.6, 4, 1.5, 0.7, 'RAM\n(<4KB)', fontsize=8)
    add_box(ax, 5.8, 2.8, 3.3, 0.8, 'Micro-Interpreter', fontsize=9, bold=True)
    add_box(ax, 5.8, 1.5, 3.3, 0.8, 'Hardware Interfaces', fontsize=8)
    
    # Sensors (left of MCU)
    add_box(ax, 0.5, 2, 1.8, 0.7, 'Temperature\nSensor', fontsize=8)
    add_box(ax, 0.5, 1, 1.8, 0.7, 'Button /\nSwitch', fontsize=8)
    
    # Actuators (below MCU) 
    add_box(ax, 5.8, 0, 1.5, 0.7, 'LED', fontsize=8)
    add_box(ax, 7.6, 0, 1.5, 0.7, 'Motor /\nServo', fontsize=8)
    
    # Arrows
    add_arrow(ax, (3, 4.6), (3.5, 4.6))
    add_arrow(ax, (5, 4.6), (5.5, 4.6))
    add_arrow(ax, (6.55, 4), (6.55, 3.6))
    add_arrow(ax, (8.35, 4), (8.35, 3.6))
    add_arrow(ax, (7.45, 2.8), (7.45, 2.3))
    
    # Sensor arrows
    add_arrow(ax, (2.3, 2.3), (5.5, 2.3))
    add_arrow(ax, (2.3, 1.3), (5.5, 1.9))
    
    # Actuator arrows
    add_arrow(ax, (6.55, 1.5), (6.55, 0.7))
    add_arrow(ax, (8.35, 1.5), (8.35, 0.7))
    
    # Update path label
    ax.text(4, 4.9, 'Program\nUpdate', fontsize=7, ha='center')
    
    plt.tight_layout()
    plt.savefig('fig5_deployment.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig5_deployment.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Created: fig5_deployment.pdf")


# ============================================================================
# Generate All Figures
# ============================================================================
if __name__ == '__main__':
    print("Generating USPTO patent figures...")
    print("-" * 40)
    
    fig1_system_overview()
    fig2_grammar_decoding()
    fig3_slora()
    fig4_interpreter()
    fig5_deployment()
    
    print("-" * 40)
    print("Done! Files created:")
    print("  - fig1_system_overview.pdf")
    print("  - fig2_grammar_decoding.pdf")
    print("  - fig3_slora.pdf")
    print("  - fig4_interpreter.pdf")
    print("  - fig5_deployment.pdf")
    print("\nCombine into single PDF with:")
    print("  pdftk fig*.pdf cat output DRAWINGS.pdf")
    print("  -- OR --")
    print("  Preview.app → Print → Save as PDF")

