# README

## requirements

centos
-----------

```bash
$ sudo yum install python3-tkinter
$ pip3 install -r requirements.txt --user
```

debian/ubuntu
---------------

```bash
$ sudo apt-get install python3-tk
$ pip3 install -r requirements.txt --user
```

## structure

- `demo/test.csv` 

you can run `spike -g` to get it.

```
$ spike -g pk your-elf 2> run-hist.log
```

you can run `spike -l` to get it.

- `demo/serial-simtiny-workload.log`

```
$ spike -l --log=serial-simtiny-workload.log pk your-elf
```

## run

pc histgram
---------------

```
$ python3 plot-pc-histgram.py --path demo/test.csv

# show
$ gio open output/test-pc-histgram.png
# or 
$ display output/test-pc-histgram.png
```

insn histgram
---------------

```
$ ./plot-insn-histgram.py --path demo/serial-simtiny-workload.log
```

macro op fusion
------------------

./macro-op-fusion-find.py --path demo/serial-simtiny-workload.log

## reference

[Spike RISC-V ISA Simulator](https://github.com/riscv-software-src/riscv-isa-sim)

