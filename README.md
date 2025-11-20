# AI_workout_recommendation
A Streamlit-powered fitness assistant using an LLM to generate personalized workout plans. Includes BMI-based progress prediction, weekly target estimation, and SQLite user data storage. Built with Python, OpenAI API, virtual environment setup, and an advanced prediction model for safe, beginner-friendly fitness guidance.

Setup Instructions:
1. Clone the Repository
2. Create a Virtual Environment
3. Activate the Virtual Environment
4. Install Dependencies
5. Add Your OpenAI API Key
6. Run the App (streamlit run app.py)

Tech Stack Used:
Frontend
1.Streamlit – lightweight web UI for Python projects
Backend
OpenAI API – used to generate customized workout plans
Python-dotenv – secure environment variable handling
SQLite3 – local database for storing user workout reports

Predictive Logic:
the number of weeks required to reach a user’s target weight using a formula based on
1. Body Mass Index (BMI)
BMI = weight / height

2. Activity Level Multiplier

| Activity Level | Multiplier |
| -------------- | ---------- |
| Low            | 0.7        |
| Moderate       | 1.0        |
| High           | 1.3        |

3. Fitness Goal Multiplier

| Goal            | Multiplier |
| --------------- | ---------- |
| Weight Loss     | 1.2        |
| Muscle Gain     | 0.7        |
| Endurance       | 0.9        |
| General Fitness | 1.0        |

4.Equipment Multiplier

| Equipment              | Multiplier |
| ---------------------- | ---------- |
| Bodyweight only        | 1.0        |
| Dumbbells / Resistance | 1.1        |
| Full Gym               | 1.3        |

5. Weekly Progress Calculation
Clamped between 0.3 and 1.8 kg per week for realism.

6. Final Weeks Estimate
Returned as a rounded integer (e.g., “~9 weeks”).

Example Output:

User Input:
Name: John
Age: 28
Gender: Male
Height: 175 cm
Current Weight: 85 kg
Target Weight: 75 kg
Activity Level: Moderate
Fitness Goal: Weight Loss
Equipment: Dumbbells + Bodyweight

Output:
Recommended Workout Plan:
- Warm-up: Jumping Jacks (2 mins), Shoulder Rotations (1 min)
- Strength: Dumbbell Squats (3x12), Push-ups (3x10), Dumbbell Rows (3x12)
- Cardio: Skipping (10 mins)
- Cooldown: Stretching (5 mins)

Predicted Time to Achieve Target: ~9 weeks

Database:
User records are saved automatically into user.db




