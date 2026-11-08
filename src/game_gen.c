#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// N-Queens-Puzzle
// Idea optimización, si valor se repite al revisar, pasar inmediatamente al siguiente bit, y no revisar hacia adentro
int N = 4; // N >= 4

void printarray(int *array){
    for (int i = 0; i<N; i++){
        printf("%i ", array[i]);
    }
        printf("\n");

}

int checkInArray(int *array, int c){
    int check;
    for (int i = 0; i<c; i++){
        //printarray(array);
        check = array[i];
        if(check == c){
            return 1;
        }
        else if (check == -1){
            return 0;
        }
    }
    return 0;
}


int *emptyArray(int n, int c){
    int * array = malloc(sizeof(int)*n);
    for (int i = 0; i<n; i++){
        array[i] = c;
    }
    return array;
}

int checkSet(int *set){
    int * check = emptyArray(N,-1);
    int prev = N+1;
    int current; 
    for (int i = 0; i<N; i++){
        current = set[i]; 
        if (abs(prev-current) <= 1 || current>N-1){
            free(check);
            return 0;
        }
        if (!checkInArray(set, current)){
            check[i] = current;
        }
        else{
            free(check);
            return 0;
        }
        prev = current;

    }
    free(check);
    return 1;
}

void printSet(int *set){
    for (int i = 0; i<N; i++){
        int local_pos = set[i];
        for (int j = 0; j<local_pos; j++){
            printf("x");
        }
        printf("o");
        for (int j = 0; j<N-local_pos-1; j++){
            printf("x");
        }
        printf("\n");
    }
    printf("\n");
}
    
int Calc(int n, int *set, int fr);    

int Calc(int n, int *set, int fr){
    if(!fr){
        set[n] = 0;
    }
    for (int i = 0; i<N; i++){
        if (n < N-1 && Calc(n+1, set, fr)){
            return 1;
        }
        fr = 0;
        if (checkSet(set)){
            return 1;
        }
        if(i != N-1){
            set[n] += 1;
        }
    }
    return 0;
}
// Game-gen
int main(int argc, char **argv){
    if (argc > 1){
        N = strtol(argv[1], NULL, 0);
    }
    srand((unsigned)time(NULL));
    long int seed = (long int)rand() % (long int)(pow(N, N));
    //int seek = (int)rand();
    int * queens = emptyArray(N,0);
    for (int i = 0; i<N; i++){
        queens[i] = (seed % N);
        if(seed > 0){
            seed = (int)(seed / N);
        }
    }

    printSet(queens);
    if (!Calc(0, queens, 1)){
        printf("lol\n");
        Calc(0, queens, 0);
    }
    printSet(queens);
    free(queens);
    return 0;
}
