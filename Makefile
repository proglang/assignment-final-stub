.PHONY: all

all: runtime.o requirements.installed

runtime.o: runtime.c runtime.h
	gcc -c -g -std=c99 runtime.c

requirements.installed:
	pip3 install -r requirements.txt
	touch requirements.installed
