class Solution {
public:
    bool isPalindrome(int x) {
        int temp=x;
        int rem=0;
        long int rev=0;
        while(temp>0)
        {
            rem=temp%10;
            rev=(rev*10)+rem;
            temp/=10;
        }
        if(x==rev)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
      