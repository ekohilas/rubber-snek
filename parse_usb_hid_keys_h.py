with open("usb_hid_keys.h", "r") as f:
    for line in f:
        items = line.split()
        if line.startswith("#define") and len(items) >= 3:
            _, key, value, *_ = items
            print('{}: {},'.format(key.split("_")[-1], hex(int(value, 16))))
