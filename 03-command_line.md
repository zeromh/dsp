# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >1. `cat >>filename` is required to be able to append text to filename.
2. Type `directoryname/` (with the slash at the end) to disambiguate whether something is a directory.
3. You have to use `rm -r` to remove a directory that has files/directories in it.
4. `pushd` changes directory but saves your current directory to go back to it later.
5. Using `mv` to move a file or directory can also rename it at the same time.
6. You can make nested directories all at once with `mkdir -p dir1/dir2/dir3`
7. The home directory is abbreviated `~`
8. The current directory is abbreviated `.`
9. You can go up one directory and then down into another directory using `cd ../other_directory`
10. Use quotes to create or access names that have spaces in them

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` lists non-hidden files in a directory  
`ls -a` lists all files, including hidden  
`ls -l` lists filenames plus extra info ("long listing")  
`ls -lh` is like the above but it print file size in human readable format  
`ls -lah` is a logical combination of the above  
`ls -t` lists files newest modified to oldest modified  
`ls -Glp` gives long listing without group names. Also appends '/' to directory names.  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -r` show list in reverse order  
`ls -R` list all sub-directories and files too  
`ls -Rp` to make it obvious which names are directories or files  
`ls -d` list only directories  
`ls -1` list one file per line  


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` can be used to pass a long list of arguments to a command.  
`find . -name "*.txt" -print | xargs grep "Data"` finds all the .txt files in the current directory and subdirectories, and passes those names as the first argument of `grep`.

 

