# MapReduce Grep solution 1

```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh grep
```
output:

```
foo	6
quux	4
```
# Map Reduce Grep Solution 2

Use regular expression to implement grep function by Map Reduce
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner2.sh grep2 ^f.o
```  
 output
```
foo 6

```
# Map Reduce Web Access Log 
#	How many distinct IP addresses accessed this website and how many times?
Use regular expression to implement grep function by Map Reduce
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_webaccesslog_runner1.sh webaccesslog
```  
 output
```
