#include <cstdlib>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Test {
public:
    void test(vector<int>& v, TreeNode* t){
         // cout << "v: " << v << endl;
         cout << "&v: " << &v << endl;
         cout << "*v: " << v << endl;
    }

};



int main(){
    int arr [] = {1, 2, 3, 4, 5};
    vector<int> iarr(arr, arr + 5);
    Test ts;
    TreeNode* tt;
    ts.test(iarr, tt);
    // TreeNode root = TreeNode(1);
    // TreeNode *root_node = &root;
    // TreeNode left_node = TreeNode(2);

    // root_node->left = &left_node;
    // TreeNode left_left_node = TreeNode(3);
    // root_node->left->left = &left_left_node;
    // printf("%d\n", root_node->val);
    // printf("%d\n", root_node->left->val);
    // printf("%d\n", root_node->left->left->val);
    return 0;
}