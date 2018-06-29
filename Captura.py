import cv2
import numpy


# Classificador para detectar uma face
classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
# Classificador para detectar os olhos
classificadorOlho = cv2.CascadeClassifier("haarcascade-eye.xml")
# Criando uma videoCapture para pegar o video da Webcam (Na posição 0)
camera = cv2.VideoCapture(0)
amostra = 1
# Quantidade de imagens que serão utilizadas para o treinamento da face
numeroAmostras = 25

id = input("Digite seu identificador: ")

# Tamanhos das imagens tiradas para treinamento
largura = 220
altura = 220

print("Capturando as faces...")

while(True):
    # Lendo a imagem da câmera e colocando na variável imagem
    conectado, imagem = camera.read()
    # Transformando imagem em escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGRA2GRAY)
    # Mostrando o valor da média dos pixels da imagem em escala de cinza para detectar a luminosidade
    #print (numpy.average(imagemCinza))
    # Utilizando o classificador de faces e a imagem para detectar todas as faces que aparecem
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100,100))

    # Pega as posições das faces detectadas e desenha um retângulo em nas faces
    for(x,y,l,a) in facesDetectadas:
        cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)
        regiao = imagem[y:y +a, x:x + l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGRA2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        #for (ox, oy, ol, oa) in olhosDetectados:
            #cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

        if cv2.waitKey(30) & 0XFF == ord('q'):
            # O valor vai de 0-255
            #if(numpy.average(imagemCinza)) > 110:
            imagemFace = cv2.resize(imagemCinza[y:y +a, x:x + l], (largura, altura))
            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("A foto " + str(amostra) + " foi capturada com sucesso!")
            amostra = amostra + 1

    # Mostrando imagem na tela e colocando o nome da janela como "Face"
    cv2.imshow("Face", imagem)
    # Aguardando um tempo (30 milissegundos)
    cv2.waitKey(1)
    if (amostra >= numeroAmostras + 1):
        break

print("*** Faces capturadas com sucesso ***")
# Liberar imagem da câmera
camera.release()
# Destrói a janela
cv2.destroyAllWindows()

















