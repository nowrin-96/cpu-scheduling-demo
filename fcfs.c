#include <stdio.h>

struct Process {
    int pid;
    int bt;
    int wt;
    int tat;
};

int main() {
    int n, i, j, time = 0;
    float avg_wt = 0, avg_tat = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    struct Process p[n];


    for (i = 0; i < n; i++) {
        p[i].pid = i + 1;
        printf("Enter Burst Time for Process %d: ", p[i].pid);
        scanf("%d", &p[i].bt);
    }


    p[0].wt = 0;

    for (i = 1; i < n; i++) {
        p[i].wt = p[i - 1].wt + p[i - 1].bt;
    }


    for (i = 0; i < n; i++) {
        p[i].tat = p[i].bt + p[i].wt;
    }


    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n");
    for (i = 0; i < n; i++) {
        printf("P%d\t\t%d\t\t%d\t\t%d\n", p[i].pid, p[i].bt, p[i].wt, p[i].tat);
        avg_wt += p[i].wt;
        avg_tat += p[i].tat;
    }

    avg_wt /= n;
    avg_tat /= n;

    printf("\nAverage Waiting Time = %.2f", avg_wt);
    printf("\nAverage Turnaround Time = %.2f\n", avg_tat);


    printf("\nGantt Chart:\n");


    printf(" ");
    for (i = 0; i < n; i++) {
        for (j = 0; j < p[i].bt; j++) printf("--");
        printf(" ");
    }
    printf("\n|");
    for (i = 0; i < n; i++) {
        for (j = 0; j < p[i].bt - 1; j++) printf(" ");
        printf("P%d", p[i].pid);
        for (j = 0; j < p[i].bt - 1; j++) printf(" ");
        printf("|");
    }
    printf("\n ");
    for (i = 0; i < n; i++) {
        for (j = 0; j < p[i].bt; j++) printf("--");
        printf(" ");
    }
    printf("\n");


    time = 0;
    printf("0");
    for (i = 0; i < n; i++) {
        for (j = 0; j < p[i].bt; j++) printf("  ");
        time += p[i].bt;
        if (time > 9) printf("\b");
        printf("%d", time);
    }

    printf("\n");

    return 0;
}
