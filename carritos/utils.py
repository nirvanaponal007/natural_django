from .models import Carro


def obtener_o_crear_carrito(request):

    usuario_pk = request.user if request.user.is_authenticated else None
    carro_pk = request.session.get('carro_id')
    carro = Carro.objects.filter(carro_id=carro_pk ).first()

    if carro is None:
        carro = Carro.objects.create(usuario=usuario_pk)

    if usuario_pk and carro.usuario is None:
        carro.usuario = usuario_pk
        carro.save()



    request.session['carro_id'] = carro.carro_id
    #print('carro_id:'+ str(carro))
    #print('carro_pk:'+ str(carro_pk))
    #print('usuario:'+ str(usuario_pk))

    return carro
