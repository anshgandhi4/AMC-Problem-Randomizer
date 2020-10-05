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

import random
import re
import urllib.request
import webbrowser
import os

filepath = os.path.abspath(os.getcwd()) + '/randomProblem.html'

def random_seed():
    """random_seed -> int
    returns randomized seed"""

    seed = random.randint(0, 1000)
    return seed

def randomize_amc8_url(hard):
    """randomize_amc8_url(hard) -> str
    combines randomized year, problem depending on difficulty
    returns final string"""

    problem = str(random.randint(21, 25)) if hard else str(random.randint(1, 25))
    year = str(random.randint(1999, 2019))
    return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AMC_8_Problems/Problem_' + problem

def randomize_amc10_url(hard):
    """randomize_amc10_url(hard) -> str
    combines randomized year, problem, and version depending on difficulty
    returns final string"""

    problem = str(random.randint(21, 25)) if hard else str(random.randint(1, 25))
    year = str(random.randint(2000, 2020))
    version = random.choice(['A', 'B'])
    if int(year) > 2001:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AMC_10' + version + '_Problems/Problem_' + problem
    else:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AMC_10_Problems/Problem_' + problem

def randomize_amc12_url(hard):
    """randomize_amc12_url(hard) -> str
    combines randomized year, problem, and version depending on difficulty
    returns final string"""

    problem = str(random.randint(21, 25)) if hard else str(random.randint(1, 25))
    year = str(random.randint(2000, 2020))
    version = random.choice(['A', 'B'])
    if int(year) > 2001:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AMC_12' + version + '_Problems/Problem_' + problem
    else:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AMC_12_Problems/Problem_' + problem

def randomize_aime_url(hard):
    """randomize_aime_url(hard) -> str
    combines randomized year, problem, and version depending on difficulty
    returns final string"""

    problem = str(random.randint(11, 15)) if hard else str(random.randint(1, 15))
    year = str(random.randint(1983, 2020))
    version = random.choice(['I', 'II'])
    if int(year) > 1999:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AIME_' + version + '_Problems/Problem_' + problem
    else:
        return 'https://www.artofproblemsolving.com/wiki/index.php/' + year + '_AIME_Problems/Problem_' + problem

def filter_html(url):
    """filter_html(url) -> str
    gets and decodes html code
    finds, isolates, and processes html code of problem
    returns final string"""

    find_problem = re.compile('Problem.{0,3}?</span>.*?</h2>\s*(<p>.*?</p>)\s*<h2>\s*<span', re.DOTALL)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    try:
        data = find_problem.findall(data)[0]
        data = re.sub('//latex.artofproblemsolving', 'http://latex.artofproblemsolving', data)
        data = re.sub('<a href.*?>', '', data)
        data = re.sub('</a>', '', data)
    except:
        #print(url)
        data = url
    return data

def open_in_browser():
    """open_in_browser()
    opens the html code in default browser"""
    
    webbrowser.open(filepath)
