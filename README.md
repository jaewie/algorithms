Algorithms and Data Structures
==========

[![Build Status](https://travis-ci.org/jaewie/algorithms.svg?branch=master)](https://travis-ci.org/jaewie/algorithms)
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](/LICENSE)

**Implementations of various algorithms and data structures.**

**Table of Contents**

- [Implementations](#collection)
   - [Collection](#collection)
   - [Combinatorics](#combinatorics)
   - [Computational geometry](#computational-geometry)
   - [Concurrency](#concurrency)
   - [Cryptographic](#cryptographic)
   - [Data mining](#data-mining)
   - [Graphs](#graphs)
   - [Interpreter](#interpreter)
   - [Intractable](#intractable)
   - [Linked lists](#linked-lists)
   - [Machine learning](#machine-learning)
   - [Numeric](#numeric)
   - [Probabilistic](#probabilistic)
   - [Sequences](#sequences)
   - [Simulation](#simulation)
   - [Sort](#sort)
   - [Strings](#strings)
- [For future](#for-future)

### Collection
- [Bit array](python/collection/bit_array.py)
- [Deque](python/collection/deque.py)
- [Dynamic array](python/collection/dynamic_array.py)
- [Priority queue](python/collection/priority_queue.py)
- [Queue](python/collection/queue.py)
- [Set](python/collection/set.py)
- [Stack](python/collection/stack.py)

### Combinatorics
- [Biased coin with fair coin](python/maths/combinatorics.py)
- [Fair coin with biased coin](python/maths/combinatorics.py)
- [Fisher-Yate's algorithm](python/maths/combinatorics.py)
- [Reservoir sampling](python/maths/combinatorics.py)

### Computational Geometry
- [Closest pair algorithm](python/computational_geometry/closest_pair.py)
- [Sweep line algorithm](python/computational_geometry/sweep_line.py)

### Concurrency
- [Bakery algorithm](python/concurrency/bakery_algorithm.py)
- [Barrier](python/concurrency/synchronization.py)
- [Dining philosophers problem](python/concurrency/dining_philosophers.py)
- [Dining savages problem](python/concurrency/dining_savages.py)
- [Light switch](python/concurrency/synchronization.py)
- [Producers–consumers problem](python/concurrency/producers_consumers.py)
- [Readers–writers problem (with writer priority)](python/concurrency/readers_writers.py)

### Cryptographic
- [Adler32](python/checksums/adler32.py)
- [Caesar cipher](python/crypto/ciphers.py)
- [Luhn](python/checksums/luhn.py)
- [One time pad](python/crypto/ciphers.py)
- [Vigenere cipher](python/crypto/ciphers.py)

### Data mining
- [Apriori algorithm](python/data_mining/apriori.py)

### Graphs
- [A*](python/graphs/graph_algos.py)
- [AVL Tree](python/graphs/avl.py)
- [BFS and DFS](python/graphs/graph_algos.py)
- [Binary search tree](python/graphs/bst.py)
- [Deepening depth first search](python/graphs/graph_algos.py)
- [Depth limited search](python/graphs/graph_algos.py)
- [Dijkstra's algorithm](python/graphs/graph_algos.py)
- [Disjoint set](python/graphs/disjoint_set.py)
- [Huffman encoding](python/graphs/huffman_encoding.py)
- [Inorder traversal](python/graphs/graph_algos.py)
- [Interval tree](python/graphs/interval_tree.py)
- [Kruskal's algorithm](python/graphs/graph_algos.py)
- [Merkle tree](python/graphs/merkle_tree.py)
- [Prim's algorithm](python/graphs/graph_algos.py)
- [Segment tree](python/graphs/segment_tree.py)
- [Skew heap](python/graphs/skew_heap.py)
- [Topological sort](python/graphs/graph_algos.py)
- [Trie](python/graphs/trie.py)

### Interpreter
- [Shunting Yard algorithm](python/interpreter/rpn.py)

### Intractable
- [Simulated annealing (Traveling Salesman Problem)](python/intractable/metaheuristics.py)

### Linked lists
- [Floyd's cycle-finding algorithm](python/linked/linked_list.py)
- [Xor linked list](python/linked/xor_linked_list.py)

### Machine learning
- [K nearest neighbor](python/machine_learning/knn.py)
- [Linear regression](python/machine_learning/linear_regression.py)

### Numeric
- [Euclid's algorithm](python/maths/numeric.py)
- [Fast exponentiation](python/maths/numeric.py)
- [Fermat's primality test](python/maths/numeric.py)
- [Kahan summation algorithm](python/maths/numeric.py)
- [Karatsuba algorithm](python/maths/numeric.py)
- [Linear congruential generator](python/maths/numeric.py)
- [Newton's method](python/maths/numeric.py)
- [Russian Peasant Multiplication algorithm](python/maths/numeric.py)
- [Sieve's primes](python/maths/numeric.py)

### Probabilistic
- [Bloom filter](python/probabilistic/bloom_filter.py)

### Sequences
- [Binary search](python/sequences/arrays.py)
- [Dutch national flag](python/sequences/arrays.py)
- [Kadane's algorithm](python/sequences/arrays.py)
- [Median of medians](python/sequences/arrays.py)
- [Quickselect](python/sequences/arrays.py)

### Simulation
- [Monte Carlo Method (for finding PI)](python/maths/numeric.py)

### Sort
- [Bubble sort](python/sequences/sort.py)
- [Bucket sort](python/sequences/sort.py)
- [Counting sort](python/sequences/sort.py)
- [Heap sort](python/sequences/sort.py)
- [Insertion sort](python/sequences/sort.py)
- [Merge sort](python/sequences/sort.py)
- [Quick sort](python/sequences/sort.py)
- [Radix sort](python/sequences/sort.py)
- [Selection sort](python/sequences/sort.py)
- [Stack sort](python/sequences/sort.py)

### Strings
- [Knuth-Morris-Pratt](python/strings/match.py)
- [Rabin-Karp algorithm](python/strings/match.py)

### For future
- [ ] Alpha-beta pruning
- [ ] Minimax
- [ ] PageRank
- [ ] Q-Learning
- [ ] Quadtree
- [ ] Spell checker
- [x] Apriori algorithm
- [x] Huffman encoding
- [x] Simulated annealing
