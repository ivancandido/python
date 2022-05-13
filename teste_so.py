import platform
import getpass
from datetime import datetime

print("Nome da Maquina...............: ", platform.node())
print("Arquitetura...................: ", platform.architecture())
print("Sistema Operacional...........: ", platform.system())
print("Versão do SO..................: ", platform.release())
print("Processdor....................: ", platform.processor())
print("Versão do Pyton...............: ", platform.python_version())

print(datetime.now().year)

#prompt para receber uma senha
senha = getpass.getpass("Digite sua senha:")