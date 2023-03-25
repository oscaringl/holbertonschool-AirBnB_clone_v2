<h1>AirBnB clone - MySQL</h1>

<h2>Background Context</h2>
<p>Environment variables will be your best friend for this project!</p>
<ul>
<li><code>HBNB_ENV</code>: running environment. It can be &ldquo;dev&rdquo; or &ldquo;test&rdquo; for the moment (&ldquo;production&rdquo; soon!)</li>
<li><code>HBNB_MYSQL_USER</code>: the username of your MySQL</li>
<li><code>HBNB_MYSQL_PWD</code>: the password of your MySQL</li>
<li><code>HBNB_MYSQL_HOST</code>: the hostname of your MySQL</li>
<li><code>HBNB_MYSQL_DB</code>: the database name of your MySQL</li>
<li><code>HBNB_TYPE_STORAGE</code>: the type of storage used. It can be &ldquo;file&rdquo; (using <code>FileStorage</code>) or <code>db</code>(using <code>DBStorage</code>)</li>
</ul>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="cmd module" href="https://intranet.hbtn.io/rltoken/n2iuMmutfCZmeMqbeBnlaw" target="_blank" rel="noopener">cmd module</a></li>
<li><strong>packages</strong> concept page</li>
<li><a title="unittest module" href="https://intranet.hbtn.io/rltoken/nUpQTzwnNi_c8AIKoBdrmw" target="_blank" rel="noopener">unittest module</a></li>
<li><a title="args/kwargs" href="https://intranet.hbtn.io/rltoken/m8vYyTQi5-raOlUJJ9NItg" target="_blank" rel="noopener">args/kwargs</a></li>
<li><a title="SQLAlchemy tutorial" href="https://intranet.hbtn.io/rltoken/2DZHkwnlEmv4Iy7hufh3Xg" target="_blank" rel="noopener">SQLAlchemy tutorial</a></li>
<li><a title="How To Create a New User and Grant Permissions in MySQL" href="https://intranet.hbtn.io/rltoken/OpbgfN52Xc5Vrwug9jAb5A" target="_blank" rel="noopener">How To Create a New User and Grant Permissions in MySQL</a></li>
<li><a title="Python3 and environment variables" href="https://intranet.hbtn.io/rltoken/VHWw0H0LGwlpUBCI1qkPSQ" target="_blank" rel="noopener">Python3 and environment variables</a></li>
<li><a title="SQLAlchemy" href="https://intranet.hbtn.io/rltoken/3rDo_Lb9DFRufb4Zh3JbdQ" target="_blank" rel="noopener">SQLAlchemy</a></li>
<li><a title="MySQL 8.0 SQL Statement Syntax" href="https://intranet.hbtn.io/rltoken/9dZyqKjKVADhWytWrK8F6A" target="_blank" rel="noopener">MySQL 8.0 SQL Statement Syntax</a></li>
<li><a title="AirBnB clone - ORM" href="https://intranet.hbtn.io/rltoken/ZsjgMgJW7i6QXz6LlRP78Q" target="_blank" rel="noopener">AirBnB clone - ORM</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/LAyje3OPhToMqWM-vuzUzA" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
<li>How to create a MySQL database</li>
<li>How to create a MySQL user and grant it privileges</li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
<li>How to handle 2 different storage engines with the same codebase</li>
<li>How to use environment variables</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h3>Python Unit Tests</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a title="unittest module" href="https://intranet.hbtn.io/rltoken/nUpQTzwnNi_c8AIKoBdrmw" target="_blank" rel="noopener">unittest module</a></li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project: ex: for <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge cases</li>
</ul>
<h3>SQL Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.4.x</code></li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>
<h3>GitHub</h3>
<p><strong>There should be one project repository per group. If you clone/fork/whatever a partner&rsquo;s project repository with the same name before the second deadline, you risk a 0% score.</strong></p>
<h2>More Info</h2>
<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/concepts/74/hbnb_step2.png" alt="" /></p>