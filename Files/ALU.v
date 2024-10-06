module ALU (
output reg [7:0] Y,
output reg C,
input [7:0] A, B,
input [1:0] Sel,
input clk, rst
);

always @ (posedge clk, negedge rst)
	begin
		if(~rst) begin
			Y <= 0;
			C <= 0;
		end
		else begin
			case(Sel)
				2'b00: begin
                  {C,Y} <= A + B; 
				end
				2'b01: begin
                  {C,Y} <= {1'b0, A} + {1'b0, (~B + 8'd1)}; 
				end
				2'b10: begin
					Y <= A & B;
					C <= 0; 
				end
				2'b11: begin
					Y <= A | B;
					C <= 0;
				end
			endcase 
		end
	end

endmodule 