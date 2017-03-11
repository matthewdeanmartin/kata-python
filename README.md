# kata-python
Kata is Japanese for form, as in patterns for practice. You practice the same pattern over and over until you're better at coding. Coding kata are short programs 
you can write over and over.

###  Origin
Most of these are inspired by an ancient book [BASIC is Fun](https://www.amazon.com/Basic-Fun-Computer-Problems-Children/dp/0380806061), which was a bunch of programs you could type and run on an 8 bit machine and as a by product maybe learn to write code. In retrospect, this was pretty crazy, since most of these are about as difficult as fizz-buzz, [which as we know some people can't solve](https://en.wikipedia.org/wiki/Fizz_buzz). I've been wanting to translate the code into a modern programing language since forever. Most of the problems were algebra story problems. The solved section isn't a translation of the original, coding styles are so radically different little would be salvagable from the original.

These questions are far easier than [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=pd_sbs_14_img_0?_encoding=UTF8&psc=1&refRID=JV9XCVQ6A174G137R2W2).

### As Interview Questions
If use in an interview, or as a "homework question", in my opinion, the demonstrate:

1. Speed. Can you solve it quickly.
2. Converation starts. Now that we have some real code, we got somethign we can talk about.
3. Aptitude. If you can solve a simple question, no one knows if you are a good programmer. If you can't solve
4. Proxy for a portfolio. Developers best code is probably locked behind non-disclosure agreements of various sorts and even if it wasn't, it sometimes so domain specific, large and mixed with other developers work that it is hard for an intervier to see what is going on.

### Layout
The kata folder holds the blanks with some boiler plate filled in.

The kata_functional, kata_oop, kata_script are for kata problems to be solved with a particular programming style.

The solve folder has

### Workflow
I'm solving the problems first, then I copy the skeleton to the corresponding root folders.

If you want to do a kata, branch and fill out the blanks.  If you want to fix bugs in my kata code, branch and modify the /solved/ folder and make pull requests.

### Python Interpretor, Libraries
I'm planning to write this in python 3 with some effort to make it python 3 compatible.
  
I plan to make some kata specifically for psycopg, pandas, and other libraries. At the moment, the goal is for all kata to be done with just the standard library and some development dependencies such as:

- pylint
- virtualenv, pyenv and similar 
