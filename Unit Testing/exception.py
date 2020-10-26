class NotIntegerError(Exception):  # a developer defined an exceptioin.
    pass


class DivisorError(Exception):  # a developer defined an exceptioin.
    pass


def test_divide():
    integers = [10, 20, 30]
    result = -1

    try:
        idx, num = input("type 2 numbers: ").split()
        idx = int(idx)
        num = int(num)

        if num < 0:
            raise DivisorError('divisor is less than 0.')

        # if False == isinstance(idx, int):
        #     raise NotIntegerError("typed none integer for idx")

        # if False == isinstance(num, int):
        #     raise NotIntegerError("typed none integer for num")

        result = integers[idx] / num

    except ZeroDivisionError as e:
        print(e)

    except DivisorError as e:
        print(e)

    except IndexError as e:
        print(e)

    except Exception as e:
        print(e)
        raise RuntimeError("exception occurred in test_divide(): ", e)

    else:
        print("result = ", result)

    finally:
        return result


quotient = test_divide()
print(quotient)
