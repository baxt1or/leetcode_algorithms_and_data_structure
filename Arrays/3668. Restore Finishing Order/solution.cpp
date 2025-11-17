#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;

class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        
       unordered_map<int, int> friends_table;

       for(int i = 0; i<friends.size();i++){
        friends_table[friends[i]] = i;
       }


       vector<int> res;

       for(const int &n : order){
        if (friends_table.find(n) != friends_table.end()) {
            res.push_back(n);
         }
       }

       return res;
    }
};

void print(vector<int> &arr){
    for(const auto &n: arr){
        cout<<n<<" ";
    }
}


int main(){

    vector<int> order = {3,1,2,5,4};
    vector<int> friends = {1,3,4};

    vector<int> result = Solution().recoverOrder(order, friends);
    
    print(result);

    return 0;
}