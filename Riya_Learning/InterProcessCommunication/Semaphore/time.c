#include <time.h>
#include <stdio.h>
#include <string.h>

#define print_log(f_, ...) printf("%s ", timestamp()), printf((f_), ##__VA_ARGS__), printf("\n")

char * timestamp(){
    time_t now = time(NULL);
    char * time = asctime(gmtime(&now));
    time[strlen(time)-1] = '\0';    // Remove \n
    return time;
}

int main(int argc, char* argv[]) {


    print_log("Hello");
    print_log("%s%d","mokumus",1996);

    return 0;
}

/*void timestamp1()
{
    time_t ltime; //calendar time
    ltime = time(NULL); // get current cal time
    printf("%s", asctime(localtime(&ltime)));
}

int main()
{   
    timestamp1();
    return 0;
}*/

