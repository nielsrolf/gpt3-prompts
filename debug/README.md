# Debugging with GPT-3

The idea is to use  a pattern of the style
```
Code:
<some code>

Output:
<Error message that is displayed if the buggy code is executed>

Fixed:
<The same code as above without bugs>
```

Concatenating a few of such snippets with a new code snippet should make GPT-3 generate the debugged code for you.

# Does it work?
No, it has done the following:
- delete the content `sqrt.py` when asked to debug it
- immediately generate a stopping sequence when asked to debug `count_lines.py`
