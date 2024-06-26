 # jojoapi

jojoapi is a simple python package for interacting with [Jojo's Bizarre Api.](https://jojos-bizarre-api.netlify.app/)

You can use it to get information (in JSON format) on Jojo's Bizarre Adventure characters and stands.

# Documentation and Functions (Characters)
**WARNING: There may be light spoilers for *Jojo's Bizarre Adventure* up ahead. Do not use an API like this if you haven't finished the series.**

Each set of functions have versions for characters and stands. We'll go over Characters first. You can first use `jojoapi.getCharacterbyID()` to get a certain character's info by their given ID on the [Jojo's Bizarre Api](https://jojos-bizarre-api.netlify.app/) site.
```
import jojoapi
x = jojoapi.getCharacterbyID(id=69)
print(x)
```
This will return:
```
{
  "id": "69",
  "name": "Ken Oyanagi",
  "japaneseName": "大柳 賢",
  "image": "ken.png",
  "abilities": "Boy II Man",
  "nationality": "Japanese",
  "catchphrase": "Hey, mister. Wanna play rock-paper-scissors?",
  "family": "none",
  "chapter": "Diamond is Unbreakable",
  "living": true,
  "isHuman": true
}
```
The only argument that `jojoapi.getCharacterbyID()` will take is `id` which must be an `int`.

There is also `jojoapi.getAllCharacters()` which returns a massive list of JSON data for *all* characters registered on the API. 

There is also `jojoapi.getRandomCharacter()` which will return a random character's data.

Finally, there is `jojoapi.getCharacterbyQuery()` which will return JSON responses for only characters that meet a criteria. You must specify the `str` argument `category` which has 8 valid values which are: `name`, `chapter`, `nationality`, `family`, `abilities`, `isHuman`, `living`, and `catchphrase`. You also must specify the `str` argument `query` which will be what the `category` argument should be equal to. For example:
```
import jojoapi
x = jojoapi.getCharacterbyQuery(category="nationality", query="Japanese")
print(x)
```
This will return all JSON data for characters with a `nationality` of `Japanese`.

# Documentation and Functions (Stands)
Each set of functions have versions for characters and stands. We'll go over Stands next. You can first use `jojoapi.getStandbyID()` to get a certain stand's info by their given ID on the [Jojo's Bizarre Api](https://jojos-bizarre-api.netlify.app/) site.
```
import jojoapi
x = jojoapi.getStandbyID(id=1)
print(x)
```
This will return:
```
{
  "id": "1",
  "name": "The World",
  "alternateName": "none",
  "japaneseName": "ザ・ワールド(世界)",
  "image": "theworld.png",
  "standUser": "2",
  "chapter": "Stardust Crusaders, Steel Ball Run",
  "abilities": "Time Stop, Super Speed, Super Strength",
  "battlecry": "MUDAMUDAMUDA"
}
```
The only argument that `jojoapi.getStandbyID()` will take is `id` which must be an `int`.

There is also `jojoapi.getAllStands()` which returns a massive list of JSON data for *all* stands registered on the API. 

There is also `jojoapi.getRandomStand()` which will return a random stand's data.

Finally, there is `jojoapi.getStandbyQuery()` which will return JSON responses for only characters that meet a criteria. You must specify the `str` argument `category` which has 8 valid values which are: `name`, `alternateName`, `standUser`, `chapter`, `abilities`, and `battlecry`. You also must specify the `str` argument `query` which will be what the `category` argument should be equal to. For example:
```
import jojoapi
x = jojoapi.getStandbyQuery(category="name", query="Gold Experience")
print(x)
```
This will return all JSON data for characters with a `name` of `Gold Experience`:
```
[
  {
    "id": "57",
    "name": "Gold Experience",
    "alternateName": "Golden Wind",
    "japaneseName": "ゴールド・エクスペリエンス (黄金体験)",
    "image": "goldexperience.png",
    "standUser": "75",
    "chapter": "Vento Aureo",
    "abilities": "Create Life, Life Shot, Flesh/Organ Creation, Life Sensor",
    "battlecry": "MUDA MUDA MUDA"
  },
  {
    "id": "58",
    "name": "Gold Experience Requiem",
    "alternateName": "Golden Wind Requiem",
    "japaneseName": "ゴールド・エクスペリエンス・レクイエム",
    "image": "goldrequiem.png",
    "standUser": "75",
    "chapter": "Vento Aureo",
    "abilities": "Return to Zero, Life Giver, Super Strength, Super Speed, Autonomy",
    "battlecry": "MUDA MUDA MUDA"
  }
]
```



