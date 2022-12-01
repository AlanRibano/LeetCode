#include <iostream>

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        int count = 0;
        while (n)
        {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
};

int main()
{
    Solution s;
    std::cout << s.hammingWeight(11111111111111111111111111111101) << std::endl;
    return 0;
}