# ddmin-algorithm

## Usage from terminal:
```
python ddmin.py -s <sequence> -f <fail_input>
```
## Example:
```
python ddmin.py -s abcvvcba -f v
```
output: 
``` 
n =  2
['v', 'c', 'b', 'a'] ==> PASS
['a', 'b', 'c', 'v'] ==> PASS
n =  4
['c', 'v', 'v', 'c', 'b', 'a'] ==> FAIL
['a', 'b', 'v', 'c', 'b', 'a'] ==> PASS
['a', 'b', 'c', 'v', 'b', 'a'] ==> PASS
['a', 'b', 'c', 'v', 'v', 'c'] ==> FAIL
n =  3
['v', 'c', 'b', 'a'] ==> PASS
['c', 'v', 'b', 'a'] ==> PASS
['c', 'v', 'v', 'c'] ==> FAIL
n =  2
['v', 'c'] ==> PASS
['c', 'v'] ==> PASS
n =  4
['v', 'v', 'c'] ==> FAIL
['c', 'v', 'c'] ==> PASS
['c', 'v', 'c'] ==> PASS
['c', 'v', 'v'] ==> FAIL
n =  3
['v', 'c'] ==> PASS
['v', 'c'] ==> PASS
['v', 'v'] ==> FAIL
n =  2
['v'] ==> PASS
['v'] ==> PASS
n =  2
['v'] ==> PASS
['v'] ==> PASS
Can't split anymore n = 2
[['v'], ['v']]

```
