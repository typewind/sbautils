def show_360(id, events):
    columns_to_use = ["360_freeze_teammate", "360_freeze_actor", "360_freeze_location_x", "360_freeze_location_y"]
    event = events[events["id"]==id][columns_to_use]
    team_1 = event[event["360_freeze_teammate"]]
    team_2 = event[event["360_freeze_teammate"]==False]
    actor = event[event["360_freeze_actor"]]
    pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
    fig, ax = pitch.draw()
    plt.scatter(team_1["360_freeze_location_x"], team_1["360_freeze_location_y"], color = "red")
    plt.scatter(team_2["360_freeze_location_x"], team_2["360_freeze_location_y"], color = "blue")
    plt.scatter(actor["360_freeze_location_x"], actor["360_freeze_location_y"], color = "white", marker = "x")
