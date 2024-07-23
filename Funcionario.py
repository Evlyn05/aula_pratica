class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self._salario = salario 
        self.__cpf = None 


    def get_cpf(self):
        return self.__cpf


    def set_cpf(self, cpf):
        self.__cpf = cpf


    def get_salario(self):
        return self._salario


    def set_salario(self, salario):
        self._salario = salario


    def descricao(self):
        return f"Funcionario: {self.nome}, Salário: R${self._salario:.2f}"


class Funcionario2:
    def __init__(self, nome, salario):
        self.nome = nome 
        self._salario = salario  
        self.__cpf = None 


 
    def get_cpf(self):
        return self.__cpf


    def set_cpf(self, cpf):
        self.__cpf = cpf


    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario


    def descricao(self):
        return f"Funcionario: {self.nome}, Salário: R${self._salario:.2f}"


# Classe derivada Engenheiro
class Engenheiro(Funcionario):
    def __init__(self, nome, salario, especialidade):
        super().__init__(nome, salario)
        self.especialidade = especialidade  


    def descricao(self):
        return f"Engenheiro: {self.nome}, Salário: R${self.get_salario():.2f}, Especialidade: {self.especialidade}"




# Classe derivada Gerente
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor 
