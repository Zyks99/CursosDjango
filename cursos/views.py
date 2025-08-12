# En cursos/views.py
from django.shortcuts import render, redirect
from .models import Cursos
from .forms import CursosForm
from django.shortcuts import get_object_or_404
# Create your views here.

def cursos(request):
    form = CursosForm()
    return render(request, "contenido/cursos.html", {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos') 
        else:
            return render(request, 'contenido/cursos.html', {'form': form})
    form = CursosForm()
    return render(request, 'contenido/cursos.html', {'form': form})

def verCursos(request):

    cursos = Cursos.objects.all()

    # Pasa los cursos obtenidos al contexto del template
    return render(request, 'contenido/ver_cursos.html', {'cursos': cursos})
def editarCurso(request, id): # Recibe el ID del curso a editar
    # get_object_or_404 busca el objeto por ID, si no lo encuentra, lanza un 404
    curso = get_object_or_404(Cursos, id=id)

    if request.method == 'POST':

        form = CursosForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save() # Guarda los cambios en el curso existente
            return redirect('ver_cursos') # Redirige a la lista de cursos
        else:
            # Si el formulario no es válido, lo renderiza de nuevo con los errores
            return render(request, 'contenido/editar_curso.html', {'form': form, 'curso': curso})
    else: # Si es GET, muestra el formulario prellenado
        form = CursosForm(instance=curso) # Instancia el formulario con los datos del curso
    return render(request, 'contenido/editar_curso.html', {'form': form, 'curso': curso})


def eliminarCurso(request, id):
    # Obtener el curso específico que se va a eliminar
    curso_a_eliminar = get_object_or_404(Cursos, id=id)

    if request.method == 'POST':
        # Si la solicitud es POST, el usuario confirmó la eliminación
        curso_a_eliminar.delete()
        # Redirigir a la vista que muestra todos los cursos
        return redirect('ver_cursos') # Asegúrate de que este sea el nombre de la URL correcta
    else:
        # Si la solicitud es GET, mostrar la página de confirmación
        # Se pasa 'curso_a_eliminar' como 'object' al contexto del template
        return render(request, 'contenido/confirmarEliminacion.html', {'object': curso_a_eliminar})
