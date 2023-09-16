#include<iostream>
using namespace std;
class Billing
{
    private:
    int food_choice;
    int food_quantity;
    char food_order;
    int pizza_price;
    int burger_price;
    int dhosa_price;
    int idli_price;
    int food_amount;
    int total_amount;

    int pizza;
    int burger;
    int dhosa;
    int idli;

    
    public:
    Billing()   //default constructor
    {   pizza_price=180;
        burger_price=100;
        dhosa_price=120;
        idli_price=50;

        food_choice=0;  
        food_order=0;
        food_quantity=0;
        total_amount=0;

        pizza=1;
        burger=2;
        dhosa=4;
        idli=3;
    }
    void Menu();
    void Calculation();
    void order();
};
void Billing :: Menu()
{
    {
        cout<<"Menu"<<endl;
        cout<<"1.pizza          price:180rs/pcs"<<endl;
        cout<<"2.Burger         price:100rs/pcs"<<endl;
        cout<<"3.Idli           price:120rs/pcs"<<endl;
        cout<<"4.Dhosa          price:50rs/pcs"<<endl;
     }
}
void Billing :: Calculation()
{
     {
        if(food_choice==1)
        {
                food_amount= food_quantity*pizza_price;
        }
        else if(food_choice==2)
        {
                food_amount= food_quantity *burger_price;
        }
        else if(food_choice==3)
        {
                 food_amount= food_quantity *idli_price;
        }
        else
        {
                food_amount=food_quantity*dhosa_price;

        }
        
    }
}

void Billing::order()
{
     {
        do
        {
        food_amount=0;
        Menu();
        cout<<"Enter your choice:";
        cin>>food_choice;

        if(food_choice==1)
        {
              cout<<"You have selected: Pizza"<<endl;
        }
        else if(food_choice==2)
        {
            cout<<"You have selected: Burger"<<endl;
        }
         else if(food_choice==3)
        {
            cout<<"You have selected: Idli"<<endl;
        }
        else
        {
            cout<<"You have selected: Dhosa"<<endl;
        }

        cout<<"Enter the quantity:";
        cin>>food_quantity;
        Calculation();
        cout<<"Amount is: "<<food_amount;
        cout<<endl<<"Do you Want to order more? PRESS Y OR N";
        cin>>food_order;
        total_amount=total_amount+food_amount;

        }while(food_order=='Y' ||food_order=='y');

        cout<<"Total order is: "<<total_amount;
    }
}

int main()
{
    Billing Abhishek;
    Abhishek.order();
}