#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void abc(int signo)
{
	printf("Received Signal with signo %d\n", signo);
}

void def(int signo)
{
	printf("Received Signal with signo %d\n", signo);
}

int main()
{
	printf("Press DEL<ctrl+\\> key\n");
	signal(SIGINT, def); // key, function
	signal(SIGQUIT, abc); // key, function
	for(;;);
	return 0;
}
