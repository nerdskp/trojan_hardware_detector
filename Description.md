[README.txt](https://github.com/user-attachments/files/23436451/README.txt)
# Project Title

HARDWARE TROJAN

---

## 1. Description

Our project focuses on detecting Hardware Trojans in digital circuits by analyzing waveform activity generated during simulation. We designed two versions of an Arithmetic Logic Unit (ALU) — one clean and one Trojan-inserted — and compared their behavior using Icarus Verilog and GTKWave.

The project simulates both ALU designs under identical input conditions and records the resulting signal transitions in a .vcd (Value Change Dump) file. These waveforms are then visualized in GTKWave, where deviations in signal timing or logic levels help identify the presence of a Trojan.

By observing and comparing the waveform patterns, users can easily spot irregularities or additional logic activity that indicates malicious modification at the hardware level. This approach demonstrates a practical and visual method for detecting hardware Trojans during the verification stage of chip design.
---

## 2. Features

* Modular Verilog design for ALU operations
* Simulation and testbench execution using **Icarus Verilog (iverilog)**
* Automated waveform generation (`activity.vcd`)
* Waveform visualization via **GTKWave**
* Python-based analysis and plotting scripts
* Easy-to-run batch script for waveform viewing

---

## 3. Project Structure

```
hackathon/
└── siliconSprint/
    ├── alu_clean.v              # Clean ALU Verilog module
    ├── alu_trojan.v             # Trojan-inserted ALU version
    ├── testbench.v              # Testbench for simulation
    ├── activity.vcd             # Generated waveform output
    ├── analyze.py               # Python script for analysis
    ├── view_waveform.py         # Python-based waveform visualizer
    ├── comparison_plot.png      # Output plot for result comparison
    ├── open_gtkwave.bat         # Windows batch file to open GTKWave
    ├── .vscode/                 # VSCode configurations
```

---

## 4. Requirements

Before running the project, make sure the following tools are installed:

* **Icarus Verilog (iverilog)** — for Verilog simulation
* **GTKWave** — for waveform visualization
* **Python 3.8+** (with matplotlib, numpy if analysis scripts are used)

---

## 5. Installation & Setup

1. Clone or unzip the project to your local machine.
2. Open the folder in **VS Code** or your preferred editor.
3. Make sure Icarus Verilog and GTKWave are installed and added to your system PATH.
4. Navigate to the project directory in your terminal:

   ```bash
   cd d:\hackathon\siliconSprint\siliconSprint
   ```

---

## 6. Usage Instructions

1️⃣ Compile and Run Simulation

```bash
iverilog -o my_sim.vvp testbench.v
vvp my_sim.vvp
```

This will generate the waveform file `activity.vcd`.

2️⃣ View Waveform using GTKWave

Once the `.vcd` file is generated, open GTKWave using the following command:

```bash
cd d:\hackathon\siliconSprint\siliconSprint
start gtkwave activity.vcd
```

Alternatively, you can double-click `open_gtkwave.bat` to launch GTKWave automatically.

3️⃣ Run Python Analysis

```bash
python analyze.py
python view_waveform.py
```

These scripts analyze simulation results and generate visual plots like `comparison_plot.png` and `waveform_view.png`.

---

7. Example Output

* **activity.vcd** — waveform dump for ALU operations
* **comparison_plot.png** — graphical comparison between ALU variants
* **waveform_view.png** — signal overview visualization

---

## 8. Troubleshooting

| Problem                   | Possible Cause     | Solution                                           |
| ------------------------- | ------------------ | -------------------------------------------------- |
| `iverilog` not recognized | Tool not installed | Install Icarus Verilog and add to PATH             |
| GTKWave doesn’t open      | Wrong file path    | Make sure to run from the correct directory        |
| No VCD file generated     | Simulation failed  | Check your Verilog syntax and re-run the testbench |

---
## 9. Quick Command Summary

```bash
# Run simulation
iverilog -o my_sim.vvp testbench.v
vvp my_sim.vvp

# View waveform
cd d:\hackathon\siliconSprint\siliconSprint
start gtkwave activity.vcd

# Analyze results 
python analyze.py
python view_waveform.py
```
