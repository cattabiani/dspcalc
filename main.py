from dspcalc import obj


def main():
    lib = obj.DspLibrary()
    print(lib.calc_base_components("electric motor", 6))


if __name__ == '__main__':
    main()
