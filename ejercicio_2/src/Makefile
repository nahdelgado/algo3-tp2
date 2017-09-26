CXX=g++
CFLAGS=-Wall -c $(DEBUG) $(OPTIM) -std=c++11
LDFLAGS=-Wall $(DEBUG) $(OPTIM)
DEBUG=-g
OPTIM=
SOURCES=main.cc solver.cc
OBJS=$(SOURCES:.cc=.o)
EXE=ej2.out

.PHONY: all clean new

all: $(EXE)

$(EXE): $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o $@

.cc.o:
	$(CXX) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(EXE)

new: clean all
