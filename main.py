import cv2
import cvzone
import cvzone as cz
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from snake import Snake
from random import randint

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(maxHands=1, detectionCon=0.9)

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    hands = detector.findHands(img=image, draw=False)
    if hands:
        hand = hands[0]['lmList']
        ind_fin = hand[8][:2]

        snake = Snake([
            ind_fin,
            (ind_fin[0] - 5, ind_fin[1] - 5)
        ])
        break
    cv2.waitKey(1)

print('Running program')

food = [randint(424, 900), randint(224, 600)]
food_image = cv2.imread('Fruit-Cherry-icon.png', cv2.IMREAD_UNCHANGED)

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)

    hands = detector.findHands(img=image, draw=False, flipType=False)

    print(food)
    image = cvzone.overlayPNG(image, food_image,
                              [food[0] - 24, food[1] - 24])

    if hands:

        hand = hands[0]['lmList']

        ind_fin = hand[8][:2]
        d_to_food = snake.distance(
            food,
            ind_fin
        )


        if d_to_food < 30:
            snake.allowed_length += 20
            food = [randint(424, 900), randint(224, 600)]


        snake.move_to(ind_fin)

    for i in range(1, len(snake.body_coords)):
        image = cv2.line(image, snake.body_coords[i], snake.body_coords[i - 1], (255, 192, 203), 5)
    cv2.imshow('Great!', image)

    cv2.waitKey(1)
