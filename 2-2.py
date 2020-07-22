# coding: utf-8
import array
symbols = "~!@#$%^&*()_+"
codes = [ord(symbol) for symbol in symbols]
print(codes)
colours = ["black", "red"]
sizes = ["S", "M", "L"]
t_shirts = [(colour, size) for colour in colours for size in sizes]
print(t_shirts)
tp = tuple(ord(symbol) for symbol in symbols)
print(tp)

arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)