// File: alu_clean.v
// This is the "golden" or correct ALU.

module alu_clean (
    input  [3:0] A,
    input  [3:0] B,
    input  [1:0] op,
    output reg [3:0] result // 'reg' because we assign it in 'always'
  );

  // This 'always' block recalculates whenever an input changes
  always @(*) begin
    case (op)
      2'b00: result = A + B;  // Op 0: Add
      2'b01: result = A - B;  // Op 1: Subtract
      2'b10: result = A & B;  // Op 2: Bitwise AND
      2'b11: result = A | B;  // Op 3: Bitwise OR
      default: result = 4'b0;
    endcase
  end

endmodule
