# Import the necessary libraries
import pygame

# Define the notes and durations of the song
notes = [
    (NOTE_C4, 4),
    (NOTE_D4, 4),
    (NOTE_E4, 4),
    (NOTE_F4, 4),
    (NOTE_G4, 4),
    (NOTE_A4, 4),
    (NOTE_B4, 4),
    (NOTE_C5, 4),
    (NOTE_D5, 4),
    (NOTE_E5, 4),
    (NOTE_F5, 4),
    (NOTE_G5, 4),
    (NOTE_A5, 4),
    (NOTE_B5, 4),
    (NOTE_C6, 4),
    (NOTE_D6, 4),
    (NOTE_E6, 4),
    (NOTE_F6, 4),
    (NOTE_G6, 4),
    (NOTE_A6, 4),
    (NOTE_B6, 4),
    (NOTE_C7, 4),
    (NOTE_D7, 4),
    (NOTE_E7, 4),
    (NOTE_F7, 4),
    (NOTE_G7, 4),
    (NOTE_A7, 4),
    (NOTE_B7, 4),
    (NOTE_C8, 4),
]

# Initialize pygame
pygame.init()

# Create a mixer object
mixer = pygame.mixer

# Play the song
for note, duration in notes:
    mixer.Sound("mario_theme.wav").play(loops=0, maxtime=duration)

# Wait for the song to finish playing
pygame.time.wait(notes[-1][1])

# Quit pygame
pygame.quit()
