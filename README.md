# kata-python
Kata is Japanese for form, as in patterns for practice. You practice the same pattern over and over until you're better at coding. Coding kata are short programs 
you can write over and over.

###  Origin
Most of these are inspired by an ancient book [BASIC is Fun](https://www.amazon.com/Basic-Fun-Computer-Problems-Children/dp/0380806061), which was a bunch of programs you could type and run on an 8 bit machine and as a by product maybe learn to write code. In retrospect, this was pretty crazy, since most of these are about as difficult as fizz-buzz, [which as we know some people can't solve](https://en.wikipedia.org/wiki/Fizz_buzz). I've been wanting to translate the code into a modern programing language since forever. Most of the problems were algebra story problems. The solved section isn't a translation of the original, coding styles are so radically different little would be salvagable from the original.

These questions are far easier than [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=pd_sbs_14_img_0?_encoding=UTF8&psc=1&refRID=JV9XCVQ6A174G137R2W2). This set of problems isn't intended to work out if you've recently graduated from a CompSci program and still remember
your algorithms and data structures classes.

### As Interview Questions
If use in an interview, or as a "homework question", in my opinion, the demonstrate:

1. Speed. Can you solve it quickly.
2. Converation starts. Now that we have some real code, we got somethign we can talk about.
3. Aptitude. If you can solve a simple question, no one knows if you are a good programmer. If you can't solve a simple question, it may be a bad sign.
4. Proxy for a portfolio. Developers best code is probably locked behind non-disclosure agreements of various sorts and even if it wasn't, it sometimes so domain specific, large and mixed with other developers work that it is hard for an intervier to see what is going on.

See [scoring](scoring.MD) for how a kata can be graded.

### Layout
The kata folder holds the blanks with some boiler plate filled in. If you are solving problems, branch and put your code here!

The kata_functional, kata_oop, kata_script are for kata problems to be solved with a particular programming style.

The solved folder has all the above solved. Except the ones I haven't gotten to yet. This is where you go to cheat or compare your code after you've already solved it.


### Kata Solving Workflow
If you want to do a kata, fork, clone and fill out the blanks in kata, kata_functiona, etc.

Run run_tests.sh to execute the tests. Initially they will pass, but that won't mean anything since the code under test
is just place holder code.

I've started a [syntax cheat sheet](SYNTAX_CHEAT_SHEET.MD) for looking up basic language questions. If you are doing
an open book, open internet or doing the kata after consoluting a solved solution-- that will depend on what your 
motivations are. If you are practicing for whiteboarding, you won't have the internet handy.

### Kata Design Workflow
I'm solving the problems first, then I copy the skeleton to the corresponding root folders.

If you want to fix bugs in my kata code, branch and modify the /solved/ folder and make pull requests.

### Python Interpretor, Libraries
I'm planning to write this in python 3 with some effort to make it python 2/3 compatible.
  
I plan to make some kata specifically for psycopg, pandas, and other libraries. At the moment, the goal is for all kata to be done with just the standard library and some development dependencies such as:

- pylint
- virtualenv, pyenv and similar 
