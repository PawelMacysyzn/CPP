# Show all filenames with .exe extension                                            ☑
# Remove them and get status                                                        ☑
# Add option list of folders to be ignored                                          ☑
# Add add-on to remove another extension e.g. (.txt, .py)                           ☑
# Add option in command prompt for that                                             ☑
# Improve the code in cmd support(), reduce the number of if statements in main()   ☑


############### CODE #####################
import types
import os
import sys
import argparse


BLUE = "\033[34m"
GREEN = "\033[32m"
CYELLOW = '\033[93m'
RED = "\033[31m"
RESET = '\033[0m'


def cmd_support():
    '''
    # cmd support
    '''

    parser = argparse.ArgumentParser(description='Allows for cmd support')
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-f', '--find', dest='search_string',
                       type=str, help='Search string')
    group.add_argument('-r', '--remove', dest='remove_string',
                       type=str, help='Remove string')
    parser.add_argument('-w', '--where', dest='search_location',
                        type=str, help='Search location')
    parser.add_argument('-i', '--ignore', dest='ignored_folders',
                        type=str, nargs='+', help='Ignored folders')

    parser.set_defaults(search_string=None,
                        remove_string=None, ignored_folders=[])

    args = parser.parse_args()

    ### LOGIC ###

    if args.search_location is not None:
        # Option in cmd: py .\cleaner_exe.py --find .exe --where C:\Users\pmacyszyn_adm\Documents\C++\CPP\TEST --ignore 'folder 1'
        # or             py .\cleaner_exe.py --find .exe --where C:\Users\pmacyszyn_adm\Documents\C++\CPP\TEST
        if args.search_string is not None:
            show_searching_files(search_location=args.search_location,
                                 file_extension=args.search_string, ignored_folders=args.ignored_folders)

        # or             py .\cleaner_exe.py --remove .exe --where C:\Users\pmacyszyn_adm\Documents\C++\CPP\TEST --ignore 'folder 2'
        # or             py .\cleaner_exe.py --remove .exe --where C:\Users\pmacyszyn_adm\Documents\C++\CPP\TEST
        elif args.remove_string is not None:
            remove_all_files(search_location=args.search_location,
                             file_extension=args.remove_string, ignored_folders=args.ignored_folders)

    # Option in cmd: py .\cleaner_exe.py --find .exe
    # or             py .\cleaner_exe.py --remove .exe

    elif args.search_location is None:
        if args.search_string is not None:
            show_searching_files(
                file_extension=args.search_string, ignored_folders=args.ignored_folders)

        elif args.remove_string is not None:
            remove_all_files(search_location=os.getcwd(
            ), file_extension=args.remove_string, ignored_folders=args.ignored_folders)

        # Option in cmd: py .\cleaner_exe.py
        else:
            show_searching_files()
    # ToDo
    # Przeplatanie walidacji parametrów z uruchomieniem algorytmu   //              show_searching_files()     remove_all_files()



def walk_thru_files_by_walk(search_location: str, file_extension: str, ignored_folders: list) -> types.GeneratorType:
    '''
    # Walk thru files by walk
    * search_location (str) - specified path
    * file_extension (str) - searched phrase
    * ignored_folders (list) - list of folders to be ignored
    '''

    found_files = False

    for dir_name, subdirs, filenames in os.walk(search_location):

        # Remove ignored folders from subdirs list
        subdirs[:] = [d for d in subdirs if d not in ignored_folders]

        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName
                found_files = True

    if not found_files:
        print(f"{CYELLOW}No files found with the specified extension!{RESET}")


def show_searching_files(search_location: str = os.getcwd(), file_extension: str = '.exe', ignored_folders: list = []):
    '''
    # Shows all searched files
    * search_location (str) - specified path
    * file_extension (str) - searched phrase
    * ignored_folders (list) - list of folders to be ignored
    '''
    generator_files = walk_thru_files_by_walk(
        search_location, file_extension, ignored_folders)
    print("="*90)
    for (num, elem) in enumerate(generator_files, start=1):
        print(f"{num}. {BLUE}{elem}{RESET}")
    print("="*90)


def remove_file(file_path: str):
    '''
    # Remove file from path
    * file_path (str) - "path/to/file.txt"
    '''

    try:
        os.remove(file_path)
        print(
            f"{GREEN}File{RESET} {BLUE}{file_path}{RESET} {GREEN}has been successfully deleted.{RESET}")
    except FileNotFoundError:
        print(
            f"{CYELLOW}File {RESET}{BLUE}{file_path}{RESET} {CYELLOW}not found.{RESET}")
    except PermissionError:
        print(f"{CYELLOW}Permission denied for file{RESET} {BLUE}{file_path}{RESET}.")
    except OSError as e:
        print(
            f"{CYELLOW}Error occurred while deleting file {RESET} {BLUE}{file_path}{RESET}: \n{e}")


def remove_all_files(search_location: str, file_extension: str, ignored_folders: list = []):
    '''
    # Remove all files from path
    * search_location (str) - specified path
    * file_extension (str) - searched phrase
    * ignored_folders (list) - list of folders to be ignored
    '''

    confirmation = input(
        f"{CYELLOW}Are you sure you want to delete all files? (Yes/No): {RESET}")
    
    if confirmation.lower() == "yes":

        generator_files = walk_thru_files_by_walk(
            search_location, file_extension, ignored_folders)

        for (num, elem) in enumerate(generator_files, start=1):
            remove_file(elem)

        print("="*90)
        print(f"{GREEN}({num}){RESET} {CYELLOW}Number of files with the extension:{RESET} {RED}{file_extension}{RESET} {CYELLOW}removed{RESET}")
        print("="*90)
    else:
        print(f"{CYELLOW}Changes rejected{RESET}")
        return


def test():

    ######################################
    ################ TEST ################
    ######################################

    my_test_folder = r"C:\Users\pmacyszyn_adm\Documents\C++\CPP\TEST"
    file_extension = '.exe'
    ignored_folders = ["folder 2"]

    show_searching_files(my_test_folder, file_extension)
    # remove_all_files(my_test_folder, file_extension, ignored_folders)

    ######################################
    ################ END #################
    ######################################


def main():

    ######################################
    ############ CODE HERE ###############
    ######################################

    cmd_support()

    ######################################
    ################ END #################
    ######################################
    pass


if __name__ == "__main__":
    main()
