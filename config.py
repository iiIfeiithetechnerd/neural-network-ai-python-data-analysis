import sys
import os
import subprocess
import matplotlib as pltmain
import numpy as np
import matplotlib.pyplot as plt

# checks if hardware_details.py exists, if it does exist, this program will automatically be closed and will run the train_model.py script
if os.path.exists("hardwaredetails.py"):
    subprocess.Popen([sys.executable, "train_model.py"])
    # terminates this script
    sys.exit()


# gets the build number of the program and certain libraries that it uses
buildNum = "0.9.8"
print("Build version: ", buildNum)
print(f"MatPlotLB version: {pltmain.__version__}")
print(f"Numpy version: {np.__version__}")

# all of these scrpts follow the same structure, they just have different purposes

def voltage_input_for_cpu():
    voltage_Input_For_CPU = [0.85, 1, 1.1, 1.25, 1.3]

    voltage_Input_Text_For_CPU = ("Voltage Input for CPU (Prediction): ", voltage_Input_For_CPU)
    
    print(voltage_Input_Text_For_CPU)
    
    return voltage_Input_For_CPU
    

def voltage_input_for_ram():
    voltage_Input_For_RAM = [1.8, 1.85, 1.9]

    voltage_Input_Text_For_RAM = ("Voltage Input for RAM (Prediction): ", voltage_Input_For_RAM)
    
    print(voltage_Input_Text_For_RAM)
    
    return voltage_Input_For_RAM
    
    
def voltage_input_for_fans():
    voltage_Input_For_Fans = [11, 11.5, 11.7, 12]
    
    voltage_Input_Text_For_Fans = ("Voltage Input for CPU Fans (Prediction): ", voltage_Input_For_Fans)
    
    print(voltage_Input_Text_For_Fans)
    
    return voltage_Input_For_Fans

    
def voltage_input_for_motherboard():
    voltage_Input_For_Motherboard = [-5, -12, 5, 7.5, 12]
    
    voltage_Input_Text_For_Motherboard = ("Voltage Input for Motherboard (Prediction): ", voltage_Input_For_Motherboard)
    
    print(voltage_Input_Text_For_Motherboard)
    
    return voltage_Input_For_Motherboard
    
# this is here so the data can be graphed properly

data1 = voltage_input_for_cpu()
data2 = voltage_input_for_ram()
data3 = voltage_input_for_fans()
data4 = voltage_input_for_motherboard()

voltage_Input_For_CPU1 = [0.85, 1, 1.1, 1.25, 1.3]
voltage_Input_For_RAM1 = [1.8, 1.85, 1.9]
voltage_Input_For_Fans1 = [11, 11.5, 11.7, 12]
voltage_Input_For_Motherboard1 = [-5, -12, 5, 7.5, 12]

# this allows user interaction
cpuV = [1.232, 1.104, 3.238, 5.14, 11.776, 4.923, 3.312, 0]
ramV = [1.8, 0]
fansV = [12, 1, 1.2, 1.5, 5, 7, 0]
boardV = [12, 5, 3.3, 5, 1.2, 1.8, 12, 0]
hddV = [12, 5, 0]
opV = [12, 5, 2.5, 2, 3.3, 9, 0]
memCrdV = [5, 3.3, 1.5, 12, -12, 5, 0]



print("CPU Voltage (Actual data): ", cpuV)
print("RAM Voltage (Actual data): ", ramV)
print("Fans Voltage (Actual data): ", fansV)
print("Motherboard Voltage (Actual data): ", boardV)
print("HDD Voltage (Actual data): ", hddV)
print("Optical Disk Drive Voltage (Actual data): ", opV)
print("Memory Card Reader Voltage (Actual data): ", memCrdV)

def create_all_graphs():
    
    #This function here creates the graphs for the CPU, RAM, fans, motherboard, and does it in a way
    # so the graphs won't overlap
    
    # in plt.subplot, the first value is the number of rows, the second value is the number of columns, and the third value is the number itself.
    plt.subplot(3, 4, 1)
    plt.hist(data1, bins=5, edgecolor='#0a3659', color='#72b3e8')
    plt.title('Voltage input for CPU (Prediction)', fontsize=7)
    
    
    #Yes, this is a note to myself. I know that plotly is not being used at the moment, but it will be used in the future.
    
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')

    plt.subplot(3, 4, 2)
    plt.hist(data2, bins=3, edgecolor='#0a3659', color='#4aa4ed')
    plt.title('Voltage input for RAM (Prediction)', fontsize=7)
    
    #Yes, this is a note to myself. I know that plotly is not being used at the moment, but it will be used in the future.
    plt.xlabel('Voltage (V)')

    plt.subplot(3, 4, 3)
    plt.hist(data3, bins=4, edgecolor='#0a3659', color='#3b6d96')
    plt.title('Voltage input for Fans (Prediction)', fontsize=7)
    
    #Yes, this is a note to myself. I know that plotly is not being used at the moment, but it will be used in the future.
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')

    plt.subplot(3, 4, 4)
    plt.hist(data4, bins=5, edgecolor='#0a3659', color='#145d99')
    plt.title('Voltage input for Motherboard (Prediction)', fontsize=7)
    
    #Yes, this is a note to myself. I know that plotly is not being used at the moment, but it will be used in the future.
    plt.xlabel('Voltage (V)')
    
    plt.subplot(3, 4, 5)
    plt.plot(cpuV, color='#72b3e8')
    plt.title('Voltage Input for CPU (Actual data gathered)', fontsize=7)
    
    #Yes, this is a note to myself. I know that plotly is not being used at the moment, but it will be used in the future.
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')
    
    plt.subplot(3, 4, 6)
    plt.plot(ramV, color='#72b3e8')
    plt.title('Voltage Input for RAM (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    
    plt.subplot(3, 4, 7)
    plt.plot(fansV, color='#72b3e8')
    plt.title('Voltage Input for fans (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    
    plt.subplot(3, 4, 8)
    plt.plot(boardV, color='#72b3e8')
    plt.title('Voltage Input for Motherboard (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    
    plt.subplot(3, 4, 9)
    plt.plot(hddV, color='#72b3e8')
    plt.title('Voltage Input for HDD (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')
    
    plt.subplot(3, 4, 10)
    plt.plot(opV, color='#72b3e8')
    plt.title('Voltage Input for Optical Disk Drive (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    
    plt.subplot(3, 4, 11)
    plt.plot(memCrdV, color='#72b3e8')
    plt.title('Voltage Input for Memory Card Reader (Actual data gathered)', fontsize=7)
    plt.xlabel('Voltage (V)')
    
    plt.tight_layout()
    plt.savefig('graphs.png')
    

def output_vals():
    
    create_all_graphs()

#this is the function above

output_vals()

# this area allows users to input their own values
print("Input the values for these variables. Use numbers only. You must have at least 6 integers for best results.")
cpuV0 = list(map(int, input("Type 6 integers for the CPU voltage. ").split()))
ramV1 = list(map(int, input("Type 6 integers for the RAM voltage.").split()))
fansV2 = list(map(int, input("Type 6 integers for the fans voltage.").split()))
boardV3 = list(map(int, input("Type 6 integers for the motherboard voltage.").split()))
hddV4 = list(map(int, input("Type 6 integers for the HDD/SSD (Or any other storage device) voltage.").split()))
opV5 = list(map(int, input("Type 6 integers for the optical disk drive voltage.").split()))
memCrdV6 = list(map(int, input("Type 6 integers for the memory card voltage.").split()))

print("These are the values that you have inserted:", cpuV0, ramV1, fansV2, boardV3, hddV4, opV5, memCrdV6)

with open('hardware_details.py', "w") as f:
    f.write(repr(cpuV0))
    f.write(repr(ramV1))
    f.write(repr(fansV2))
    f.write(repr(boardV3))
    f.write(repr(hddV4))
    f.write(repr(opV5))
    f.write(repr(memCrdV6))

print("A file containing your voltage inputs has been created.")