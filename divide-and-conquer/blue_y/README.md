# hops

## Question
![question](./question.png)

## Explanation
This algorithm here is a variation of the Merge Sort algorithm. In the merge step, we are first adding routes from every planet in left subarray to the first planet of the right subarray, i.e., to (1 + mid) position. Then, we add routes from planet at (1 + mid) position to every other planet of right subarray. So, in every merge step, we would get route segments connecting every planet in both left and right subarrays completely by a maximum of 2 route segments. Thus, by using the divide-and-conquer approach, we make two recursive calls for n/2 planets (indicating each half of the main planets array), we get n route segments in each merge step. Thus, recurrence relation for number of route segments will be: 
T(n) = 2T(n/2) + n.
Solving this using Master’s theorem case 2, where a = 2, b = 2, f(n) = Ω(n $log_2$ 2) = n, we get:
T(n) = Θ(n log n)

## Runtime
O(n log n)

