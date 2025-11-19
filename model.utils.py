import math

# ADVANCED PREDICTION MODEL
def advanced_prediction(height, current_weight, target_weight, activity_level, fitness_goal, equipment):

    height_m = height / 100
    bmi = current_weight / (height_m ** 2)

    # Base metabolic factors
    base_loss = 0.4 if bmi < 25 else 0.7 if bmi < 30 else 1.1

    # Activity multipliers
    activity_mult = {"Low": 0.7, "Moderate": 1.0, "High": 1.3}[activity_level]

    # Goal multipliers
    goal_mult = {"Weight Loss": 1.2, "Muscle Gain": 0.7, "Endurance": 0.9, "General Fitness": 1.0}[fitness_goal]

    # Equipment intensity
    eq = equipment.lower()
    equip_mult = 1.0
    if "dumbbell" in eq or "resistance" in eq:
        equip_mult = 1.1
    if "gym" in eq:
        equip_mult = 1.3

    # Final weekly kg change
    weekly_kg = base_loss * activity_mult * goal_mult * equip_mult
    weekly_kg = max(0.3, min(weekly_kg, 1.8))

    diff = abs(current_weight - target_weight)
    weeks = diff / weekly_kg

    return weeks, bmi
