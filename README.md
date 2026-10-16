## vmescape
Some challenges and techniques for vmescape learning.

Os desafios são de escape de VM em dispositivos emulados do QEMU. Este repositório
guarda, para estudo, os arquivos de cada desafio, os scripts de build e os
exploits de referência. A execução deve ocorrer apenas no ambiente oficial do
respectivo CTF, não neste repositório.

### Desafios

| Diretório | Descrição | Writeup / referência |
|---|---|---|
| `babyqemu/` | Device `hitb` com DMA sem validação de endereço | `babyqemu/README.md` |
| `EC3/` | Use-after-free em heap (fastbin) dentro do guest | `EC3/README.md` |
| `strng/` | Device `STRNG` (Blizzard CTF 2017), acesso por MMIO e PMIO | `strng/README.md` |
| `xnuca/` | Device SSD (XNU CTF) | https://www.w0lfzhang.com/2018/12/05/xnuca-SSD-QEMU-escape/ |

### Estrutura

- `babyqemu/`: `edu.c` (device), `exp.c`, `auto.sh` (monta o rootfs), `babyqemu.tar.gz`, `flag`, `debug.txt`.
- `EC3/`: `src/` (fonte do QEMU modificado e Makefile), `EC3.tar.gz`, `exp.c`, `exp.py` (driver pwntools), `auto.sh`, `debug.txt`.
- `strng/`: `strng.c` (device), `exp.c`, `README.md` (setup do ambiente).
- `xnuca/`: `xnuca.zip`, `exp.c`, `exp-no-main-arena.c`, `auto.sh` (reempacota o rootfs), `flag`, `debug.txt`.

### Build

Os `auto.sh` de cada desafio montam o rootfs com `musl-gcc -static` e `cpio`
(formato `newc`). Eles não iniciam o QEMU nem executam nada.

### Aviso

Os arquivos `flag` e alguns comentários contêm valores de flag em texto puro.
Trate-os como material de estudo.
