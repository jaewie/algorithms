#include "bitwise_manipulations.h"
#include <string.h>
#include <stdio.h>


char turn_rightmost_1bit_off(char x) {
    // 0101 0110 -> 0101 0100
    return x & (x - 1);
}

char turn_rightmost_0bit_on(char x) {
    // 0101 0101 -> 0101 0111
    return x | (x + 1);
}

char turn_trailing_1s_off(char x) {
    // 0101 0111 -> 0101 0000
    return x & (x + 1);
}

char turn_trailing_0s_on(char x) {
    // 0101 1000 -> 0101 1111
    return x | (x - 1);
}

char take_single_rightmost_0(char x) {
    // 0101 0111 -> 0000 1000
    return ~x & (x + 1);
}

char all_1s_except_rightmost_1(char x) {
    // 1100 1000 -> 1111 0111
    return ~x | (x - 1);
}

unsigned snoob(unsigned x) {
    // Return next bigger than x using same # of 1 bits
    // xxx0 1111 0000 -> xxx1 0000 0111
    unsigned smallest, ripple, ones;

    smallest = x & (~x + 1);
    ripple = x + smallest;
    ones = x ^ ripple;

    return ripple | ((ones / smallest) >> 2);
}

unsigned xor(unsigned a, unsigned b) {
    return (a | b) - (a & b);
}

unsigned bitwise_and(unsigned a, unsigned b) {
    return (~a | b) - ~a;
}

unsigned bitwise_or(unsigned a, unsigned b) {
    return (a & ~b) + b;
}

int abs(int x) {
    int y = x >> 31;

    // Other solutions:
    // (x + y) ^ y
    // x - (2*x & y)
    return (x ^ y) - y;
}

int sign(int x) {
    // -1 if x < 0
    // 0  if x = 0
    // 1  if x > 0
    unsigned x_unsigned = x;

    // Other solutions:
    // (x > 0) - (x < 0)
    // -(x_unsigned >> 31) | (x_unsigned >> 31)
    return (x >> 31) | (-x_unsigned >> 31);
}

unsigned avg_floor(unsigned a, unsigned b) {
    // floor((a + b) / 2) without overflowing

    // Works by taking sum of averages of
    // - bits in a and b that intersect
    // - bits in a and b that don't intersect
    return (a & b) + ((a ^ b) >> 1);
}


unsigned avg_ceil(unsigned a, unsigned b) {
    // ceil((a + b) / 2) without overflowing
    //
    // Let x, y be bits in a, b resp. that are intersecting.
    // and j, k be bits in a, b resp. that are not intersecting.
    //
    // (x + y) is even because they are pairs of bits that are intersecting.
    //
    // (a | b) = (x + y) / 2 + j + k
    // (a ^ b) >> 1 = floor((j + k) / 2)
    //
    // (a | b) - ((a ^ b) >> 1) = (x + y) / 2 + j + k - floor((j + k) / 2)
    //                          = (x + y) / 2 + ceil((j + k) / 2)
    //                          = ceil((x + y + j + k) / 2)
    //                          = ceil((a + b) / 2)
    return (a | b) - ((a ^ b) >> 1);
}

int equal_to_zero(int x) {
    // Other solutions:
    // (abs(x) - 1) >> 31
    // abs(x + 0x80000000) >> 31
    // (nlz(x) << 26) >> 31 where x is unsigned
    // -(nlz(x) >> 5) >> 31
    // (~x & (x - 31)) >> 31
    return ((unsigned) ~(x | -x)) >> 31;
}

int not_equal_to_zero(int x) {
    // Other solutions:
    // nabs(x) >> 31
    // (nlz(x) - 32) >> 31
    // ((x >> 1) - x) >> 31 where x is unsigned
    return ((unsigned) (x | -x)) >> 31;
}

int less_than_zero(int x) {
    return ((unsigned) x) >> 31;
}

int less_than_or_equal_to_zero(int x) {
    // Other solutions:
    // (x | ~-x) >> 31
    // (x ^ nabs(x)) >> 31
    return ((unsigned) (x | (x - 1))) >> 31;
}

int greater_than_zero(int x) {
    // Other solutions:
    // (x ^ nabs(x)) >> 31
    // (-x & ~x) >> 31
    return ((unsigned) ((x >> 1) - x)) >> 31;
}

int greater_than_or_equal_to_zero(int x) {
    return ((unsigned) ~x) >> 31;
}

int sum_overflows(int x, int y, int c) {
    // z is 0x8000000 if x and y have same signs, otherwsie 0
    //
    // If different signs, then no overflow.
    // Otherwise:
    // Case 1: x >= 0, and y >= 0
    // Then returns 1 if (x - 2^31 + y + c) >= 0
    //                            x + y + c >= 2^31
    // and 0 otherwise
    //
    // Case 2: x < 0 and y < 0
    // Then returns 1 if (x + 2^31 + y + c) < 0
    //                            x + y + c < -2^31
    // and 0 otherwise
    int z = ~(x ^ y) & 0x8000000;
    return z & ~(((x ^ z) + y + c) ^ y);
}

int division_overflows(int x, int y) {
    // 0x80000000 is 1 << 31
    return (y == 0) | (x == 0x80000000 & y == -1);
}

int count_bits(int x) {
    int total = 0;
    while (x) {
        x &= x - 1;
        total++;
    }
    return total;
}

void swap(int *x, int *y) {
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

int branch(int a, int b, int cond) {
    // cond is 0 or 1.

    // if (cond) {
    //     return a;
    // } else {
    //     return b;
    // }

    return (-cond & a) | ((-1 + cond) & b);
}

int is_odd(int x) {
    return x & 1;
}

int is_even(int x) {
    return 1 - (x & 1);
}

int same_sign(int x, int y) {
    return ((unsigned) ~(x ^ y)) >> 31;
}

int rotate_left(int x, int n) {
    return (x << n) | (((unsigned) x) >> (32 - n));
}

int rotate_right(int x, int n) {
    return (((unsigned) x) >> n) | (x << (32 - n));
}
