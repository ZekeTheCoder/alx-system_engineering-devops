#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - function that creates an infinite loop.
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * creates 5 zombie processes.
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t PID;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		PID = fork();
		if (PID == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", PID);
	}
	infinite_while();
	return (0);
}
