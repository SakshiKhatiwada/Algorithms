#include <stdio.h>

int main()
{
    int totalWeightOfBag = 15, totalItems = 9;
    int values[9] = {2, 3, 3, 4, 4, 5, 7, 8, 8}, weights[9] = {3, 5, 7, 4, 3, 9, 2, 11, 5};
    int knapsack[9 + 1][15 + 1] = {0}; // we need case for no items too, so 1 extra row and column

    // filling the knapsack matrix
    // knapsack matrix printed
    printf("----------------- 0-1 Knapsack Problem----------------\n\n");
    for (int i = 0; i <= totalItems; i++)
    {
        for (int w = 0; w <= totalWeightOfBag; w++)
        {
            if (i == 0 || w == 0)
                knapsack[i][w] = 0;

            else if (i > 0 && weights[i - 1] > w) // we are saying 0th index weight as 1st weight
                knapsack[i][w] = knapsack[i - 1][w];
            // formula: c[i-1][w]

            else if (i > 0 && w >= weights[i - 1])
                knapsack[i][w] = (values[i - 1] + knapsack[i - 1][w - weights[i - 1]]) > (knapsack[i - 1][w]) ? (values[i - 1] + knapsack[i - 1][w - weights[i - 1]]) : (knapsack[i - 1][w]);
            // formula: max {v_i + c[i-1][w-w_i], c[i-1][w]}

            printf("%d \t", knapsack[i][w]);
        }
        printf("\n");
    }

    printf("The maximum value the thief can get is %d.", knapsack[totalItems][totalWeightOfBag]);
}
