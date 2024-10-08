def menu():
    menu = '''

    ======= Selecione a opção desejada =======

                [d] Depositar
                [s] Sacar
                [e] Extrato
                [nu] Novo Usuário
                [nc] Nova Conta
                [lc] Listar Contas
                [q] Sair

    ==========================================

    : '''
    return input(menu)

def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso===')
    else:
        print('Não foi possivel realizar o depósito.\n Por favor verifique o valor digitado.')
    
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Saldo INsuficiente')

    elif excedeu_limite:
        print('O valor máximo para saques é R$ 500,00')
    
    elif excedeu_saques:
        print('Você excedeu o limite diário de saques')

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque de: R$ {valor:.2f}\n'
    else:
        print('Não foi possivel realizar o depósito.\n Por favor verifique o valor digitado.')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print('\n======EXTRATO======')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=====================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já cadastrado')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o endereço completo(logradouro, numero, bairro, cidade/estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'cpf': cpf})

    print('Usuário criado com sucesso')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input('Digite o CPF do usuário(somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {'agencia': agencia, 'numero_da_conta': numero_da_conta, 'usuario': usuario}
    else:
        print('Usuário não encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)







def main(): 
    saldo = 0
    limite = 500
    extrato = ''
    saques = 0
    usuarios = []
    contas = []
    LIMITE_DE_SAQUES = 3
    AGENCIA = '0001'

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

            
        elif opcao == 's':
            valor = float(input('Informe o valor para saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=saques,
                limite_saques=LIMITE_DE_SAQUES,
            )


        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)    

        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_da_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)
        
                
        elif opcao == 'q':
            break

        else:
            print('Operação inválida, tente novamente.')
   
main()