#!/usr/bin/env python
""" Deck Manager for any type of Card objects
Creates abstracted functionality to modify a deck of cards in standard ways.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Mason Dupont"
__credits__ = ["Mason Dupont"]
__version__ = "0.1"
__maintainer__ = "Mason Dupont"
__license__ = "GPLv3"
__status__ = "Development"


class card:
    def __init__(self, **kwargs):
        self.create_details(**kwargs)
    
    def create_details(self, **kwargs):
        for k in kwargs:
            if not k.startswith("_"):
                setattr(self, k, kwargs[k])

    def __str__(self) -> str:
        s = " : ".join([str(v) for v in self.__dict__.values()])
        return s

if __name__ == "__main__":
    # Example 1
    ## Standard Playing Cards
    from itertools import product


    suits = ("hearts", "diamonds", "spades", "clubs")
    values = ['A'] + list(range(2,11)) + ["J", "Q", "K"]
    deck = [card(value=v[0], suit=v[1]) for v in product(values, suits)]
    for c in deck:
        print(c)