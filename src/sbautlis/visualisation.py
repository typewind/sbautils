import matplotlib.pyplot as plt
from mplsoccer import Pitch


def init_pitch_dark():
    """The first step to visualise anything related to pitch.
    Define the fig and ax for the next steps
    """
    pitch = Pitch(pitch_type="statsbomb", 
    positional=True, shade_middle=True, 
    positional_color='#232344', shade_color='#151524', pitch_color="#111122", line_color="#222233"
    )
    fig, ax = pitch.draw()


