BIN_DIR=bin
SRC_DIR=src
BIN_NAME=ej3
BIN=$(BIN_DIR)/$(BIN_NAME)
SRC_BIN=$(SRC_DIR)/$(BIN_NAME).out

.PHONY: all clean new $(BIN)

all: $(BIN)

$(BIN): $(BIN_DIR)
	make -C $(SRC_DIR) all
	cp -f $(SRC_BIN) $(BIN)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

clean:
	make -C $(SRC_DIR) clean
	rm -rf $(BIN)

new: clean all
