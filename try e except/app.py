try:
    numero = int(input("Digite um número: "))
    print(f"O número é: {numero}")
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")
except ValueError:
    print("Você digitou um valor inválido.")
finally:
    print("Execução finalizada independente de sucesso ou erro.")