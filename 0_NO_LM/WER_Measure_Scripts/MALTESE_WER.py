#-*- coding: utf-8 -*- 
#############################################################################################
#MALTESE_WER.py

#Autor: Carlos Daniel Hernández Mena
#Fecha: 10 de Septiembre de 2020
#Lugar: Universidad de Malta

#Uso:

#	$ conda activate base
#	$ time python MALTESE_WER.py <json_in>

#Ejemplo de uso concreto:

#	$ conda activate base
#	$ time python MALTESE_WER.py Test_MASRI_HEADSET_V2.json

#Este programa toma como entrada un JSON de los audios que se
#quieren evaluar y se calcula el WER, el cual es mostrado 
#en la terminal.

#Este script utiliza el script jasper_eval.py que viene dentro
#de las utilidades de NeMo.

#NOTA. No olvidar el:

#	$ conda activate base

#Antes de correr este script.

#Nota: Este programa está pensado para Python 3
#Nota: Si el archivo de salida ya existía, este programa lo sobre-escribe
#############################################################################################
#Importar módulos necesarios

#Módulo para funciones del sistema operativo
import sys

#Módulo para manejar expresiones regulares
import re

#Módulo para manejar funciones del sistema operativo
import os

#Módulo para hacer operaciones con archivos y carpetas
import shutil

#Módulo para capturar lo que entrea un os.system()
import subprocess

#Librería para poder abrir paginas web
#from urllib.request import urlopen
#############################################################################################

#Crear el archivo de salida
#archivo_out = open("archivo_out.txt",'w')

#Abrir el archivo de entrada cuyo nombre es tomado de la línea de comandos
	
#Nota:
#sys.argv[0] me entrega el nombre de este script
#sys.argv[1] me entrega el primer argumento enviado desde la línea de comandos
#sys.argv[n] me entrega el enesimo argumento enviado desde la línea de comandos
#sys.argv    me entrega una lista con todos los argumentos desde el argv[0] hasta el argv[n]

#Este es el JSON con los audios que se quieren evaluar.
EVAL_DATASETS = sys.argv[1]

#############################################################################################
#VARIABLES GLOBALES.

#Estas variables se le pasan directamemnte al script jasper_eval.py

BATCH_SIZE = 32

MODEL_CONFIG = '/home/carlos/DATOS/VARIOS_PROGRAMAS/NeMo/MALTESE_WER/Model_Architecture/jasper_an4_NEW_ORTHO.yaml'

#Checkpoints of baseline models
LOAD_DIR = '/home/carlos/Desktop/EXPERIMENTS/0_NO_LM/WER_Measure_Scripts/Baseline_CHECKPOINTS'

#Checkpoints of Best WER found
#LOAD_DIR = '/home/carlos/Desktop/EXPERIMENTS/0_NO_LM/WER_Measure_Scripts/BestWER_CHECHPOINTS'

#LM_8.7MB_AGAINST
#LM_PATH = '/home/carlos/Desktop/EXPERIMENTS/0_NO_LM/LM_8.7MB_AGAINST/Maltese-6-gram-lm.binary'

#LM_9.5MB_IN_FAVOR
LM_PATH = '/home/carlos/Desktop/EXPERIMENTS/0_NO_LM/LM_9.5MB_IN_FAVOR/Texto_Maltes_para_ML-lm.binary'

#############################################################################################
#Se ejecuta el script jasper_eval.py

#NOTA. No olvidar el:
#	$ conda activate base

#El comando exacto invicado es:

#python jasper_eval.py --batch_size=32 --model_config=/home/carlos/DATOS/VARIOS_PROGRAMAS/NeMo/ENGLISH_WER/Model_Architecture/jasper12x1SEP.yaml --eval_datasets "../DEV_CLEAN.json" --load_dir=/home/carlos/DATOS/VARIOS_PROGRAMAS/NeMo/ENGLISH_WER/CHECKPOINTS --lm_path=/home/carlos/DATOS/VARIOS_PROGRAMAS/NeMo/LANGUAGE_MODELS/ENGLISH-6-gram-lm.binary

#Crea el comando
comando = 'python jasper_eval.py --batch_size='+str(BATCH_SIZE)+' --model_config='+MODEL_CONFIG+' --eval_datasets \"../'+EVAL_DATASETS+'\" --load_dir='+LOAD_DIR+' --lm_path='+LM_PATH

#Cambiar al directorio donde esta el script jasper_eval.py
os.chdir('JASPER_EVAL')

#Corre el comando
os.system(comando)

#############################################################################################

