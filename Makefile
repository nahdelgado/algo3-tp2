EJ1_DIR=ejercicio_1
EJ2_DIR=ejercicio_2
EJ3_DIR=ejercicio_3
BUNDLE_DIR=AED3-TP2
TEX_DIR=tex
PDF_NAME=informe.pdf
BUNDLE=AED3-TP2.tar.gz
BUNDLE_FILES=$(EJ1_DIR) $(EJ2_DIR) $(EJ3_DIR) tex enunciado.pdf informe.pdf Makefile README.md

.PHONY: all clean new clean-tex ejercicios bundle $(PDF_NAME)

all: ejercicios $(PDF_NAME)

ejercicios:
	make -C $(EJ1_DIR) all
	make -C $(EJ2_DIR) all
	make -C $(EJ3_DIR) all

$(PDF_NAME):
	make -C $(TEX_DIR) all
	cp -f $(TEX_DIR)/$(PDF_NAME) .

bundle: clean $(PDF_NAME)
	mkdir $(BUNDLE_DIR)
	cp -r $(BUNDLE_FILES) $(BUNDLE_DIR)
	tar zcf $(BUNDLE) $(BUNDLE_DIR)
	rm -rf $(BUNDLE_DIR)

clean: clean-tex
	make -C $(EJ1_DIR) clean
	make -C $(EJ2_DIR) clean
	make -C $(EJ3_DIR) clean
	rm -rf $(PDF_NAME) $(BUNDLE) $(BUNDLE_DIR)

clean-tex:
	make -C $(TEX_DIR) clean

new: clean all
