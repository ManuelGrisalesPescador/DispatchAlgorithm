import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg


import pylab

fig, ax = pylab.subplots(figsize=(5,5))

ax.broken_barh([(0,30), (60,10)], (10,2))


canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True