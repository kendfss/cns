# CNS
<!-- ![](https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg "credit to Nick Shillingford")   -->
<!-- <center><img src="https://live.staticflickr.com/6049/6323682453_f58f16b56b_w_d.jpg" ...></center> -->

CNS (Central Nervous System) is a productivity oriented python environment which offers a REPL for file system management and navigation.  
<!-- It essentially bundles relevant aspects of [filey](https://github.com/kendfss/filey) and [sl4ng](https://github.com/kendfss/sl4ng) into a shell-like environment with some additional offerings built on the standard library.   -->
It essentially bundles relevant aspects of [filey](../filey) and [sl4ng](../sl4ng) into a shell-like environment with some additional offerings built on the standard library.  
You can customize it to fit your system/workflow by editing the [env](./cns/env.py) file.  

**why?** because you're worth it. But also, I don't have internet access from my main station so I tend to use a lot of offline documentation/screencaps as reference material. But also, as cool as Pathlib is, the lack of search-ability (excluding grep - which isn't ideal for newbs, or particularly thorough) makes it a sub-optimal tool for the use cases laid out below.  
[**how?**](#usage)  

### Usage  

##### Start
This starts the REPL which *-imports all of the contents from the [env](./cns/env.py) file.  
```shell
$ cns
```

##### Navigation
```python
>>> pwd
Place(name=System32, dir=Windows)
>>> cd(os.path.expanduser('~'))
>>> pwd
Place(name=Me, dir=Users)
>>> downloads = Place('~') / "downloads" # accesible as "downs" in the REPL
```

##### Linear Search
By default, searches only look for files, but you can see the techniques for directory finding [here](#directory)
```python
>>> show(downloads("term1 term2 term3 ... termN", exts='pdf md htm'))
search_result_1.md
search_result_2.htm
...
search_result_n.pdf
```

##### Threaded Search
```python
>>> show(downloads("term1 term2 term3 ... termN", threads=3)) # defaults to zero
search_result_1.ext
search_result_2.ext
...
search_result_n.ext
```

##### Depth-restricted Search
This constrains the search to a given depth of directory. Any argument lower than zero goes as deeply as possible.  
The following indicates how only look in space corresponding to `os.listdir(downloads.path)`
```python
>>> show(downloads("term1 term2 term3 ... termN", depth=0)) # defaults to zero
```


### Examples
##### Scanning Source Files for useful info
```python
>>> show(filter(filey.Scanner("File) Read(", case=True), filey.files(r"C:\Program Files\Go\src")))
C:\Program Files\Go\src\cmd\pack\pack_test.go 
C:\Program Files\Go\src\net\http\fs.go
C:\Program Files\Go\src\os\file.go
C:\Program Files\Go\src\runtime\race\testdata\mop_test.go
C:\Program Files\Go\src\testing\fstest\mapfs.go
``` 
- First one did the trick :wink:



### Change Log
**v 1.0.1**
- Adds  
    - threaded searching  
    - depth-controlled searching  
    - globbing to Places  
    - filey.files to repl
