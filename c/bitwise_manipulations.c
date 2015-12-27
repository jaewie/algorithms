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
