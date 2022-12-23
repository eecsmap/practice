#include <cstdio>
#include <fstream>

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    std::ifstream file(argv[1]);
    if (!file.is_open())
    {
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }
    char buf[BUFSIZ] = new char[BUFSIZ];
    file.read(buf, BUFSIZ);
}
