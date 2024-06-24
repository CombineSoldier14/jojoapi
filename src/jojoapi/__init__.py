#  MIT License
#  Copyright (c) 2024 CombineSoldier14 & Contributors

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import requests
import json
import random

def get(link: str):
    r = requests.get(link)
    return json.loads(r.text)

def getCharacterbyID(id: int):
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(str(id)))
    
def getAllCharacters():
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/")

def getCharacterbyQuery(category: str, query: str):
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/query/query?{0}={1}".format(category, query))

def getRandomCharacter():
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(random.randint(1, 155)))

def getStandbyID(id: int):
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/{}".format(str(id)))

def getAllStands():
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/")

def getStandbyQuery(category: str, query: str):
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/query/query?{0}={1}".format(category, query))

def getRandomStand():
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/{}".format(random.randint(1, 155)))
