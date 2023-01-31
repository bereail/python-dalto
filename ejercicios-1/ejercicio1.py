#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#diferencias de duracion
diferencia_con_min = dalto_curso = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = dalto_curso = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = dalto_curso = 100 - dalto_curso / otros_cursos_promedio * 100

print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')

#diferecia de crudos
crudos_promedio = 5
crudo_dalto = 3.5

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudos_promedio / 10

print(f"El cirps de dañtp dura un {tiempo_vacio_promedio}% de tiempo vacio")

