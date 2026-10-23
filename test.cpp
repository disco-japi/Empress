#include <iostream>
#include <vector>

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        
    }
};

int main(){
	Solution * solution = new Solution;
	for (int i = 4; i <= 8; i++){
		std::cout << solution->solveNQueens(i) << std::endl;
	}
	return 0;
}
