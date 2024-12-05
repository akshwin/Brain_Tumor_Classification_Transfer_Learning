import streamlit as st 
from PIL import Image
from tensorflow.keras.utils import load_img,img_to_array
import numpy as np 
from keras.models import load_model 

model = load_model ("brain_tumor.h5")
labels ={0:'Glioma',1:'Meningioma',2:'Notumor',3:'Pituitary'}
tumor = {'Glioma','Meningioma','Pituitary'}
notumor = {'Notumor'}

def processed_img(img_path):
    img=load_img(img_path,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    return res.capitalize()

def run():
    st.title("Brain Tumor Classifier 🧠")
    st.subheader("Upload the MRI Image:")
    
    st.sidebar.header(" 📌 About the projet :")
    st.sidebar.write("📌 The project is developed using CNN Arcitectures such as VGG-16, InveptionNet, XceptionNet and DenseNet121.")
    st.sidebar.write("'📌 The different types of tumor that the model identifies are Glioma , Meningioma , Pituitary")
    st.sidebar.write("📌 The model acheived an accuracy of 95.3% when XceptionNet is used.")

    img_file = st.file_uploader("Choose an image",type=['jpg','jpeg','png'])

    if img_file is not None :
        img  = Image.open(img_file).resize((250,250))
        st.image(img)
        save_image_path = './upload_image/'+img_file.name
        with open(save_image_path,"wb") as f:
            f.write(img_file.getbuffer())

        if img_file is not None :
            result = processed_img(save_image_path)
            if result in tumor:
                st.error('**TUMOR DETECTED!!**')
                st.info("**Predicted tumor in the brain is "+  result+" Tumor**")
            else :
                st.success('**NO TUMOR!!**')
run()
