<h1 align="center">Read zip-files script</h1>

<span style="align-items: center; display: flex;">
<img src="resources/python_icon.png" style="width: 2%">&nbsp
<b>Python version:</b>&nbsp; 3.8
</span>

To read any file contained within a zip file, please provide the following arguments:
1. Path of the file expected to be read
   1. The path can consist entirely of both backward slashes ``\`` or forward slashes ``/``
2. Directory path for extracted files (can be omitted if the path contains no whitespaces and is of type ``.zip``)
   1. Paths containing ".7z" or ".zip" with whitespaces need to be extracted. 
   2. Paths containing ".zip" but no whitespaces do not get extracted.

## Example
```
python read_zip_file.py resources/test.zip/test.txt output
```
or
```
python read_zip_file.py resources\test.zip\test.txt output
```
Python executes read_zip_file.py and reads test.txt contained in ``resources/test.zip``. The output path is the
directory ``output``.

The script print the output in the console.

## Output
The script prints the output as an array, where every newline ``\n`` introduces a new entry within the array.

### Example
```text
Hello
how are you doing
this is a temporary file

Please remember to delete it
With kind regards
Alfa Bravonson
```

Returns:
```python
['Hello', 'how are you doing', 'this is a temporary file', '', 'Please remember to delete it', 'With kind regards', 'Alfa Bravonson']
```