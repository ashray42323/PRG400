#include <ctype.h>
#include <stddef.h>

void to_upper(const char *input, char *output, size_t out_size) {
    size_t i;
    for (i = 0; input[i] != '\0' && i + 1 < out_size; ++i) {
        output[i] = (char) toupper((unsigned char) input[i]);
    }
    output[i] = '\0';
}
