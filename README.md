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
	How many distinct IP addresses accessed this website and how many times?
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_webaccesslog_runner1.sh webaccesslog
```  
 output

10.128.2.1      4257
10.129.2.1      1652
10.130.2.1      4056
10.131.0.1      4198
10.131.2.1      1626
```
	
	How many times was each  distinct webpage (ie, home.php, etc) accessed
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_webaccesslog_runner2.sh webaccesslog
```  
 output


```
