import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
while True:
    check, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = Hand.process(imgRGB)
    hand_points = result.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if hand_points:
        for points in hand_points:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id_dedo, coord in enumerate(points.landmark):

                cx, cy = int(coord.x * w), int(coord.y * h)
                pontos.append((cx, cy))
        pontas_dedos = [8, 12, 16, 20]
        contador = 0
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador += 1
            for x in pontas_dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador += 1
        cv2.rectangle(img, (80, 10), (200, 100), (255, 0, 0), -1)
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)
    cv2.imshow('Imagem', img)
    cv2.waitKey(1)
