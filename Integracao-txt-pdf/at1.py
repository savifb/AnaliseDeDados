import os
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'Alunos.txt')
arquivo = open(file_path, 'r')
print(arquivo.readlines())
