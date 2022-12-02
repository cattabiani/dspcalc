from dspcalc import obj

#A main
def main():
    lib = obj.DspLibrary()
    print(lib.calc_base_components("plasma exciter", 3))


if __name__ == '__main__':
    main()
