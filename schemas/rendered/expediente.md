# Expediente (Suprema Corte de Justicia de la Nación) Schema

```txt
http://lexpp.com/lexLibrary/scjn/expediente.schema.json
```

Sentencias y Datos de Expedientes de la Suprema Corte de Justicia de la Nación


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [expediente.schema.json](../../out/expediente.schema.json "open original schema") |

## Expediente (Suprema Corte de Justicia de la Nación) Type

`object` ([Expediente (Suprema Corte de Justicia de la Nación)](expediente.md))

# Expediente (Suprema Corte de Justicia de la Nación) Properties

| Property                                              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                   |
| :---------------------------------------------------- | ------------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [LexppId](#LexppId)                                   | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexppid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/LexppId")                                   |
| [Lexpp_expedientes_id](#Lexpp_expedientes_id)         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexpp_expedientes_id.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/Lexpp_expedientes_id")         |
| [asuntoId](#asuntoId)                                 | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-asuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/asuntoId")                                 |
| [expedienteId](#expedienteId)                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-expedienteid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/expedienteId")                         |
| [tipoAsuntoId](#tipoAsuntoId)                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsuntoId")                         |
| [tipoAsunto](#tipoAsunto)                             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasunto.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsunto")                             |
| [pertenenciaId](#pertenenciaId)                       | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaId")                       |
| [pertenenecia](#pertenenecia)                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenecia.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenecia")                         |
| [oficioId](#oficioId)                                 | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-oficioid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/oficioId")                                 |
| [estadoDelExpediente](#estadoDelExpediente)           | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-estadodelexpediente.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/estadoDelExpediente")           |
| [ministroId](#ministroId)                             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroId")                             |
| [ministro](#ministro)                                 | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministro")                                 |
| [secretarioProyectista](#secretarioProyectista)       | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioproyectista.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioProyectista")       |
| [secretarioAuxiliar](#secretarioAuxiliar)             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioauxiliar.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioAuxiliar")             |
| [fechaRecepcion](#fechaRecepcion)                     | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharecepcion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaRecepcion")                     |
| [fechaTurnoMinistro](#fechaTurnoMinistro)             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechaturnoministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaTurnoMinistro")             |
| [fechaResolucion](#fechaResolucion)                   | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucion")                   |
| [actoReclamado](#actoReclamado)                       | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-actoreclamado.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/actoReclamado")                       |
| [autoridades](#autoridades)                           | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridades.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridades")                           |
| [autoridadesContendientes](#autoridadesContendientes) | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridadescontendientes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridadesContendientes") |
| [promoventes](#promoventes)                           | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-promoventes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/promoventes")                           |
| [area](#area)                                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-area.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/area")                                         |
| [tema](#tema)                                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tema.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tema")                                         |
| [temaFondo](#temaFondo)                               | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temafondo.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaFondo")                               |
| [resumenResolucion](#resumenResolucion)               | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resumenresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resumenResolucion")               |
| [organoOrigen](#organoOrigen)                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-organoorigen.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/organoOrigen")                         |
| [engroseUrl](#engroseUrl)                             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-engroseurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/engroseUrl")                             |
| [votosEspecialesUrl](#votosEspecialesUrl)             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votosespecialesurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosEspecialesUrl")             |
| [ministroResolucion](#ministroResolucion)             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucion")             |
| [secretarioResolucionId](#secretarioResolucionId)     | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucionId")     |
| [secretarioResolucion](#secretarioResolucion)         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucion")         |
| [resolucionId](#resolucionId)                         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resolucionId")                         |
| [pertenenciaResolucionId](#pertenenciaResolucionId)   | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucionId")   |
| [pertenenciaResolucion](#pertenenciaResolucion)       | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucion")       |
| [fechaSesion](#fechaSesion)                           | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechasesion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaSesion")                           |
| [fechaResolucionEngrose](#fechaResolucionEngrose)     | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucionengrose.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucionEngrose")     |
| [puntosResolutivos](#puntosResolutivos)               | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-puntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/puntosResolutivos")               |

## LexppId




`LexppId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexppid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/LexppId")

### LexppId Type

unknown

## Lexpp_expedientes_id




`Lexpp_expedientes_id`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexpp_expedientes_id.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/Lexpp_expedientes_id")

### Lexpp_expedientes_id Type

unknown

## asuntoId




`asuntoId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-asuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/asuntoId")

### asuntoId Type

unknown

## expedienteId




`expedienteId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-expedienteid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/expedienteId")

### expedienteId Type

unknown

## tipoAsuntoId




`tipoAsuntoId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsuntoId")

### tipoAsuntoId Type

unknown

## tipoAsunto




`tipoAsunto`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasunto.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsunto")

### tipoAsunto Type

unknown

## pertenenciaId




`pertenenciaId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaId")

### pertenenciaId Type

unknown

## pertenenecia




`pertenenecia`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenecia.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenecia")

### pertenenecia Type

unknown

## oficioId




`oficioId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-oficioid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/oficioId")

### oficioId Type

unknown

## estadoDelExpediente




`estadoDelExpediente`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-estadodelexpediente.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/estadoDelExpediente")

### estadoDelExpediente Type

unknown

## ministroId




`ministroId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroId")

### ministroId Type

unknown

## ministro




`ministro`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministro")

### ministro Type

unknown

## secretarioProyectista




`secretarioProyectista`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioproyectista.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioProyectista")

### secretarioProyectista Type

unknown

## secretarioAuxiliar




`secretarioAuxiliar`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioauxiliar.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioAuxiliar")

### secretarioAuxiliar Type

unknown

## fechaRecepcion




`fechaRecepcion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharecepcion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaRecepcion")

### fechaRecepcion Type

unknown

## fechaTurnoMinistro




`fechaTurnoMinistro`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechaturnoministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaTurnoMinistro")

### fechaTurnoMinistro Type

unknown

## fechaResolucion




`fechaResolucion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucion")

### fechaResolucion Type

unknown

## actoReclamado




`actoReclamado`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-actoreclamado.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/actoReclamado")

### actoReclamado Type

unknown

## autoridades




`autoridades`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridades.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridades")

### autoridades Type

unknown

## autoridadesContendientes




`autoridadesContendientes`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridadescontendientes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridadesContendientes")

### autoridadesContendientes Type

unknown

## promoventes




`promoventes`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-promoventes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/promoventes")

### promoventes Type

unknown

## area




`area`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-area.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/area")

### area Type

unknown

## tema




`tema`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tema.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tema")

### tema Type

unknown

## temaFondo




`temaFondo`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temafondo.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaFondo")

### temaFondo Type

unknown

## resumenResolucion




`resumenResolucion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resumenresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resumenResolucion")

### resumenResolucion Type

unknown

## organoOrigen




`organoOrigen`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-organoorigen.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/organoOrigen")

### organoOrigen Type

unknown

## engroseUrl




`engroseUrl`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-engroseurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/engroseUrl")

### engroseUrl Type

unknown

## votosEspecialesUrl




`votosEspecialesUrl`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votosespecialesurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosEspecialesUrl")

### votosEspecialesUrl Type

unknown

## ministroResolucion




`ministroResolucion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucion")

### ministroResolucion Type

unknown

## secretarioResolucionId




`secretarioResolucionId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucionId")

### secretarioResolucionId Type

unknown

## secretarioResolucion




`secretarioResolucion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucion")

### secretarioResolucion Type

unknown

## resolucionId




`resolucionId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resolucionId")

### resolucionId Type

unknown

## pertenenciaResolucionId




`pertenenciaResolucionId`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucionId")

### pertenenciaResolucionId Type

unknown

## pertenenciaResolucion




`pertenenciaResolucion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucion")

### pertenenciaResolucion Type

unknown

## fechaSesion




`fechaSesion`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechasesion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaSesion")

### fechaSesion Type

unknown

## fechaResolucionEngrose




`fechaResolucionEngrose`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucionengrose.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucionEngrose")

### fechaResolucionEngrose Type

unknown

## puntosResolutivos




`puntosResolutivos`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-puntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/puntosResolutivos")

### puntosResolutivos Type

unknown
