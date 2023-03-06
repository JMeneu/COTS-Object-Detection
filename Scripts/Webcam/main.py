from ultralytics import YOLO

model = YOLO('/Users/jorgemeneumoreno/JupyterNotebooks/Computer Vision/Individual Assignment/nano.pt')

results = model.predict(source = 0, show = True)


