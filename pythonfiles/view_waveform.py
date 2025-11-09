import matplotlib.pyplot as plt
import numpy as np
from vcdvcd import VCDVCD
import os
import sys

def plot_waveform(vcd, signal_names, max_signals=20):
    """
    Plot waveforms for selected signals.
    """
    fig, axes = plt.subplots(len(signal_names), 1, figsize=(15, 2 * len(signal_names)))
    if len(signal_names) == 1:
        axes = [axes]
    
    for idx, signal_name in enumerate(signal_names):
        if signal_name not in vcd.signals:
            print(f"Warning: Signal '{signal_name}' not found in VCD file")
            continue
            
        signal = vcd[signal_name]
        ax = axes[idx]
        
        times = [0]
        values = [signal.tv[0][1] if signal.tv else '0']
        
        for time, value in signal.tv[1:]:
            times.append(time)
            values.append(values[-1])
            times.append(time)
            values.append(value)
        
        plot_values = []
        for val in values:
            try:
                if 'x' in val.lower() or 'z' in val.lower():
                    plot_values.append(0)  
                else:
                    plot_values.append(int(val, 2) if isinstance(val, str) else int(val))
            except:
                plot_values.append(0)
        
        ax.plot(times, plot_values, drawstyle='steps-post', linewidth=2)
        ax.set_ylabel(signal_name, fontsize=10, rotation=0, ha='right')
        ax.set_xlim(0, max(times) if times else 100)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.5, max(plot_values) + 0.5 if plot_values else 1.5)
    
    axes[-1].set_xlabel('Time (simulation units)')
    plt.suptitle('Waveform Viewer', fontsize=14, y=0.995)
    plt.tight_layout()
    return fig

def list_signals(vcd):
    """List all available signals in the VCD file."""
    signals = sorted(vcd.signals)
    print("\n=== Available Signals ===")
    for i, sig in enumerate(signals, 1):
        print(f"{i:3d}. {sig}")
    return signals

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vcd_path = os.path.join(script_dir, 'activity.vcd')
    
    if not os.path.exists(vcd_path):
        print(f"Error: 'activity.vcd' not found at {vcd_path}")
        print("Please run the simulation first (vvp mysim.vvp)")
        sys.exit(1)
    
    print(f"Loading VCD file: {vcd_path}")
    try:
        vcd = VCDVCD(vcd_path)
    except Exception as e:
        print(f"Error loading VCD file: {e}")
        sys.exit(1)
    
    print(f"Loaded VCD file with {len(vcd.signals)} signals")
    
    all_signals = list_signals(vcd)
    
    interesting_signals = []
    
    priority_keywords = ['result', 'A', 'B', 'op', 'trojan', 'clean']
    
    for keyword in priority_keywords:
        for sig in all_signals:
            if keyword.lower() in sig.lower() and sig not in interesting_signals:
                interesting_signals.append(sig)
                if len(interesting_signals) >= 15: 
                    break
        if len(interesting_signals) >= 15:
            break
    
    if len(interesting_signals) < 10:
        for sig in all_signals:
            if sig not in interesting_signals:
                interesting_signals.append(sig)
                if len(interesting_signals) >= 15:
                    break
    
    print(f"\n=== Plotting {len(interesting_signals)} signals ===")
    for sig in interesting_signals:
        print(f"  - {sig}")
    
    fig = plot_waveform(vcd, interesting_signals[:15])  
    
    output_path = os.path.join(script_dir, 'waveform_view.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\nWaveform saved to: {output_path}")
    print("Opening waveform viewer...")
    
    plt.show()
    
    print("="*60)

if __name__ == "__main__":
    main()

