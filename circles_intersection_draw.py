import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):

    fig, ax = plt.subplots()

    circle1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"], fill=False, color="blue")
    circle2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"], fill=False, color="red")

    ax.add_patch(circle1)
    ax.add_patch(circle2)

    ax.set_aspect("equal")
    plt.grid(True)

    plt.show()