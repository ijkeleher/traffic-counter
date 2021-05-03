# Traffic Counter
---
## Running the program

### Install requirements
    $ pip3 install requirements.txt

### Run the program
    $ python3 counter.py  # to use default 'traffic.log'
    $ python3 counter.py $FILE_NAME  # to use a different logfile

You should see something similar to the output below:

```
============= Total ============
398
============= Daily ============
2016-12-01 179
2016-12-05 81
2016-12-08 134
2016-12-09 4
============= Most =============
2016-12-01T07:30:00 46
2016-12-01T08:00:00 42
2016-12-08T18:00:00 33
============= Least ============
2016-12-05 11:00:00 7
```
    
### Run unit tests
    $ pytest

Hopefully you will see something similar to this:

```
================= 5 passed in 0.75s =================
```

## Files in this repo
```
.
├── README.md
├── counter.py  # the actual program
├── requirements.txt  # packages
├── test_counter.py  # pytest unit tests
└── traffic.log  # example logfile 
```
