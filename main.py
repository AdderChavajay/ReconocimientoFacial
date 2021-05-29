import take_photo as tk
import recognize_face as rf
# import number_to_speech as nts


def main():
    steps = input("Bienvenidos... Programa modificado\n Opciones\na. Presiona 1 para crear dataset y training data\nb. Presione 2 solo para reconocer\n> ")
    # print('\n Use el ID 2 profesor para probar')
    if(steps == '1'):
        #agregar cara a reconocer
        tk.create_dataset()
        rf.run()
        main()
    elif(steps == '2'):
        #reconocer caras
        image_recognized = tk.recognize()
        # if(image_recognized):
        #     menu()
    else:
        print('Opcion no Valida')
        main()

def sum():
    numero1 = int(input('Dame el numero> '))
    numero2 = int(input('Dame el numero2> '))

    return numero1 + numero2

if __name__ == '__main__':
    main()
