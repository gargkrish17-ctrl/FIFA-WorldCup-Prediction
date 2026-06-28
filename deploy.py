import streamlit as st
import pandas as pd

schedule = pd.read_csv("schedule_2026.csv")
nb_prob = pd.read_csv("NB_probability.csv")
rf_prob = pd.read_csv("RF_probability.csv")
matches = []
for i,row in schedule.iterrows():
    match = str(row["Date"]) + "  ->  " + row["home_team"] + " vs " + row["away_team"]
    matches.append(match)

st.title("Fifa Predictor App")
st.markdown('BY KRISH GARG')
st.markdown("> This is fifa match winner predictor based on ML model predictions")

st.sidebar.header("MODEL SELECTION")
model_choice = st.sidebar.selectbox("Select the model to know about its evaluation metrics", ["NONE", "NAIVE BAYES", "RANDOM FOREST", "BOTH"])
if model_choice == "NAIVE BAYES":
    st.sidebar.write("NAIVE BAYES")
    st.sidebar.text(
        """
        Accuracy  :  60.93%
        Precision :  64.50%
        Recall    :  55.29%
        F1_score  :  54.04%
        """
        )

elif model_choice == "RANDOM FOREST":
    st.sidebar.write("RANDOM FOREST")
    st.sidebar.text(
            """
            Accuracy  :  59.37%
            Precision :  55.29%
            Recall    :  53.62%
            F1_score  :  52.79%
              """
            )

elif model_choice == "BOTH":
    col1, col2 = st.columns(2)

    with col1:
        st.sidebar.write("NAIVE BAYES")
        st.sidebar.text(
            """
            Accuracy  :  60.93%
            Precision :  64.50%
            Recall    :  55.29%
            F1_score  :  54.04%
            """
            )

    with col2:
        st.sidebar.write("RANDOM FOREST")
        st.sidebar.text(
                """
                Accuracy  :  59.37%
                Precision :  55.29%
                Recall    :  53.62%
                F1_score  :  52.79%
                """
                )        


st.write("")

choice = st.sidebar.selectbox("Choose model for prediction", ["NONE","NAIVE BAYES", "RANDOM FOREST"])
if choice == "NONE":
    st.warning("Please select a prediction model from the sidebar.")
if choice == "NAIVE BAYES":
    st.sidebar.text("You have chosen NAIVE BAYES")

if choice == "RANDOM FOREST":
    st.sidebar.text("You have chosen RANDOM FOREST")

st.write("")

match_data = st.selectbox("Choose the match to predict", ["NONE"]+matches)


if match_data != "NONE":
    if choice == "NONE":
        st.warning("Please select a prediction model from the sidebar.")
    if match_data:
        match_index = matches.index(match_data)
        if choice == "NAIVE BAYES":
            st.write("HOME WIN % : ",nb_prob.iloc[match_index]["Home Win %"])
            st.write("AWAY WIN % : ",nb_prob.iloc[match_index]["Away Win %"])
            st.write("DRAW % : ",nb_prob.iloc[match_index]["Draw %"])

        if choice == "RANDOM FOREST":
            st.write("HOME WIN % : ", rf_prob.iloc[match_index]["Home Win %"])
            st.write("AWAY WIN % : ",rf_prob.iloc[match_index]["Away Win %"])
            st.write("DRAW % : ",rf_prob.iloc[match_index]["Draw %"])

