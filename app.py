import streamlit as st
from PIL import Image
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
from keras.models import load_model
import os

# Load the trained model
model = load_model("brain_tumor.h5")

# Labels for prediction output
labels = {0: 'Glioma', 1: 'Meningioma', 2: 'Notumor', 3: 'Pituitary'}
tumor_types = {'Glioma', 'Meningioma', 'Pituitary'}

# Image Preprocessing and Prediction
def processed_img(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)[0]
    predicted_class = np.argmax(prediction)
    confidence = round(np.max(prediction) * 100, 2)
    label = labels[predicted_class]
    return label.capitalize(), confidence

# Main App Function
def run():
    st.set_page_config(page_title="Brain Tumor Classifier", layout="centered", page_icon="🧠")
    
    # Title and Description
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>🧠 Brain Tumor Classification </h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center;'>Upload an MRI image or use a sample image to detect the presence of a brain tumor.</p>", 
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🧠 Project Info")
        st.markdown("""
        This application uses **deep learning models** to detect brain tumors from MRI images.  
        Powered by **Convolutional Neural Networks (CNNs) and Transfer learning** trained on real medical data.
        """)

        with st.expander("🔍 Model Details"):
            st.markdown("""
            - **Architectures Used**:  
              - VGG16  
              - XceptionNet  
              - InceptionNet  
              - DenseNet121  
            - **Best Accuracy**: 95.3% (VGG-16)
            """)

        with st.expander("📂 Classes Detected"):
            st.markdown("""
            - 🧬 **Glioma Tumor**  
            - 🧠 **Meningioma Tumor**  
            - 🕳️ **Pituitary Tumor**  
            - ✅ **No Tumor**
            """)

        with st.expander("📁 Dataset Info"):
            st.markdown("""
            - Aggregated from public datasets  
            - Thousands of labeled MRI images  
            - Preprocessed and resized to 224x224 pixels
            """)

        st.markdown("---")
        st.markdown("👨‍💻 Developed by Akshwin T ")
        st.markdown("📬 Contact: [akshwint.2003@gmail.com](mailto:akshwint.2003@gmail.com)")

    # Upload or Use Sample Image
    st.markdown("## 📤 Upload an MRI Image")
    img_file = st.file_uploader("Choose a JPG, JPEG, or PNG file", type=['jpg', 'jpeg', 'png'])

    st.markdown("### OR")
    use_sample = st.button("📷 Use Sample Image")

    if img_file or use_sample:
        if use_sample:
            sample_path = "upload_image/tumor-g.jpg"  # Ensure this file exists
            if not os.path.exists(sample_path):
                st.error("❌ Sample image not found. Please ensure 'tumor-g.jpg' exists in the 'upload_image' folder.")
                return
            save_path = sample_path
            st.image(Image.open(save_path), caption='🖼 Sample MRI Scan', width=300)
        else:
            upload_dir = "./upload_image"
            os.makedirs(upload_dir, exist_ok=True)
            save_path = os.path.join(upload_dir, img_file.name)
            with open(save_path, "wb") as f:
                f.write(img_file.getbuffer())

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(Image.open(save_path), caption='🖼 Uploaded MRI Scan', width=300)

        # Prediction
        with st.spinner("🧠 Analyzing the image..."):
            result, confidence = processed_img(save_path)

        st.markdown("### 🔍 Prediction Result")
        if result in tumor_types:
            st.error(f"🚨 **Tumor Detected: {result} Tumor**")
        else:
            st.success("✅ **No Tumor Detected**")

        st.info(f"📊 **Confidence Score: {round(confidence, 2)}%**")

        # Remove uploaded image to keep folder clean
        if not use_sample and os.path.exists(save_path):
            os.remove(save_path)

# Run the app
if __name__ == "__main__":
    run()