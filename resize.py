import cv2 
import os

def resize_images(input_dir, output_dir, new_size):
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Obtener la lista de archivos en el directorio de entrada
    file_list = os.listdir(input_dir)

    for file_name in file_list:
        # Construir la ruta completa de entrada
        input_path = os.path.join(input_dir, file_name)

        # Leer la imagen
        img = cv2.imread(input_path)

        # Redimensionar la imagen
        img_resized = cv2.resize(img, new_size)

        # Construir la ruta completa de salida
        output_path = os.path.join(output_dir, file_name)

        # Guardar la imagen redimensionada
        cv2.imwrite(output_path, img_resized)

if __name__ == "__main__":
    # Especificar el directorio de entrada, el directorio de salida y el nuevo tamaño
    input_directory = "data/valid/images"
    output_directory = "basuraKatamaranResize"
    new_size = (640, 480)  # Especifica el nuevo tamaño, por ejemplo, (300, 200)

    # Llamar a la función para redimensionar las imágenes
    resize_images(input_directory, output_directory, new_size)
    #imagen = cv2.imread("data/")
    #imagen = cv2.resize()
