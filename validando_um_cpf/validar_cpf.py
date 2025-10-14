def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'ERRO: O CPF deve conter apenas números.'
    if len(cpf) != 11:
         return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."
