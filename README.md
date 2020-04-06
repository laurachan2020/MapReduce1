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
```  
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
action.php      83
adminpanel.php  1
allsubmission.php       170
announcement.php        8
archive.php     309
compile.php     96
compiler.php    98
contest.php     249
contestproblem.php      556
contestshowcode.php     6
contestsubmission.php   228
contestsubmit.php       53
countdown.php   73
createadmin.php 4
description.php 124
details.php     297
edit.php        14
editcontest.php 3
editcontestproblem.php  12
home.php        2655
index.php       6
login.php       3426
logout.php      44
pcompile.php    80
process.php     317
profile.php     147
setcontest.php  6
setcontestproblem.php   4
setproblem.php  12
showcode.php    54
sign.php        136
standings.php   167
submit.php      54
update.php      7

```
How many accesses occurred before noon vs afternoon?
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_webaccesslog_runner3.sh webaccesslog
```  
 output
```
afternoon       13125
beforenoon      2664
```
Per IP, what is the number of accesses per webpage? (ie: how many times did IP 0.0.0.0 access login.php? Home.php? etc)
```
sudo docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_webaccesslog_runner5.sh webaccesslog
```
output
```
10.128.2.1~action.php   25
10.128.2.1~allsubmission.php    43
10.128.2.1~announcement.php     1
10.128.2.1~archive.php  64
10.128.2.1~compile.php  15
10.128.2.1~compiler.php 20
10.128.2.1~contest.php  55
10.128.2.1~contestproblem.php   116
10.128.2.1~contestsubmission.php        44
10.128.2.1~contestsubmit.php    10
10.128.2.1~countdown.php        10
10.128.2.1~createadmin.php      2
10.128.2.1~description.php      22
10.128.2.1~details.php  59
10.128.2.1~edit.php     4
10.128.2.1~editcontest.php      1
10.128.2.1~editcontestproblem.php       3
10.128.2.1~home.php     875
10.128.2.1~index.php    3
10.128.2.1~login.php    1027
10.128.2.1~logout.php   11
10.128.2.1~pcompile.php 17
10.128.2.1~process.php  65
10.128.2.1~profile.php  48
10.128.2.1~setcontest.php       2
10.128.2.1~setproblem.php       4
10.128.2.1~showcode.php 13
10.128.2.1~sign.php     35
10.128.2.1~standings.php        32
10.128.2.1~submit.php   7
10.128.2.1~update.php   3
10.129.2.1~action.php   6
10.129.2.1~allsubmission.php    24
10.129.2.1~announcement.php     6
10.129.2.1~archive.php  51
10.129.2.1~compile.php  16
10.129.2.1~compiler.php 7
......
```
