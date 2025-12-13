#!/usr/bin/env python3
"""
Generate visualizations for the Abstraction Gap Benchmark.
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Load data
with open('benchmark_results.json', 'r') as f:
    data = json.load(f)

# Colors
COLORS = {
    'mcu_feasible': '#2ecc71',      # Green
    'mcu_marginal': '#f39c12',      # Orange  
    'non_mcu': '#e74c3c',           # Red
    'embino': '#3498db',            # Blue (highlight)
}

def get_color(item):
    if item['name'] == 'Embino (GC-SLM)':
        return COLORS['embino']
    elif not item['can_run_on_mcu']:
        return COLORS['non_mcu']
    elif item['ram_runtime_bytes'] > 50000:  # >50KB
        return COLORS['mcu_marginal']
    else:
        return COLORS['mcu_feasible']


# =============================================================================
# PLOT 1: Size Comparison (Log Scale)
# =============================================================================
def plot_size_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    names = [d['name'] for d in data]
    sizes = [d['binary_size_bytes'] for d in data]
    colors = [get_color(d) for d in data]
    
    bars = ax.barh(names, sizes, color=colors, edgecolor='black', linewidth=0.5)
    ax.set_xscale('log')
    ax.set_xlabel('Binary/Model Size (bytes)', fontsize=12)
    ax.set_title('Abstraction Gap: Storage Requirements', fontsize=14, fontweight='bold')
    
    # Add size labels
    for bar, size in zip(bars, sizes):
        label = format_size(size)
        ax.text(bar.get_width() * 1.5, bar.get_y() + bar.get_height()/2, 
                label, va='center', fontsize=9)
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=COLORS['mcu_feasible'], label='MCU-feasible'),
        mpatches.Patch(color=COLORS['mcu_marginal'], label='MCU-marginal'),
        mpatches.Patch(color=COLORS['non_mcu'], label='Non-MCU'),
        mpatches.Patch(color=COLORS['embino'], label='Embino (ours)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right')
    
    # MCU limit line
    ax.axvline(x=4_000_000, color='gray', linestyle='--', linewidth=1.5, label='ESP32 Flash (4MB)')
    ax.text(4_000_000 * 1.2, 0.5, 'ESP32 Flash\n(4MB)', fontsize=8, color='gray')
    
    plt.tight_layout()
    plt.savefig('fig_size_comparison.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig_size_comparison.pdf', bbox_inches='tight')
    print("Saved: fig_size_comparison.png/pdf")
    plt.close()


# =============================================================================
# PLOT 2: RAM Comparison (Log Scale)
# =============================================================================
def plot_ram_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    names = [d['name'] for d in data]
    rams = [d['ram_runtime_bytes'] for d in data]
    colors = [get_color(d) for d in data]
    
    bars = ax.barh(names, rams, color=colors, edgecolor='black', linewidth=0.5)
    ax.set_xscale('log')
    ax.set_xlabel('Runtime RAM (bytes)', fontsize=12)
    ax.set_title('Abstraction Gap: RAM Requirements', fontsize=14, fontweight='bold')
    
    # Add size labels
    for bar, ram in zip(bars, rams):
        label = format_size(ram)
        ax.text(bar.get_width() * 1.5, bar.get_y() + bar.get_height()/2, 
                label, va='center', fontsize=9)
    
    # ESP32 RAM limit
    ax.axvline(x=520_000, color='gray', linestyle='--', linewidth=1.5)
    ax.text(520_000 * 1.2, 0.5, 'ESP32 SRAM\n(520KB)', fontsize=8, color='gray')
    
    plt.tight_layout()
    plt.savefig('fig_ram_comparison.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig_ram_comparison.pdf', bbox_inches='tight')
    print("Saved: fig_ram_comparison.png/pdf")
    plt.close()


# =============================================================================
# PLOT 3: Development Time vs Latency Trade-off
# =============================================================================
def plot_tradeoff():
    fig, ax = plt.subplots(figsize=(10, 7))
    
    for d in data:
        color = get_color(d)
        size = np.log10(d['binary_size_bytes']) * 15  # Scale marker by size
        ax.scatter(d['dev_time_min'], d['latency_us'], 
                   s=size, c=color, edgecolor='black', linewidth=1, alpha=0.8)
        
        # Label
        offset = (5, 5) if d['name'] != 'LLM (GPT-4)' else (-80, 5)
        ax.annotate(d['name'], (d['dev_time_min'], d['latency_us']),
                    textcoords='offset points', xytext=offset, fontsize=9)
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Development Time (minutes)', fontsize=12)
    ax.set_ylabel('Execution Latency (µs)', fontsize=12)
    ax.set_title('Trade-off: Development Speed vs Runtime Performance', fontsize=14, fontweight='bold')
    
    # Ideal region (fast dev, low latency)
    ax.axhspan(0.001, 1000, xmin=0, xmax=0.15, alpha=0.1, color='green')
    ax.text(1.5, 0.1, 'Ideal:\nFast dev\nLow latency', fontsize=8, color='green')
    
    plt.tight_layout()
    plt.savefig('fig_tradeoff.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig_tradeoff.pdf', bbox_inches='tight')
    print("Saved: fig_tradeoff.png/pdf")
    plt.close()


# =============================================================================
# PLOT 4: Timeline / Evolution
# =============================================================================
def plot_timeline():
    fig, ax = plt.subplots(figsize=(12, 5))
    
    eras = ['1950s', '1960s', '1970s', '1980s', '2010s', '2020s', '2025']
    positions = [0, 1, 2, 3, 4, 5, 6]
    
    # Plot line
    ax.plot(positions, [0]*len(positions), 'k-', linewidth=2, zorder=1)
    
    for i, d in enumerate(data):
        color = get_color(d)
        y_offset = 0.5 if i % 2 == 0 else -0.5
        
        # Marker
        ax.scatter(i, 0, s=200, c=color, edgecolor='black', linewidth=2, zorder=2)
        
        # Label above/below
        ax.annotate(f"{d['name']}\n{format_size(d['binary_size_bytes'])}", 
                    (i, 0), textcoords='offset points',
                    xytext=(0, 40 if y_offset > 0 else -50),
                    ha='center', fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))
        
        # Era label
        ax.text(i, -0.15, d['era'], ha='center', fontsize=8, color='gray')
    
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1, 1.5)
    ax.axis('off')
    ax.set_title('Evolution of Programming Abstraction', fontsize=14, fontweight='bold')
    
    # Add "THE GAP" annotation
    ax.annotate('', xy=(5, 0.8), xytext=(4, 0.8),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(4.5, 0.95, 'THE GAP\n(1000×+ params)', ha='center', fontsize=10, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('fig_timeline.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig_timeline.pdf', bbox_inches='tight')
    print("Saved: fig_timeline.png/pdf")
    plt.close()


# =============================================================================
# PLOT 5: Summary Dashboard
# =============================================================================
def plot_dashboard():
    fig = plt.figure(figsize=(14, 10))
    
    # Create grid
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # --- Panel 1: Size ---
    ax1 = fig.add_subplot(gs[0, 0])
    names = [d['name'][:12] for d in data]
    sizes = [d['binary_size_bytes'] for d in data]
    colors = [get_color(d) for d in data]
    ax1.barh(names, sizes, color=colors)
    ax1.set_xscale('log')
    ax1.set_xlabel('Binary Size (bytes)')
    ax1.set_title('Storage', fontweight='bold')
    ax1.axvline(x=4_000_000, color='gray', linestyle='--', alpha=0.5)
    
    # --- Panel 2: RAM ---
    ax2 = fig.add_subplot(gs[0, 1])
    rams = [d['ram_runtime_bytes'] for d in data]
    ax2.barh(names, rams, color=colors)
    ax2.set_xscale('log')
    ax2.set_xlabel('Runtime RAM (bytes)')
    ax2.set_title('Memory', fontweight='bold')
    ax2.axvline(x=520_000, color='gray', linestyle='--', alpha=0.5)
    
    # --- Panel 3: Latency ---
    ax3 = fig.add_subplot(gs[1, 0])
    latencies = [d['latency_us'] for d in data]
    ax3.barh(names, latencies, color=colors)
    ax3.set_xscale('log')
    ax3.set_xlabel('Latency (µs)')
    ax3.set_title('Speed', fontweight='bold')
    
    # --- Panel 4: Dev Time ---
    ax4 = fig.add_subplot(gs[1, 1])
    dev_times = [d['dev_time_min'] for d in data]
    ax4.barh(names, dev_times, color=colors)
    ax4.set_xlabel('Dev Time (minutes)')
    ax4.set_title('Developer Productivity', fontweight='bold')
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=COLORS['mcu_feasible'], label='MCU-feasible'),
        mpatches.Patch(color=COLORS['mcu_marginal'], label='MCU-marginal'),
        mpatches.Patch(color=COLORS['non_mcu'], label='Non-MCU'),
        mpatches.Patch(color=COLORS['embino'], label='Embino'),
    ]
    fig.legend(handles=legend_elements, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 0.02))
    
    fig.suptitle('Abstraction Gap Benchmark: "Blink LED every 1s" on ESP32', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    plt.savefig('fig_dashboard.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig_dashboard.pdf', bbox_inches='tight')
    print("Saved: fig_dashboard.png/pdf")
    plt.close()


# =============================================================================
# HELPERS
# =============================================================================

def format_size(bytes_val: int) -> str:
    if bytes_val >= 1_000_000_000:
        return f"{bytes_val / 1_000_000_000:.0f}GB"
    elif bytes_val >= 1_000_000:
        return f"{bytes_val / 1_000_000:.0f}MB"
    elif bytes_val >= 1_000:
        return f"{bytes_val / 1_000:.1f}KB"
    else:
        return f"{bytes_val}B"


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Generating plots...")
    plot_size_comparison()
    plot_ram_comparison()
    plot_tradeoff()
    plot_timeline()
    plot_dashboard()
    print("\nAll plots generated!")

