import cv2  # pip install opencv-python
import mediapipe as mp  # pip install mediapipe

# Para abrir a web cam, captura de vídeo

cap = cv2.VideoCapture(0)

# Mapeamento das mãos

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)  # Quantidade de mãos que vamos permitir
# Para desenhar as mãos

mpDraw = mp.solutions.drawing_utils

while True:

    check, img = cap.read()

    # Transformando em RBG para proccessamento da Imagem

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processamdno a imagens

    result = Hand.process(imgRGB)

    # Identificado os pontos (mostrar no site) das mãos

    hand_points = result.multi_hand_landmarks

    h, w, _ = img.shape

    pontos = []

    # Se detectar as mãos

    if hand_points:

        for points in hand_points:
            # print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)

            # Enumerando cada ponto da mão
            # Landmark retorna uma proporção na inagem, precisamos converter em pixels
            for id_dedo, coord in enumerate(points.landmark):

                cx, cy = int(coord.x * w), int(coord.y * h)
                # Para ver o texto com as coordenadas

                # cv2.putText(img, str(id_dedo), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                #
                # incrementando os pontos à lista

                pontos.append((cx, cy))

        # Lógica para os dedos

        pontas_dedos = [8, 12, 16, 20]
        contador = 0
        if points:

            # Lógica para o dedão, eixo x

            if pontos[4][0] < pontos[2][0]:

                contador += 1

            # Lógica para os outros dedos, que estão no eixo y, controlados pelo valor de cy

            for x in pontas_dedos:
                if pontos[x][1] < pontos[x-2][1]:

                    contador += 1

        # print(contador)

        # inserindo um retângulo na imagem: Opcional, por depois

        cv2.rectangle(img, (80, 10), (200, 100), (255, 0, 0), -1)

        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    # Mostrando as coordenadas das dos pontos das mãos

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)




