from django.shortcuts import render

# Create your views here.
#Lista para almacenar datos temporalmente
contacts = []
def insertar(request):
    nombre = correo = mensaje = ''  # Inicializamos las variables

    # Si la solicitud es POST, capturamos los datos enviados por el formulario
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('correo', '')
        mensaje = request.POST.get('mensaje', '')

        #agregar datos a la lista
        contacts.append({'nombre':nombre,'correo':correo,'mensaje':mensaje})
    
    # Pasamos los datos al template para mostrarlos
    return render(request, 'insertar.html', {
        # 'nombre': nombre,
        # 'correo': correo,
        # 'mensaje': mensaje
        'contacts': contacts
    })