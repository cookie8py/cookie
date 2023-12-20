# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
for number in range(1, 4):
    root = number ** 0.5
    mo = number * 2
    print('Root', end=' ')
    print_hi(root)
    print('number', end=' ')
    print_hi(number)
    print('double', end=' ')
    print_hi(mo)
    print('-------------')
