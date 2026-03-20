from agent import Agent
from environment import Environment
import matplotlib.pyplot as plt
from visualization import animate_environment

crowd_sizes = [10, 20, 50, 100, 500, 1000]
SIMULATIONS = 100
MODEL_TYPE = "social_influence"  # 3 types - "additive", "multiplicative", "social_influence"
avg_results = []

print ("SIMULATION STARTED")
for num_agents in crowd_sizes:
    results = []

    for run in range(SIMULATIONS):
        env = Environment(num_agents = num_agents)
    env. simulate(model_type=MODEL_TYPE)
    helpers = env.count_helpers()
    help_rate = helpers / num_agents * 100

    results.append(help_rate) # Store the help rate for this run
    average_help_rate = sum(results) / len(results)
    avg_results.append(average_help_rate)

    print("*" * 80)  
    print(f"Simulation results for {MODEL_TYPE.replace('_', ' ').title()} Model")
    print(f"Model: {MODEL_TYPE.replace('_', ' ').title()} Model")
    print(f"Crowd size: {num_agents} agents -> Average help rate over {SIMULATIONS} simulations: {average_help_rate:.2f}%")

print("SIMULATION COMPLETED")

# plt.figure()
# plt.plot(crowd_sizes, avg_results, marker='o')
# plt.xlabel('Crowd Size')
# plt.ylabel('Average Help Rate (%)')
# plt.title(f'Simulation Results for {MODEL_TYPE.replace("_", " ").title()} Model')
# plt.grid()
# plt.show()

env = Environment(num_agents = 100)
animate_environment(env, model_type=MODEL_TYPE)

