prefix = /usr/local
bindir = $(prefix)/bin

install:
	cp query.py $(bindir)/pglocate
	chmod 0755 $(bindir)/pglocate

