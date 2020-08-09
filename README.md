## Install kin settings

contains arm-none-eabi-gcc profiles and os=Bare in settings.yml.

```sh
# Create the zip file, install it then delete it
cd kin-conan-config \
  && zip -r ../kin-conan-config.zip . \
  && cd .. \
  && conan config install kin-conan-config.zip \
  && rm kin-conan-config.zip
```

## Build and run

```sh
# Build then start qemu
conan create hello kin/testing \
    -pr arm-none-eabi-gcc \
    -pr cortex-m3 \
    && conan create lm3s6965-hal kin/testing \
      -pr arm-none-eabi-gcc \
      -pr cortex-m3 \
    && rm -rf app/build \
    && conan install app \
        -if app/build \
        -pr arm-none-eabi-gcc \
        -pr cortex-m3 \
        --build=missing \
        -s build_type=Debug \
    && conan build app -bf app/build \
    && qemu-system-arm \
        -cpu cortex-m3 \
        -machine lm3s6965evb \
        -nographic \
        -monitor null \
        -serial stdio \
        # -gdb tcp::3333 \
        # -S \
        -kernel app/build/App
```

# Debug

```sh
arm-none-eabi-gdb app/build/App -ex "target extended-remote :3333"
```
