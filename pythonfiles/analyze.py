import matplotlib.pyplot as plt
import numpy as np
from vcdvcd import VCDVCD
import sys
import os

print("Starting analysis...")

script_dir = os.path.dirname(os.path.abspath(__file__))
vcd_path = os.path.join(script_dir, 'activity.vcd')

print(f"Looking for VCD file at: {vcd_path}")
print(f"Current working directory: {os.getcwd()}")

try:
    if not os.path.exists(vcd_path):
        print(f"Error: 'activity.vcd' not found at {vcd_path}")
        print("Please run the simulation first (vvp mysim.vvp)")
        print("\nTo generate the VCD file:")
        print("  1. Compile: iverilog -o mysim.vvp testbench.v alu_clean.v alu_trojan.v")
        print("  2. Simulate: vvp mysim.vvp")
        sys.exit(1)
    
    vcd = VCDVCD(vcd_path)
except FileNotFoundError:
    print(f"Error: 'activity.vcd' not found at {vcd_path}")
    print("Please run the simulation first (vvp mysim.vvp)")
    sys.exit(1)
except Exception as e:
    print(f"Error loading VCD file: {e}")
    sys.exit(1)

all_signals = vcd.signals

toggle_counts = {}
for signal_name in all_signals:
    signal = vcd[signal_name]
    num_toggles = len(signal.tv) - 1
    toggle_counts[signal_name] = num_toggles

clean_data = {}
trojan_data = {}

for full_name, count in toggle_counts.items():
    if 'UUT_clean.' in full_name:
        short_name = full_name.split('UUT_clean.')[1]
        clean_data[short_name] = count
        
    elif 'UUT_trojan.' in full_name:
        short_name = full_name.split('UUT_trojan.')[1]
        trojan_data[short_name] = count

print(f"Found {len(clean_data)} signals in Clean ALU.")
print(f"Found {len(trojan_data)} signals in Trojan ALU.")

suspicious_signals = []
print("\n--- Side-Channel Analysis Report ---")

all_signal_names = sorted(list(set(clean_data.keys()) | set(trojan_data.keys())))

for sig in all_signal_names:
    clean_count = clean_data.get(sig, 0)
    trojan_count = trojan_data.get(sig, 0)
    
    if sig not in clean_data:
        print(f"!! SUSPICIOUS (Exists only in Trojan): {sig} | Toggles: {trojan_count}")
        suspicious_signals.append(sig)
        continue

    if clean_count == 0 and trojan_count > 0:
        deviation = 100.0 
    elif clean_count == 0:
        deviation = 0.0
    else:
        deviation = (abs(trojan_count - clean_count) / clean_count) * 100

    if deviation > 25.0: 
        print(f"!! SUSPICIOUS (High Deviation): {sig}")
        print(f"   Clean: {clean_count} | Trojan: {trojan_count} | Deviation: {deviation:.2f}%")
        suspicious_signals.append(sig)

labels = all_signal_names
clean_values = [clean_data.get(s, 0) for s in labels]
trojan_values = [trojan_data.get(s, 0) for s in labels]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(15, 7))
rects1 = ax.bar(x - width/2, clean_values, width, label='Clean ALU')
rects2 = ax.bar(x + width/2, trojan_values, width, label='Trojan ALU')

ax.set_ylabel('Total Toggle Counts')
ax.set_title('Side-Channel Analysis: Toggle Count Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=90, fontsize=8)
ax.legend()

for i, label in enumerate(labels):
    if label in suspicious_signals:
        rects2[i].set_color('red')

fig.tight_layout()
plot_path = os.path.join(script_dir, 'comparison_plot.png')
plt.savefig(plot_path)

print(f"\nAnalysis complete. Plot saved to '{plot_path}'")

