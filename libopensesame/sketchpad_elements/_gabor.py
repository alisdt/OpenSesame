#-*- coding:utf-8 -*-

"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.sketchpad_elements._base_element import base_element

class gabor(base_element):

	"""
	desc:
		A gabor-patch element for the sketchpad.
	"""

	def __init__(self, sketchpad, string):

		"""
		desc:
			Constructor.

		arguments:
			sketchpad:		A sketchpad object.
			string:			A definition string.
		"""

		defaults = [
			(u'x',		0),
			(u'y',		0),
			(u'orient',	0),
			(u'freq',	.1),
			(u'env',	u'gaussian'),
			(u'size', 	96),
			(u'stdev',	12),
			(u'phase',	0),
			(u'color1',	u'white'),
			(u'color2', u'black'),
			(u'bgmode',	u'avg')
			]
		super(gabor, self).__init__(sketchpad, string, defaults=defaults)

	def draw(self):

		"""
		desc:
			Draws the element to the canvas of the sketchpad.
		"""

		self.canvas.gabor(x=self.properties[u'x'], y=self.properties[u'y'],
			orient=self.properties[u'orient'], freq=self.properties[u'freq'],
			env=self.properties[u'env'], size=self.properties[u'size'],
			stdev=self.properties[u'stdev'], phase=self.properties[u'phase'],
			col1=self.properties[u'color1'], col2=self.properties[u'color2'],
			bgmode=self.properties[u'bgmode'])