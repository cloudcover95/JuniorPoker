/* Fisher-Yates. Compile: cc -O2 -fPIC -shared -o libjp_shuffle.so shuffle.c */
#include <stdint.h>

void jp_shuffle(uint16_t *a, int n, uint32_t seed) {
    uint32_t s = seed ? seed : 1u;
    for (int i = n - 1; i > 0; --i) {
        s = s * 1664525u + 1013904223u;
        int j = (int)(s % (uint32_t)(i + 1));
        uint16_t t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
