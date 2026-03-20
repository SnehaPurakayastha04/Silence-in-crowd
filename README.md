# Silence in the Crowd

## A Study on the Bystander Effect in Digital Spaces

---

## Overview

**Silence in the Crowd** is an agent-based simulation that models the *bystander effect* — a social psychological phenomenon where individuals are less likely to help a victim when others are present.

This project explores how human helping behavior can be translated into a computational model. By simulating individual decisions within a crowd, the project demonstrates how simple local interactions can lead to complex group dynamics.

---

##  Features

*  Agent-based modeling of human behavior
*  Multiple decision models (Additive, Multiplicative, Social Influence)
*  Visibility-based perception of emergencies
*  Local social influence between agents
*  Leader presence as a global confidence factor
*  Real-time animated visualization using `matplotlib`

---

##  How It Works

A virtual environment is created where agents are randomly positioned in a 2D space. Each agent is assigned behavioral traits such as:

* empathy
* bravery
* fear
* caution

When an emergency occurs, agents decide whether to help based on:

* internal personality traits
* number of nearby helpers
* visibility of the victim
* size of the crowd (bystander effect)
* presence of a leader

Decisions are probabilistic, allowing for realistic variation in behavior.

---

##  Decision Model

In the **Social Influence Model**, each agent computes a *help score* based on both internal and external factors.

### Positive Influences:

* Empathy and bravery (intrinsic motivation)
* Nearby helpers (social influence)
* Visibility of the emergency
* Leader presence (situational confidence boost)

### Negative Influences:

* Fear and caution (hesitation)
* Crowd effect (diffusion of responsibility)

### Conceptual Model:

Help Score ∝
(Bravery × Empathy)

* Social Influence
* Visibility
* Leader Presence
  − (Fear × Caution)
  − Crowd Effect

This score is used in a probabilistic decision function to determine whether an agent helps.

---

##  Simulation Setup

* Crowd sizes: `10, 20, 50, 100, 500, 1000`
* Simulations per size: `100`
* Environment size: `100 × 100` grid

---

##  Results & Observations

The simulation was executed using the **Social Influence Model**, with 100 runs per crowd size.

### Average Helping Rate

| Crowd Size | Average Help Rate (%) |
| ---------- | --------------------- |
| 10         | 0.00                  |
| 20         | 10.00                 |
| 50         | 4.00                  |
| 100        | 4.00                  |
| 500        | 5.40                  |
| 1000       | 2.80                  |

---

###  Observations

*  Helping behavior remains low across all crowd sizes
*  The expected strong decrease in helping with increasing crowd size is not clearly observed
*  Small crowds show extremely low response, indicating strict decision conditions
*  Social influence alone does not significantly trigger helping behavior under current parameters
*  Variations suggest randomness and local interactions influence outcomes

---

### Interpretation

The results indicate that the model currently produces a **low probability of helping**, which may be due to:

* limited visibility range
* strong bystander effect penalty
* weak influence from nearby helpers
* conservative decision thresholds

These findings highlight the importance of **parameter tuning in agent-based simulations**.

---

## Visualization

The simulation includes:

* animated crowd movement
* color-coded agent states:

  * 🔵 unaware
  * 🟡 aware but not helping
  * 🟢 helping
  * ❌ victim location
  * real-time display of leader presence and helper count

*(Insert your graph and animation here)*

<img width="631" height="472" alt="Screenshot 2026-03-20 at 7 02 28 PM" src="https://github.com/user-attachments/assets/8ef93371-6aa6-4a76-8bae-1d05dc60c9bf" />


<img width="631" height="472" alt="Screenshot 2026-03-20 at 7 03 07 PM" src="https://github.com/user-attachments/assets/71bd330a-2890-4469-83e2-674d2e389fae" />



---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Silence-in-the-Crowd.git
cd Silence-in-the-Crowd
```

### 2. Create virtual environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the simulation

```bash
python main.py
```

---

## Project Structure

```
Silence-in-the-Crowd/
│
├── agent.py
├── environment.py
├── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

---


## Motivation

This project was built to explore how **individual decision-making interacts with group dynamics**, and how computational models can help us understand complex social behavior.

---

## Author

Sneha Purakayastha (https://github.com/SnehaPurakayastha04)

---
