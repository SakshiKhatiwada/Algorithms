#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

#define NUM 10000 // Number of random numbers to generate
void BubbleSort(int *A);
int main()
{

    SYSTEMTIME st1, st2; // Variables to store start and stop time
    // Open the file for writing
    FILE *inputFile = fopen("input.txt", "rw");
    if (inputFile == NULL)
    {
        printf("Failed to create input file!\n");
        return 1;
    }

    // Seed the random number generator
    srand((unsigned int)time(NULL));
    // NOTE: Without setting a seed, the rand function will produce the same sequence of numbers every time the program runs. The time function returns the current time in seconds since the Unix epoch (January 1, 1970).Passing NULL as the argument tells time to return the current time without storing it in a variable.

    // Generate random numbers and write them to the file
    for (int i = 0; i < NUM; i++)
    {
        fprintf(inputFile, "%d ", rand() % (NUM + 1)); // Random number between 0 and NUM
    }

    // reading now
    if (inputFile == NULL)
    {
        printf("Failed to open input file!\n");
        return 1;
    }

    // Allocate memory for the array
    int *A = (int *)malloc(NUM * sizeof(int));
    if (A == NULL)
    {
        printf("Memory allocation failed!\n");
        fclose(inputFile);
        return 1;
    }

    // Read numbers from the file into the array
    for (int i = 0; i < NUM; i++)
    {
        if (fscanf(inputFile, "%d", &A[i]) != 1) // reads 1 integer, if failed, it returns EOF
        {
            printf("Error reading input file!\n");
            free(A);
            fclose(inputFile);
            return 1;
        }
    }
    fclose(inputFile);
    printf("Input file 'input.txt' generated successfully with %d random numbers.\n", NUM);

    printf("\n------------Bubble Sort------------\n");

    // Record the start time
    GetSystemTime(&st1);

    // Perform Bubble Sort
    BubbleSort(A);

    // Record the stop time
    GetSystemTime(&st2);

    // Open output file for writing
    FILE *outputFile = fopen("output.txt", "w");
    if (outputFile == NULL)
    {
        printf("Failed to open output file!\n");
        free(A);
        return 1;
    }

    // Write the sorted array to the file
    fprintf(outputFile, "--------------Sorted Array------------\n");
    for (int i = 0; i < NUM; i++)
    {
        fprintf(outputFile, "%d ", A[i]);
    }
    fprintf(outputFile, "\n\nSorting Start Time: %02d:%02d:%02d.%03d\n", st1.wHour, st1.wMinute, st1.wSecond, st1.wMilliseconds);
    fprintf(outputFile, "Sorting Stopped Time: %02d:%02d:%02d.%03d\n", st2.wHour, st2.wMinute, st2.wSecond, st2.wMilliseconds);

    fclose(outputFile);
    free(A);

    printf("Sorting completed. Results written to output.txt\n");
    return 0;
}

// BUBBLE SORT
void BubbleSort(int *A)
{
    for (int round = 0; round < NUM - 1; round++)
    {
        for (int pass = 0; pass < NUM - round - 1; pass++)
        {
            if (A[pass] > A[pass + 1])
            {
                // Swap
                int temp = A[pass + 1];
                A[pass + 1] = A[pass];
                A[pass] = temp;
            }
        }
    }
}