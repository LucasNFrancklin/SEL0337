# SEL0337 Projetos em Sistemas Embarcados - Entrega 3 parte 1.1 
# Danilo Djovano Selli Junior 13836692
# Lucas Nogueira Francklin 13677080 

import RPi.GPIO as GPIO
import lgpio
import time

#configurando os GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setando o GPIO 18 como o LED
GPIO.setup(18, GPIO.OUT)

#fucao botao
def button(bt):
	if GPIO.input(bt):
		print("released")
		GPIO.output(18, GPIO.LOW)
	else:
		print("pressed")
		GPIO.output(18, GPIO.HIGH)

#setando o GPIO 15 como o botao
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP) 
GPIO.add_event_detect(17, GPIO.BOTH, callback=button, bouncetime=200)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()


