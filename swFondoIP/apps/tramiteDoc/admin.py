from django.contrib import admin
from .models import MTabla, DTabla, MPersonal, MCliente, MProyecto, MProtocolo, DProtocolo, DProyecto, MColaborador, MUsuarioDer, Bandeja, PProyectos, CPProyectos, CargaPresupuesto

admin.site.register(MTabla)
admin.site.register(DTabla)
admin.site.register(MPersonal)
admin.site.register(MCliente)
admin.site.register(MProyecto)
admin.site.register(MProtocolo)
admin.site.register(DProtocolo)
admin.site.register(DProyecto)
admin.site.register(MColaborador)
admin.site.register(MUsuarioDer)
admin.site.register(Bandeja)
admin.site.register(PProyectos)
admin.site.register(CPProyectos)
admin.site.register(CargaPresupuesto)