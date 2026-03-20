import random
import math
class Agent:
    def __init__(self, agent_id):

        self.agent_id = agent_id

        #position in 2D space
        self.x = random.uniform(0, 100)
        self.y = random.uniform(0, 100)

        # emotional traits (0 to 1)
        self.bravery = random.random()
        self.empathy = random.random()
        self.fear = random.random()
        self.caution = random.random()  
        self.social_dependency = random.random()

        # state
        self.helping = False

        #Leader
        self.is_leader = False

    def move(self):
        self.x += random.uniform(-2, 2)
        self.y += random.uniform(-2, 2)

        self.x = max(0, min(100, self.x))
        self.y = max(0, min(100, self.y))

    def decision(self, model_type, bystanders, helpers, visibility, leader_presence):

        crowd_effect = math.log(bystanders + 1)

        if model_type == "additive":
            help_score = (self.bravery * self.empathy) - self.fear - self.caution
        elif model_type == "multiplicative":
            help_score = (self.bravery * self.empathy) - (self.fear * self.caution)
        elif model_type == "social_influence":
            help_score = (self.bravery * self.empathy) + helpers * 0.02 + visibility * 0.4 + (1 if leader_presence else 0) * 0.2 - crowd_effect * 0.3 - (self.fear * self.caution) 
        
        if self.is_leader:
            help_score += 1 # Leaders are more likely to help
        noise = random.uniform(-0.5, 0.5)  # Add some randomness to the decision
        help_score += noise

        probability_to_help = 1 / (1 + pow(2.71828, -help_score))  # Sigmoid function to convert score to probability

        if random.random() < probability_to_help:
            self.helping = True
        else:
            self.helping = False

