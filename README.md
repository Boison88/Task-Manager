## Study project #4 — «Task Manager»  

[![Actions Status](https://github.com/Boison88/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Boison88/python-project-52/actions)
[![CI](https://github.com/Boison88/python-project-83/actions/workflows/CI.yml/badge.svg)](https://github.com/Boison88/python-project-83/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/88d76722c4af7dcbd032/maintainability)](https://codeclimate.com/github/Boison88/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/88d76722c4af7dcbd032/test_coverage)](https://codeclimate.com/github/Boison88/python-project-52/test_coverage)

This repository was created as part of a [Hexlet study project](https://ru.hexlet.io/programs/python/projects/52).

*Task Manager* this is a task management system based on the Django framework.  
It allows you to set tasks, assign performers and change their statuses.

### Try the project in work [HERE](https://task-manager-x2gg.onrender.com)

***
### How to install
#### 1. Clone this repository
```
    git clone https://github.com/Boison88/Task-Manager
```

#### 2. Change Directory
```
    cd Task-Manager
```

#### 3. Create .env file with secret key
```
    make env
```

#### 4. Install poetry and required packages from pyproject.toml
```
    make install
```

#### 5. Migrate all models inside SQLite database
```
    make migration
```

#### 6. Run application
```
    # for dev and local use
    make dev
    
    # for deploy
    make start
```
