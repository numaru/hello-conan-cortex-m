#include <embedded-hal/console.h>
#include <hello/hello.h>

#include <stdbool.h>

void init(void) {
  say_hello();
  console_write_string("hello\n");
}

void step(void) {}

int main(void) {
  init();
  while (true) {
    step();
  }
  return 0;
}
