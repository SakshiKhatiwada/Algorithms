// Bubble Sort
#include <stdio.h>
#include <time.h>
#include <windows.h>

#define NUM 10000

void BubbleSort(int *A);

int main()
{

    SYSTEMTIME st1, st2;

    int *A = (int *)malloc(NUM * sizeof(int)); // Allocate memory
    int *p = A;
    if (A == NULL) // Check if allocation was successful
    {
        printf("Memory allocation failed!\n");
        return 1;
    }
    for (int i = 0; i < NUM; i++)
    {
        *(A + i) = rand() % (NUM + 1);
        printf("%d ", *(A + i));
    }
    printf("\n------------Bubble Sort------------\n");

    GetSystemTime(&st1);

    BubbleSort(A);

    GetSystemTime(&st2);

    printf("\n--------------sorted array------------\n");
    for (int i = 0; i < NUM; i++)
    {
        printf("%d ", *(p + i));
    }
    printf("\n\nSorting Start Time: %02d: %02d: %02d.%03d\n", st1.wHour, st1.wMinute, st1.wSecond, st1.wMilliseconds);
    printf("Sorting Stopped Time: %02d: %02d: %02d.%03d\n", st2.wHour, st2.wMinute, st2.wSecond, st2.wMilliseconds);
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
                // swap
                int temp = A[pass + 1];
                A[pass + 1] = A[pass];
                A[pass] = temp;
            }
        }
    }
}
