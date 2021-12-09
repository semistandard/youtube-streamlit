import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'
# if st.checkbox('Show Image'):
#     img = Image.open('jaco.png')
#     st.image(img, caption='jaco',use_column_width=True)

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'    

left_column,right_columun = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_columun.write('ここは右からむ')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせの解答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')


# option = st.text_input('あなたの趣味は？')
# condition = st.slider('あなたの今の調子は？',0,100,50)


# 'あなたの趣味：',option

# 'コンディション：',condition