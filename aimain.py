import config
import subprocess
import numpy as np
import tensorflow as tf
import importlib.metadata
import matplotlib.pyplot as plt

try:
   
    print(f"TF Lite loaded from TensorFlow version: {tf.__version__}")
    
    interpreter = tf.lite.Interpreter(model_path="voltage_model.tflite")
    interpreter.allocate_tensors()
except Exception as e:
    print(f"Critical Error: Could not load TFLite model. {e}")
    interpreter = None

# this allows the AI to specify how the data is going to be processed
def predict_voltage_output(component_id):
    """
    component_id: 0 for CPU, 1 for RAM, 2 for Fans
    """
    if interpreter is None:
        return None
     
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    input_data = np.array([[component_id]], dtype=np.float32)
    
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])
    
    return float(prediction[0][0])

suggested_voltage = predict_voltage_output(0)
suggested_voltage1 = predict_voltage_output(1)
suggested_voltage2 = predict_voltage_output(2)
suggested_voltage3 = predict_voltage_output(3)
suggested_voltage4 = predict_voltage_output(4)
suggested_voltage5 = predict_voltage_output(5)
suggested_voltage6 = predict_voltage_output(6)
# this allows the AI to decide the voltage and fails if none of these conditions are met
if suggested_voltage is not None:
    print(f"The AI Suggested this for the CPU Voltage: {suggested_voltage:.3f}V")
    print(f"The AI Suggested this for the RAM Voltage: {suggested_voltage1:.3f}V")
    print(f"The AI Suggested this for the fans Voltage: {suggested_voltage2:.3f}V")
    print(f"The AI Suggested this for the motherboard Voltage: {suggested_voltage3:.3f}V")
    print(f"The AI Suggested this for the HDD Voltage: {suggested_voltage4:.3f}V")
    print(f"The AI Suggested this for the Optical Disk Drive Voltage: {suggested_voltage5:.3f}V")
    print(f"The AI Suggested this for the Memory Card Reader Voltage: {suggested_voltage6:.3f}V")
    actual_min = min(config.cpuV)
    actual_max = max(config.cpuV)
    print(f"This is the actual Data Range: {actual_min}V - {actual_max}V")
else:
    print("Inference failed. Check if 'voltage_model.tflite' is in your folder.")

def create_ai_data_graphs():

    # This clears the graphs made in config.py so the graphs won't overlap
    plt.clf()   

    plt.subplot(3, 3, 1)
    # In plt.scatter, I had to create duplicate values so it won't cause conficts. If i didn't use the duplicate values, it wouldn't work as it is not able to point
    # float values in a scatter plot
    plt.scatter(range(len(config.cpuV0)), config.cpuV, color='#72b3e8')
    plt.title("AI suggested CPU voltage", fontsize=7)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')

    plt.subplot(3, 3, 2)
    plt.scatter(range(len(config.ramV1)), config.ramV, color='#72b3e8')
    plt.title("AI suggested RAM voltage", fontsize=7)
    plt.xlabel('Voltage (V)')

    plt.subplot(3, 3, 3)
    plt.scatter(range(len(config.fansV2)), config.fansV, color='#72b3e8')
    plt.title("AI suggested fans voltage", fontsize=7)
    plt.xlabel('Voltage (V)')

    plt.subplot(3, 3, 4)
    plt.scatter(range(len(config.boardV3)), config.boardV, color='#72b3e8')
    plt.title("AI suggested Motherboard voltage", fontsize=7)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')

    plt.subplot(3, 3, 5)
    plt.scatter(range(len(config.hddV4)), config.hddV, color='#72b3e8')
    plt.title("AI suggested HDD voltage", fontsize=7)
    plt.xlabel('Voltage (V)')

    plt.subplot(3, 3, 6)
    plt.scatter(range(len(config.opV5)), config.opV, color='#72b3e8')
    plt.title("AI suggested Optical Disk Drive voltage", fontsize=7)
    plt.xlabel('Voltage (V)')

    plt.subplot(3, 3, 7)
    plt.scatter(range(len(config.memCrdV6)), config.memCrdV, color='#72b3e8')
    plt.title("AI suggested Memory Card Reader voltage", fontsize=7)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig('graphs_ai.png')


create_ai_data_graphs()