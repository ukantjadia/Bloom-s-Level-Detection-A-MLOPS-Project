import streamlit as st
from blooms.pipeline.prediction import PredictionPipeline

obj = PredictionPipeline()


def homePage():
    return "Hello World"


def main():
    ## title 
    st.markdown(
        """<div style="
                background-color: #3498db;
                border: 2px solid #e74c3c;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                ">
                <h1 style="color: white;">Blooms level detection ML App</h1>
            </div>""",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.text("")
        st.text("")
        st.text("")
        input = st.text_area(label="Question Statement",placeholder="Enter here",height=10)
        output = ""

    with col2:
        st.text("")
        st.text("")
        st.text("")
        _,col22,_ = st.columns([.3,2.0,.0001])
        with col22:
            st.text("")
            st.text("")
            if st.button(":rainbow[Predict]",use_container_width=True):
                if not input:
                    st.toast("Question Statement is empty!!")
                else:
                    output = obj.predicter([input])
                    st.success("The predicted output is {}".format(output))
    cot = st.container()
    if cot.button("About"):
        cot.text("Lets Learn")
        cot.text("Built with Streamlit")
        

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
