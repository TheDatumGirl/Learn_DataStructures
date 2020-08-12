Both DP and greedy are solution to optimization problems.
Difference between Greedy and Dynamic Programming:
Greedy method : try to follow predefined procedure to get the optimal result. The procedure is known to be optimal and that is used. eg Djikstra's algorithm for shortest path. 
DP : finds all possible solutions and then chooses the most optimal solution. Mostly uses recursive formulas, not necessarily recursive prgramming. 
DP follows Principle of optimality : A problem can be solved by taking sequence of decisions to get optimal solution. Greedy takes only one decision and follows the procedure. DP makes decisions at each stage. 

For eg : Fibonnacci sequence : 0,1,1,2,3,5,8,13,… 
If I want to know 10th term call n=10. 
def fib(n):
    if (n <= 1) :
        return n
    else return fib(n-2) + fib(n-1)

The entire recursive program for fib forms a binary tree.
Time complexity using recurrence relation : T(n) = 2T(n-1) + 1 // Decreasing function Master theorem : O(2^n)

Can we reduce the time ? Yes, you see fib(1) being called so many times. Same goes for fib(2). So if we store the result for 1st call of fib(1) , we wont have to call it again. Let's store it in the form of a predefined array where index=n and value is -1 initially. As soon as fib(n) is called, we check the array :  if it has fib(n) = -1 -> not yet called -> so call fib(n) ; else if fib(n) not equal to -1 then fib(n) = array[n] . The number of calls now has reduced to n+1. This makes it O(n) . This is called memoization. It follows Top Down Approach. 

Tabulation Method : Iterative function for fibonacci series.
def fib(n):
    F[0] = 0
    F[1] = 1
    for i in range(2,n):
        F[n] = F[n-1] + F[n-2]

Here , F[i]=F[i-1] + F[i-2] //bottom up approach O(n)

Mostly we use Tabulation Method for DP.

Problem 1 : Multistage Graph :
A multistage graph is directed weighted graph. Vertices are divided into stages; such that edges are connected vertices from one stage to next stage
Usually used for resource allocation. 
Problem statement : find minimum cost -> Optimization problem -> check if we can use DP.

To check if we can use DP, check Principle of optimality : problem must be solved in seq of decisions.
In multistage graph to go from vertex A in stage 1 to stage 2 first decision : need to choose one of the many vertices in stage 2. 
Similarly from stage 2 to stage 3 , it is a sequence of deciding the optimal vertex at each stage.



