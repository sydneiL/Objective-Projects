//Terrorist Hacking Bank Account Program//
//A hacking program funded by the CIA to train agents for transaction missions combating terrorists//
//For this first mission as a trained CIA agent, you must hack and switch funds within the terrorist bank account to the bank account of a failing coffee shop local to your city//

#include <iostream>
#include <string>
#include <thread>
#include<chrono>
using namespace std;

string agentName="";
string assignAns = "";
string coffeeShop = "Joe's Coffee Shop";
string swap = "";


//Mission Assignment//
int runAssign();


void opening(){
    
    cout<<"\n--------------------\n\n";
    cout<<"For this mission, we will spy on the bank account of a terrorist syndicate at Terror Bank."<<endl;
    cout<<"When deemed appropriate, we will switch their bank account balance to that of a local coffee shop on the verge of bankruptcy,"<<coffeeShop<<"."<<endl;
    cout<<"When we send you the signal to attack, you will input 'switch' and switch the bank account balances."<<endl;
    cout<<"Accept mission by entering 'yes'. Refuse assignment by entering 'no'.\n";
    cout<<"\n--------------------\n\n";
}
void normBal(double terrBal, double coffeeBal)
{
    double tempSwap = terrBal;//Sets tempSwitch as terrBal to store values during balance switch//
    terrBal = coffeeBal;//Sets the current terrBal to the amount of the coffeeBal//
    coffeeBal = tempSwap;//Sets the coffeeBal amount to the original amount of the terrBal, completing the switch//
}
void swapBal(double* const terrBalSwap, double* const coffeeBalSwap)
{
double tempSwap = *terrBalSwap;//Sets the tempSwitch as terrBalSwitch, storing current values for later usage//
    *terrBalSwap = *coffeeBalSwap;//Sets current terrBalSwitch to the amount of the coffeeBalSwitch//
    *coffeeBalSwap= tempSwap;//Sets coffeeBalSwitch's amount to original amount of terrBalSwitch, finishing the switch with pointers//
}
int main()
{
    cout<<"Login in for credential verifications./n";
    cout<<"Login Last Name:";
    cin>>agentName;
    cout<<"\nGreetings, Agent"<<agentName<<".\n";
    //Run assignment if answer is yes//
    opening();
    cout<<":";
    cin>>assignAns;
    if(assignAns=="yes"|| assignAns=="Yes"|| assignAns=="YES"){
        runAssign();
    }
//If agent types in anything but yes after mission introduction, values will return to 0, ending the program//
    else{
        cout<<"\nConnection voided....Farewell Agent"<<agentName<<".\n";
        return 0;
    }
    
}
//Run Mission//
//Bank Balances//

int runAssign()
{
    double terrBal = 534889.77;
    double coffeBal = 270.55;
    string swap= "";
    
    normBal(terrBal,coffeBal);//Activates normal function//
    cout<<"\nNow Agent"<<agentName<<", we make the switch today."<<endl;
    cout<<"First, we must check the current balance of Joe's Coffee Shop.\n"<<endl;
    cout.precision(10);//Sets cout precision up to 10 places, decimals included, balancing readouts//
    cout<<"Currently reading"<<coffeeShop<<"account balance...."<<endl;
    cout<<coffeeShop<<"balance is $"<<coffeBal<<""<<endl;
    cout<<"\nNow will we check the terrorist current balance.\n"<<endl;
    cout.precision(10);//Sets cout precision up to 10 places, decimals included, balancing readouts//
    cout<<"Currently reading 'TERR_ORG' account balance..."<<endl;
    cout<<"'TERR_ORG' balance is $"<<terrBal<<""<<endl;
    //Swap Bank Balances//
    
    cout<<"\nSince we know current balances of both accounts,it's time to switch them."<<endl;
    cout<<"At my signal, type 'swap' and the account balances will switch.\n"<<endl;
    cout<<"3.....\n"<<endl;
    cout<<"2...\n"<<endl;
    cout<<"1...\n"<<endl;
    cout<<"Switch them!\n"<<endl;
    
    //Loop while user hasn't typed swap//
    
    while(swap !="swap"|| swap !="Swap"){
        cout<<":";
        cin>>swap;
        //Break loop once user has typed swap//
        if(swap !="swap"|| swap !="Swap"){
            break;
        }
        //Loop again if user hasn't typed swap correctly//
        else{
            cout<<"\nNot right,you need to type 'swap' \n\n";
        }
    }
    //Swapped Balances//
    swapBal(&terrBal,&coffeBal);//Activates swap function//
    cout<<"\nWell done, let's check the new account balances.\n\n";
    cout.precision(10);//Sets cout precision up to 10 places, decimals included, balancing readouts//
    cout<<"Currently reading"<<coffeeShop<<"account balance...."<<endl;
    cout<<coffeeShop<<"balance is $"<<coffeBal<<""<<endl;
    cout<<"\nNow will we check the terrorist current balance.\n"<<endl;
    cout.precision(10);//Sets cout precision up to 10 places, decimals included, balancing readouts//
    cout<<"Currently reading 'TERR_ORG' account balance..."<<endl;
    cout<<"'TERR_ORG' balance is $"<<terrBal<<""<<endl;
//End of Mission//
    
    cout<<"\nFantastic work, Agent!"<<agentName<<". We have emptied the bank account of the terrorist organization and benefitted"<<coffeeShop<<"."<<endl;
    cout<<"\nA new mission will be given to you within the coming weeks. Until then, please stand by for further direction."<<endl;
    cout<<"\nConnection voided....Farewell Agent"<<agentName<<".\n"<<endl;
    return 0;
    
}
//End of Terrorist Hack & Switch Program//
