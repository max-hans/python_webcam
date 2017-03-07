import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((1280,1024),pygame.FULLSCREEN)

cam_list = pygame.camera.list_cameras()
print cam_list
webcam = pygame.camera.Camera(cam_list[0])
webcam.start()

while True:
	imagen = webcam.get_image()
	imagen = pygame.transform.scale(imagen,(1280,1024))
	screen.blit(imagen,(0,0))
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			webcam.stop()
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			webcam.stop()
			pygame.quit()
			sys.exit()
