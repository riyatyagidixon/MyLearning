#include <time.h>
#include "shm_sem.h"

int semaphore_p(int sem_id);
int semaphore_v(int sem_id);

FILE *fptr = NULL;

char * timestamp()
{
    time_t ltime; /* calendar time */
    ltime = time(NULL); /* get current cal time */

    char * curr_local_time = asctime(localtime(&ltime));
    curr_local_time[strlen(curr_local_time) - 1] = '\0'; // removed \n
    return curr_local_time;
}

int main()
{
	int start = 1;
	void *shm = NULL;
	struct sh_dat *sh_ptr;
	char buffer[TEXT_SZ];
	int shmid, semid;

    fptr = fopen("/home/guest/Riya/MyLearning/Riya_Learning/InterProcessCommunication/Semaphore/mylog.txt", "a+");

	shmid = shmget((key_t)1234, sizeof(struct sh_dat), 0666 | IPC_CREAT);
	if(shmid == -1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] shmget failed\n", timestamp(), __FILE__, __func__, __LINE__);
		exit(EXIT_FAILURE);
	}
    sleep(1);
	fprintf(fptr, "[%s] [%s] [%s] [%d] Shared Memory created\n", timestamp(), __FILE__, __func__, __LINE__);
	
	semid = semget((key_t)1235, 1, 0666 | IPC_CREAT);
	if(semid == -1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] semget failed\n", timestamp(), __FILE__, __func__, __LINE__);
		shmctl(shmid, IPC_RMID, NULL);
		exit(EXIT_FAILURE);
	}
    sleep(1);
	fprintf(fptr, "[%s] [%s] [%s] [%d] Semaphore created\n", timestamp(), __FILE__, __func__, __LINE__);

	shm = shmat(shmid, (void *)0, 0);
	if(shm == (void *)-1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] shmat failed\n", timestamp(), __FILE__, __func__, __LINE__);
		exit(EXIT_FAILURE);
	}
    sleep(1);
	fprintf(fptr, "[%s] [%s] [%s] [%d] Shared Memory Attached\n", timestamp(), __FILE__, __func__, __LINE__);
	sh_ptr = (struct sh_dat *)shm;
	while(start) 				/* entering the loop */
	{
		/* Waiting while server reads the data written by the client */
		if(semaphore_p(semid))	/* Check if server has written the data */
		{
			printf("Enter some text: ");
			fprintf(fptr, "[%s] [%s] [%s] [%d] Enter some text: ", timestamp(), __FILE__, __func__, __LINE__);
			fgets(buffer, TEXT_SZ, stdin);
		
			strncpy(sh_ptr->text, buffer, TEXT_SZ);
			fprintf(fptr, "[%s] [%s] [%s] [%d] User has type the message: %s", timestamp(), __FILE__, __func__, __LINE__, buffer);
			semaphore_v(semid);	/* Giving the memory to the server for reading */
			sleep(1);
			if(strncmp(sh_ptr->text, "end",3) == 0)
			{
				start = 0;		/* Stopping the program */
			    fprintf(fptr, "[%s] [%s] [%s] [%d] User has type the message: %s", timestamp(), __FILE__, __func__, __LINE__, sh_ptr->text);
			}
		}
	}
	if(shmdt(sh_ptr) == -1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] shmdt failed\n", timestamp(), __FILE__, __func__, __LINE__);
		exit(EXIT_FAILURE);
	}
	fprintf(fptr, "[%s] [%s] [%s] [%d] Shared Memory Detached\n", timestamp(), __FILE__, __func__, __LINE__);
	exit(EXIT_SUCCESS);
}

int semaphore_p(int sem_id)
{
	struct sembuf sem_b;
	sem_b.sem_num = 0;
	sem_b.sem_op = -1;
	sem_b.sem_flg = SEM_UNDO;
	if(semop(sem_id, &sem_b, 1) == -1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] semaphore_p failed \n", timestamp(), __FILE__, __func__, __LINE__);
		return 0;
	}
	return 1;
}

int semaphore_v(int sem_id)
{
	struct sembuf sem_b;
	sem_b.sem_num = 0;
	sem_b.sem_op = 1;
	sem_b.sem_flg = SEM_UNDO;
	if(semop(sem_id, &sem_b, 1) == -1)
	{
		fprintf(fptr, "[%s] [%s] [%s] [%d] semaphore_v failed \n", timestamp(), __FILE__, __func__, __LINE__);
		return 0;
	}
	return 1;
}
