class Restaurante: 

  def __init__(self, nome, tipo_cozinha):
      self.restaurante = nome
      self.tipo = tipo_cozinha
      self.status = 'Aberto'
      self.atendidas = 0

  def Atendidas(self):
    print(f'<Quantidade de pessoas atendidas : {self.atendidas}>')
    atendidas = int(input("/nentre com o numero de clientes atendidos"))
    return atendidas


    

  def exibir(self):
    descricao= f'Restaurante {self.restaurante}: cozinha:{self.tipo}'
    return descricao

  def situacao(self):
    print(f'O restaurante está {self.status}. Verifique o horário de funcionamento')

  def horario(self):
    horarios = f'Seg a Sex: 12h-16h\nSab: 12h- 22h\n Dom: fechado.'
    return horarios

  def __str__(self):
   return f'<Restaurante: {self.restaurante}>'


class Usuario:
  def __init__(self,sexo, nome, sobrenome, tipo_pagamento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.pagamento_tipo = tipo_pagamento

  def Desc(self):
        descricao = f'Usuario : {self.nome} {self.sobrenome} realizara o pagamento por : {self.pagamento}'
        return descricao

  def Saudacao(self):
        saudacao = f'Bem vindo(a) {self.nome} {self.sobrenome}'
        return saudacao
    