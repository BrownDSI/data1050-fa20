# Test-Driven Design
Think before you speak and ...
> Read before you think -- Fran Lebowitz 1981

> Test before you code -- Some Programmer 1960s

---
[Test Driven Design](https://en.wikipedia.org/wiki/Test-driven_development) is a
"test-first" software design and maintenance methodology.
<hr>
It requires you to implement tests before you implement code.
<hr>
This approach has proved to be very helpful for new and old
programmers, alike.
<hr>
We'll use the following approach in DATA1050:
<hr>
**Test-First Design Steps** for creating a new function  

1. Inputs - what are arguments?
1. Outputs - what should be returned?
1. Usual cases 
1. Special cases 
1. Create **function specification** (signature + docstring)
1. Create "test cases" 
1. Implement function
1. Add/improve tests as needed
<hr>
---
## Example
Solve the following problem using Test-First Design (TFD):

> Write a function `gap(x,y)` that returns the distance 
  between two numbers?  Use only `if` statements and not 
  functions like `abs` or `max`. 

---
1. Inputs - what are arguments? <hr>
2. Outputs - what should be returned? <hr>  
3. Usual cases <hr> 
4. Special cases <hr>  
5. Create **function specification** (signature + docstring) <hr>
6. Implement tests for each case <hr>
7. Implement function  <hr>
8. add/improve tests as needed <hr> 

---
## Annotated Solution
See `gap-soln.py`

---
### No signature
In coding interviews, when no signature is given, come up with enough of one to restate the question using it. Confirm this restatement with the interviewer, and then proceed.
<hr>
Interviewer: "Please write a function that returns the distance between two numbers?  Use if statements and not a function like abs or max."
<hr>
Interviewee: "Ok, so I think you want me to write a function, let's call it `dist(x,y)` that returns the distance between the numbers `x` and `y`."

---
### Break-out (10 minutes)
Go through the TDD Steps for `twoNumberSum`!
1. Annotate your solution like the one above for `gap(x,y)`
1. When everyone is back, when asked, everyone should paste their group's solution.






