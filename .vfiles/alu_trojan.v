// File: alu_trojan.v
// This ALU has a hidden, malicious trigger.

module alu_trojan (
    input  [3:0] A,
    input  [3:0] B,
    input  [1:0] op,
    output reg [3:0] result // 'reg' because we assign it in 'always'
  );

  // --- Trojan Trigger Wires ---
  // The trojan will activate when (A == 15) AND (op == 1)
  wire trigger_A  = (A == 4'b1111);
  wire trigger_op = (op == 2'b01); // Subtract operation
  wire trojan_trigger = trigger_A & trigger_op;

  // This 'always' block recalculates whenever an input changes
  always @(*) begin
    if (trojan_trigger) begin
      // --- TROJAN ACTIVATED ---
      // Instead of A - B, it leaks A by outputting A.
      // (Or it could be result = A ^ B, or any other wrong value)
      result = A; 
    end
    else begin
      // --- Normal Operation ---
      // Behaves exactly like alu_clean
      case (op)
        2'b00: result = A + B;
        2'b01: result = A - B;
        2'b10: result = A & B;
        2'b11: result = A | B;
        default: result = 4'b0;
      endcase
    end
  end

endmodule
