# Python-Excersices-WorkBook
This repo contains exercises about python.

# Exercise Number 9.
## Compound Interest
In this exercise I use an equation that makes easier to calculate the savings.  Here I show the steps to understand the formula.

**Author:** Alejandro Jose Meza Ramos  
**Date:** September 2025

The equation about compound interest can be deduced as follows.  

Let \(M\) be the initial amount of money deposited. This is the initial amount we want to save. Let \(r\) be the annual interest rate (in decimal form). With these parameters, we can calculate the amount earned in the first year: 

$$
\text{Income First Year} = r \cdot M
$$

And the total after the first year is: 

$$
T_1 = M + rM = M(1+r)
$$

In the next year, the income is determined by:

$$
\text{Income Second Year} = T_1 \cdot r = (M + rM) \cdot r = rM(1+r)
$$

So the total after the second year becomes:

$$
T_2 = \text{Income Second Year} + T_1 = rM(1+r) + M(1+r) = M(1+r)^2
$$

Observing the pattern, we can generalize for \(n\) years to get the final equation used to solve problem number 9:

$$
A(n) = M(1+r)^n
$$

We can note that the total amount of money grows **exponentially** with the number of years, and also depends proportionally on the initial amount \(M\).
