# AirBnB_clone

![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190704%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190704T144425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cba77781d9c11fea7bece26ffdcde190e657fa7ab6e2fcf2b408ca2fe6191251)

### Description
Welcome to the AirBnB clone project! (The Holberton B&amp;B), This is ours first version the AirBnB, n
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
| create | Create new instance | create <class name> |
| show | Show of representación of a object | show <class name> <id> |
| destroy | Remove  an instance | destroy <class name> <id> |
| all | prints all string representations, can be specified by class | all |
