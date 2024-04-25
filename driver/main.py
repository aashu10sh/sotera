import ada as sensor

import time
import serial

uart = serial.Serial("/dev/ttyACM0", baudrate=57600, timeout=1)

finger = sensor.Adafruit_Fingerprint(uart)

##################################################


def get_fingerprint():
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != sensor.OK:
        pass
    print("Templating...")
    if finger.image_2_tz(1) != sensor.OK:
        return False
    print("Searching...")
    if finger.finger_search() != sensor.OK:
        return False
    return True


def get_fingerprint_2():
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != sensor.OK:
        pass
    print("Templating...")
    if finger.image_2_tz(1) != sensor.OK:
        return 0
    print("Searching...")
    i = finger.finger_fast_search()
    return i


# pylint: disable=too-many-branches
def get_fingerprint_detail():
    """Get a finger print image, template it, and see if it matches!
    This time, print out each error instead of just returning on failure"""
    print("Getting image...", end="")
    i = finger.get_image()
    if i == sensor.OK:
        print("Image taken")
    else:
        if i == sensor.NOFINGER:
            print("No finger detected")
        elif i == sensor.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return 0

    print("Templating...", end="")
    i = finger.image_2_tz(1)
    if i == sensor.OK:
        print("Templated")
    else:
        if i == sensor.IMAGEMESS:
            print("Image too messy")
        elif i == sensor.FEATUREFAIL:
            print("Could not identify features")
        elif i == sensor.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return 0

    print("Searching...", end="")
    i = finger.finger_fast_search()
    # pylint: disable=no-else-return
    # This block needs to be refactored when it can be tested.
    if i == sensor.OK:
        print("Found fingerprint!")
        return i
    else:
        if i == sensor.NOTFOUND:
            print("No match found")
            return 0
        else:
            print(i)
            print("Other error")
        return 0


def search_fingerprint() -> int | None:
    # i = get_fingerprint_2()
    # i = get_fingerprint_detail()
    get_fingerprint()
    return finger.finger_id
    i = 1
    print("The I is ", i)
    return i if i else None


# pylint: disable=too-many-statements
def enroll_finger(location: int):
    """Take a 2 finger images and template it, then store in 'location'"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="")
        else:
            print("Place same finger again...", end="")

        while True:
            i = finger.get_image()
            if i == sensor.OK:
                print("Image taken")
                break
            if i == sensor.NOFINGER:
                print(".", end="")
            elif i == sensor.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...", end="")
        i = finger.image_2_tz(fingerimg)
        if i == sensor.OK:
            print("Templated")
        else:
            if i == sensor.IMAGEMESS:
                print("Image too messy")
            elif i == sensor.FEATUREFAIL:
                print("Could not identify features")
            elif i == sensor.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while i != sensor.NOFINGER:
                i = finger.get_image()

    print("Creating model...", end="")
    i = finger.create_model()
    if i == sensor.OK:
        print("Created")
    else:
        if i == sensor.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return False

    print("Storing model #%d..." % location, end="")
    i = finger.store_model(location)
    if i == sensor.OK:
        print("Stored")
    else:
        if i == sensor.BADLOCATION:
            print("Bad storage location")
        elif i == sensor.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return False

    return True


def get_num():
    """Use input() to get a valid number from 1 to 127. Retry till success!"""
    i = 0
    while (i > 127) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-127: "))
        except ValueError:
            pass
    return i


# while True:
#     print("----------------")
#     if finger.read_templates() != sensor.OK:
#         raise RuntimeError("Failed to read templates")
#     # print("Fingerprint templates:", finger.templates)
#     for template in finger.templates:
#         print(template)
#     print("e) enroll print")
#     print("f) find print")
#     print("d) delete print")
#     print("----------------")
#     c = input("> ")

#     if c == "e":
#         enroll_finger(get_num())
#     if c == "f":
#         if get_fingerprint():
#             print("Detected #", finger.finger_id, "with confidence", finger.confidence)
#         else:
#             print("Finger not found")
#     if c == "d":
#         if finger.delete_model(get_num()) == sensor.OK:
#             print("Deleted!")
#         else:
#             print("Failed to delete")

if __name__ == "__main__":
    print("Welcome to Sotera!")
    # finger.soft_reset()
    outp = finger.empty_library()
    print(outp)
    if outp != sensor.OK:
        print("Failed to remove Library Stuff")
    print("Soft Reset Done!")
    # get_user_choice()
    # enroll_finger(1)
    # print(finger.read_sysparam())
    # print(finger.__dict__)
    # enroll_finger(2)
    # finger.read_templates()
    # f_data = finger.get_fpdata()
    # print(f_data)
    # got = get_fingerprint()
    # if got:
    #     print("Detected #", finger.finger_id, "with confidence", finger.confidence)
