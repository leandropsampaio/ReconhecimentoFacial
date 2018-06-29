import cv2
import numpy
import os

# Quanto menor o threshold, mais seguro ele vai ser. Porém vai ser difícil reconhecer, pois as imagens
# tem que serem muito parecidas
eigenface = cv2.face.EigenFaceRecognizer_create(40, 8000)
#eigenface = cv2.face.EigenFaceRecognizer_create(num_components=10, threshold = 2)
#eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create(3, 2000)
#fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 50)
#lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemComId():
    # Pega todos os caminhos das imagens desse diretório
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

    print(caminhos)
    # Lista de faces
    faces = []
    # Lista de ids
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGRA2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])

        #Colocar as faces e ids na lista
        faces.append(imagemFace)
        ids.append(id)
        #cv2.imshow("Face", imagemFace)
        #cv2.waitKey(10)
    return numpy.array(ids), faces

ids, faces = getImagemComId()

#print(ids)

print("Treinando...")

# Faz o treinamento
eigenface.train(faces, ids)
# Cria um classificador já treinado
eigenface.write("classificadorEigen.yml")

# Faz o treinamento
fisherface.train(faces, ids)
# Cria um classificador já treinado
fisherface.write("classificadorFisher.yml")

# Faz o treinamento
lbph.train(faces, ids)
# Cria um classificador já treinado
lbph.write("classificadorLBPH.yml")

print("Treinamento Realizado com Sucesso!")




