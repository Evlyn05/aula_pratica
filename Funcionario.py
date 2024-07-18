class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome  # Atributo público
        self._salario = salario  # Atributo protegido
        self.__cpf = None  # Atributo privado


    # Método para consultar o CPF (atributo privado)
    def get_cpf(self):
        return self.__cpf


    # Método para modificar o CPF (atributo privado)
    def set_cpf(self, cpf):
        self.__cpf = cpf


    # Método para consultar o salário (atributo protegido)
    def get_salario(self):
        return self._salario


    # Método para modificar o salário (atributo protegido)
    def set_salario(self, salario):
        self._salario = salario


    def descricao(self):
        return f"Funcionario: {self.nome}, Salário: R${self._salario:.2f}"




# Classe derivada Engenheiro
class Engenheiro(Funcionario):
    def __init__(self, nome, salario, especialidade):
        super().__init__(nome, salario)
        self.especialidade = especialidade  # Atributo público específico da classe derivada


    def descricao(self):
        return f"Engenheiro: {self.nome}, Salário: R${self.get_salario():.2f}, Especialidade: {self.especialidade}"




# Classe derivada Gerente
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor  # Atributo público específico da classe derivada
