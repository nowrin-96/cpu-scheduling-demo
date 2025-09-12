#include <stdio.h>
struct Process {
    int pid, at, bt, ct, tat, wt;
};
int main() {
    int n,i,j;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    struct Process p[n];
    for( i=0; i<n; i++) {
        p[i].pid = i+1;
        printf("Enter Arrival Time and Burst Time for P%d: ", i+1);
        scanf("%d %d", &p[i].at, &p[i].bt);
    }
    for( i=0; i<n-1; i++) {
        for( j=i+1; j<n; j++) {
            if(p[i].at > p[j].at) {
                struct Process temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }
    int time = 0;
    for( i=0; i<n; i++) {
        if(time < p[i].at) time = p[i].at;
        p[i].ct = time + p[i].bt;
        time = p[i].ct;

        p[i].tat = p[i].ct - p[i].at;
        p[i].wt  = p[i].tat - p[i].bt;
    }
    printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
    float avg_tat=0, avg_wt=0;
    for( i=0; i<n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
            p[i].pid, p[i].at, p[i].bt, p[i].ct, p[i].tat, p[i].wt);
        avg_tat += p[i].tat;
        avg_wt  += p[i].wt;
    }
    printf("Average TAT = %.2f\n", avg_tat/n);
    printf("Average WT  = %.2f\n", avg_wt/n);

    printf("\nGantt Chart:\n");
    printf(" ");
    for( i=0; i<n; i++) {
        for( j=0; j<p[i].bt; j++) printf("--");
        printf(" ");
    }
    printf("\n|");
    for( i=0; i<n; i++) {
        for( j=0; j<p[i].bt-1; j++) printf(" ");
        printf("P%d", p[i].pid);
        for( j=0; j<p[i].bt-1; j++) printf(" ");
        printf("|");
    }
    printf("\n ");
    for( i=0; i<n; i++) {
        for( j=0; j<p[i].bt; j++) printf("--");
        printf(" ");
    }
    printf("\n");
    printf("0");
    time = 0;
    for( i=0; i<n; i++) {
        if(time < p[i].at) time = p[i].at;
        time += p[i].bt;
        printf("%*d", p[i].bt*2, time);
    }
    printf("\n");
    return 0;
}
