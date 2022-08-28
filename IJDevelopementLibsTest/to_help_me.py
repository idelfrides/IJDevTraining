import os, sys
import shutil

from IJGeneralUsagePackage.hold_constants_paths import (
    IJG_USAGE
)

'''
os.remove('nome do arquivo') #remove arquivo
os.removedirs('caminho do diretorio') #remove estrutura de diretorios
os.rename('nome antigo','nome novo') #renomeia arquivo
os.getcwd() #retorna diretorio atual
os.rmdir('nome do diretorio') #remove diretorio
os.mkdir('nome do diretorio') #cria diretorio
os.chdir('nome do diretorio') #muda diretorio (cd)
os.listdir('diretorio base') #lista diretorio
os.walk('diretorio base') #navega pela arvore de diretorios
os.path.exists('nome_do_arquivo') #verifica se arquivo existe
os.path.basename('nome do arquivo') #retorna o nome do arquivo, sem diretorio
os.path.dirname('nome do arquivo') #retorna o caminho do arquivo, sem o nome
os.path.getatime('nome do arquivo') #retorna a data do ultimo acesso
os.path.getctime('nome do arquivo') #retorna a data de criacao
os.path.getmtime('nome do arquivo') #retorna a data da ultima alteracao
os.path.getsize('nome do arquivo') #retorna o tamanho do arquivo em bytes
os.path.isdir('nome do arquivo') #verifica se o arquivo passado é um diretório
os.path.isfile('nome do arquivo') #verifica se o arquivo passado é um arquivo
os.path.join('dir1', 'dir2') #concatena dois elementos para formar um caminho
os.path.split('dir1', 'dir2') #retorna lista com todas as partes de um caminho
shutil.copy('origem','destino') #copia arquivo
shutil.move('origem','destino') #move arquivo


PROFISSIONAL_FOLDER = '/media/ijdev/DATA/PROFISSIONAL/'
DOWNLOAD_FOLDER_PATH = '/home/ijdev/Downloads/'
VALERIA_PROJECT_FOLDER_PATH = '/media/ijdev/DATA/PROFISSIONAL/VALERIA_FERREIRA_LIMA/'

COMERCIAL_FOLDER = 'COMERCIALFERREIRALIMA'
MAGALU_STORE = 'MAGAZINE_LUIZA'
ODERCO = 'ODERCO'
ODERCO_PATH = VALERIA_PROJECT_FOLDER_PATH + MAGALU_STORE + '/' + ODERCO + '/'
SD_STAGE = '/media/ijdev/DATA/senseData/sc_bin/stage/c93_navita/'


echo "# testChange_branch" >> README.md

'''
