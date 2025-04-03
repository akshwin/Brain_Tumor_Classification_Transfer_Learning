# Brain Tumor Classification using Transfer Learning

## Overview
This project aims to classify brain tumors from MRI scans using deep learning techniques, specifically leveraging transfer learning. The model is trained on a dataset containing MRI images classified into four categories: **glioma, meningioma, pituitary tumor, and no tumor**. 

## Dataset
The dataset used in this project is a combination of:
- **Figshare dataset**
- **SARTAJ dataset**
- **Br35H dataset**

Total images: **7023**
- Glioma
- Meningioma
- Pituitary
- No Tumor (extracted from Br35H dataset)

## Approach
This project utilizes **transfer learning** with pre-trained Convolutional Neural Networks (CNNs). The following architectures are evaluated:
- **VGG16**
- **ResNet50**
- **InceptionV3**
- **Xception**
- **DenseNet121**

## Methodology
1. **Data Preprocessing**
   - Image resizing to match input size of pre-trained models
   - Normalization
   - Data augmentation to improve generalization
   
2. **Model Training**
   - Pre-trained CNN architectures are used as feature extractors
   - Fully connected layers are added for classification
   - Fine-tuning is performed on selected layers
   
3. **Evaluation Metrics**
   - Accuracy
   - Precision
   - Recall
   - F1-score
   - Confusion Matrix

## Installation
To run the project, follow these steps:

### Requirements
- Python 3.x
- TensorFlow/Keras
- NumPy
- OpenCV
- Matplotlib
- Scikit-learn

### Setup
```sh
# Clone the repository
git clone https://github.com/your-repo/brain-tumor-classification.git
cd brain-tumor-classification

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. Place the dataset in the appropriate folder.
2. Run the training script:
   ```sh
   python train.py
   ```
3. Evaluate the model:
   ```sh
   python evaluate.py
   ```
4. Predict on a new MRI image:
   ```sh
   python predict.py --image path/to/image.jpg
   ```

## Results
The best-performing model is **[insert best model name]**, achieving:
- Accuracy: **96%**
- Precision: **XX%**
- Recall: **XX%**

## Future Work
- Experiment with additional CNN architectures
- Hyperparameter tuning for further performance improvement
- Deploy as a web-based application for real-world use

## Acknowledgments
- Research papers on transfer learning and medical image classification
- The authors of the datasets used

## License
This project is licensed under the MIT License. See the LICENSE file for details.

