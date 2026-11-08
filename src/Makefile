CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -O2
LDFLAGS = -lm
TARGET = game_gen
SRC = game_gen.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
