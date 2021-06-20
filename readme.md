# CNS
<!-- ![](https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg "credit to Nick Shillingford")   -->
<!-- <center><img src="https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg" ...></center> -->

CNS (Central Nervous System) is REPL for pythonic file system management and navigation.  
It essentially bundles relevant aspects of [filey](https://github.com/kendfss/filey) and [sl4ng](https://github.com/kendfss/sl4ng) into a shell-like environment.  
You can customize it to fit your system/workflow by editing the [env](./cns/env.py) file.  

**why?** because you're worth it. It's usually faster than searching with windows on my miserably old setup. having everything handy makes it faster to control search specificity  
[**how?**](#usage)  

### Usage  

##### Start
```shell
$ cns
```

##### Navigation
```python
>>> pwd
Place(name=System32, dir=Windows)
>>> cd(os.path.expanduser('~'))
>>> pwd
Place(name=Me, dir=User)
```

##### Linear Search
```python
>>> show(downloads("name of that documentation file i seem to have misplaced/lost the will to look for manually", exts='pdf md htm'))
search result #1.pdf
search result #2.pdf
...
search result #n
```



