FILENAME=informe
TEX=$(FILENAME).tex
PDF=$(FILENAME).pdf

.PHONY: all clean new

all: $(PDF)

$(PDF): $(TEX)
	pdflatex -interaction=nonstopmode -halt-on-error $(TEX) && \
	pdflatex -interaction=nonstopmode -halt-on-error $(TEX)

clean:
	rm -f *.aux *.log *.toc *.out *.pdf

new: clean all
