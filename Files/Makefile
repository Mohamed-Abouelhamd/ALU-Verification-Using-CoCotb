# First Make Venv 
# python3 -m venv venv 
# source /venv/bin/activate.csh
# pip -- version 
# U must check that pip is pointing to your venv not to the global venv of the machine 
# pip install cocotb 
# pip -- version 
# U must check that pip is pointing to your venv not to the global venv of the machine 
# now you are ok call make command 
# if it says i cant find the simulator 
# module load the simulator 
# pip -- version 
# U must check that pip is pointing to your venv not to the global venv of the machine  
# use module load out of the venv 
# then return to venv again 
gui?=1
TOPLEVEL_LANG ?= verilog
SIM ?=xcelium   
PWD=$(shell pwd)


ifeq ($(TOPLEVEL_LANG),verilog)
    VERILOG_SOURCES = $(PWD)/ALU.v
else ifeq ($(TOPLEVEL_LANG),vhdl)
    VHDL_SOURCES = $(PWD)/counter.vhdl
else
    $(error A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG))
endif

TOPLEVEL := ALU             #Module_NAME
MODULE   := Test     #File_Python_Name

# SIM_ARGS ?= -gui
include $(shell cocotb-config --makefiles)/Makefile.sim