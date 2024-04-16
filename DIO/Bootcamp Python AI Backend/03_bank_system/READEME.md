## Desafio: Modelando o Sistema Bancário em POO com Python

- Desafio:

    - Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.


    #### Classe Cliente

    - Inicia com o Endereço 

    - E a conta bancária como uma lista vazia

    - Conforme solicitado no problema, inicializamos o "realizar_transacao" e "adicionar_conta".

    ```python
    class Cliente:
        def __init__(self, endereco):
            self.endereco = endereco
            self.contas = []
            
        def realizar_transacao(self, conta, transacao):
            transacao.registrar(conta)
        
        def adicionar_conta(self, conta):
            self.contas.append(conta)
    ```

    #### Classe Pessoa Física

    - Chamamos o endereço da classe pai

    - Acrescentamos: nome, data de nascimento e cpf

    ```python
    class PessoaFisica(Cliente):
        def __init__(self, nome, data_nascimento, cpf,endereco):
            super().__init__(endereco)
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.cpf = cpf
    ```

    #### Classe Conta

    - Implementação do: Saldo, numero, agencia, cliente e historico

    - Implementação dos métodos: Sacar e Depositar

    ```python
    class Conta:
        def __init__(self, numero, cliente):
            self._saldo = 0
            self._numero = numero
            self._agencia = "0001"
            self._cliente = cliente
            self._historico = Historico()
        
        @classmethod
        def nova_conta(cls, cliente, numero):
            return cls(numero, cliente)
        
        @property
        def saldo(self):
            return self._saldo
        
        @property
        def numero(self):
            return self._numero
        
        @property
        def agencia(self):
            return self._agencia
        
        @property
        def cliente(self):
            return self._cliente
        
        @property
        def historico(self):
            return self._historico
        
        def sacar(self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo
    
            if excedeu_saldo:
                print("\n!!! Operação Falhou. Saldo insuficiente !!!")
    
            elif valor > 0:
                self._saldo -= valor
                print("\n=== Saque realizado com sucesso! ===")
                return True
            else:
                print("\n!!! Operação falhou! Valor inválido !!!")
            
            return False
        
        def depositar(self, valor):
            if valor > 0:
                self._saldo += valor
                print("\n=== Depósito realizado com sucesso! ===")
            else:
                print("\n!!! Operação falhou. Valor inválido. !!!")
                return False
            
            return True
    ```

    - 

    #### Classe Conta Corrente

    - Vamos estabelecer o valor máximo de saque e a e a quatidade máxima de saques.

    - Somente após essa checagem, que podemos realmente realizar o saque.

    - Por isso criamos essa função saque, que após passar pelas validações necessárias, chamará a função Saque da classe conta.

    - O histórico vai armazenar os saques e depósitos, para calcular essa quantidade, foi validado dentro do histórico se o tipo da transação é saque.

    - Definimos tambem o print da função Conta Corrente (__str__), com as informações relativas a conta.

    ```python
    class ContaCorrente(Conta):
        def __init__(self, numero, cliente, limite=500,limite_saques=3):
            super().__init__(numero,cliente)
            self.limite = limite
            self.limite_saques = limite_saques
    
        def sacar(self, valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes 
                 if transacao["tipo"] == Saque.__name__])
            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques
    
            if excedeu_limite:
                print("\n!!! Operação falhou. Valor excede o limite de saque !!!")
            elif excedeu_saques:
                print("\n!!! Operação falhou. Número máximo de saques atingido. !!!")
            else:
                return super().sacar(valor)
            
            return False
    ```

    #### Classe Histórico

    - Inicio o histórico com a lista de transações vazias

    - Propriedade para pegar as transações

    - Adiciono as transações a partir de um dicionario.

    - A transação pode ser um Saque ou um Depósito.

    ```python
    class Historico:
        def __init__(self):
            self._transacoes = []
        
        @property
        def transacoes(self):
            return self._transacoes
    
        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                    "tipo": transacao.__class__.__name__,
                    "valor": transacao.valor,
                    "data": datetime.now().strftime("$d-%m-%Y %H:%M%s"),
                }
            )
    ```

    #### Classe Transacao

    - Classe abstrata com o Valor e o registrar

    - Que será herdada nas Classes de Saque e deposito posteriormente.

    ```python
    class Transacao(ABC):
        @property
        @abstractproperty
        def valor(self):
            pass
    
        @abstractclassmethod
        def registrar(self, conta):
            pass
    ```

    #### Classe Saque

    ```python
    class Saque(Transacao):
        def __init__(self, valor):
            self._valor = valor
        
        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.sacar(self.valor)
    
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)
    ```

    #### Classe Deposito

    ```python
    class Deposito(Transacao):
        def __init__(self, valor):
            self._valor = valor
    
        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)
    
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)
    ```

