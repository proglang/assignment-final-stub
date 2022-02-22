.PHONY: all clean distclean

all: runtime.o requirements.installed

runtime.o: runtime.c runtime.h
	gcc -c -g -std=c99 runtime.c

requirements.installed: requirements.txt
	pip3 install -r requirements.txt
	touch requirements.installed

clean:
	rm tests/*/*.s
	rm tests/*/*.out
	rm a.out

distclean: clean
	rm runtime.o
	rm -rf __pycache__
