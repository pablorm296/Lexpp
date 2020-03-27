# Expediente (Suprema Corte de Justicia de la Nación) Schema

```txt
http://lexpp.com/lexLibrary/scjn/expediente.schema.json
```

Sentencias y Datos de Expedientes de la Suprema Corte de Justicia de la Nación


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Allowed               | none                | [expediente.schema.json](../../out/expediente.schema.json "open original schema") |

## Expediente (Suprema Corte de Justicia de la Nación) Type

`object` ([Expediente (Suprema Corte de Justicia de la Nación)](expediente.md))

# Expediente (Suprema Corte de Justicia de la Nación) Definitions

## Definitions group archivoAdjunto

Reference this group by using

```json
{"$ref":"http://lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto"}
```

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :---------------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                       | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-type.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/type")                       |
| [rawMeta](#rawMeta)                 | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawmeta.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawMeta")                 |
| [rawContent](#rawContent)           | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContent")           |
| [rawContentPlain](#rawContentPlain) | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontentplain.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContentPlain") |
| [content](#content)                 | `array`  | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/content")                 |

### type

Tipo de archivo adjunto (engrose o votos)


`type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-type.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/type")

#### type Type

`string`

### rawMeta

Metadata sin procesar extraída por Apache Tika


`rawMeta`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawmeta.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawMeta")

#### rawMeta Type

`string`

### rawContent

Contenido del archivo extraído por Apache Tika en formato XHTML


`rawContent`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContent")

#### rawContent Type

`string`

### rawContentPlain

Contenido del archivo extraído por Apache Tika en texto plano (sin formato alguno)


`rawContentPlain`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontentplain.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContentPlain")

#### rawContentPlain Type

`string`

### content

Contenido procesado del archivo. Cada elemento en el array es un párrado del archivo


`content`

-   is optional
-   Type: `object[]` ([Details](expediente-definitions-parrafo.md))
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/content")

#### content Type

`object[]` ([Details](expediente-definitions-parrafo.md))

## Definitions group parrafo

Reference this group by using

```json
{"$ref":"http://lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/parrafo"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                               |
| :------------------------ | ------------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [content](#content)       | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-parrafo-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/parrafo/properties/content")       |
| [attributes](#attributes) | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-parrafo-properties-attributes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/parrafo/properties/attributes") |

### content

Contenido del párrafo en formato XHTML


`content`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-parrafo-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/parrafo/properties/content")

#### content Type

`string`

### attributes

Atributos asociados al párrafo en formato XHTML


`attributes`

-   is optional
-   Type: unknown
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-parrafo-properties-attributes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/parrafo/properties/attributes")

#### attributes Type

unknown

# Expediente (Suprema Corte de Justicia de la Nación) Properties

| Property                                                | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :------------------------------------------------------ | ------------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [LexppId](#LexppId)                                     | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexppid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/LexppId")                                     |
| [Lexpp_expedientesId](#Lexpp_expedientesId)             | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexpp_expedientesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/Lexpp_expedientesId")             |
| [asuntoId](#asuntoId)                                   | `integer`     | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-asuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/asuntoId")                                   |
| [expedienteId](#expedienteId)                           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-expedienteid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/expedienteId")                           |
| [tipoAsuntoId](#tipoAsuntoId)                           | `integer`     | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsuntoId")                           |
| [tipoAsunto](#tipoAsunto)                               | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasunto.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsunto")                               |
| [pertenenecia](#pertenenecia)                           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenecia.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenecia")                           |
| [oficioId](#oficioId)                                   | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-oficioid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/oficioId")                                   |
| [estadoDelExpediente](#estadoDelExpediente)             | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-estadodelexpediente.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/estadoDelExpediente")             |
| [ministroId](#ministroId)                               | `integer`     | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroId")                               |
| [ministro](#ministro)                                   | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministro")                                   |
| [secretarioProyectista](#secretarioProyectista)         | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioproyectista.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioProyectista")         |
| [secretarioAuxiliar](#secretarioAuxiliar)               | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioauxiliar.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioAuxiliar")               |
| [fechaRecepcion](#fechaRecepcion)                       | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharecepcion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaRecepcion")                       |
| [fechaTurnoMinistro](#fechaTurnoMinistro)               | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechaturnoministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaTurnoMinistro")               |
| [fechaResolucion](#fechaResolucion)                     | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucion")                     |
| [actoReclamado](#actoReclamado)                         | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-actoreclamado.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/actoReclamado")                         |
| [autoridades](#autoridades)                             | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridades.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridades")                             |
| [autoridadesContendientes](#autoridadesContendientes)   | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridadescontendientes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridadesContendientes")   |
| [promoventes](#promoventes)                             | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-promoventes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/promoventes")                             |
| [area](#area)                                           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-area.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/area")                                           |
| [tema](#tema)                                           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tema.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tema")                                           |
| [temaLexpp](#temaLexpp)                                 | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temalexpp.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaLexpp")                                 |
| [temaFondo](#temaFondo)                                 | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temafondo.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaFondo")                                 |
| [resumenResolucion](#resumenResolucion)                 | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resumenresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resumenResolucion")                 |
| [organoOrigen](#organoOrigen)                           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-organoorigen.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/organoOrigen")                           |
| [engroseUrl](#engroseUrl)                               | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-engroseurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/engroseUrl")                               |
| [ministroResolucionId](#ministroResolucionId)           | `integer`     | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucionId")           |
| [ministroResolucion](#ministroResolucion)               | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucion")               |
| [secretarioResolucionId](#secretarioResolucionId)       | `integer`     | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucionId")       |
| [secretarioResolucion](#secretarioResolucion)           | `string`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucion")           |
| [resolucionId](#resolucionId)                           | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resolucionId")                           |
| [pertenenciaResolucionId](#pertenenciaResolucionId)     | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucionId")     |
| [pertenenciaResolucion](#pertenenciaResolucion)         | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenciaresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenciaResolucion")         |
| [fechaSesion](#fechaSesion)                             | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechasesion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaSesion")                             |
| [fechaResolucionEngrose](#fechaResolucionEngrose)       | Not specified | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucionengrose.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucionEngrose")       |
| [puntosResolutivos](#puntosResolutivos)                 | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-puntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/puntosResolutivos")                 |
| [votosPuntosResolutivos](#votosPuntosResolutivos)       | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votospuntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosPuntosResolutivos")       |
| [ministroVotosEspeciales](#ministroVotosEspeciales)     | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministrovotosespeciales.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroVotosEspeciales")     |
| [ministroVotosEspecialesId](#ministroVotosEspecialesId) | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministrovotosespecialesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroVotosEspecialesId") |
| [tipoVotosEspeciales](#tipoVotosEspeciales)             | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipovotosespeciales.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoVotosEspeciales")             |
| [tipoVotosEspecialesId](#tipoVotosEspecialesId)         | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipovotosespecialesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoVotosEspecialesId")         |
| [votosEspecialesUrl](#votosEspecialesUrl)               | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votosespecialesurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosEspecialesUrl")               |
| [rawContent](#rawContent)                               | `object`      | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/rawContent")                               |
| [documents](#documents)                                 | `array`       | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-documents.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/documents")                                 |

## LexppId

ID del documento (asignado para toda la biblioteca de Lex++)


`LexppId`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexppid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/LexppId")

### LexppId Type

`string`

## Lexpp_expedientesId

ID del documento (asignado para la biblioteca de expedientes de Lex++)


`Lexpp_expedientesId`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-lexpp_expedientesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/Lexpp_expedientesId")

### Lexpp_expedientesId Type

`string`

## asuntoId

ID numérico del expediente (asignado por la SCJN)


`asuntoId`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-asuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/asuntoId")

### asuntoId Type

`integer`

## expedienteId

ID del expediente (asignado por la SCJN en formato número/año)


`expedienteId`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-expedienteid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/expedienteId")

### expedienteId Type

`string`

## tipoAsuntoId

ID del tipo de asunto


`tipoAsuntoId`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasuntoid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsuntoId")

### tipoAsuntoId Type

`integer`

## tipoAsunto

Tipo de asunto


`tipoAsunto`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipoasunto.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoAsunto")

### tipoAsunto Type

`string`

## pertenenecia

Órgano de pertenencia con el que se registró el expediente (pleno, primera o segunda sala)


`pertenenecia`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-pertenenecia.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/pertenenecia")

### pertenenecia Type

`string`

## oficioId




`oficioId`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-oficioid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/oficioId")

### oficioId Type

`string`

## estadoDelExpediente




`estadoDelExpediente`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-estadodelexpediente.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/estadoDelExpediente")

### estadoDelExpediente Type

`string`

## ministroId

ID del Ministro al que se turnó el expediente


`ministroId`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroId")

### ministroId Type

`integer`

## ministro

Ministro al que se turnó el expediente


`ministro`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministro")

### ministro Type

`string`

## secretarioProyectista

Secretario Proyectista con el que se registró el expediente


`secretarioProyectista`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioproyectista.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioProyectista")

### secretarioProyectista Type

`string`

## secretarioAuxiliar

Secretario Auxiliar con el que s e registró el expediente


`secretarioAuxiliar`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioauxiliar.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioAuxiliar")

### secretarioAuxiliar Type

`string`

## fechaRecepcion

Fecha de recepción del expediente


`fechaRecepcion`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharecepcion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaRecepcion")

### fechaRecepcion Type

`string`

## fechaTurnoMinistro

Fecha en que se turnó el expediente al Ministro correspondiente


`fechaTurnoMinistro`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fechaturnoministro.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaTurnoMinistro")

### fechaTurnoMinistro Type

`string`

## fechaResolucion

Fecha en que se emitió una resolución (sentencia) al expediente


`fechaResolucion`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-fecharesolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/fechaResolucion")

### fechaResolucion Type

`string`

## actoReclamado

Acto reclamado


`actoReclamado`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-actoreclamado.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/actoReclamado")

### actoReclamado Type

`string`

## autoridades

Autoridades a las que se les hace el reclamo


`autoridades`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridades.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridades")

### autoridades Type

`string`

## autoridadesContendientes

Autoridades contendientes


`autoridadesContendientes`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-autoridadescontendientes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/autoridadesContendientes")

### autoridadesContendientes Type

`string`

## promoventes

Promoventes del expediente


`promoventes`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-promoventes.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/promoventes")

### promoventes Type

`string`

## area

Área en que se registró el expediente


`area`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-area.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/area")

### area Type

`string`

## tema

Tema(s) registrados por el catálogo de la SCJN


`tema`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tema.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tema")

### tema Type

`string`

## temaLexpp

Tema(s) registrados por el sistema de Lex++


`temaLexpp`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temalexpp.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaLexpp")

### temaLexpp Type

`array`

## temaFondo

Tema de fondo registrado por el catálogo de la SCJN


`temaFondo`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-temafondo.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/temaFondo")

### temaFondo Type

`string`

## resumenResolucion

Resumen de la resolución (sentencia) que dio la SCJN al expediente


`resumenResolucion`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-resumenresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/resumenResolucion")

### resumenResolucion Type

`string`

## organoOrigen

Órgano(s) de origen del expediente


`organoOrigen`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-organoorigen.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/organoOrigen")

### organoOrigen Type

`string`

## engroseUrl

URL de la versión pública del engrose generado por la resolución del expediente


`engroseUrl`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-engroseurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/engroseUrl")

### engroseUrl Type

`string`

## ministroResolucionId

ID del Ministro que llevó la resolución del expediente


`ministroResolucionId`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucionId")

### ministroResolucionId Type

`integer`

## ministroResolucion

Ministro que llevó la resolución del expediente


`ministroResolucion`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministroresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroResolucion")

### ministroResolucion Type

`string`

## secretarioResolucionId

ID del Secretario que llevó la resolución del expediente


`secretarioResolucionId`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucionid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucionId")

### secretarioResolucionId Type

`integer`

## secretarioResolucion

Secretario que llevó la resolución del expediente


`secretarioResolucion`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-secretarioresolucion.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/secretarioResolucion")

### secretarioResolucion Type

`string`

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
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-puntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/puntosResolutivos")

### puntosResolutivos Type

`array`

## votosPuntosResolutivos




`votosPuntosResolutivos`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votospuntosresolutivos.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosPuntosResolutivos")

### votosPuntosResolutivos Type

`array`

## ministroVotosEspeciales




`ministroVotosEspeciales`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministrovotosespeciales.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroVotosEspeciales")

### ministroVotosEspeciales Type

`array`

## ministroVotosEspecialesId




`ministroVotosEspecialesId`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-ministrovotosespecialesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/ministroVotosEspecialesId")

### ministroVotosEspecialesId Type

`array`

## tipoVotosEspeciales




`tipoVotosEspeciales`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipovotosespeciales.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoVotosEspeciales")

### tipoVotosEspeciales Type

`array`

## tipoVotosEspecialesId




`tipoVotosEspecialesId`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-tipovotosespecialesid.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/tipoVotosEspecialesId")

### tipoVotosEspecialesId Type

`array`

## votosEspecialesUrl

URL(s) de los votos especiales registrados en el expediente


`votosEspecialesUrl`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-votosespecialesurl.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/votosEspecialesUrl")

### votosEspecialesUrl Type

`array`

## rawContent

Contenido del expediente (tal cual se recibió del servidor de la SCJN)


`rawContent`

-   is optional
-   Type: `object` ([Details](expediente-properties-rawcontent.md))
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/rawContent")

### rawContent Type

`object` ([Details](expediente-properties-rawcontent.md))

## documents

Lista de archivos (engroses y votos particulares) que venían adjuntos al expediente.


`documents`

-   is optional
-   Type: `object[]` ([Details](expediente-definitions-archivoadjunto.md))
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-properties-documents.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/properties/documents")

### documents Type

`object[]` ([Details](expediente-definitions-archivoadjunto.md))
