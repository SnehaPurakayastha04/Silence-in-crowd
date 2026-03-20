import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_environment(env, model_type, steps=50):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        x_max = ax.get_xlim()[1]
        y_max = ax.get_ylim()[1]

        ax.set_facecolor('white')
        fig.patch.set_facecolor('white')

        circle = plt. Circle(
            (env. victim_x, env. victim_y),
            env.visibilty_radius,
            color='red',
            fill = False,
            linestyle='--',
            alpha=0.5
        )
        ax.add_patch(circle)

        ax.text(65, 95, f" Leader Present: {env.leader_presence}", color='white', fontsize=10, bbox=dict(facecolor='black', alpha=0.7))

        env.simulate(model_type=model_type)

        for agent in env.agents:
            agent.move()
        
        x_vals = [agent.x for agent in env.agents]
        y_vals = [agent.y for agent in env.agents]

        #colors = ["green" if agent.helping else "blue" for agent in env.agents]

        colors = []
        for agent in env.agents:
            if agent.helping:
                colors.append("green") # Agents who are helping
            elif env.distance_to_victim(agent) <= env.visibilty_radius:
                colors.append("orange")  # Agents who can see the victim but are not helping
            else:
                colors.append("blue")  # Agents who cannot see the victim
        ax.scatter(x_vals, y_vals, c = colors)
        ax.scatter(env.victim_x, env.victim_y, c='red', marker='X', s=100, label='Victim', edgecolors='black')

        # if agent.is_leader:
        #     ax.scatter(agent.x, agent.y, c='magenta', s=150, label='Leader')
       
        helpers = env.count_helpers()

        ax.text(
    2, 95,
    f"Helpers: {helpers}/{len(env.agents)}",
    fontsize=10,
    bbox=dict(facecolor='white', alpha=0.7)
)

        ax.set_title(f"Step {frame}")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)

    ani = animation.FuncAnimation(fig, update, frames=steps, repeat=False, interval = 500)
    plt.show()