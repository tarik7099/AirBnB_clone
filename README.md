# AirBnB Clone Project

Welcome to the AirBnB clone project! This project aims to create a command interpreter to manage AirBnB objects, serving as the foundation for building a full web application. Each task in this project is crucial for developing subsequent functionalities like HTML/CSS templating, database storage, API, and front-end integration.

## Table of Contents
- [Overview](#overview)
- [Command Interpreter](#command-interpreter)
- [File Organization](#file-organization)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [Licens

## Overview
In this project, we implement a command interpreter that allows the management of AirBnB objects. The core functionalities include creating new objects, retrieving objects, performing operations on objects, updating object attributes, and destroying objects. The project is structured to promote code modularity, serialization/deserialization, and unit testing.

## Command Interpreter
The command interpreter is designed to provide a user-friendly interface for managing AirBnB objects. Users can interact with the interpreter to perform various operations on objects, facilitating the development and testing of different functionalities.

## File Organization
The project follows a well-organized file structure to enhance readability and maintainability. Key components include:
- `models`: Contains classes representing different AirBnB objects (e.g., BaseModel, User, State, City, Place).
- `tests`: Houses unit tests for validating the functionality of classes and modules.
- `cmd`: Includes the command interpreter module for user interaction.
- `storage`: Manages file storage, serialization, and deserialization of objects.

## Learning Objectives
The project aims to impart essential skills and knowledge, including:
- Creating a Python package
- Developing a command interpreter using the cmd module
- Implementing unit testing in a large project
- Serializing and deserializing classes
- Writing and reading JSON files
- Managing datetime and UUID in Python
- Utilizing *args and **kwargs for flexible function parameters

## Requirements
- Python 3.8.5
- Pycodestyle 2.8.*
- Ubuntu 20.04 LTS

## Usage
1. Clone the repository: `git clone https://github.com/your-username/AirBnB-Clone.git`
2. Navigate to the project directory: `cd AirBnB-Clone`
3. Run the command interpreter: `./console.py`

## Testing
Execute unit tests using the following command:
```bash
python3 -m unittest discover tests

