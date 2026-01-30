---
created: 2026-01-30
tags:
  - python
---

## Statements

A *statement* is the part of the program that executes something. It often - but not always - refers to a single command. 

[!example]
> For example `print("Hi")` is a statement which prints out a line text. Likewise, `number = 2` is a statement which assigns a value to a variable. A statement can also be more complex, and can contain other statements. 

## Block

A block is a group of consecutive statements that are at the same level in the structure of the program. For example, the block of a conditional statement contains those statements which are executed only if the condition is true.

if age > 17:
    # beginning of the conditional block
    print("You are of age!")
    age = age + 1
    print("You are now one year older...")
    # end of the conditional block

print("This here belongs to another block")

In Python blocks are expressed by indenting all code in the block by the same amount of whitespace.

NB: the main block of a Python program must always be at the leftmost edge of the file, without indentation:

:
