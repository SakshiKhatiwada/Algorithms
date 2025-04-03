# defining the function
def subset_sum(W, sum, i, m, sol):
    """
    Statement:
    
    “Given 𝑛 positive numbers w_i (1 <= i <= n) and another number m, find all subsets of the numbers whose sums are m”
    
    Attributes:
    W : input array of numbers
    sum: currently evaluated sum
    i: starting index of input
    m: target sum
    sol: solution list
    """
    if sum == m:
        print("soln: ", sol)

    if sum < m:
        for j in range(
            i, W.__len__()
        ):  # NOTE Generating all child, that's how DFS works!
            subset_sum(
                W, sum + W[j], j + 1, m, sol + [W[j]]
            )  # NOTE not push, append in list, add in set

            # learnt W, sum + W[j], j + 1, m, sol.append(W[j]) -> it modifies the original list sol and returns null in recursive call, so we need to add [] so that it returns a new list


# driver code
# W = {11, 13, 24, 7}
# print(W) # printed in ascending order
W = [11, 13, 24, 7, 34, 23, 8, 19, 12, 30, 1]
m = 31
sol = []
# print('sol',sol)
subset_sum(W, 0, 0, 31, sol)
