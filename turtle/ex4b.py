#ex4.py nm
import turtle  #Inside_Out
from turtle import *
w = turtle.Screen()
image = "/home/duck/documents/github/html/test_server/img/egg.gif"
w.bgpic("img/egg.gif")
t = turtle.Turtle()
t.color("#ffffff")
t.width(2)
t.speed(5)
f = turtle.Turtle()
f.color("#E71010")
f.width(2)
f.speed(5)
y = turtle.Turtle()
y.color("#CA05CA")
y.width(2)
y.speed(5)
z = turtle.Turtle()
z.color("#FF8F8F")
z.width(2)
z.speed(5)
p = turtle.Turtle()
p.color("#FFED00")
p.width(3)
p.speed(5)

def oof(size):
	for i in range(35):
		t.fd(size)
		t.left(75)
		size = size + 11
		
def foo(size):
	for i in range(35):
		f.fd(size)
		f.left(75)
		size = size + 11.2
		
def yikes(size):
	for i in range(35):
		y.fd(size)
		y.left(75)
		size = size + 11.4
		
def yikes2(size):
	for i in range(35):
		z.fd(size)
		z.left(75)
		size = size + 11.6
		
def poof(size):
	for i in range(35):
		p.fd(size)
		p.left(75)
		size = size + 12

oof(6)
foo(7)
yikes(8)
yikes2(9)
poof(10)
oof(26)
foo(27)
yikes(28)
yikes2(29)
poof(30)
oof(46)
foo(47)
yikes(48)
yikes2(49)
poof(50)
oof(8)
foo(9)
yikes(10)
yikes2(11)
poof(12)

holdit = input();
