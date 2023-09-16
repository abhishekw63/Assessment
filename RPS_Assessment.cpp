#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

class RPS
 {
private:
    string player_name;
    int player_choice;
    int computer_choice;
    int player_score;
    int computer_score;
    int round_no;

public:
    RPS()
     {
        player_choice = 0;
        computer_choice = 0;
        player_score = 0;
        computer_score = 0;
        round_no = 0;
    }

    void DisplayMenu() 
    {
        cout << "Menu" << endl;
        cout << "1. Rock" << endl;
        cout << "2. Paper" << endl;
        cout << "3. Scissors" << endl;
    }

    int computer()
     {
        return (rand() % 3) + 1;
    }

    void play() 
    {
        cout << "Welcome to the Game of ROCK, PAPER, AND SCISSORS" << endl;
        cout << "----------------------------------------------" << endl;
        cout << "Enter the player's name: ";
        cin >> player_name;
        cout << "Enter the number of rounds you want to play: ";
        cin >> round_no;

        if (round_no > 0)
         {
            for (int i = 1; i <= round_no; i++) 
            {
                cout << "************************" << endl;
                cout << "Round No." << i << endl;

                DisplayMenu();

                cout << "Enter Your Choice: ";
                cin >> player_choice;

                computer_choice = computer();

                if ((player_choice == 1 && computer_choice == 3) ||
                    (player_choice == 2 && computer_choice == 1) ||
                    (player_choice == 3 && computer_choice == 2))
                 {
                    Choice();
                    player_score++;
                  
                    cout << player_name << "--> Wins" << endl; 
                    cout << "-->" << player_name << "'s score is: " << player_score << endl;
                    cout << "--> Computer Score is: " << computer_score << endl;
                } 
                else if (player_choice == computer_choice)
                 {
                    Choice();
                    cout << "-->It is a tie" << endl;
                    cout << "-->" << player_name << "'s score is: " << player_score << endl;
                    cout << "--> Computer Score is: " << computer_score << endl;
                } 
                else 
                {
                    Choice();

                    computer_score++;
                    cout << "-->Computer wins" << endl;
                    cout << "-->" << player_name << "'s score is: " << player_score << endl;
                    cout << "--> Computer Score is: " << computer_score << endl;
                   
                }
            }
        }
         else 
         {
            cout << "Invalid Round Number!" << endl;
        }
        
         
    }
     void result()
        {
            cout<<"*************************"<<endl;
            cout<<"        GAME OVER        "<<endl;
            cout<<"**************************"; 
            
            if (player_score > computer_score)
             {
            cout << "CONGRATULATIONS, YOU WIN!" << endl;
            cout << "Your Total score is: " << player_score << endl;
             cout << "Computer score is: " << computer_score << endl;
            } 
        else if (player_score < computer_score) 
            {
                cout<<endl << "BETTER LUCK NEXT TIME." << endl;
                cout << "Computer Wins" << endl;
                cout << "Your Total score is: " << player_score << endl;
                cout << "Computer score is: " << computer_score << endl;
            } 
        else 
            {
                cout <<endl<<"It's a TIE!" << endl;
                cout << "Your Total score is: " << player_score << endl;
                cout << "Computer score is: " << computer_score << endl;
            }
        }   

    void Choice()
     {
        cout << endl;
        cout << "Your choice is: " << player_choice << endl;
        cout << "Computer's choice is: " << computer_choice << endl;
        
    }
};

int main() {
    RPS Game;
    Game.play();
    Game.result();
    return 0;
}
