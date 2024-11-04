from aeroalpes.modulos.vuelos.dominio.objetos_valor import Odo, ParametroBusca, Segmento, Leg, CodigoIATA, Itinerario
from aeroalpes.modulos.vuelos.dominio.entidades import Proveedor,Aeropuerto

def filtrar_mejores_itinerarios(itinerarios: list[Itinerario]) -> list[Itinerario]:
    # Logica compleja para filtrar itinerarios
    ...
    return itinerarios


def buscar_itinerarios(odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
    itinerarios: list[Itinerario] = list()
    proveedores: list[Proveedor] = rp.obtener_todos()

    itinerarios.append([proveedor.obtener_itinerarios(odos, parametros) for proveedor in proveedores])

    return filtrar_mejores_itinerarios(itinerarios)
