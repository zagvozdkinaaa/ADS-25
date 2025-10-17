#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int data)
    {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};

class BST
{
public:
    Node *root;
    int diameter;

    BST()
    {
        root = NULL;
        diameter = 0;
    }

    Node *insert(Node *node, int val)
    {
        if (node == NULL)
        {
            return new Node(val);
        }
        if (val < node->data)
        {
            node->left = insert(node->left, val);
        }
        else if (val > node->data)
        {
            node->right = insert(node->right, val);
        }
        return node;
    }

    void insertValue(int val)
    {
        root = insert(root, val);
    }

    int depth(Node *node)
    {
        if (node == NULL)
            return 0;

        int leftDepth = depth(node->left);
        int rightDepth = depth(node->right);

        diameter = max(diameter, leftDepth + rightDepth);

        return 1 + max(leftDepth, rightDepth);
    }

    int getDiameter()
    {
        diameter = 0;
        depth(root);
        return diameter + 1;
    }
};

int main()
{
    int n;
    cin >> n;

    BST tree;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        tree.root = tree.insert(tree.root, x);
    }

    cout << tree.getDiameter() << "\n";

    return 0;
}