import streamlit as st
from blooms.pipeline.prediction import PredictionPipeline

obj = PredictionPipeline()


def homePage():
    return "Hello World"


def main():
    st.title("Blooms taxonomy level Detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Blooms level detection ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    input = st.text_area("Question Statement", "Type here")
    output = ""

    if st.button("Predict"):
        output = obj.predicter([input])
    st.success("The predicted output is {}".format(output))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")


if __name__ == "__main__":
    main()
