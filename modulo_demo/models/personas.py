# -*- coding: utf-8 -*-
from odoo import models, fields


class Persona(models.Model):
    _name = 'persona.main_data'

    name = fields.Char(
        string="Nombre de la persona",
        required=True,
        help="Esta es la ayuda para el nombre de la persona",
        index=True,
    )

    edad = fields.Integer(
        string="Edad de la persona",
        required=True,
        default=15,
    )

    es_casado = fields.Boolean(
        string="¿Es casado?"
    )

    datos_personales = fields.Html(
        string="Datos personales",
    )

    informacion_adicional = fields.Text(
        string="Información adicional"
    )

    foto = fields.Binary(
        string="Foto",
        help="Agregue la foto de la persona"
    )

    sexo = fields.Selection(
        selection=[
            ('femenino', 'Femenino'),
            ('masculino', 'Masculino'),
            ('otro', 'Otro'),
        ],
        string="Sexo",
        required=True,
        default='otro'
    )
