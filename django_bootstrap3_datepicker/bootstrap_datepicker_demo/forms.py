# forms.py

# Copyright (C) 2016 Fabian Wenzelmann
#
# This file is part of foodle.
#
# foodle is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# foodle is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with foodle. If not, see <http://www.gnu.org/licenses/>.
#

from django import forms

class DemoForm(forms.Form):
    name = forms.CharField()
