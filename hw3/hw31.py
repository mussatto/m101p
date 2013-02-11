#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import pymongo


students = pymongo.connection.Connection().school.students

for student in students.find():
    min_score_index, _ = min(
        ((index, score) for index, score in enumerate(student["scores"])
        if score["type"] == "homework"),
        key=operator.itemgetter(1),
    )
    print "student", student["name"], "pop", min_score_index
    student["scores"].pop(min_score_index)
    students.save(student)