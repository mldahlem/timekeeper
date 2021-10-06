# timekeeper
Python program to keep track of working hours. This was written only with python3 in mind and it's not expected/guaranteed to work with any older versions. It doesn't work with any DB, it uses 'txt files'.

You can define any local do save the 'dat' files. To do it, change the following parameters:
- arq_projetos
- arq_tempos
- arq_valores

In this version, the file in the parameter arq_valores needs manual creation. The template for this file is:

project_name,value_per_hour

For example:

Project XYZ,100.00
Project ACME,125.00

The projects names need to be equal on both files: arq_projetos and arq_valores.

The file arq_projetos will be create by the program and you can create project names using menu option 1.
