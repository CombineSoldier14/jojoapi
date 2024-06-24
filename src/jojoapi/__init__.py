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
    """Run a HTTP GET request to the given URL, parse for JSON, and return a `dict` of said response."""
    r = requests.get(link)
    return json.loads(r.text)

def getCharacterbyID(id: int):
    """Get a JoJo character by it's API ID."""
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(str(id)))
    
def getAllCharacters():
    """Get all JoJo characters."""
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/")

def getCharacterbyQuery(category: str, query: str):
    """Get a character by it's query
    :arg category: Character Category
    :arg query: Character Query"""
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/query/query?{0}={1}".format(category, query))

def getRandomCharacter():
    """Get a random JoJo Character"""
    return get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(random.randint(1, 155)))

def getStandbyID(id: int):
    """Get a JoJo stand by it's API ID.
    :arg id: The API ID of the stand"""
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/{}".format(str(id)))

def getAllStands():
    """Get all JoJo stands"""
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/")

def getStandbyQuery(category: str, query: str):
    """Get a stand by it's query
    :arg category: Stand Category
    :arg query: Stand Query"""
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/query/query?{0}={1}".format(category, query))

def getRandomStand():
    """Get a random JoJo stand."""
    return get("https://stand-by-me.herokuapp.com/api/v1/stands/{}".format(random.randint(1, 155)))
