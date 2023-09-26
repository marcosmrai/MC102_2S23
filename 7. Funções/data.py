def converte_tempo_segundos(segundos_totais):
    dias = segundos_totais // 86400
    resto = segundos_totais % 86400
    horas = resto // 3600
    resto = resto % 3600
    minutos = resto // 60
    segundos = resto % 60
    if dias == 0:
        print('{:d} horas {:d} minutos {:d} segundos'.format(horas, minutos, segundos))
    else:
        print('{:d} dias {:d} horas {:d} minutos {:d} segundos'.format(dias, horas, minutos, segundos))

converte_tempo_segundos(498)