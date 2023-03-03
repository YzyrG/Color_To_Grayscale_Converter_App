import streamlit as st
from PIL import Image  # pillow package

st.subheader("Color to Grayscale Converter")


# 通过上传获取图像
uploaded_image = st.file_uploader("Upload Image")

# 未上传图片之前uploaded_image值为None会报错, 判断有值时再处理成灰度
if uploaded_image:
    # 创建一个pillow image 实例
    img = Image.open(uploaded_image)
    # 将pillow image 转为 grayscale
    gray_upload_img = img.convert('L')
    # 网页显示转换后的grayscale
    st.image(gray_upload_img)


# 通过摄像头获取照片
with st.expander("Start Camera"):
    # 开启摄像头
    camera_photo = st.camera_input("Camera")

# 未take photo之前camera_photo值为None会报错, 判断有值时再处理成灰度
if camera_photo:
    # 创建一个pillow image 实例
    img = Image.open(camera_photo)
    # 将pillow image 转为 grayscale
    gray_camera_img = img.convert('L')
    # 网页显示转换后的grayscale
    st.image(gray_camera_img)