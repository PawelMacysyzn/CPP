#include <iostream>
#include <windows.h>
#include <string>
#include <sstream>

using namespace std;
int cells[6];
int dimension;

//-----------------------------
void view_stack()
{
    system("CLS");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 14);

    cout << endl;
    cout << "----------------" << endl;
    cout << "STACK CONTENT:" << endl;
    cout << "----------------" << endl;

    for (int i = dimension; i >= 1; i--)

    {
        cout << cells[i] << endl;
    }

    if (dimension == 0)
        cout << "pusty" << endl;

    cout << "----------------" << endl
         << endl;

    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 15);
}

//-----------------------------
void push()
{
    if (dimension >= 5)

    {
        cout << "Stack full!";
        Sleep(1000);
    }
    else
    {
        cout << endl
             << "PUSH (how many to put on the stack): ";

        dimension = dimension + 1;
        cin >> cells[dimension];
    }
}

//-----------------------------
void pop()
{
    if (dimension >= 1)

    {
        cout << endl
             << "POP - number will be removed from the stack: " << cells[dimension];
        Sleep(2000);

        dimension = dimension - 1;
    }
    else
    {
        cout << "ChoiEmpty stackce!";
        Sleep(1000);
    }
}
//-----------------------------
void size()
{
    cout << endl
         << "Liczba elementow na stosie: " << dimension;
    Sleep(2000);
}
//-----------------------------
void empty()
{

    if (dimension == 0)
        cout << endl
             << "EMPTY (ChoiEmpty stackce?) -> TRUE";
    else
        cout << endl
             << "EMPTY (ChoiEmpty stackce?) -> FALSE";
    Sleep(2000);
}

//-----------------------------

int main()
{

    string mystr;
    int choice;
    dimension = 0;

    do

    {
        view_stack();

        cout << "STACK MAIN MENU:" << endl;
        cout << "------------------------------------------" << endl;
        cout << "1. PUSH (adds an item to the top of the stack) " << endl;
        cout << "2. POP (removes an item from the top of the stack) " << endl;
        cout << "3. SIZE (how many items on the stack) " << endl;
        cout << "4. EMPTY (is the stack empty?) " << endl;
        cout << "5. Program End " << endl;
        cout << "------------------------------------------" << endl;

        cout << "Choice: ";
        getline (cin, mystr);
        stringstream(mystr) >> choice;

        switch (choice)

        {
        case 1:
            push();
            break;

        case 2:
            pop();
            break;

        case 3:
            size();
            break;

        case 4:
            empty();
            break;
        }

    } while (choice != 5);

    return 0;
}