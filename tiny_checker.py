import csv

# Symptom descriptions for "not sure" responses
DESCRIPTIONS = {
    "Chest pain or pressure": """
What it might feel like:
- A heavy weight or elephant sitting on your chest
- A tight band squeezing around your ribs
- Deep ache or pressure (not always sharp pain)

What it's usually NOT:
- Brief, sharp pains that come and go in seconds
""",
    
    "Pain radiating to arms/jaw/back": """
What it might feel like:
- Pressure, squeezing, heaviness, or a dull ache
- Pain that spreads from chest to arms, jaw, or back

What it's usually NOT:
- Sharp pain that can be pinpointed with one finger
""",
    
    "Shortness of breath": """
What it might feel like:
- "Gasping" or "choking" - severe difficulty breathing
- Effortful breathing - working harder to breathe
- Chest tightness or pressure

What it's usually NOT:
- Normal breathlessness after exercise or climbing stairs
""",
    
    "Profuse sweating": """
What it might feel like:
- Sudden, heavy sweating or a "cold sweat"
- Occurs without physical exertion or high temperatures

What it's usually NOT:
- Normal sweating from exercise, hot weather, or fever
""",
    
    "Nausea or vomiting": """
What it might feel like:
- Sudden feeling of sickness or actual vomiting
- Comes on without clear cause

What it's usually NOT:
- Nausea from food poisoning or stomach bug
""",
    
    "Upper back pain": """
What it feels like:
- Dull ache, pressure, or tightness between shoulder blades
- May feel like a rope tied around chest and back
- Doesn't change with movement

What it's usually NOT:
- Sharp pain that worsens when you press the area
""",
    
    "Jaw or neck pain": """
What it feels like:
- Aching, tightness, or discomfort in jaw, neck, or teeth
- Hard to pinpoint exact location
- May radiate from chest or arms

What it's usually NOT:
- Pain in a single tooth or specific joint
""",
    
    "Indigestion-like discomfort": """
What it feels like:
- Upper abdomen discomfort like heartburn or fullness
- Persists for more than a few minutes
- May come and go

What it's usually NOT:
- Burning that travels to throat and is quickly relieved by antacids
""",
    
    "Sudden anxiety or dread": """
What it feels like:
- Overwhelming sense of impending doom
- Sudden, unexplained fear or panic
- Feeling that something is very wrong

What it's usually NOT:
- Normal stress or worry about daily concerns
""",
    
    "Unusual fatigue": """
What it feels like:
- Overwhelming, unexplained exhaustion
- New and unusual for you
- Limits ability to do simple everyday activities

What it's usually NOT:
- Normal tiredness after a busy day that's relieved by rest
""",
    
    "Dizziness or lightheadedness": """
What it feels like:
- Sudden feeling of unsteadiness or like you might faint
- Especially with other symptoms like shortness of breath

What it's usually NOT:
- Momentary lightheadedness from standing up too quickly
""",
}

def load_symptoms():
    import os
    
    symptoms = []
    with open('C:/Users/alhaw/Downloads/book cover/math/CREST/symptoms_table.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            symptom_name = row['symptom']
            weight = int(row['prelim_weight'])
            symptom_dict = {"name": symptom_name, "weight": weight}
            symptoms.append(symptom_dict)
    
    return symptoms
def ask_question(symptom_name, weight):
    print(f"\nDo you have {symptom_name}?")
    answer = input("Answer (yes/no/not sure): ").lower().strip()
    

    while answer == "not sure":
        print(DESCRIPTIONS[symptom_name])
        print(f"\nDo you have {symptom_name}?")
        answer = input("Answer (yes/no/not sure): ").lower().strip()
    if answer == "yes":
        return weight
    else:
        return 0 


def has_symptom(user_symptoms, symptom_name):
    for symptom in user_symptoms:
        if symptom["name"] == symptom_name:
            return True
    return False

def calculate_risk(user_symptoms, total_score):
    # Safety Rule 1: Chest pain + any other symptom ≥3
    if has_symptom(user_symptoms, "Chest pain or pressure"):
        for symptom in user_symptoms:
            if symptom["weight"] >= 3 and symptom["name"] != "Chest pain or pressure":
                return "Emergency"
    #safety rule 2: shortness of breath & any other symptom 
    if has_symptom(user_symptoms, "Shortness of breath"):
        if len(user_symptoms)>1:
                return"Emergency"
    #safety rule 4: pain radiating to arms/jaw/back, even without chest pain.women often experaince it with the classic chest pain. 
    if has_symptom(user_symptoms, "Pain radiating to arms/jaw/back"):
        return "Emergency"

    
    # If no safety rules triggered, use score thresholds
    if total_score >= 7:
        return "Emergency"
    elif total_score >= 4:
        return "A&E"
    elif total_score >= 1:
        return "GP"
    else:
        return "Monitor"
    
def main():
    print("=" * 50)
    print("HEART SYMPTOM CHECKER")
    print("=" * 50)
    print("This tool does NOT diagnose heart attacks.")
    print("If you're in immediate danger, call 999 now!")
    print("=" * 50)
    input("\nPress Enter to continue...")
    
    symptoms = load_symptoms()    
    user_symptoms = []  # Store symptoms they report
    total_score = 0     # Running total of weights
    for symptom in symptoms:
        result = ask_question(symptom["name"], symptom ["weight"])
        if result > 0: 
            user_symptoms.append(symptom)#this adds the symptom to the list AND adds the weight to the total!
            total_score += result 
    risk_level = calculate_risk(user_symptoms, total_score)
    show_outcome(risk_level)

def show_outcome(risk_level):
    if risk_level == "Emergency":
        print("\nYour symptoms could be serious. It's safest to call emergency services right now.")
    elif risk_level == "A&E":
        print("\nThese symptoms may need prompt medical attention. Please go to A&E or urgent care as soon as possible.")
    elif risk_level == "GP":
        print("\nYour symptoms don't strongly suggest an emergency, but it's important to speak with a GP soon.")
    else:
        print("\nYour answers don't indicate typical heart-related warning signs. If symptoms change or worsen, seek medical care.")
if __name__ == "__main__":
    main()
   
# STARTS with: List of all symptoms the user said YES to (with their weights)
# DOES: 
#   - Adds up all the weights
#   - Checks safety rules (chest pain + other symptom, etc.)
#   - Compares total score to thresholds:
#       ≥7 = Emergency
#       4-6 = A&E
#       1-3 = GP
#       0 = Monitor
# PRODUCES: The risk category (Emergency/A&E/GP/Monitor)
    
    # Step 6: Show outcome
    # TODO: Call show_outcome()


# DATA STRUCTURES ILL USE:

# 1. Symptom list (loaded from CSV):
# symptoms = [
#     {"name": "Chest pain", "weight": 5, "description": "..."},
#     {"name": "Nausea", "weight": 3, "description": "..."},
# ]

# 2. User's responses (built as Application asks questions):
# user_symptoms = [
#     {"name": "Chest pain", "weight": 5},
#     {"name": "Nausea", "weight": 3},
# ]
# total_score = 8  # Running total

# 3. Final risk level (calculated at the end):
# risk_level = "Emergency"  # or "A&E" or "GP" or "Monitor"



# TINY_CHECKER.PY - Structure Plan

# Mini-machine #1: load_symptoms()
# STARTS with: The filename "symptoms_table.csv"
# DOES: 
#   - Opens the CSV file
#   - Reads each row (symptom name and weight)
#   - Puts all symptoms into a list
# PRODUCES: A list of symptoms with their weights
#   Example: [{"symptom": "Chest pain", "weight": 5}, {"symptom": "Nausea", "weight": 3}, ...]

# Mini-machine #2: ask_question(symptom_name, symptom_description, weight)
# STARTS with: One symptom name, its description, and its weight
# DOES:
#   - Prints the question ("Do you have [symptom]?")
#   - Gets user input (yes/no/not sure)
#   - If "not sure": shows description, asks again
#   - Records if they said YES
# PRODUCES: True (if YES) or False (if NO), and the weight if True

# Mini-machine #3: calculate_risk(symptoms_reported)
# STARTS with: List of all symptoms the user said YES to (with their weights)
# DOES:
#   - Adds up all the weights
#   - Checks safety rules (chest pain + other symptom, etc.)
#   - Compares total score to thresholds:
#       ≥7 = Emergency
#       4-6 = A&E
#       1-3 = GP
#       0 = Monitor
# PRODUCES: The risk category (Emergency/A&E/GP/Monitor)

# Mini-machine #4: show_outcome(risk_category)
# STARTS with: The risk category (Emergency, A&E, GP, or Monitor)
# DOES:
#   - Prints the appropriate message
#   - Shows emergency numbers or advice
# PRODUCES: Nothing (just displays to user)

# Mini-machine #5: main()
# This runs the whole program:
#   1. Call load_symptoms()
#   2. For each symptom, call ask_question()
#   3. Call calculate_risk()
#   4. Call show_outcome()




# Function: ask_question(symptom_name, weight)
#
# NEEDS: symptom name, weight
# DOES:
#   Step 1: Print question
#   Step 2: Get user input (yes/no/not sure)
#   Step 3: While input is "not sure":
#       - Look up description from DESCRIPTIONS dictionary
#       - Print description
#       - Ask question again
#       - Get new input
#   Step 4: If input is "yes":
#       - Return the weight
#   Step 5: If input is "no":
#       - Return 0
# RETURNS: weight (number) or 0


# Function: calculate_risk(user_symptoms, total_score)
#
# NEEDS: list of symptoms user reported, total score
# DOES:
#   Step 1: Check safety rules FIRST (override)
#       - Check if "Chest pain" in user_symptoms
#       - If yes, check if any other symptom has weight ≥3
#       - If yes → return "Emergency"
#       
#       - Check if they have chest + arm/jaw/back pain
#       - If yes → return "Emergency"
#       
#       [Add other safety rules...]
#   
#   Step 2: If no safety rules triggered, check score:
#       - If total_score ≥7 → return "Emergency"
#       - If total_score 4-6 → return "A&E"
#       - If total_score 1-3 → return "GP"
#       - If total_score 0 → return "Monitor"
#
# RETURNS: risk level (string)
# Run the program:
