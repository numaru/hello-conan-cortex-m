#include <hello/hello.h>

#include <stdio.h>

#ifndef GREETINGS
#define GREETINGS "Hello World!"
#endif

void say_hello(void) { printf(GREETINGS "\n"); }
