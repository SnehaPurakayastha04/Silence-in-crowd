from agent import Agent
import random
import math

class Environment:
    def __init__(self, num_agents):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.bystanders = num_agents - 1  # All other agents are bystanders except the victim
        self.helpers = 0
        self.visibility = random.random()  # 0 to 1
        self.leader_presence = random.choice([True, False])
        

        # victim position
        self.victim_x = random.uniform(0, 100)
        self.victim_y = random.uniform(0, 100)

        self.visibilty_radius = 30  # Agents within this distance can see the victim
    
    def distance_to_victim(self, agent):
        return math.sqrt((agent.x - self.victim_x) ** 2 + (agent.y - self.victim_y) ** 2)

    def count_helpers(self):
        self.helpers = sum(agent.helping for agent in self.agents)
        return self.helpers
    def simulate(self, model_type):
            helpers = self.count_helpers()
            for agent in self.agents:
                distance = self.distance_to_victim(agent)
                if distance <= self.visibilty_radius:
                    agent.decision(model_type, bystanders=self.bystanders, helpers=helpers or 0, visibility=self.visibility, leader_presence=self.leader_presence)
           
    def trigger_emergency(self, model_type):
        print("Emergency triggered! Simulating agent decisions...")
        self.simulate(model_type=model_type)
        print(f"Total helpers: {self.helpers} out of {len(self.agents)} agents.")