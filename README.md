## 🧠 Brain Tumor Classification using Transfer Learning

<p align="center">
 
</p>

<p align="center">
  <a href="https://brain-tumor-classifiers.streamlit.app/"><img src="https://img.shields.io/badge/Live%20Demo-Streamlit-green?style=for-the-badge&logo=streamlit" /></a>
  <a href="#"><img src="https://img.shields.io/github/license/yourusername/brain-tumor-classifier?style=for-the-badge" /></a>
</p>

---

### 📖 Abstract

Brain tumors are abnormal growths in the brain that can be life-threatening. Accurate and early diagnosis is essential for effective treatment. This project leverages **transfer learning** using a pre-trained deep learning model (`pneumonia.h5`) to **classify brain MRI images** into tumor and non-tumor categories.

We built an **interactive Streamlit web application** that enables users to upload MRI images and receive real-time predictions, improving accessibility for non-technical users.

---

### 🚀 Key Features

* ✅ Binary classification: Tumor vs. No Tumor
* 🧠 Transfer learning with fine-tuned CNN model
* 🖼️ Real-time image upload and prediction
* 📊 Model trained and evaluated on curated MRI dataset
* 🌐 Deployed with Streamlit cloud

---

### 🧪 Dataset Used

* The dataset consists of **human brain MRI images** labeled as:

  * **No Tumor**
  * **Tumor**
* The images were resized and preprocessed for model compatibility (grayscale, resizing, normalization).
* Data Augmentation and preprocessing was applied using Keras utilities.

---

### 🧠 Methodology

```text
                 +----------------------+
                 |   Input MRI Image    |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |    Preprocessing     |
                 | (resize, normalize)  |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |  CNN Feature Extractor|
                 |  (Transfer Learning) |
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |  Fully Connected Layer|
                 +----------------------+
                            |
                            v
                 +----------------------+
                 |  Tumor / No Tumor   |
                 +----------------------+
```

---

### 📂 Folder Structure

```
├── README.md
├── requirements.txt
├── app.py                    # Streamlit app
├── pneumonia.h5              # Trained Keras model
├── upload_image              # Folder for image uploads
└── assets/                   # (Optional) Icons or sample data
```

---

### ⚙️ Installation & Usage

#### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/brain-tumor-classifier.git
cd brain-tumor-classifier
```

#### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### ▶️ 3. Run the Streamlit App Locally

```bash
streamlit run app.py
```

#### 🌐 4. Or Try it Online

👉 [Click to Launch the Live App](https://brain-tumor-classifiers.streamlit.app/)

---

### 🖼️ Sample Output

<p align="center">
  <img src="./d6fa2fa5-4048-441c-9f7a-203f4334cbdb.png" alt="Sample Output" width="600"/>
</p>

---

### 📈 Model Performance

| Metric    | Value |
| --------- | ----- |
| Accuracy  | \~96% |
| Precision | High  |
| Recall    | High  |
| Loss      | Low   |

Model was evaluated using standard classification metrics on a held-out test set.

---

### 🛣 Future Scope

* 🔄 Multi-class classification (e.g., Glioma, Meningioma, Pituitary)
* 🔬 Integration with explainable AI (Grad-CAM)
* ☁️ Integration with cloud platforms for scalable deployment
* 📲 Mobile app version using TensorFlow Lite

---

### 📜 License

This project is open-source under the [MIT License](LICENSE).

---

### 📧 Contact

**Akshwin T**
Data Scientist | AI Engineer | Web Developer
📫 [akshwin@example.com](mailto:akshwin@example.com)
🌐 [LinkedIn](https://linkedin.com/in/akshwin) | [Portfolio](https://akshwin.dev)

---

### ⭐ Star the Repo

If you found this project useful, consider starring it! ⭐

---