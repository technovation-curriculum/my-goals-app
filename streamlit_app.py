import streamlit as st
st.title("🎯 My goals for the month")
goals = st.session_state.get("goals", [])
new_goal = st.text_input("Write a new goal:")

if st.button("Add goal"):
    if new_goal:
        goals.append({"text": new_goal, "completed": False})
        st.session_state.goals = goals

st.write("### Goal List:")
for i, goal in enumerate(goals):
    completed = st.checkbox(goal["text"], value=goal["completed"], key=i)
    goals[i]["completed"] = completed
