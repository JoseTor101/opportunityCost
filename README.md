# Coste de oportunidad

## Realizado por:

### Julián Mejia

### José Tordecilla


## Descripción:

As with most types of products, buying a new phone can be difficult. One of the main challenges
is that there are a lot of different aspects of the phone that you might care about, such as its price,
its performance, and how user-friendly the phone is. Typically, there will be no single phone that is
simultaneously the best at all of these things: the cheapest phone, the most powerful phone, and the
most user-friendly phone will likely be different phones.

Thus when buying a phone, you are forced to make some sacrifices by balancing the different aspects you care about against each other and choosing the phone that achieves the best compromise (where “best” of course depends on what your priorities happen to be). One way of measuring this sacrifice is
known as the opportunity cost, which (for the purposes of this problem) we define as follows. Suppose that you have bought a phone with price x, performance y, and user-friendliness z. For simplicity, we assume that these three values are measured on a comparable numeric scale where higher
is better. If there are n available phones, and the values (xi, yi, zi) represent the (price, performance,user-friendliness) of the i-th phone, then the opportunity cost of your phone is defined as

max 1≤i≤n (max(xi − x, 0) + max(yi − y, 0) + max(zi − z, 0)).

Write a program that, given the list of available phones, finds a phone with the minimum opportunity cost.

### Input:

The first line of input contains an integer n (2 ≤ n ≤ 200 000), the number of phones considered.
Following that are n lines. The i-th of these lines contains three integers xi, yi, and zi, where xi is the price, yi is the performance, and zi is the user-friendliness of the i-th phone (1 ≤ xi, yi, zi ≤ 10^9).

### Output

Output a single line containing two integers: the smallest possible opportunity cost and an integer between 1 and n indicating the phone achieving that opportunity cost. If there are multiple such phones,
output the one with the smallest index.


## Versión de Python: 3.10.4
