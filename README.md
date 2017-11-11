# Queue-Simulator
Este projeto consiste em criar um simulador de um sistema com taxa de entrada e saída e inferir estatísticas sobre o tempo de atendimento e comprimento da fila.

# How to install

clone this project:
```sh
$ git clone https://github.com/matecomp/Queue-Simulator.git
```

create a virtualenv on new folder:
```sh
$ virtualenv -p python3 Queue-Simulator
```

init Queue-Simulator env:
```sh
$ cd Queue-Simulator
$ source bin/activate
```
If ok, will be printed:
```sh
(Queue-Simulator) server@localhost:~$
```

install all requeriments on env:
```sh
$ pip install -r requirements.txt
```

execute pytest files:
```sh
$ pytest -q test/
```

If ok, will be printed:
```sh
.....
5 passed in X.XX seconds
```
