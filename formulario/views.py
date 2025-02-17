from django.shortcuts import render, redirect
#Importamos para validar correo 
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

# Create your views here.
#Lista para almacenar datos temporalmente
contacts = []
def insertar(request):
    nombre = correo = mensaje = ''  # Inicializamos las variables
    #Lista para agregar Errores, es necesaria?
    errors = []

    # Si la solicitud es POST, capturamos los datos enviados por el formulario
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('correo', '')
        mensaje = request.POST.get('mensaje', '')

        #Comprobar campos vacios
        if not nombre:
            errors.append("EL campo nombre es obligatorio")
        if not correo:
            errors.append("EL campo correo es obligatorio")
        if not mensaje:
            errors.append("EL campo mensaje es obligatorio")

        #validamos el formato de correo electronico
        validarCorreo = EmailValidator()    
        try:
            validarCorreo(correo)
        except ValidationError:
            errors.append('El formato de correo es invalido.')
            print(errors)

        #Si estan todos los campos completos los pasamos a la lista de contacts
        if not errors:
            #agregar datos a la lista
            contacts.append({'nombre':nombre,'correo':correo,'mensaje':mensaje})
    
    # Pasamos los datos al template para mostrarlos
    return render(request, 'insertar.html', {
        # 'nombre': nombre,
        # 'correo': correo,
        # 'mensaje': mensaje
        'contacts': contacts,
        'errors': errors #retornamos los errores
    })

##Editar
def editar(request, index):
    contact = contacts[index]
    if request.method == 'POST':
        contacts[index]= {
            'nombre': request.POST.get('nombre',contact['nombre']),
            'correo': request.POST.get('correo',contact['correo']),
            'mensaje': request.POST.get('mensaje',contact['mensaje']),
        }
        #redirige a la url "" que es la inicial
        return redirect('')
    return render(request, 'editar.html', {'contact':contact, 'index':index})

##Eliminar
def eliminar(request, index):
    if request.method == 'POST':
        contacts.pop(index) # elimina
        return redirect('') #redirige
    return render(request, 'eliminar.html', {'contact': contacts[index], 'index': index}) #envia a la vista y confirma
