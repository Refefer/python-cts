Description
-------
'python-cts' adds a new executable, 'cts', which searches ctag files for your tag and then executes a command on the selected tag.  By default, it executes "$EDITOR +{lineNumber} {file}", which opens the found file your default editor.

Since 'cts' is only as good as your ctag files, it is recommended running ctags with '--extra=+f' so as to index filenames as well.  This will let you do 'cts Foo.java' to automatically open up Foo.java in your editor of choice.

Example 1
-------
    cts bar -i -c /some/directory/tags

1. '-c /some/directory/tags' indicates cts should use that tags file rather than attempting to find one.

2. '-i' indicates that it's a case insensitive search.  The resulting search query is /^bar$/i

3. Upon selecting a tag, executes "$EDITOR +{pattern} {file}.

Example 2
---------
    cts Foo -p -kc -t scala,py -e "grep def {file}"

1. Since no ctag file was specified, recurse from the current directory up until a 'tags' file is found.

2. '-p' indicates a partial search, so look for a /.*Foo.*/ in the tag file.

3. '-kc' 
indicates to filter out everything that isn't kind 'c', or class definitions.

4. '-t scala,py' indicates to filter out all tags that are not files with 'scala' or py as the extension.

5. '-e "grep def {file}"' indicates that after a selection has been made, to execute "grep def {file}" where {file} will be filled in with the absolute path to the reference file.

To Install (From Pip)
----------

pip install python-cts

To Install (From Source)
----------

1. Checkout the repo
2. python setup.py install
3. Profit!

Usage
-----

Type 'cts -h' to get usage information

