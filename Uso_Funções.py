#!/usr/bin/env python
# coding: utf-8

# # Criando programa desconto cinema 

# ### 1 - Aluno do ensino público 25% de desconto 
# ### 2 - Aluno com carteirinha de estudante 50% de desconto
# ### 3 - Professores 60% de desconto
# ### 4 - Idosos acima dos 60 anos 75% de desconto
# ### 5 - Crianças abaixo de 6 anos 80% de desconto 

# In[1]:


print("********************Programa desconto************************\n")
   
def aluno(x):
   return round(x - (x * 0.25),2)

def aluno_carteirinha(x):
   return round(x - (x * 0.5),2)

def professores(x):
   return round(x - (x * 0.6),2)

def idosos(x):
   return round(x - (x * 0.75),2)

def criancas(x):
   return round(x - (x * 0.8),2)


print("\nSelecione a opção correspondente.\n")
print("1 - Aluno do ensino público")
print("2 - Aluno com carteirinha de estudante")
print("3 - Professores")
print("4 - Idosos acima dos 60 anos")
print("5 - Crianças abaixo dos 6 anos\n")

escolha = input("\nDigite a opção do cliente: ")

valor_ingresso = float(input("Digite o valor do ingresso: "))

if escolha == "1":
   print("\n")
   print("O valor do ingresso com desconto de 25% é: R$", aluno(valor_ingresso))
   print("\n")
   
elif escolha == '2':
   print("\n")
   print("O valor do ingresso com desconto de 50% é: R$", aluno_carteirinha(valor_ingresso))
   print("\n")
   
elif escolha == '3':
   print("\n")
   print("O valor do ingresso com desconto de 60% é: R$", professores(valor_ingresso))
   print("\n")
   
elif escolha == '4':
   print("\n")
   print("O valor do ingresso com desconto de 75% é: R$", idosos(valor_ingresso))
   print("\n")
   
elif escolha == '5':
   print("\n")
   print("O valor do ingresso com desconto de 80% é: R$", criancas(valor_ingresso))
   print("\n")
   
else:
   print("Digite uma opção válida.")




# In[ ]:




