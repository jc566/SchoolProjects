/*
Joseph Choi
Professor Aljamal
11/21/2013

Dynamic Linked List STACKS
*/
#include <iostream>

using namespace std;

struct data
{
       char name[50];
       int id;
       data * next;
       data * top;
       
};
data info;//intialize structure

void menu();
int empty();
void checkIfEmpty();
void createStack();
void pushToStack();
void display();
void popStack();
void purgeStack();


int main()
{
    createStack();
    
    menu();
    
    //end of program
    system("pause");
    return 0;
}
void menu()
{
     int answer;
     char loop;
     
     
     do
     {
     cout<<"Select from the menu\n";
     cout<<"\n1 : Push to Stack";
     cout<<"\n2 : Pop top element";
     cout<<"\n3 : Display All";
     cout<<"\n4 : Purge Stack";
     cout<<"\n5 : Check if Stack is Empty\n";
     
     cin>>answer;
     
     switch(answer)
     {
          case 1: pushToStack();
          break;
          case 2: popStack();
          break;
          case 3: display();
          break;
          case 4: purgeStack();
          break;
          case 5: checkIfEmpty();
          break;
     }
     cout<<"\nWould you like to end program?\n";
     cin>>loop;
     }while(loop != 'y');
}
void createStack()
{
     info.top = NULL;
}
void pushToStack()
{
     data * newNode;
     newNode = new data;
     
     //populate record
     cout<<"\nEnter the name\n";
     cin>>newNode -> name;
     cout<<"\nEnter the ID number\n";
     cin>>newNode -> id;
     
     //this new node is pointing to NULL, basically at the end
     newNode -> next = NULL;
     
     /*****************************************************************************************
     if its the first element, or stack is empty, then this newNode is at the top of stack now
     *****************************************************************************************/
     if(info.top == NULL)
     {
        info.top = newNode;
        newNode -> next = NULL;
     }
     /*************************************************************
     otherwise this newNode is pointing to the current top element,
     and then this newnode becomes the new top element
     ***************************************************************/
     else
     {
         newNode -> next = info.top;
         info.top = newNode;
     }
     
}
int empty()
{
    return(info.top == NULL);
}
void checkIfEmpty()
{
    if(empty())
    {
        cout<<"\nStack is currently empty\n";      
    }
    else
    {
        cout<<"\nStack is not empty\n";
        cout<<"\n\nSTACK CURRENTLY HAS THE FOLLOWING :\n";
        display();
    }
}
void display()
{
     data * temp;
     temp = info.top;
     
     //if Stack is currently empty
     if(temp == NULL)
     {
             cout<<"\n\nStack is currently empty\n";
     }
     //while Stack is NOT empty
     else
     {
         while(temp != NULL)
         {
                    
              cout<<"\nName : "<<temp -> name<<"\n";
              cout<<"ID Number : "<<temp -> id<<"\n";
              temp = temp -> next;
         }
     }
}
void popStack()
{
      if(info.top == NULL)
     {
        cout<<"\nStack is currently empty\n";
     }
     else
     {
     data * temp;
     temp = info.top;
     info.top = info.top -> next;
     delete temp;
     }
}
void purgeStack()
{
     while(!empty())
     {
          popStack();
     }
}
