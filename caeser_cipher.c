/* Demonstrates a simple ceaser cipher
 * ie, we shift all the letters of the alphabet by the number given by the cipher
 * so, if cipher is 1 then A->B, ..., Z->A, or whatever is after Z in the ASCII index
 */
#include <stdio.h>
#include <stdlib.h>
#include "../file_pack.h"

#define MOD(x,n) ((x % n + n) % n)
#define RING_SIZE 128

void encrypt(FILE *unencrypted, FILE *encrypted, int cipher);
void decrypt(FILE* unencrypted, FILE *encrypted, int cipher);

int main(int argc, char *argv[])
{
    /*command line argument 1 is the in file and command argument 2 is the
     *out file and 3 is the cipher in the form of an integer
     *4 is the mode given in string format either (e) encrypt or (d) decrypt
     *so, to encrypt we would say ./program infile outfile 10 e
     *and to decrypt we would say ./program infile outfile 10 d*/
    file_s *in_file = open_file(argv[1], "r");
    file_s *out_file = open_file(argv[2], "w");
    int cipher = atoi(argv[3]);
    char *mode = argv[4];
    
    if(mode[0] == 'e') encrypt(in_file->fp, out_file->fp, cipher);
    else if(mode[0] == 'd') decrypt(in_file->fp, out_file->fp, cipher);
    /*close the files and end the program*/
    close_file(in_file);
    close_file(out_file);
    return 0;
}

/*take each character from the unencrypted in file, add the caeser cipher to it
 *(thus changing it's ASCII value) and write it to the encrypted out_file*/
void encrypt(FILE *in, FILE *out, int cipher)
{
    char c;
    c = fgetc(in);
    printf("encrypting file...\n");
    while(c != EOF)
    {
	    c = MOD(c + cipher, RING_SIZE);
    	fputc(c, out);
	    c = fgetc(in);
    }
    printf("file encrypted...\n");
}

void decrypt(FILE *in, FILE *out, int cipher)
{
    char c;
    c = fgetc(in);
    printf("decrypting file...\n");
    while(c != EOF)
    {
	    c = MOD(c - cipher, RING_SIZE);
	    fputc(c, out);
	    c = fgetc(in);
    }
    printf("file decrypted...\n");
}
