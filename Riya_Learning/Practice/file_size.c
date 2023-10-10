// C program to find the size of file
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	tag: FILE *fp = fopen("riya1.txt","a+");
     fseek(fp, 0L, SEEK_END);

       long int byt = ftell(fp);
       if(byt>50)
       {
      FILE *ls_cmd = popen("find . -type f -name 'riya*.txt' | grep -o -E '[0-9]+' | sort -rn | head -n 1", "r");
      if (ls_cmd == NULL)
      {
        fprintf(stderr, "popen(3) error");
       // exit(EXIT_FAILURE);
       }

    char buff[1024];
    size_t n;
    while ((n = fread(buff, 1, sizeof(buff)-1, ls_cmd)) > 0)
    {
        buff[n] = '\0';
        printf("file_content is = %s", buff);
    }

       int val;
       char filename[30];
       val = atoi(buff);
       val= val+1;
       sprintf(filename,"riya%d.txt", val);
       system("mv riya1.txt %s", filename);
       fprintf(fp, "hello dixon\n");
       goto tag;
       }
       else
       {
           fprintf(fp,"I have entered some content\n");
           fclose(fp);
       }
       return 0;
}


