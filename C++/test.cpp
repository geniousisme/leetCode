#include <cstdlib>
#include <cstdio>

using namespace std;

typedef struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
}TreeNode;

int main(){
    TreeNode root = TreeNode(1);
    TreeNode *root_node = &root;
    TreeNode left_node = TreeNode(2);

    root_node->left = &left_node;
    TreeNode left_left_node = TreeNode(3);
    root_node->left->left = &left_left_node;
    printf("%d\n", root_node->val);
    printf("%d\n", root_node->left->val);
    printf("%d\n", root_node->left->left->val);
    return 0;
}