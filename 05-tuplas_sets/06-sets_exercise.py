python_course = {'Ana', 'Luis', 'Carlos', 'Marta','Pedro'}
java_course = {'Luis', 'Marta', 'Sofia', 'Diego'}

# Estudiantes inscritos en ambos cursos
both_courses = python_course.intersection(java_course)
print("Estudiantes en ambos cursos:", both_courses)
# Estudiantes inscritos en el de python pero no en el de java
only_python = python_course.difference(java_course)
print("Estudiantes solo en el curso de Python pero no en Java:", only_python)
# Todos los estudiantes inscritos en al menos uno de los cursos
all_students = python_course.union(java_course)
print("Todos los estudiantes en ambos cursos:", all_students)
# Estudiantes inscritos en un solo curso (no en ambos), quitramos la intersección
exclusive_students = python_course.symmetric_difference(java_course)
print("Estudiantes en un solo curso:", exclusive_students)

