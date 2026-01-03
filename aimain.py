import config
import subprocess
import numpy as np
import tensorflow as tf
import importlib.metadata

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

# this allows the AI to decide the voltage and fails if none of these conditions are met
if suggested_voltage is not None:
    print(f"The AI Suggested this for the CPU Voltage: {suggested_voltage:.3f}V")
    actual_min = min(config.cpuV)
    actual_max = max(config.cpuV)
    print(f"This is the actual Data Range: {actual_min}V - {actual_max}V")
else:
    print("Inference failed. Check if 'voltage_model.tflite' is in your folder.")