#include <stddef.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <stdio.h>

void dump(uint8_t *buff, size_t buff_size)
{
    size_t i;
    for (i = 0; i < buff_size; i++)
    {
        printf("%02x", buff[i]);
        if (i % 16 == 15)
            printf("\n");
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <file>\n", argv[0]);
        return 1;
    }
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1)
    {
        perror("open");
        return 1;
    }
    struct stat st;
    if (fstat(fd, &st) == -1)
    {
        perror("fstat");
        return 1;
    }
    size_t size = st.st_size;
    if (st.st_size < 0)
    {
        printf("st.st_size is negative\n");
        return 1;
    }
    uint8_t *p = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0);
    if (p == MAP_FAILED)
    {
        perror("mmap");
        return 1;
    }

    printf("program size: %zu\n", size);

    mem_t mem;
    mem_init(&mem, p, size);
    //dump(p, size);

    int result = munmap(p, size);
    if (result == -1)
    {
        perror("munmap");
        return 1;
    }

    return 0;
}
