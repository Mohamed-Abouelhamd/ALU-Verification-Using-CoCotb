import cocotb
import random
from cocotb.clock import Clock
from cocotb.handle import Force
from cocotb.triggers import RisingEdge, FallingEdge, ReadWrite
from random import randint


@cocotb.test()
async def tb_ALU(dut):   
    # Clock and Reset setup
    clk = Clock(dut.clk,20, units="ns")
    await cocotb.start(clk.start())
    dut.rst.value = Force(0)
    await FallingEdge(dut.clk)
    dut.rst.value = Force(1)

    # Function to drive inputs and check outputs
    async def check_alu(A, B, Sel, expected_Y, expected_C):
        dut.A   = A
        dut.B   = B
        dut.Sel = Sel

        await RisingEdge(dut.clk)
        await ReadWrite();

        Y = int(dut.Y.value)
        C = int(dut.C.value)

        if(Y == expected_Y and C == expected_C):
            cocotb.log.info(f"Test passed for Sel={bin(Sel)}, A={bin(A)}, B={bin(B)}: Y={bin(Y)}, C={bin(C)}")
        else:
            cocotb.log.info(f"Test failed for Sel={bin(Sel)}, A={bin(A)}, B={bin(B)}: Y={bin(Y)}, C={bin(C)}")
            
    # Function to generate expected_Y and expected_C
    def generate_outputs(A, B, Sel):
        if(Sel == 0b00):
            Y = (A + B) & 0xFF
            C = (A + B) >> 8
        elif (Sel == 0b01):
            Y = (A - B) & 0xFF
            C = 1 if A >= B else 0
        elif (Sel == 0b10):
            Y = A & B
            C = 0
        else:
            Y = A | B
            C = 0
        return (Y, C) 

    # Stimulus generation
    for x in range(20):
        A = randint(0,255)
        B = randint(0,255)
        Sel = randint(0,3)
        expected_Y, expected_C = generate_outputs (A, B, Sel)
        await check_alu(A, B, Sel, expected_Y, expected_C)
