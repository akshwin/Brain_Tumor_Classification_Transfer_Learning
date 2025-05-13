# 🧠 Brain Tumor Classification Using Transfer Learning 

This is a **Streamlit-based web application** that uses a **deep learning model** to classify brain tumors from MRI scans. The model can detect four classes:

* **Glioma Tumor**
* **Meningioma Tumor**
* **Pituitary Tumor**
* **No Tumor**

The app provides an intuitive interface to upload an MRI scan and receive instant predictions powered by a trained **CNN model**.

---

##  Model Architecture
The deep learning model follows this architecture:


Input image → CNN base layers → Flatten → Dense layers → Output class

## 🚀 Demo

📍 Live Demo: brain-tumor-classifier-app.streamlit.app
> Upload an MRI image, and the AI will tell you whether it shows a tumor — and if so, what kind!

---

## 🔍 Features

* 🎯 **High Accuracy**: Best-performing model achieved **95.3% accuracy** (XceptionNet).
* 🖼 **Image Upload**: Upload MRI scans in `.jpg`, `.jpeg`, or `.png` formats.
* 🤖 **Deep Learning Based**: Built using **Keras/TensorFlow** with **Transfer Learning**.
* 📊 **Confidence Score**: Displays prediction confidence to gauge model certainty.
* 📁 **Clean UI**: Minimalistic and informative layout with sidebar information.

---

## 🧠 Model Details

* **Architectures Evaluated**:

  * VGG16
  * XceptionNet
  * InceptionNet
  * DenseNet121
* **Best Model**: XceptionNet with **95.3%** accuracy
* **Input Size**: 224x224 pixels
* **Output Classes**: Glioma, Meningioma, Pituitary, No Tumor

---

## 📂 Dataset

* Aggregated from **public medical MRI datasets**
* Preprocessed, augmented, and resized to 224x224
* Over **7000 labeled images**

---

## 🛠 Tech Stack

* Python
* Streamlit
* TensorFlow / Keras
* PIL, NumPy
* Web deployment (can be done via Streamlit Sharing, Render, or Heroku)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/brain-tumor-classifier.git
   cd brain-tumor-classifier
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Place your trained model** (`brain_tumor.h5`) in the root directory.

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

---

## 📁 Folder Structure

```
brain-tumor-classifier/
├── app.py                # Main Streamlit application
├── brain_tumor.h5        # Trained model (not included in repo)
├── requirements.txt      # Python dependencies
└── upload_image/         # Temporary folder for uploaded images
```

---

## 📧 Contact

Developed by **Akshwin T**

📬 Email: [akshwint.2003@gmail.com](mailto:akshwint.2003@gmail.com)

---

## ⚠️ Disclaimer

> This application is intended for **educational and research purposes only**. It is not a replacement for professional medical advice or diagnosis.

---

## 🌟 Acknowledgements

* Open-source medical imaging datasets (Figshare, Br35H, SARTAJ, etc.)
* TensorFlow/Keras community
* Streamlit for rapid web prototyping
