
CC = gcc
CFLAGS = -Wall -g -std=c89 -pedantic-errors

TARGET = caeser_cipher

all: $(TARGET)

$(TARGET): $(TARGET).c ../file_pack.c
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c ../file_pack.c

clean:
	rm $(TARGET)

val:
	valgrind --leak-check=yes ./caeser_cipher in.txt out.txt 10 e
