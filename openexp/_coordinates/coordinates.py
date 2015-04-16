#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

class coordinates(object):

	"""
	desc:
		A base class for classes that need to perform coordinate conversions.
	"""

	def to_xy(self, x, y=None):

		"""
		desc:
			Converts coordinates from the OpenSesame reference frame to the
			back-end specific reference frame. `None` values are taken as the
			display center.

		arguments:
			x:
				desc:	An x coordinate, or an (x,y) tuple.
				type:	[float, int, NoneType, tuple]

		keywords:
			y:
				desc:	A y coordinate. Only applicable if x was not a tuple.
				type:	[float, int, NoneType]

		returns:
			desc:	An (x, y) coordinate tuple in the back-end specific
					reference frame.
			type:	tuple
		"""

		raise NotImplementedError()

	def from_xy(self, x, y=None):

		"""
		desc:
			Converts coordinates from the back-end specific reference frame to
			the OpenSesame reference frame. `None` values are taken as the
			display center.

		arguments:
			x:
				desc:	An x coordinate, or an (x,y) tuple.
				type:	[float, int, NoneType, tuple]

		keywords:
			y:
				desc:	A y coordinate. Only applicable if x was not a tuple.
				type:	[float, int, NoneType]

		returns:
			desc:	An (x, y) coordinate tuple in the OpenSesame reference
					frame.
			type:	tuple
		"""

		raise NotImplementedError()