title: Yet Another Markup Language
language: en


I recently needed to choose a file format for a complex software configuration.
I decided to use YAML. In this post, I explaned why I choose it,
and what I learned about it.




## Choosing the right format for configuration file

There are plenty of file formats that exist and can be used to store a software configuration.
If its not enough, it is easy to create a custom format. But who wants another standard?


[![xkcd 927](https://imgs.xkcd.com/comics/standards.png "Fortunately, the charging one has been solved now that we've all standardized on mini-USB. Or is it micro-USB? Shit.")](https://xkcd.com/927/)

(Source: <https://xkcd.com/927/>)


The [ini file](https://en.wikipedia.org/wiki/INI_file) is very common, and used very frequently.
In Python, it is easy to manipulate using [configparser](https://docs.python.org/3/library/configparser.html).
In Qt, it can be used with the [QSettings](https://doc.qt.io/qt-5/qsettings.html) class.
It is so common that each software has its own interpretation of what the ini file specification should be.
It can be a good choice if you need a simple key/value storage, but if your configuration becomes
more complex, you end up creating conventions over the ini file, and you finish by creating a new
file format based on ini.

[TOML](https://toml.io/en/) can be see as a superset of the ini file. But the syntax is well defined,
and it allow more complex representations. In fact, it almost looks like Python code.
This format was [chosen to store build system dependencies in Python](https://www.python.org/dev/peps/pep-0518/#file-format).

JSON is a very popular format these days, mainly because it is the standard (a native) format for JavaScript.
Therefore, it can be parsed very quickly in the context of a JavaScript application.
However, it is less human-friendly, because you cannot really add comments to it,
and because you need a tool to format it if you want to be able to understand its structure.

[YAML](https://yaml.org/) it a superset of JSON. It means that a YAML parser can read JSON
(but not the opposite: a JSON parser cannot read YAML). While more complex (and powerful)
than the other format, I do not agree that it is complicated and error prone for humans.
You only need to be able to indent text, and know the difference between a list and a map.
With those two concepts, you should be able to work with yaml.
We see YAML as the config language of many CI, such as GitHub Action, GitLab CI, Travis...

Finally, I put XML here for historical reasons. But you don't want to work with XML, do you?


When working with Python, another option is to use native Python script as a configuration file.
This is what [Sphinx](https://www.sphinx-doc.org/en/master/) uses,
and also what [Pelican](https://blog.getpelican.com/) uses. But in the context of a C++ application,
or with any other compiled language, this is not really a option...


|                                                   | ini   | toml | json  | yaml   | xml   |
|                                                   | :---: | :---:| :---: | :---:  | :---: | 
| Well defined                                      |       | ✓     | ✓    | ✓     | ✓    |
| Allow comments                                    | ✓    | ✓     |      | ✓      | ✓    |
| <del>Easy</del> <ins>Fun</ins> to edit by a human | ✓    | ✓     |      | ✓      |       |
| Allow nested structures                           |       | ✓     | ✓    | ✓     | ✓    |






## Libraries to parse YAML

With Python, [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation) does a pretty decent job.
However, it doesn't fully support YAML 1.2 yet.

In C++, there is [yaml-cpp](https://github.com/jbeder/yaml-cpp).
It support YAML 1.2. However, it has a few problems:

- It causes warnings in C++17 because it derives from std::iterator [ [issue #946](https://github.com/jbeder/yaml-cpp/issues/946) ]
- It cannot interfer scalar types correctly, because it doesn't distinguish between quoted and unquoted scalars [ [issue #261](https://github.com/jbeder/ yaml-cpp/issues/261) ]

There is also [Rapid YAML](https://github.com/biojppm/rapidyaml) that seems promising. <del>However, it is not really usable
in a projet yet since it is not versionned and has no official releases.</del> 
<ins datetime="2020-11-02">It now has a first official release, but API is not stable yet.</ins>
