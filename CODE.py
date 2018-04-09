class Professor:
    def __init__(self, nome = 'Luan Santos', email= 'luanlpg@hotmail.com', ra='1701387', celular=964658699):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__disciplina = Disciplina

    def nomeGet(self):
        return self.__nome

    def nomeSet (self):
        self.__nome = str(input('Digite o nome do professor: '))

    def emailGet (self):
        return self.__email

    def emailSet(self):
        self.__email = str(input('Digite o email do professor: '))

    def raGet (self):
        return self.__ra

    def raSet (self):
        self.__ra = str(input('Digite o ra do professor: '))

    def celularGet (self):
        return self.__celular

    def celularSet (self):
        self.__celular = int(input('Digite o celular do professor: '))

    def return_sobrenome (self):
        nomes = self.__nome.split()
        return (nomes[-1])

    def disciplinaGet (self):
        return Disciplina.nomedcpGet

    


        
#----------------------------------------------------------------------------------



class Disciplina :
    def __init__(self, nomedcp = 'Física I', carg_hor = 120, valor = 50.00,):
        self.__nomedcp = nomedcp
        self.__carg_hor = carg_hor
        self.__valor = valor
        self.__Professor = Professor
      
    def nomedcpGet (self):
        return self.__nomedcp

    def nomedcpSet (self):
        self.__nomedcp = str(input('Digite o nome da disciplina: '))

    
    def carg_horGet (self):
        return self.__carg_hor

    def carg_horSet (self):
        x=int(input(' Digite: 1 -Para adicionar horas / 2 - Para remover horas: '))
        if x == 1:
            return dcp.adicionaHorasCarga()
        elif x == 2:
            return dcp.removeHorasCarga()
        else:
            print ('Opção inválida!')
    def adicionaHorasCarga (self):
        horaadc = int(input('Digite a quantidade de horas a serem adicionadas: '))
        horaadc = (horaadc + self.__carg_hor)
        while horaadc> 40:
            horaadc = 0
            horaadc = int(input('Limite de 40hr excedido, tente novamente: '))
            horaadc = (horaadc + self.__carg_hor)
        if horaadc <= 40:
            self.__carg_hor = horaadc
            return self.__carg_hor

    def removeHorasCarga (self):
        horasub = int(input('Digite a quantidade de horas a serem subtraídas: '))
        horasub = (self.__carg_hor - horasub)
        while horasub < 0:
            horasub = 0
            horasub = int(input('Professor não possui esta quantidade de horas para serem subitraídas, tente novamente: '))
            horasub = (self.__carg_hor - horasub)
        if horasub >= 0:
            self.__carg_hor = horasub
            return self.__carg_hor


    def ProfessorGet (self):
        return self.__Professor

    def ProfessorSet (self):
        self.__Professor = Professor

    def retornaValorHora (self):
        return self.__valor

    
#-------------------------------------------------------------------------------


prof = Professor()
dcp= Disciplina()

opt= 999
while opt == 999:
    print('             BEM VINDO AO SISTEMA ALUNO/DISCIPLINA!!!         \n1 - Para cadastrar Professor; \n2 - Para editar Professor; \n3 - Para cadastrar Disciplina; \n4 - Para editar Disciplina; \n5 - para info. do Professor; \n6 - Para info. da Disciplina. ')
    opt = int(input('>>>>>>'))
    while opt < 1 or opt > 6:
        print('           OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!     \n1 - Para cadastrar Professor; \n2 - Para editar Professor; \n3 - Para cadastrar Disciplina; \n4 - Para editar Disciplina; \n5 - para info. do Professor; \n6 - Para info. da Disciplina. ')
        opt = int(input('>>>>>>'))

    if opt == 1 :
        nome = str(input('Nome do professor:  '))
        email = str(input('Email do professor:  '))
        ra = str(input('RA do professor:  '))
        celular = int(input('Celular do professor:  '))
        print('          CONCLUÍDO!!!    \n          .          \n          .          \n          .')
        opt = 999

    
    if opt == 2:
        print ('Ecolha a informação a ser editada:  \n1 - Para nome; \n2 - Para email; \n3 - Para RA; \n4 - Para celular.')
        opteditp = int(input('>>>>>>'))
        while opteditp < 1 or opteditp > 4:
            print ('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!\nEcolha a informação a ser editada:  \n1 - Para nome; \n2 - Para email; \n3 - Para RA; \n4 - Para celular.')
            opteditp = int(input('>>>>>>'))
        if opteditp == 1:
            print (prof.nomeSet())
        if opteditp == 2:
            print (prof.emailSet())
        if opteditp == 3:
            print (prof.raSet())
        if opteditp == 4:
            print (prof.celularSet())
        print('          CONCLUÍDO!!!    \n          .          \n          .          \n          .')
        opt = 999

    if opt == 3:
        nomedcp = str(input('Nome da disciplina:  '))
        carg_hor = int(input('Carga horária da Disciplina: '))
        valor = float(input('Valor/hora:  '))
        print('          CONCLUÍDO!!!    \n          .          \n          .          \n          .')
        opt = 999

    if opt == 4:
        print ('Ecolha a informação a ser editada:  \n1 - Para nome; \n2 - Para carga horária.')
        opteditd = int(input('>>>>>>'))
        while opteditd < 1 or opteditd > 2:
            print ('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!\nEcolha a informação a ser editada:  \n1 - Para nome; \n2 - Para carga horária. ')
            opteditd = int(input('>>>>>>'))
        if opteditd == 1:
            print (dcp.nomedcpSet())
        if opteditd == 2:
            print (dcp.carg_horSet())
        print('          CONCLUÍDO!!!    \n          .          \n          .          \n          .')
        opt = 999

    if opt == 5:
        print ('Nome do professor: ',prof.nomeGet())
        print ('Email: ',prof.emailGet())
        print ('RA: ',prof.raGet())
        print ('Celular: ',prof.celularGet())
        print ('Disciplina: ',dcp.nomedcpGet())
        pause = str(input('>>>Qualquer tecla para continuar...'))
        print ('          CONCLUÍDO!!!    \n          .          \n          .          \n          .')
        opt = 999


    if opt == 6:
        print ('Nome da disciplina: ',dcp.nomedcpGet())
        print ('Carga horária: ',dcp.carg_horGet(),'H')
        print ('Professor: ',prof.nomeGet())
        pause = str(input('>>>Qualquer tecla para continuar...'))
        print ('          CONCLUÍDO!!!    \n          .          \n.          \n          .')
        opt = 999
        
#--------------------------------------------------------------------------------------        
        
        















