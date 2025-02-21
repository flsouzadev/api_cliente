import re
from validate_docbr import CPF

def nome_valido(nome):
    return nome.isalpha()

# Validar CPF
def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)  # True

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    """Verifica se o celular é válido  (11 99999-9999)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9{4}]'
    resposta = re.findall(modelo, numero_do_celular)
    return resposta

    # or 
    # modelo = r'^\d{2} \d{5}-\d{4}$'
    # return bool(re.match(modelo, numero_do_celular))