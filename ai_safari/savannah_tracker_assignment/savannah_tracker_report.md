# 🧭 SAVANNAH TRACKER REPORT  
## Precision Prompting Challenge – AfyaTech

---

## 🟢 Introduction

Precision matters in maternal health because small wording errors can lead to unsafe, unaffordable, or culturally irrelevant advice. In rural Kenya and Uganda, AI must reflect local diets, transport constraints, and healthcare access realities. Generic prompts risk misinformation and loss of trust.

---

# 🟡 PROMPT A: Nutrition Advice

### Original Prompt
Give nutrition tips for pregnant women.

---

## AIM FRAMEWORK
- **A (Audience):** Pregnant women in rural Kenya and Uganda
- **I (Instruction):** Provide nutrition advice using local foods
- **M (Modality):** SMS format (≤160 characters)

---

## MAP FRAMEWORK
- **M (Memory):** ugali, matooke, beans, sukuma wiki, fish, eggs
- **A (Action):** Suggest balanced affordable meals
- **P (Personalization):** Rural + low-income constraints

---

### Rewritten Prompt
You are an SMS maternal health assistant for rural Kenya and Uganda.  
Use only local foods (ugali, matooke, beans, sukuma wiki, eggs, tilapia).  
Give affordable pregnancy meal ideas in ≤160 characters.  
Avoid urban/imported foods.

---

### Key Improvement
Grounds nutrition advice in **local food systems**, reducing hallucinated or urban-biased recommendations.

---

# 🟡 PROMPT B: Appointment Reminders

### Original Prompt
Remind users about doctor visits.

---

## AIM FRAMEWORK
- **A:** Rural pregnant women
- **I:** Appointment reminders with travel awareness
- **M:** SMS alerts

---

## MAP FRAMEWORK
- **M:** Clinics 5–20km away, CHWs available, rain affects travel
- **A:** Remind + suggest departure time + CHW contact
- **P:** Adjust for transport affordability (M-Pesa)

---

### Rewritten Prompt
Generate SMS reminders including clinic date, travel time (5–20km), weather delays, CHW contact option, and M-Pesa transport support.

---

### Key Improvement
Integrates **real logistics constraints**, reducing missed appointments.

---

# 🟡 PROMPT C: Emergency Triage

### Original Prompt
Tell me what to do if I feel unwell during pregnancy.

---

## Chain-of-Thought + Verifier

### Process
1. Ask symptoms first  
2. Classify severity (mild/moderate/emergency)  
3. Provide safe response  
4. Verify no panic-inducing advice  

---

### Rewritten Prompt
Before answering, ask symptoms and pregnancy stage.  
Classify risk level internally.  
Provide calm, safe next steps.  
Avoid panic. If unclear, advise CHW or clinic contact.

---

### Key Improvement
Prevents unsafe assumptions and reduces panic through structured reasoning + verification.

---

## 🔵 Reflection

AI in healthcare must move beyond generic responses to context-aware systems. In rural East Africa, constraints like distance to clinics, food availability, and income levels shape health outcomes. Frameworks like AIM and MAP ensure relevance, while Chain-of-Thought and Verifier patterns improve safety. This exercise shows AI is not just a generator of answers but a system that must reason within real-world limits to be useful in maternal health.

---