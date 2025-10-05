def monitor_temperatura():
    temperatura = float(input('Digite a temperatura atual: '))

    if (temperatura > 25):
        print('Alerta! Temperatura acima do limite permitido.')

def main():
    monitor_temperatura()

if __name__ == '__main__':
    main()