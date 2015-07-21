#include <cstdlib>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>

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
         // cout << "*v: " << v << endl;
    }
    void test2(vector<int>& v) {
         for (int i = 0; i < 10; i++) {
              v.push_back(i);
         };
         for (int i = 0; i < v.size(); i++){
              cout << "begin: " << *v.begin() << endl;
              v.erase(v.begin());
              cout << "v[" << i << "]: " << v[i] << endl;
              cout << "size: " << v.size() << endl; 
         }
         return;
    }

};



int main(){
    int arr [] = {1, 2, 3, 4, 5};
    vector<int> iarr(arr, arr + 5);
    vector<int> lalala;
    Test ts;
    TreeNode* tt;
    // ts.test(iarr, tt);
    ts.test2(lalala);
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