import streamlit as st


name= st.text_input("Input your name: ")
father= st.text_input("Input your father name: ")
mother = st.text_input("Input your mother name: ")
text= st.text_area("Enter your text. ")
age= st.selectbox("Enter your class: ",(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
button= st.button("Done")

if button:
    st.write(f"""
          NAME: {name}\n
          FATHER NAME: {father}\n
          MOTHER NAME: {mother}\n
          TEXT: {text}\n
          AGE: {age}
          """)