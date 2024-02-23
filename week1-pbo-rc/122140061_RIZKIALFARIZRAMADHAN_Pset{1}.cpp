#include <iostream>
using namespace std;

int main(){

    for(int i = 0;i<5;i++){
      for(int j=0;j<5;j++)
      {
        cout<<" ";
      }
      for(int j = i; j<5;j++){
        cout<<" ";
      }
      for(int j=1;j<i;j++){
        cout<<"*";
      }
      for(int j=0;j<i;j++){
        cout<<"*";
      }
      cout<<endl;
    }
  return 0;
}