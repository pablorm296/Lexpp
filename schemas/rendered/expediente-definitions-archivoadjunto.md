# Untitled object in Expediente (Suprema Corte de Justicia de la Nación) Schema

```txt
http://lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [expediente.schema.json\*](../../out/expediente.schema.json "open original schema") |

## archivoAdjunto Type

`object` ([Details](expediente-definitions-archivoadjunto.md))

# undefined Properties

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                       |
| :---------------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                       | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-type.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/type")                       |
| [rawMeta](#rawMeta)                 | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawmeta.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawMeta")                 |
| [rawContent](#rawContent)           | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContent")           |
| [rawContentPlain](#rawContentPlain) | `string` | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontentplain.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContentPlain") |
| [content](#content)                 | `array`  | Optional | cannot be null | [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/content")                 |

## type

Tipo de archivo adjunto (engrose o votos)


`type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-type.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/type")

### type Type

`string`

## rawMeta

Metadata sin procesar extraída por Apache Tika


`rawMeta`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawmeta.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawMeta")

### rawMeta Type

`string`

## rawContent

Contenido del archivo extraído por Apache Tika en formato XHTML


`rawContent`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontent.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContent")

### rawContent Type

`string`

## rawContentPlain

Contenido del archivo extraído por Apache Tika en texto plano (sin formato alguno)


`rawContentPlain`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-rawcontentplain.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/rawContentPlain")

### rawContentPlain Type

`string`

## content

Contenido procesado del archivo. Cada elemento en el array es un párrado del archivo


`content`

-   is optional
-   Type: `object[]` ([Details](expediente-definitions-parrafo.md))
-   cannot be null
-   defined in: [Expediente (Suprema Corte de Justicia de la Nación)](expediente-definitions-archivoadjunto-properties-content.md "http&#x3A;//lexpp.com/lexLibrary/scjn/expediente.schema.json#/definitions/archivoAdjunto/properties/content")

### content Type

`object[]` ([Details](expediente-definitions-parrafo.md))
