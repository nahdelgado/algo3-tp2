CXX=g++
CFLAGS=-Wall -c $(OPTIM) -std=c++11
LDFLAGS=-Wall $(OPTIM)
DEBUG_FLAGS=-Wall $(DEBUG) -std=c++11
DEBUG=-g
OPTIM=
SOURCES=main.cc solver.cc
OBJS=$(SOURCES:.cc=.o)
EXE=ej1.out

.PHONY: all debug clean new

all: $(EXE)

debug:
	$(CXX) $(DEBUG_FLAGS) $(SOURCES) -o $(EXE)

$(EXE): $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o $@

.cc.o:
	$(CXX) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(EXE)

new: clean all
