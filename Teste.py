from Funcionario import Funcionario, Engenheiro, Gerente, Funcionario2


# Classe de teste
class Teste:
    def __init__(self):
        pass


    def criar_e_testar_funcionario(self):
        f = Funcionario("Thauane", 3000.00)
        f.set_cpf("131.453.749-09")
        f.set_salario(3500.00)
        print(f.descricao())
        print(f"CPF: {f.get_cpf()}")

     def criar_e_testar_funcionario2(self):
        f = Funcionario("Luís", 3000.00)
        f.set_cpf("097.536.009-89")
        f.set_salario(3500.00)
        print(f.descricao())
        print(f"CPF: {f.get_cpf()}")

    def criar_e_testar_engenheiro(self):
        e = Engenheiro("Evlyn", 5000.00, "Software")
        e.set_salario(5500.00)
        e.set_cpf("967.654.321-30")
        print(e.descricao())
        print(f"CPF: {e.get_cpf()}")


    def criar_e_testar_gerente(self):
        g = Gerente("Raissa", 7000.00, "TI")
        g.set_salario(7500.00)
        g.set_cpf("111.222.333-44")
        print(g.descricao())
        print(f"CPF: {g.get_cpf()}")


# Instanciar a classe de teste e realizar os testes
if __name__ == "__main__":
    teste = Teste()
    teste.criar_e_testar_funcionario()
    teste.criar_e_testar_engenheiro()
    teste.criar_e_testar_funcionario2()
    teste.criar_e_testar_gerente()
