class Solution {
public:
    int romanToInt(string s) {
        int conv=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='I')
            {
                if(s[i+1]=='V'||s[i+1]=='X')
                    conv-=1;
                else
                    conv+=1;
            }
            else if(s[i]=='V')
            {
                conv+=5;
            }
            else if(s[i]=='X')
            {

                if(s[i+1]=='L'||s[i+1]=='C')
                    conv-=10;
                else
                    conv+=10;
            }
            else if(s[i]=='L')
            {
                conv+=50;
            }
            else if(s[i]=='C')
            {
                if(s[i+1]=='D'||s[i+1]=='M')
                    conv-=100;
                else
                    conv+=100;
            }
            else if(s[i]=='D')
            {
                conv+=500;
            }
            else if(s[i]=='M')
            {
                conv+=1000;
            }
        }
        return conv;
    }
};