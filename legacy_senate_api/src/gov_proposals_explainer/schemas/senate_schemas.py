import datetime
from pydantic import BaseModel, Field, field_serializer


class BillParams(BaseModel):
    year: int | None
    bill_type: str | None
    number: int | None
    author: str | None
    keyword: str | None


class BillCode(BaseModel):
    code: str


class BillType(BaseModel):
    bill_type: str = Field(alias="Sigla", serialization_alias="bill_type")
    description: str = Field(alias="Descricao", serialization_alias="description")


class BillSpecs(BaseModel):
    code: str = Field(alias="Codigo", serialization_alias="code")
    process_id: str = Field(
        alias="IdentificacaoProcesso", serialization_alias="process_id"
    )
    decription_id: str = Field(
        alias="DescricaoIdentificacao", serialization_alias="decription_id"
    )
    bill_type: str = Field(alias="Sigla", serialization_alias="bill_type")
    number: str = Field(alias="Numero", serialization_alias="number")
    year: int = Field(alias="Ano", serialization_alias="year")
    syllabus: str = Field(alias="Ementa", serialization_alias="syllabus")
    author: str = Field(alias="Autor", serialization_alias="author")
    date: datetime.date = Field(alias="Data", serialization_alias="date")


class BillText(BaseModel):
    code: str = Field(alias="CodigoTexto", serialization_alias="code")
    document_type: str = Field(
        alias="TipoDocumento", serialization_alias="document_type"
    )
    text_format: str = Field(alias="FormatoTexto", serialization_alias="text_format")
    text_type: str = Field(
        alias="DescricaoTipoTexto", serialization_alias="text_type"
    )
    text_description: str = Field(
        alias="DescricaoTexto", serialization_alias="text_description"
    )
    text_author: str = Field(alias="AutoriaTexto", serialization_alias="text_author")
    text_date: datetime.date = Field(
        alias="DataTexto", serialization_alias="text_date"
    )
    text_url: str = Field(alias="UrlTexto", serialization_alias="text_url")

    @field_serializer("text_url")
    def serialize_text_url(self, text_url: str, _info):
        inline_text_url = f"{text_url}&disposition=inline"
        return inline_text_url
