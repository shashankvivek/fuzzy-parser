To run the script, run below command
```python
> python main.py ../data/input.txt
```

The File should contain:
* [Line 1] => Input Paragraph to search for answers 
* [Line 2 - 6] => Individual question on each line
* [Line 7] => Jumbled answers separated by delimiter

```
positional arguments:
  filePath              Path of Input File

optional arguments:
  -h, --help            show this help message and exit
  --delimiter DELIMITER
                        Delimiter for jumbled answer
```

To run tests, run below commands:

```python
>python -m unittest test_engine\test_tokenizer.py
```