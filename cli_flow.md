 **STEP 1 — Legal + Safety Disclaimer (required)**

- very large text, short sentences.

*Example:*

> **This app does not diagnose heart attacks.**
>   If you think you’re in immediate danger, **call emergency services now.**
>   This tool can help you decide if you should seek urgent medical care.

Add a big button:
“Call Emergency Services”(autodetect region if possible)

---

**STEP 2 — Calming Screen**

When someone is panicking, they can’t process information.So the screen will display :

* Use *soft colors*, large text
* Provide *one or two* sentences max
* Encourage deep, slow breathing

*Example:*

   You’re not alone.
 Let’s take this step by step.
 Tap **Continue** when you’re ready.


---

**STEP 3 — Quick Choice UI **
People under distress struggle with reading blocks of text.
Use large buttons like:

* **YES**
* **NO**
* **I’m not sure** (<--- helpful)

Keep each question on its own screen.

---

 **Symptom Question Flow Structure (Safe Medical UX)**

For each question:

## **(A) Question Screen**

Example:
**“Do you feel pressure, heaviness, or tightness in your chest?”**

Buttons:

* **Yes**
* **No**
* **Not sure** (leads to explanation)

---

## **(B) If “Not Sure” → Show a Symptom Description Screen**
simple language, small examples.

 It may feel like:

  A weight on your chest
  A tight bra strap
  Someone pressing with a hand
  A deep ache, not sharp

Buttons:

* **Yes, I feel this**
* **No, not like this**

---

## **(C) If “Yes” → Add to Risk Score**

the app wont say things like “you are at risk.”
rather:

 Thank you. I’ve recorded your symptom.
 Let’s continue.

---

## **(D) If “No” → Move On**

Thank you. Let’s check the next symptom.

Scoring + Outcome Messaging (Very Important)

neutral and non-medical language

Avoid:
“You are having a heart attack.”
 “You are at severe risk.”

Use:
 “Your symptoms may be serious.”
“It’s safest to get help now.”

---

# Possible Final Outcomes

**Outcome A — Emergency symptoms detected**

 Your symptoms could be serious.
 It’s safest to get urgent medical help.
 Please consider calling emergency services now.

**Buttons:**

* **Call Emergency Services**
* **Find Nearest Hospital**

---

**Outcome B — Some concerning symptoms**

 You have some symptoms that can be related to heart problems.
 We recommend contacting a doctor or calling your GP as soon as possible.

Buttons:

* **Call Doctor**
 **Find Urgent Care. eg, th NHS numbers **

---

**Outcome C — Mild / unclear symptoms**

Your answers do not strongly suggest emergency heart symptoms.
 If anything changes, or you still feel worried, please seek medical advice book an appointment with your GP.

**scoring threshold**
-Emergency-level (call ambulance)

    Score ≥ 7 OR
    Chest pain (5) + ANY symptom ≥ 3

        Examples that trigger this:
        chest (5) + shortness of breath (4) = 9
        chest (5) + sweating (3) = 8
        radiating pain (4) + shortness of breath (4) = 8
        nausea (3) + back pain (3) + fatigue (2) = 8 

    example output Message:
        Your symptoms could be serious.
        It's safest to call emergency services right now.

-Urgent evaluation, go to A&E:
        
        Score 4–6
        AND no chest-pain emergency rule triggered.

        Examples:
            nausea (3) + fatigue (2) = 5
            back pain (3) + indigestion (2) = 5
            dizziness (1) + anxiety (2) + fatigue (2) = 5
        Message:
            These symptoms may need prompt medical attention.
            Please go to A&E or urgent care as soon as possible.


-Non-urgent but follow up with GP
    Score 1–3
    Examples:
        fatigue (2)
        dizziness (1) + anxiety (2) = 3
Message:
    Your symptoms don’t strongly suggest an emergency, but it’s important to speak with a GP soon.

-No symptoms or score 0

    Your answers don't indicate typical heart-related warning signs.
    If symptoms change or worsen, seek medical care.
 
**Hard Safety Rules (override scoring)**
-override the score if these are present:

    Rule 1 — Sudden chest pain lasting >5 minutes
        Emergency

    Rule 2 — Difficulty breathing + any discomfort
        Emergency

    Rule 3 — Collapse, fainting, confusion
        Emergency
    

    Rule 4 — Pain spreading from chest to left arm/jaw/back
        Emergency, even if no chest pain reported initially(common in women)
    

    Rule 5 — “Crushing” or “tight band” sensation
     Emergency