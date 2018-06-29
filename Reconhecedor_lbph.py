import cv2

# Detector de faces
detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
# Cria um reconhecedor com o eigenface
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
# Ler o classificador criado a partir das fotos tiradas - Foi criado no Treinamento.py
reconhecedor.read("classificadorLBPH.yml")
# Largura e altura das imagem
largura, altura = 220, 220
# Criando uma fonte
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# Fazendo a conexão com a Webcam
camera = cv2.VideoCapture(0)

while (True):
    # Escrevendo nas variáveis a imagem lida pela Webcam
    conectado, imagem = camera.read()
    # Transformando a imagem capturada em escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Detectando as faces através do haarcascade e a imagem em escala de cinza
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30,30))

    for (x, y, l, a) in facesDetectadas:
        # Redimensionando a imagem
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        # Colocando um retângulo na imagem para visualização
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,0,255), 2)
        #
        id, confianca = reconhecedor.predict(imagemFace)
        nome = ""
        # Através do classificador obtemos o id da imagem reconhecida
        if id == 1:
            nome = 'Leandro'
        elif id == 2:
            nome = 'Adriana'

        # Quanto menor o valor de confiança melhor (Variável confiança- distância que a
        # imagem do classificador está da original)
        if confianca < 7000:
            # Escrevendo na imagem o nome
            cv2.putText(imagem, nome, (x,y +(a+30)), font, 2, (0,0,255))
            cv2.putText(imagem, str(confianca), (x,y + (a+50)), font, 1, (0,0,255))

    # Criando uma janela para mostrar a imagem com o título "Face"
    cv2.imshow("Face", imagem)
    # Caso o usuário aperte a letra "q"
    if cv2.waitKey(1) == ord('q'):
        break


# Limpa tudo que tinha criado anteriormente
camera.release()
cv2.destroyAllWindows()
