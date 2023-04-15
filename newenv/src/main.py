import cv2
import cvzone
import random
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

#points
player_point = 0
AI_point = 0
RPC = ["rock", "paper", "scissor"]

#timer
timer = 0
state_result = False
start_game = False

print("Press s to start the game")

while True:
    success, img = cap.read()
    
    hands, img = detector.findHands(img)
    cv2.imshow("Image", img)

    if start_game:
        if state_result is False:
            timer = time.time() - initial_time
            print("Countdown: ", str(int(timer)), end="\r")

            if timer>4:
                state_result = True
                timer = 0

                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    if fingers == [0,0,0,0,0]:
                        player_move = "rock"
                    if fingers == [1,1,1,1,1]:
                        player_move = "paper"
                    if fingers == [0, 1, 1, 0, 0]:
                        player_move = "scissor"

                    print("\n\nPlayer's move: ", player_move)
                    AI_choice = random.choice(RPC)
                    print("AI choice: "+ AI_choice)
                    
                    if(AI_choice == player_move):
                        print("Issa tie!!")
                    else:
                        if(AI_choice == "rock"):
                            if(player_move == "paper"):
                                win = True
                            else:
                                win = False

                        if(AI_choice == "paper"):
                            if(player_move == "scissor"):
                                win = True
                            else:
                                win = False

                        if(AI_choice == "scissor"):
                            if(player_move == "rock"):
                                win = True
                            else:
                                win = False
                        
                        if(win):
                            print("You win!!")
                            player_point += 1
                        else:
                            print("you suck!!!!!")
                            AI_point += 1
                        
                    print("\nPlayer's score: ", str(player_point))
                    print("AI's score: " + str(AI_point) + "\n")

                    state_result = False
                    start_game = False

                    #print(fingers)

    key = cv2.waitKey(1)
    if key == ord('s'):
        start_game = True
        initial_time = time.time()