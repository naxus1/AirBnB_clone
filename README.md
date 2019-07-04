# AirBnB_clone

<a href=""><img src="https://camo.githubusercontent.com/70996d3dcffa41c27a6f5d59f56a42d978a4684c/687474703a2f2f696d6775722e636f6d2f4a42434d4844502e706e67" title="FVCproductions" alt="FVCproductions"></a>

### Description

Welcome to the AirBnB clone project! (The Holberton B&amp;B), This is ours first version the AirBnB.

> this project we create the console it drive the creation, update and deleted and management of objects. This is ours first version the AirBnB, in this project we create the console it drive the creation, update and deleted and management of objects. 

### Synopsis

The interpreter has specific use-cases for managing objects:
 - Create a new object
 - Retrieve an object from a file
 - Do operations on objects
 - Update attributes of an object
 - Destroy an object

### Environment

Our AirBnB Clone has been tested on Ubuntu 14.04 LTS using python3 (version 3.4.3) and adheres to PEP8

### Contents

| File | Description |
| --- | --- |
| console.py | Command interpreter |
| models/base_model.py | This Class define all methods of objects |
| models/city.py | Class City |
| models/place.py | Class Place |
| models/review.py | Class Review
| models/state.py | Class State |
| models/user.py | Class User |
| models/engine/file_storage.py | Class serializes instances to a JSON |
| models/init.py | creates an instance of FileStorage |

### Usage

For use of console, execute command

```python
./console.py
```

### Command console

| Command | Description | example |
| --- | --- | --- |
| help | Display Commands, if have documentación | help |
| quit | Quit of console | quit |
| EOF | Quit of console | EOF |
| create | Create new instance | create class name |
| show | Show of representación of a object | show class name id |
| destroy | Remove  an instance | destroy class name id |
| all | prints all string representations, can be specified by class | all |

### Authors
Fesus Rockus - <a href ="https://github.com/fesusrocuts">GitHub</a>
</br>
Oscar vargas Molina - <a href ="https://github.com/naxus1">GitHub</a>