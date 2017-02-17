/*
Joseph Choi
Professor Aljamal
11/21/2013
Dynamic Linked List Queues
*/

#include <iostream>

using namespace std;

struct data
{
       char name[50];
       int id;
       data *next;
       data *front;
       data *back;
};

data info;//initialize structure

//prototypes
void menu();
void create();
void dequeue();
void enqueue();
void purgeQueue();
void display();
int empty();
void checkIfEmpty();


int main()
{
    create();
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
             
     cout<<"Select an option\n";
     
     cout<<"1 : Empty\n";
     cout<<"2 : Purge Queue\n";
     cout<<"3 : Enque\n";
     cout<<"4 : Deque\n";
     cout<<"5 : Display\n";
     cin>>answer;
     
     switch(answer)
     {
         case 1: checkIfEmpty();
         break;
         case 2: purgeQueue();
         break;
         case 3: enqueue();
         break;
         case 4: dequeue();
         break;
         case 5: display();
         break;
     }
     
     }while(loop != 'y');
     
}
void create()
{
     info.front = info.back = NULL;
}
void checkIfEmpty()
{
     if(empty())
     {
          cout<<"\nQueue is currently empty\n";
     }
     else
     {
         cout<<"\nQueue is currently NOT empty\n";
         cout<<"\n\nTHE QUEUE HAS THE FOLLOWING :\n";
         display();
     }
}
int empty()
{
    return(!info.front);
    //if empty, info.front == 0, not 0 is 1, 1 is true, so if empty, return true
}

void enqueue()
{
     data * newNode;
     newNode = new data;
     
     //populate record
     cout<<"\nEnter name\n";
     cin>>newNode -> name;
     cout<<"\nEnter ID Number\n";
     cin>>newNode -> id;
     
     newNode -> next = NULL;
     
     if(info.front == NULL)
     {
          info.front = newNode;
     }
     else
     {
          info.back -> next = newNode;
     }
     info.back = newNode;
}
void dequeue()
{
     if(info.front == NULL)
     {
          info.back = NULL;//nothing to remove
     }
     else
     {
         info.front = info.front -> next;
     }
}
void purgeQueue()
{
     info.front = info.back = NULL;
}
void display()
{
     data *temp;
     temp = info.front;
     if(temp == NULL)
     {
             cout<<"\nQueue is empty\n";
     }
     else
     {
         while(temp != NULL)
         {
               cout<<"\nName : "<<temp -> name<<"\n";
               cout<<"ID Number : "<<temp -> id<<"\n\n";
               
               temp = temp -> next;
         }
     }
     
     
}
