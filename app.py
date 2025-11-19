import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

from db import init_db, save_user_data
from model_utils import advanced_prediction

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize database
init_db()

st.title("🏋️ Advanced AI Workout Recommendation System")

st.write("Fill in your details to generate a personalized workout plan and progress prediction.")

# -----------------------------------------
# USER INPUT
# -----------------------------------------
name = st.text_input("Name")
age = st.number_input("Age", 10, 90)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", 100, 250)
current_weight = st.number_input("Current Weight (kg)", 20, 300)
target_weight = st.number_input("Target Weight (kg)", 20, 300)
activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
fitness_goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Endurance", "General Fitness"])
equipment = st.text_input("Equipment (e.g., Dumbbells + Bodyweight)")

# -----------------------------------------
# GENERATE
# -----------------------------------------
if st.button("Generate Workout Plan"):

    weeks_needed, bmi = advanced_prediction(
        height, current_weight, target_weight,
        activity_level, fitness_goal, equipment
    )

    with st.spinner("AI is generating your optimized workout plan..."):

        prompt = f"""
        Generate a beginner-friendly workout plan.

        Format EXACTLY LIKE THIS:

        - Warm-up: ...
        - Strength: ...
        - Cardio: ...
        - Cooldown: ...

        User Data:
        Name: {name}
        Age: {age}
        Gender: {gender}
        Height: {height}
        Current Weight: {current_weight}
        Target Weight: {target_weight}
        Activity Level: {activity_level}
        Fitness Goal: {fitness_goal}
        Equipment: {equipment}

        Keep plan simple and safe.
        """

        ai_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )

    workout_plan = ai_response.choices[0].message.content.strip()

    # FORMAT OUTPUT
    final_output = f"""
Recommended Workout Plan:
{workout_plan}

Predicted Time to Achieve Target: ~{weeks_needed:.0f} weeks
"""

    st.subheader("🏆 Your Plan")
    st.text(final_output)

    # SAVE TO DATABASE
    save_user_data({
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "current_weight": current_weight,
        "target_weight": target_weight,
        "activity_level": activity_level,
        "fitness_goal": fitness_goal,
        "equipment": equipment,
        "workout_plan": workout_plan,
        "predicted_weeks": round(weeks_needed, 2)
    })

    st.success("User data saved to database successfully!")
