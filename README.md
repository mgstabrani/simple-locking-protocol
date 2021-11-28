# simple-locking-protocol
> A simple locking concurrency control protocol (exclusive locks only) using python.

## Requirements
- Python 3

## How to Run
- Run `main.py`
```
python main.py
```
- Input yout txt file containing table of transaction. The following is the input file example.
```
T1      T2      T3
R(A)
U(A)
        R(B)
        U(B)
                R(C)
                R(A)
                U(C)
        W(A)
R(A)
C
        C
                C
```
