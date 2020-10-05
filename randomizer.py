#  Copyright © 2020 Ansh Gandhi
#
#  This file is part of AMC Problem Randomizer.
#
#  AMC Problem Randomizer is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  AMC Problem Randomizer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with AMC Problem Randomizer.  If not, see <https://www.gnu.org/licenses/>.
#
#  Original Author: Ansh Gandhi
#  Original Source Code: <https://github.com/anshgandhi4/AMC-Problem-Randomizer/>
#
#  EVERYTHING ABOVE THIS LINE MUST BE KEPT AS IS UNDER GNU GPL LICENSE RULES.

from functions import *

seed = random_seed()
random.seed(seed)

test = #'AMC 8', 'AMC 10', 'AMC 12', 'AIME'

problemFile = open(filepath, 'w')
problemFile.write('<!DOCTYPE html><head><title>' + test + ' Random Problems ' + str(seed) + '</title><style>p {font-family: sans-serif;font-size: 15px;}a {font-family: sans-serif;font-size: 21px;color: #1b365d;text-decoration: none;}</style></head><body>')

for problemNumber in range(1, 6):
    if test == 'AMC 8':
        url = randomize_amc8_url(problemNumber > 1)
    elif test == 'AMC 10':
        url = randomize_amc10_url(problemNumber > 2)
    elif test == 'AMC 12':
        url = randomize_amc12_url(problemNumber > 3)
    elif test == 'AIME':
        url = randomize_aime_url(problemNumber > 4)
    htmlCode = '<h2><a href="' + url + '">Problem ' + str(problemNumber) + '</a></h2>' + filter_html(url)
    try:
        problemFile.write(htmlCode)
    except UnicodeEncodeError as e:
        problemFile.write('<h2><a href="' + url + '">' + url + '</a></h2>')

problemFile.write('</body>')
problemFile.close()

open_in_browser()
