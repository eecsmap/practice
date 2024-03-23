bus_add_device(bus_t *bus, device_t *device)
{
    if (bus->devices == NULL)
    {
        bus->devices = device;
    }
    else
    {
        device_t *current = bus->devices;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = device;
    }
}