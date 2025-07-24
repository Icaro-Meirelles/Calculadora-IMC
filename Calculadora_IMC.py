
# Calculadora IMC

import pyfiglet




def calculadora(): # Função da Calculadora IMC
    while True:
        try:

            # ASCII Art Banner
            banner = "Calculadora IMC"
            ascii_art_banner = pyfiglet.figlet_format(banner)  
            print(ascii_art_banner)




            # Input convertendo "," em "."
            str_peso = str(input("Qual o seu Peso? ")).replace(",", ".") 
            str_altura = str(input("Qual sua Altura? ")).replace(",", ".")
            

            # Variavel com valores em Float
            var_peso = float(str_peso) 
            var_altura = float(str_altura)


            # Operação
            calc = var_peso / (var_altura ** 2)
            print(f"Seu IMC é {calc:.2f}")


            # Categorias IMC
            if calc < 18.5:
                print("Magreza")

            elif calc <= 24.9:
                print("Normal")

            elif calc <= 29.9:
                print("Sobrepeso ")

            elif calc <= 34.9:
                print("Obesidade 1")

            elif calc <= 39.9:
                print("Obesidade 2")

            elif calc >= 40.0:
                print("Obesidade Grave 3")
        
        except ValueError:
            print("Erro: Digite um Valor Válido!")




        print("By IC4R0")




# Entry Point
if __name__ == "__main__":
    calculadora()