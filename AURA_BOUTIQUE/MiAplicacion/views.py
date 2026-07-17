from django.shortcuts import render,HttpResponse


# Create your views here.
def hola_mundo(request):
    return HttpResponse("""
                          <h1> hola mundo </h1>
                       """)



def pagina(request):
    return HttpResponse("""
                          <h1> Sitio Web </h1>
                          <h3> vistete diferente sientete unica </h3>
                       """)