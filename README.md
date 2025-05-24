🧠 Skin Disorder Diagnosis with Deep Learning
An AI-powered web application that assists in diagnosing common skin conditions such as psoriasis and chickenpox using a convolutional neural network (CNN). Trained on a limited dataset, the model achieves 97% accuracy and is deployed for public access via a cloud server.

🔗 Live Demo: fouman-ai.onrender.com
⚠️ Note: The server is was hosted on a free plan and had resource limitations. For best results, we used small image files. the Demo is currently unavailable.

📌 Project Overview
In recent years, artificial intelligence has made significant contributions to medicine. One of the key applications of image processing in healthcare includes tumor detection in CT scans, bone deformity identification, patient status monitoring, and more.

This project focuses on diagnosing skin diseases—specifically psoriasis and chickenpox—using deep learning techniques. The model was trained using a limited dataset comprising images of both conditions and healthy skin. It was then integrated into a Flask-based web app, allowing users to upload an image and receive an instant prediction.

🚀 Features
Detects psoriasis, chickenpox, or healthy skin from an image

Deep CNN architecture trained to 97% accuracy

Web-based interface for ease of access

Fully functional deployment on Render

🖼️ Screenshots
(Add screenshots of the web interface and sample results here if possible)

🧪 Tech Stack
Python

TensorFlow / Keras

Flask

HTML/CSS (Jinja templates)

Render (deployment)

🛠 Installation
To run the project locally:

bash
Copy
Edit
# Clone the repo
git clone https://github.com/ArefCheraghali/skin-disorder-diagnosis
cd skin-disorder-diagnosis

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Then visit http://localhost:5000 in your browser.

🧠 Model Training 
To retrain the model:

Place your dataset in the correct directory

Run the training script (if included, e.g. train.py)

Save and export the .h5 model file

Update the app’s model loading path accordingly

📦 Deployment Notes
The app is hosted on Render using a free tier. This means:

The server may take a few seconds to wake up on first load.

Heavy or large image files might lead to a timeout or crash.

Please use small, optimized images (e.g., <1MB) for reliable results.

📬 Contact
For questions or collaborations:

GitHub: @ArefCheraghali
