"""
    Virtual Reality Systems - Real Solutions for Virtual Systems.
    Email : info@virtualrealitysystems.net
    Copyright (C) 2017  Virtual Reality Systems

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib.auth.models import User
from django.db.models import *


class Upload(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='upload')
    dump_location = CharField(max_length=100)
    status = CharField(max_length=20)
    platform = CharField(max_length=100)
    uploaded_on = DateTimeField()


class RegFlag(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='reg_flagbit')
    name = CharField(max_length=100, null=False)
    company = CharField(max_length=100, null=False)
    flag = IntegerField()
