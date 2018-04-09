# -*- coding: utf-8 -*-

from odoo import models, fields, api


class academy(models.Model):
    _name = 'academy.academy'

    name = fields.Char("Nombre")
    active = fields.Boolean("Activo", default=True)
    students = fields.Integer("Cantidad de Estudiantes")
    budget = fields.Float("Presupuesto")
    history = fields.Text("Historia")
    career = fields.Selection([('ings', 'Ingenieria en Systemas'),
                               ('med', 'Medicina')])
    website = fields.Html("Website")
    start_date = fields.Date("Fundada")
    open_time = fields.Datetime("Hora de apertura")
    course_ids = fields.One2many("course", "academy_id")
    tags = fields.Many2many("tags")


class tags(models.Model):
    _name = "tags"

    name = fields.Char("Tags")


class course(models.Model):
    _name = "course"

    academy_id = fields.Many2one("academy.academy")
    name = fields.Char("Nombre", index=1)
    start = fields.Datetime("Inicio")
    end = fields.Datetime("Finaliza")
    professor_id = fields.Many2one("professor")
    student_ids = fields.One2many("student", "course_id")


class Professor(models.Model):
    _name = "professor"

    name = fields.Char("Profesor")
    career_ids = fields.Many2many("career")


class Student(models.Model):
    _name = "student"

    course_id = fields.Many2one("course")
    name = fields.Char("Estudiante")


class Career(models.Model):
    _name = "career"

    name = fields.Char("Nombre")
