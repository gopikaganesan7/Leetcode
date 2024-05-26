class Solution {
public:
    char findTheDifference(string s, string t) 
    {
      int a=0;
      int b=0;
      for(int i=0;i<s.length();i++)
      {
          a+=s[i];
      }
      for(int j=0;j<t.length();j++)
      {
          b+=t[j];
      }
      return b-a;
    }
};