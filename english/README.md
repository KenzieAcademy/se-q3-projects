# The English Programming Language

This is a simple syntax layer on top of Python for running
code that resembles english sentences.

## Usage
```python english.py main.eng```

### Available English Commands

- `make x 1` &mdash; assign a value to a variable.
- `show x` &mdash; display a value.
- `is x 1` &mdash; compare two values.
- `subtract 1 from x` &mdash; subtract a value from a variable.
- `comment: text here` &mdash; insert a single-line comment.

### Commenting
- `comments:` &mdash; begin a multi-line comment.
- `end comments` &mdash; end a multi-line comment.
Example:
```
comments:
a bunch of
comment text
end comments
```