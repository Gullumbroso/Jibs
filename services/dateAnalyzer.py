__license__ = """
Copyright (c) 2004-2006 Mike Taylor
Copyright (c) 2006 Darshana Chhajed
All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import parsedatetime as pdt


def time_analyzer(line):
    c = pdt.Constants()
    c.BirthdayEpoch = 60
    p = pdt.Calendar(c)
    result = p.parse(line)

    return result
    year, month, day, hour, mins, secs = result[0][:6]
    UTS = result[1]

print(time_analyzer("i want to eat next week at 12 pm and today"))