[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# markdown-icons (`iconfonts.py`)

Easily display icon fonts in python markdown. Just add the CSS necessary for your font and add this extension. 

This is a 3rd party extension for [Python Markdown](https://pythonhosted.org/Markdown/). You can see a [full list of 3rd party extensions here](https://github.com/waylan/Python-Markdown/wiki/Third-Party-Extensions).

Although this works with any icon font, users can use a `mod` syntax to add more prefixed classes to support [Font Awesome](http://fortawesome.github.io/Font-Awesome/) and its special classes such as `2x, 3x, muted, spin, etc`

Furthermore, users can add their own `user_mod` syntax to add additional, non-prefixed, pre-defined classes for greater control over their icons while allowing you to control exactly what styles are allowed.

- You can create your own Icon Fonts using the IcoMoon app: http://icomoon.io/app/
- A great pre-made Icon Font is [Font Awesome (GitHub Project)](http://fortawesome.github.io/Font-Awesome/)

See the [python markdown documentation](http://pythonhosted.org/Markdown/) for more information.

Use it in any personal or commercial project you want.

# Syntax:

- Accepts a-z, A-Z, 0-9, _(underscore), and - (hypen)
- Uses [HTML Entity](http://www.w3schools.com/html/html_entities.asp) like syntax: `&entity_name;`

```
&icon-html5;
&icon-css3;
&icon-my-icon;
```

Mod syntax:
```
&icon-html5:2x;
&icon-quote:3x,muted;
&icon-spinner:large,spin;
```

User mod syntax:
```
&icon-html5::red;
&icon-quote:2x:bold;
```

#### Example Markdown:

```
I love &icon-html5; and &icon-css3;
&icon-spinner:large,spin; Sorry we have to load...
```

##### Output:

```
I love <i aria-hidden="true" class="icon-html5"></i> and <i aria-hidden="true" class="icon-css3"></i>
<i aria-hidden="true" class="icon-spinner icon-large icon-spin"></i> Sorry we have to load...
```

# Installation:

```bash
pip install markdown-iconfonts
```

# Usage / Setup:

## Default Prefix is "icon-":

```python
import markdown

md = markdown.Markdown(extensions=['iconfonts'])
```

or 

```Python
import markdown
from iconfonts import IconFontsExtension

md = markdown.Markdown(extensions=[IconFontsExtension()])
```

#### The `base` option allows for use of Bootstrap 3 and FontAwesome 4 icons

```python
md = markdown.Markdown(extensions=['iconfonts'],
                       extension_configs={"base":"icon"})
converted_text = md.convert(text)
```

**Input:** `&icon-html5;`

**Output:** `<i aria-hidden="true" class="icon icon-html5"></i>`

#### `prefix_base_pairs` option

The `prefix_base_pairs` option allows for multiple prefix-base pairs to be specified, to allow you to support both Bootstrap 3/Glyphicon and FontAwesome icons

``` 
md = markdown.Markdown(extensions=['iconfonts'],
                       extension_configs={
                           'iconfonts': {
                               'prefix_base_pairs': {
                                   'fa-': 'fa',
                                   'glyphicon-': 'glyphicon',
                               }
                           }
                       })
converted_text = md.convert(text)
```

**Input:** `&glyphicon-remove; &fa-html5;`

**Output:** `<i aria-hidden="true" class="glyphicon glyphicon-remove"></i><i aria-hidden="true" class="fa fa-html5"></i>`

# How to run the unit tests

 - Install `Markdown`: `pip install markdown`
 - Install markdown icons. Copy the `iconfonts.py` file into `site-packages/markdown/extensions/`
 - Navigate to the test directory in CMD/terminal and run `python unit-tests.py -v`
