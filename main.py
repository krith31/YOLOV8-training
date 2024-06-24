from ultralytics import YOLO 

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from scratch

# Use the model
results = model.train(data='C:/Users/K.S RAO/OneDrive/Documents/VS CODE FILES/PYTHON AND HTML/YOLO/config.yaml', epochs=5)  # train the model
