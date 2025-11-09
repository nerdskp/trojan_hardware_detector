// File: testbench.v
// This testbench runs *both* ALUs with identical inputs.
// (Your code, which is correct)

module testbench;

    // 1. Declare signals to feed the ALUs
    reg  [3:0] A;
    reg  [3:0] B;
    reg  [1:0] op;

    // 2. Declare wires to catch the outputs
    wire [3:0] clean_result;
    wire [3:0] trojan_result;

    // 3. Instantiate (create) both ALUs
    //    'UUT' stands for 'Unit Under Test'
    alu_clean  UUT_clean (
        .A(A), 
        .B(B), 
        .op(op), 
        .result(clean_result)
    );

    alu_trojan UUT_trojan (
        .A(A), 
        .B(B), 
        .op(op), 
        .result(trojan_result)
    );


    // 4. VCD Dump Setup: This is critical
    initial begin
        $dumpfile("activity.vcd");
        $dumpvars(0, testbench); 
    end

    // 5. Stimulus: Generate all possible inputs
    integer i;
    initial begin
        for (i = 0; i < 1024; i = i + 1) begin
            {A, B, op} = i; // Assign all bits at once
            #10;            // Wait 10 time units
        end

        $finish; // End the simulation
    end

endmodule
